..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation, with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: hash tables; open hashing
   pair: open hashing; collisions

Open hashing
============
One collision-resolution strategy is :term:`separate chaining`, also called
*open hashing*. In separate chaining, the hash table is an array of buckets.
Each bucket refers to a collection that can hold every key mapped to that
bucket. A linked list is a traditional choice for the collection, which is
where the term "chaining" originates, but other containers are possible.

The first item in a bucket is not itself a collision. A collision occurs when a
second or later key maps to the same bucket index. The bucket's collection
stores all of those keys together.

.. tb-group::
   :name: tab_graph

   .. tb-tab:: Example set

      The following diagram uses seven buckets. The bucket assignments are
      shown directly so that the two chains are easy to follow; a real table
      would compute each assignment with its hash function.

      .. digraph:: hashtable
         :alt: Fruit set with separate chains
         :align: center

         graph [
           fontname = "Bitstream Vera Sans",
           labelloc=b,
           label="Fruit set hash table",
           nodesep = .05,
           rankdir = LR
         ];

         node[shape = record, width = .1, height = .1,
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ", height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | <p>}"];
         node2[label = "{<n> pear | <p>}"];
         node3[label = "{<n> apple | <p>}"];
         node4[label = "{<n> lemon | <p>}"];
         node5[label = "{<n> grape | <p>}"];
         node6[label = "{<n> lime | <p>}"];
         node7[label = "{<n> banana | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p:c->node6:n [arrowtail=dot, dir=both, tailclip=false];
         node4:p:c->node7:n [arrowtail=dot, dir=both, tailclip=false];

   .. tb-tab:: Example map

      When the ADT is a map, the process is similar. The value hashed is the
      map :term:`key`, since the key uniquely identifies a map entry. Each
      bucket provides access to one or more key-value pairs.

      .. digraph:: hashtable
         :alt: Fruit inventory map with separate chains
         :align: center

         graph [
           fontname = "Bitstream Vera Sans",
           labelloc=b,
           label="Fruit inventory hash table",
           nodesep = .05,
           rankdir = LR
         ];

         node[shape = record, width = .1, height = .1,
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ", height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | 8 | <p>}"];
         node2[label = "{<n> pear | 5 | <p>}"];
         node3[label = "{<n> apple | 12 | <p>}"];
         node4[label = "{<n> lemon | 1 | <p>}"];
         node5[label = "{<n> grape | 13 | <p>}"];
         node6[label = "{<n> lime | 35 | <p>}"];
         node7[label = "{<n> banana | 3 | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p:c->node6:n [arrowtail=dot, dir=both, tailclip=false];
         node4:p:c->node7:n [arrowtail=dot, dir=both, tailclip=false];

The linked lists allow the contents of each bucket to grow as needed, while
the array provides the first lookup step. A fixed bucket count is used here to
keep the implementation focused; production hash tables also monitor load
factor and rehash when appropriate.

A :term:`set` provides a simple demonstration of a hashed data structure.
Recall that :container:`set` stores unique items. The implementation below is
similar to a set, but intentionally leaves out iterators over all buckets,
rehashing, allocator support, and many other standard-library features.

.. tb-group::
   :name: hash_set_tab_group

   .. tb-tab:: hash_set

      The template parameters describe the key type, the fixed number of
      buckets, the hash function, and the equality predicate. Equivalent keys
      must compare equal and must produce the same hash value.

      .. code-block:: bash
         :caption: Simplified interface

         template <class Key,
                   std::size_t N,
                   class Hash = std::hash<Key>,
                   class KeyEqual = std::equal_to<Key>>
         class hash_set {
           using iterator = typename Container::iterator;
           using const_iterator = typename Container::const_iterator;

           std::pair<iterator, bool> insert(const Key& value);
           iterator find(const Key& value);
           const_iterator find(const Key& value) const;
           std::size_t count(const Key& value) const;
           std::size_t erase(const Key& value);
         };

   .. tb-tab:: find

      Finding a value using separate chaining has two steps:

      1. Compute the hash value and reduce it to a bucket index.
      2. Search the selected bucket, comparing keys with the equality
         predicate.

      The following diagram uses ``value % 10`` as its illustrative hash for
      integer keys. The chain in bucket ``4`` contains two values, so finding
      ``54`` requires checking more than one entry.

      .. digraph:: hashtable
         :alt: Integer hash table with a collision chain
         :align: center

         graph [
           fontname = "Bitstream Vera Sans",
           labelloc=b,
           label="Integer hash table: value % 10",
           nodesep = .05,
           rankdir = LR
         ];

         node [fontname = "Bitstream Vera Sans", fontsize=14,
               style=filled, fillcolor=lightblue,
               width = .1, height = .1, shape=record];
         edge [arrowhead=vee, arrowsize=0.5];

         bucket[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 | <f7>7 | <f8>8 | <f9>9 ", height = 2.5];

         a [label="{ <data> 21 | <ref>  }"];
         b [label="{ <data> 12 | <ref>  }"];
         c [label="{ <data> 34 | <ref>  }"];
         d [label="{ <data> 5 | <ref>  }"];
         e [label="{ <data> 8 | <ref>  }"];
         f [label="{ <data> 54 | <ref>  }"];
         g [label="{ <data> 89 | <ref>  }"];
         h [label="{ <data> 42 | <ref>  }"];

         bucket:f1 -> a:data:w;
         bucket:f2 -> b:data;
         bucket:f4 -> c:data;
         bucket:f5 -> d:data;
         bucket:f8 -> e:data:w;
         c:ref:c -> f:data [arrowtail=dot, dir=both, tailclip=false];
         b:ref:c -> h:data [arrowtail=dot, dir=both, tailclip=false];

      To find ``54``, the table computes ``54 % 10 == 4`` and selects bucket
      ``4``. It compares ``54`` with ``34`` first, then with ``54``. The
      equality predicate confirms the match, and ``find`` returns an iterator
      to the stored value. If the value is absent, it returns the bucket's
      ``end()`` iterator.

      .. code-block:: bash
         :caption: Pseudocode

         bucket <- buckets[hash(value) % bucket_count]
         for each item in bucket:
             if equal(item, value):
                 return iterator to item
         return bucket.end()

      A hash function that always returns ``42`` still satisfies the basic hash
      contract: equivalent keys produce the same hash value, and collisions
      are allowed. It is nevertheless a poor choice. Every key would be
      placed in bucket ``42 % bucket_count``, so a lookup would linearly scan
      one growing chain and lose the expected constant-time benefit.

   .. tb-tab:: insert

      Inserting into a set follows the same two steps as finding:

      1. Select the bucket.
      2. Search for an equivalent key.

      If the key is already present, the set remains unchanged. Otherwise, the
      new key is appended to the bucket. Returning an iterator and a Boolean
      follows the contract used by standard associative containers: the
      Boolean is ``true`` only when a new key was inserted.

      .. code-block:: bash
         :caption: Pseudocode

         bucket <- buckets[hash(value) % bucket_count]
         position <- find equivalent value in bucket
         if position != bucket.end():
             return {position, false}
         append value to bucket
         return {iterator to new value, true}

   .. tb-tab:: erase

      Erasing is also a bucket search followed by an equality comparison. If
      the key is found, remove it and return ``1``. Otherwise return ``0``.

      .. code-block:: bash
         :caption: Pseudocode

         bucket <- buckets[hash(value) % bucket_count]
         position <- find equivalent value in bucket
         if position == bucket.end():
             return 0
         erase position from bucket
         return 1

   .. tb-tab:: Run it

      This complete example uses an identity hash for positive integers so
      that its bucket assignments are predictable. Values such as ``34`` and
      ``45`` deliberately collide in bucket ``1`` when there are ``11``
      buckets.

      .. tb-code:: cpp
         :name: hash_table_open_ac

         #include <algorithm>
         #include <array>
         #include <cstddef>
         #include <functional>
         #include <iostream>
         #include <iterator>
         #include <list>
         #include <ostream>
         #include <utility>

         struct identity_hash {
           std::size_t operator()(int value) const noexcept {
             return static_cast<std::size_t>(value);
           }
         };

         template <class Key,
                   std::size_t N,
                   class Hash = std::hash<Key>,
                   class KeyEqual = std::equal_to<Key>>
         class hash_set {
           static_assert(N > 0, "hash_set needs at least one bucket");

           using container_type = std::list<Key>;

         public:
           using value_type = Key;
           using key_type = Key;
           using size_type = std::size_t;
           using iterator = typename container_type::iterator;
           using const_iterator = typename container_type::const_iterator;
           using insert_result = std::pair<iterator, bool>;

           insert_result insert(const Key& value) {
             auto& bucket = find_bucket(value);
             const auto position = find_in_bucket(bucket, value);
             if (position != bucket.end()) {
               return {position, false};
             }

             bucket.push_back(value);
             ++size_;
             return {std::prev(bucket.end()), true};
           }

           iterator find(const Key& value) {
             return find_in_bucket(find_bucket(value), value);
           }

           const_iterator find(const Key& value) const {
             return find_in_bucket(find_bucket(value), value);
           }

           size_type count(const Key& value) const {
             const auto& bucket = find_bucket(value);
             return find_in_bucket(bucket, value) == bucket.end() ? 0 : 1;
           }

           size_type erase(const Key& value) {
             auto& bucket = find_bucket(value);
             const auto position = find_in_bucket(bucket, value);
             if (position == bucket.end()) {
               return 0;
             }

             bucket.erase(position);
             --size_;
             return 1;
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
             for (size_type bucket_index = 0;
                  bucket_index < N; ++bucket_index) {
               for (const auto& value : set.buckets_[bucket_index]) {
                 os << bucket_index << ':' << value << ' ';
               }
             }
             return os << ']';
           }

         private:
           container_type& find_bucket(const Key& value) {
             return buckets_[hasher_(value) % N];
           }

           const container_type& find_bucket(const Key& value) const {
             return buckets_[hasher_(value) % N];
           }

           iterator find_in_bucket(container_type& bucket,
                                   const Key& value) {
             return std::find_if(bucket.begin(), bucket.end(),
                                 [this, &value](const Key& item) {
                                   return equal_(item, value);
                                 });
           }

           const_iterator find_in_bucket(const container_type& bucket,
                                         const Key& value) const {
             return std::find_if(bucket.begin(), bucket.end(),
                                 [this, &value](const Key& item) {
                                   return equal_(item, value);
                                 });
           }

           std::array<container_type, N> buckets_;
           Hash hasher_;
           KeyEqual equal_;
           size_type size_ = 0;
         };

         int main() {
           hash_set<int, 11, identity_hash> values;

           const auto first = values.insert(34);
           const auto duplicate = values.insert(34);
           values.insert(45);
           values.insert(21);

           std::cout << std::boolalpha
                     << "first insertion: " << first.second << '\n'
                     << "duplicate insertion: " << duplicate.second << '\n'
                     << "count(45): " << values.count(45) << '\n'
                     << "values: " << values << '\n';

           values.erase(34);
           std::cout << "after erase, count(34): " << values.count(34)
                     << '\n';
         }

-----

.. admonition:: More to Explore

   - :doc:`Resolving collisions <hash_table_collisions>`
   - :doc:`Open addressing (closed hashing) <closed_hashing>`
   - :cpp:`std::unordered_set <container/unordered_set>`
   - :cpp:`std::unordered_map <container/unordered_map>`
