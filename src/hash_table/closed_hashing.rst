..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation, with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: closed hashing; collisions
   single: linear probing
   single: quadratic probing
   single: double hashing

Open addressing (closed hashing)
=================================
In open addressing, also called *closed hashing*, the table stores entries
directly in its array of slots rather than storing a collection at each
bucket. When a key collides with an occupied home slot, the table searches for
another slot according to a probe sequence.

Each slot contains a ``hash_entry`` with one data element and a status field.
The status distinguishes an ``OCCUPIED`` slot from an ``EMPTY`` slot that has
never been used and a ``DELETED`` slot that contains a tombstone.

.. note::

   The complete example on this page is intentionally simplified.
   It omits rehashing, iterators, allocator support, and many
   other features of the standard unordered containers. It is meant to make
   probe sequences and tombstones visible.

The ``hash_entry`` type uses a live ``T data`` member even when its slot is
empty. As a result, this particular implementation requires ``T`` to
be default-constructible. Standard containers do not impose that requirement
on every key merely because a slot is empty.

.. tb-group::
   :name: hash_set_tab_group

   .. tb-tab:: hash_set

      .. code-block:: cpp

         enum class hash_status { OCCUPIED, EMPTY, DELETED };

         template <class T>
         struct hash_entry {
           T data;
           hash_status status = hash_status::EMPTY;
         };

      The table stores an array of entries. The hash policy and equality
      predicate are separate template parameters. As with every unordered
      container, equivalent keys must compare equal and must produce the same
      hash value.

      .. code-block:: cpp
         :caption: Simplified interface

         template <class Key,
                   std::size_t N,
                   class Hash = std::hash<Key>,
                   class KeyEqual = std::equal_to<Key>>
         class hash_set {
           std::pair<std::size_t, bool> insert(const Key& value);
           std::size_t find(const Key& value) const;
           bool contains(const Key& value) const;
           std::size_t count(const Key& value) const;
           std::size_t erase(const Key& value);
         };

   .. tb-tab:: find

      The table first computes the home slot:

      .. math::

         home(value) = hash(value) \mathbin{\%} N

      The probe sequence then computes each candidate position from that home
      slot:

      .. math::

         position_i = (home(value) + offset(value, i)) \mathbin{\%} N

      Searching examines at most ``N`` positions:

      - If the position is ``OCCUPIED`` and contains an equivalent key, the
        search succeeds.
      - If the position is ``EMPTY``, the search fails. No later insertion can
        have placed the key beyond a slot that has never been used.
      - If the position is ``DELETED`` or contains a different key, probing
        continues.

      .. code-block:: bash
         :caption: ``find`` Pseudocode

         home <- hash(value) % bucket_count
         for probe from 0 through bucket_count - 1:
             position <- (home + offset(value, probe)) % bucket_count
             if table[position] is EMPTY:
                 return not found
             if table[position] is OCCUPIED and equal(table[position], value):
                 return position
         return not found

      A tombstone cannot terminate a search. The requested key might have
      been inserted farther along the probe sequence before an earlier key was
      erased.

   .. tb-tab:: contains

      Once ``find`` is available, membership operations are straightforward.
      This interface returns a slot index, with ``N`` meaning that
      the key was not found.

      .. code-block:: cpp

         bool contains(const Key& value) const {
           return find(value) != N;
         }

         std::size_t count(const Key& value) const {
           return contains(value) ? 1 : 0;
         }

      A set enforces uniqueness, so ``count`` can only return ``0`` or ``1``.

   .. tb-tab:: erase

      Erasing an entry marks its slot ``DELETED`` instead of changing it to
      ``EMPTY``. This tombstone preserves the probe path for keys stored later
      in the sequence.

      .. code-block:: bash
         :caption: Pseudocode

         position <- find(value)
         if position == not found:
             return 0
         table[position].status <- DELETED
         decrease size
         return 1

      Tombstones can accumulate and make searches longer. A practical table
      can rebuild or rehash its storage when tombstones or the load factor
      become too numerous.

   .. tb-tab:: insert

      Insertion must continue past a tombstone so it can detect a duplicate
      key later in the probe sequence. It remembers the first tombstone and
      uses it only after the search confirms that the key is not already in the
      table.

      .. code-block:: bash
         :caption: Pseudocode

         first_deleted <- not found
         home <- hash(value) % bucket_count
         for probe from 0 through bucket_count - 1:
             position <- (home + offset(value, probe)) % bucket_count
             if table[position] is OCCUPIED:
                 if equal(table[position], value):
                     return {position, false}
             else if table[position] is DELETED:
                 if first_deleted == not found:
                     first_deleted <- position
             else:
                 if first_deleted != not found:
                     position <- first_deleted
                 store value at position
                 mark position OCCUPIED
                 increase size
                 return {position, true}

         if first_deleted != not found:
             store value at first_deleted
             mark first_deleted OCCUPIED
             increase size
             return {first_deleted, true}
         return {not found, false}

      The second parameter returns ``true`` when a new key is inserted,
      ``false`` otherwise.
      A duplicate does not replace the existing key.

   .. tb-tab:: Run it

      The preprocessor symbol selects the probe strategy. Leave the default
      definition in place for linear probing, or define one of the other
      symbols before compiling to compare the strategies.

      .. tb-code:: cpp
         :name: hash_table_closed_ac

         #include <array>
         #include <cstddef>
         #include <functional>
         #include <iostream>
         #include <ostream>
         #include <utility>

         #if !defined(USE_LINEAR_PROBING) \
             && !defined(USE_QUADRATIC_PROBING) \
             && !defined(USE_DOUBLE_HASHING)
         #define USE_LINEAR_PROBING
         #endif

         enum class hash_status { OCCUPIED, EMPTY, DELETED };

         struct identity_hash {
           std::size_t operator()(int value) const noexcept {
             return static_cast<std::size_t>(value);
           }
         };

         template <class T>
         struct hash_entry {
           T data;
           hash_status status = hash_status::EMPTY;
         };

         template <class Key,
                   std::size_t N,
                   class Hash = std::hash<Key>,
                   class KeyEqual = std::equal_to<Key>>
         class hash_set {
           static_assert(N > 0, "hash_set needs at least one slot");

         public:
           using size_type = std::size_t;
           using insert_result = std::pair<size_type, bool>;

           size_type find(const Key& value) const {
             const size_type home = home_slot(value);
             for (size_type probe = 0; probe < N; ++probe) {
               const size_type position = probe_position(value, home, probe);
               const auto& entry = table_[position];
               if (entry.status == hash_status::EMPTY) {
                 return N;
               }
               if (entry.status == hash_status::OCCUPIED
                   && equal_(entry.data, value)) {
                 return position;
               }
             }
             return N;
           }

           bool contains(const Key& value) const {
             return find(value) != N;
           }

           size_type count(const Key& value) const {
             return contains(value) ? 1 : 0;
           }

           size_type erase(const Key& value) {
             const size_type position = find(value);
             if (position == N) {
               return 0;
             }
             table_[position].status = hash_status::DELETED;
             --size_;
             return 1;
           }

           insert_result insert(const Key& value) {
             const size_type home = home_slot(value);
             size_type first_deleted = N;

             for (size_type probe = 0; probe < N; ++probe) {
               const size_type position = probe_position(value, home, probe);
               auto& entry = table_[position];

               if (entry.status == hash_status::OCCUPIED) {
                 if (equal_(entry.data, value)) {
                   return {position, false};
                 }
               } else if (entry.status == hash_status::DELETED) {
                 if (first_deleted == N) {
                   first_deleted = position;
                 }
               } else {
                 const size_type target =
                     first_deleted == N ? position : first_deleted;
                 table_[target].data = value;
                 table_[target].status = hash_status::OCCUPIED;
                 ++size_;
                 return {target, true};
               }
             }

             if (first_deleted != N) {
               table_[first_deleted].data = value;
               table_[first_deleted].status = hash_status::OCCUPIED;
               ++size_;
               return {first_deleted, true};
             }
             return {N, false};
           }

           size_type size() const noexcept {
             return size_;
           }

           bool empty() const noexcept {
             return size_ == 0;
           }

           friend std::ostream& operator<<(std::ostream& os,
                                           const hash_set& set) {
             os << '[';
             for (size_type position = 0; position < N; ++position) {
               const auto& entry = set.table_[position];
               if (entry.status == hash_status::OCCUPIED) {
                 os << position << ':' << entry.data << ' ';
               } else if (entry.status == hash_status::DELETED) {
                 os << position << ":D ";
               } else {
                 os << position << ":E ";
               }
             }
             return os << ']';
           }

         private:
           size_type home_slot(const Key& value) const {
             return hasher_(value) % N;
           }

           size_type probe_position(const Key& value,
                                    size_type home,
                                    size_type probe) const {
             return (home + probe_offset(value, probe)) % N;
           }

           size_type probe_offset(const Key& value,
                                  size_type probe) const {
         #if !defined(USE_DOUBLE_HASHING)
             (void)value;
         #endif
         #if defined(USE_QUADRATIC_PROBING)
             return probe * probe;
         #elif defined(USE_DOUBLE_HASHING)
             return probe * secondary_step(value);
         #else
             return probe;
         #endif
           }

           size_type secondary_step(const Key& value) const {
             if constexpr (N == 1) {
               return 1;
             } else {
               return 1 + (hasher_(value) % (N - 1));
             }
           }

           std::array<hash_entry<Key>, N> table_;
           Hash hasher_;
           KeyEqual equal_;
           size_type size_ = 0;
         };

         template <class T>
         std::ostream& operator<<(std::ostream& os,
                                  const hash_entry<T>& entry) {
           if (entry.status == hash_status::OCCUPIED) {
             return os << entry.data;
           }
           return os << (entry.status == hash_status::DELETED ? 'D' : 'E');
         }

         int main() {
           hash_set<int, 11, identity_hash> values;

           std::cout << "size: " << values.size() << '\n'
                     << std::boolalpha
                     << "empty: " << values.empty() << '\n';

           const auto first = values.insert(72);
           const auto duplicate = values.insert(72);
           std::cout << "first insertion: " << first.second << '\n'
                     << "duplicate insertion: " << duplicate.second << '\n'
                     << "count(72): " << values.count(72) << '\n';

           values.erase(72);
           std::cout << "after erase, count(72): " << values.count(72)
                     << '\n';

           values.insert(34);
           values.insert(45);
           values.insert(21);
           std::cout << "values: " << values << '\n'
                     << "contains(45): " << values.contains(45) << '\n';
         }

The default linear-probing strategy checks the home slot, then consecutive
slots, wrapping at the end of the array. It is simple, but entries tend to
form contiguous clusters. This is called *primary clustering* because a
cluster makes later probe sequences longer.

.. code-block:: bash
   :caption: Linear probing

   offset(value, i) <- i
   position_i <- (home(value) + i) % N

Quadratic probing uses increasing offsets:

.. code-block:: bash
   :caption: Quadratic probing

   offset(value, i) <- i * i
   position_i <- (home(value) + i * i) % N

Quadratic probing reduces primary clustering, but different keys with the same
home slot still follow the same sequence. That is called secondary clustering.
The simple ``i * i`` sequence is not guaranteed to visit every slot for every
table size. A common analysis uses a prime table size and keeps the load factor
below one half, but these conditions describe a particular probing scheme,
not a universal guarantee.

Double hashing uses a second hash function to choose the step size:

.. math::

   offset(value, i) = i \mathbin{\times} h_2(value)

   position_i = (home(value) + i \mathbin{\times} h_2(value)) \mathbin{\%} N

The step must be nonzero and relatively prime to ``N``. When ``N`` is prime,
choosing ``h_2(value)`` in the range ``1`` through ``N - 1`` guarantees this
property. For a non-prime table size, the secondary hash must be designed so
that the step and ``N`` are relatively prime; otherwise the sequence can skip
slots and fail even when an empty slot exists.

The three strategies have different clustering behavior and probe costs. The
table must also keep enough empty capacity for a probe sequence to terminate,
and tombstones effectively increase the amount of occupied search history.

Analysis of open addressing
---------------------------
Let :math:`N` be the number of occupied entries and :math:`M` be the number of
slots in the table. The :term:`load factor` is:

.. math::

   \lambda = \frac{N}{M}

For open addressing, :math:`0 \leq \lambda \leq 1`, and insertion cannot
succeed when every slot is occupied. Under an idealized uniform-probing model,
the expected number of probes for an unsuccessful search or insertion is:

.. math::

   \frac{1}{1 - \lambda}

This formula does not describe every probe strategy exactly. Successful
searches have a different expected cost, and linear probing can perform worse
because of primary clustering. The formula is useful for showing why open
addressing becomes increasingly sensitive to load factor.

The graph shows the expected number of *extra* probes beyond the first under
the idealized model:

.. plot::

   import numpy as np
   import matplotlib.pyplot as plt

   load_factor = np.linspace(0, 0.96, 100)
   extra_probes = 1 / (1 - load_factor) - 1
   plt.plot(load_factor, extra_probes)

   plt.ylim(0, 20.5)
   plt.xlim(0, 0.96)
   plt.title('Expected extra probes vs. load factor')
   plt.xlabel(r'Load factor ($\lambda$)')
   plt.ylabel('Expected extra probes')
   plt.xticks(np.arange(0, 1, step=0.1))
   plt.yticks(np.arange(0, 20.5, step=2))

   plt.show()

If the table is less than half full, then the idealized unsuccessful-search
estimate is less than two probes on average. As :math:`\lambda` approaches
one, the estimate grows without bound, although a real table can examine no
more than ``M`` slots before declaring failure. In practice, clustering and
tombstones make the actual cost dependent on the selected strategy.

Keeping the table comfortably below full is therefore necessary, but there is
no universal half-full rule. A practical implementation chooses a threshold
based on its probe strategy and workload, then rehashes before the table or its
tombstones make searches too long.

-----

.. admonition:: More to Explore

   - :doc:`Resolving collisions <hash_table_collisions>`
   - :doc:`Separate chaining (open hashing) <open_hashing>`
   - :cpp:`std::unordered_set <container/unordered_set>`
   - :cpp:`std::unordered_map <container/unordered_map>`
