..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: closed hashing; collisions

Closed hashing
==============
In closed hashing, the hash array contains individual elements 
rather than a collection of elements. 
When a key we want to insert collides with a key already in the table,
we resolve the collision by searching for another open :term:`slot` within
the table where we can place the new key.

Each slot in the hash table contains a ``hash_entry``, composed of
one data element and a status field indicating whether that slot is
*occupied*, *empty*, or *deleted*.

.. tabbed:: hash_set_tab_group

   .. tab:: hash_set

      .. code-block:: cpp

         enum class hash_status { OCCUPIED, EMPTY, DELETED };

         template <class T>
         struct hash_entry 
         {
           T data;
           hash_status info;

           hash_entry(): info(hash_status::EMPTY)  {}
           hash_entry(const T& value, hash_status status)
             : data{value}
             , info(status)
             {}
         };

      The ``hash_set`` backing store is an array of ``hash_entry``
      objects.

      .. code-block:: cpp

         template <class Key,
                   size_t N,
                   class Comparator=std::equal_to<Key>>
         class hash_set
         {
           public:
             using value_type = Key;
             using key_type   = Key;

             hash_set() = default;
           private:
             array<hash_entry<Key>, N> table;
             Comparator compare;
             size_t sz = 0;
         };


      Collisions are resolved by trying a series of locations,
      :math:`p_0, p_1, p_2, \ldots p_{N-1}`
      until we find what we are looking for.
      Each position is calculated as:

      .. math::

         pos_i = hash(value) + f(n) 

      where:
     
      - ``hash(value)`` is the :term:`home slot`
      - ``f()`` is a function taking an integer
        number of tries and returns an integer offset.

      How are new positions used in the hash table?

      Searching:
         Try positions :math:`p_0, p_1, p_2, \ldots`
         until we find the requested value or an ``EMPTY`` slot.
      Inserting:
         Try positions :math:`p_0, p_1, p_2, \ldots`
         until we find the same value, an ``EMPTY`` slot, or
         a ``DELETED`` slot.
         Put the new value in the position pound and
         mark the position as ``OCCUPIED``.
      Erasing:
         Try positions :math:`p_0, p_1, p_2, \ldots`
         until we find the requested value or an ``EMPTY`` slot.
         If we find the value, then
         mark the position as ``DELETED``.


   .. tab:: find

      Find takes a value of the ``hash_entry`` key type as a parameter
      and returns the position of the value in the table.
      It returns ``N`` if the value is not in the table.

      .. code-block:: cpp
         :emphasize-lines: 6-9

         size_t find (const Key& value) const
         {
           size_t hash = std::hash<Key>()(value);
           size_t pos = hash % N;
           size_t count = 0;
           while ((table[pos].info == hash_status::DELETED ||
                  (table[pos].info == hash_status::OCCUPIED 
                  && (!compare(table[pos].data, value))))
               && count < N)
           {
             ++count;
             pos = (hash + next_slot(count)) % N;
           }
           if (count >= N || table[pos].info == hash_status::EMPTY) {
             return N;
           }
           return pos;
         }

      The loop condition is fairly complicated and needs discussion.
      There are three ways to exit this loop:

      - We hit an ``EMPTY`` space (not ``DELETED``, and not ``OCCUPIED``)
      - We hit an ``OCCUPIED`` space that has the value we want
      - We have tried ``N`` different positions. (No place left to look!)

   .. tab:: contains

      With ``find`` in place, other search operations are easy.
      Simply call find and evaluate the results.

      .. code-block:: cpp

         constexpr
           bool contains (const Key& value) const noexcept
         {
           return  find(value) != N;
         }

         int count (const Key& value)
         {
           unsigned pos = find(value);
           return  (pos == N) ? 0 : 1;
         }

      Note that since our set is still forcing a uniqueness constraint,
      ``count`` will return only ``0`` or ``1``.

   .. tab:: erase

      The code to remove elements is just as simple.
      Easier than the ``erase`` we implemented for open hashing.
      
      We try to find that element.

      - If found, we mark that slot ``DELETED`` and decrement the size.
      - Otherwise, do nothing.

      .. code-block:: cpp

         void erase (const Key& value)
         {
           unsigned pos = find(value);
           if (pos != N) {
             table[pos].info = hash_status::DELETED;
             --sz;
           }
         }

   .. tab:: insert

      Inserts are a bit more work, because they involve potentially
      looking for an open slot to store a value.

      Because this is a set (and not a multiset) we first call ``find``
      to see if the value is already there.

      .. code-block:: cpp

         bool insert (const Key& value)
         {
           size_t hash = std::hash<Key>()(value);
           unsigned pos = find(value);
           if (pos == N) {
             size_t count = 0;
             pos = hash % N;
             while (table[pos].info == hash_status::OCCUPIED && count < N)
             {
               ++count;
               pos = (hash + next_slot(count)) % N;
             }
             if (count >= N) {
               return false;  // could not add, table is full
             }
             table[pos].info = hash_status::OCCUPIED;
             table[pos].data = value;
             ++sz;
             return true;
           }
           // else replace existing value
           table[pos].data = value;
           return true;
         }

      If not found (``pos == N``), then we need to find a slot.
      The loop that does this is similar the ``find`` loop, 
      but unlike ``find``, we stop at the first ``DELETED`` or ``EMPTY`` slot.

      In the other searches, we had kept going past ``DELETED`` slots, 
      because the element we wanted might have been stored 
      after an element that was later erased.
      But now we are only looking for an unoccupied slot to put something,
      so either a slot that has never been occupied (``EMPTY``) or
      a slot that used to be occupied but is no longer (``DELETED``) works.

   .. tab:: Run it

      The example contains ``#define`` statements you can use to change
      how the next slot is found.

      Try it with different hash table sizes to see how clumping changes
      with the different probing strategies.

      .. activecode:: hash_table_closed_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:


         #include <array>
         #include <cstddef>
         #include <iomanip>
         #include <iostream>
         #include <utility>

         using std::array;

         #define USE_LINEAR_PROBING

         #if defined(USE_QUADRATIC_PROBING)
             // find next slot using quadratic probing
             constexpr
               size_t next_slot(size_t count) noexcept { return count*count; }

         #elif defined(USE_DOUBLE_HASHING)

             // find next slot using double hashing
             constexpr
               size_t next_slot(size_t count) noexcept { return count * std::hash<size_t>()(count); }
         #else   // default to USE_LINEAR_PROBING
             // find next slot using linear probing
             constexpr
               size_t next_slot(size_t count) noexcept { return count; }

         #endif


         enum class hash_status { OCCUPIED, EMPTY, DELETED };

         template <class T>
         struct hash_entry 
         {
           T data;
           hash_status info;

           hash_entry(): info(hash_status::EMPTY)  {}
           hash_entry(const T& value, hash_status status)
             : data{value}
             , info(status)
             {}
         };

         template <class T>
         std::ostream& operator<<(std::ostream& os, const hash_entry<T>& rhs)
         {
           if (rhs.info == hash_status::OCCUPIED) {
             os << rhs.data;
           } else if (rhs.info == hash_status::EMPTY) {
             os << 'E';
           } else {
             os << 'D';
           }
           return os;
         }

         template <class Key,
                  size_t N,
                  class Comparator=std::equal_to<Key>>
         class hash_set
         {
           public:
             using value_type = Key;
             using key_type   = Key;

             hash_set() = default;

             size_t find (const Key& value) const
             {
               size_t hash = std::hash<Key>()(value);
               size_t pos = hash % N;
               size_t count = 0;
               while ((table[pos].info == hash_status::DELETED ||
                      (table[pos].info == hash_status::OCCUPIED 
                      && (!compare(table[pos].data, value))))
                   && count < N)
               {
                 ++count;
                 pos = (hash + next_slot(count)) % N;
               }
               if (count >= N || table[pos].info == hash_status::EMPTY) {
                 return N;
               }
               return pos;
             }

             constexpr
               bool contains (const Key& value) const noexcept
             {
               return  find(value) != N;
             }

             int count (const Key& value)
             {
               unsigned pos = find(value);
               return  (pos == N) ? 0 : 1;
             }

             void erase (const Key& value)
             {
               unsigned pos = find(value);
               if (pos != N) {
                 table[pos].info = hash_status::DELETED;
                 --sz;
               }
             }


             bool insert (const Key& value)
             {
               size_t hash = std::hash<Key>()(value);
               unsigned pos = find(value);
               if (pos == N) {
                 size_t count = 0;
                 pos = hash % N;
                 while (table[pos].info == hash_status::OCCUPIED && count < N)
                 {
                   ++count;
                   pos = (hash + next_slot(count)) % N;
                 }
                 if (count >= N) {
                   return false;  // could not add, table is full
                 }
                 table[pos].info = hash_status::OCCUPIED;
                 table[pos].data = value;
                 ++sz;
                 return true;
               }
               // else replace existing value
               table[pos].data = value;
               return true;
             }


             constexpr
               size_t size() const noexcept { return sz; }

             constexpr
               bool empty() const noexcept { return sz == 0; }

           private:
             array<hash_entry<Key>, N> table;
             Comparator compare;
             size_t sz = 0;

             friend
               std::ostream& operator<<(std::ostream& os, const hash_set& rhs)
               {
                 os << '[';
                 for (const auto& slot: rhs.table) {
                   os << slot << ',';
                 }
                 return os << ']';
               }

         };

         int main() {
           using std::cout;
           using std::endl;
           auto foo = hash_set<int, 11>{};
           cout << "sz: " << foo.size() << endl;
           cout << std::boolalpha << "mt?: " << foo.empty() << endl;
           cout << foo << endl;
           foo.insert(72);
           foo.insert(72);
           cout << "insert two 72's count:"<< endl;
           cout << foo.count(72) << endl;
           cout << foo << endl;
           cout << "mt?: " << foo.empty() << endl;

           foo.erase(72);
           cout << "count after erase:"<< endl;
           cout << foo.count(72) << endl;

           foo.insert(-1);
           foo.insert(0);
           foo.insert(1);
           foo.insert(2);
           foo.insert(9);
           foo.insert(81);
           foo.insert(121);
           foo.insert(572);
           foo.insert(999);
           cout << foo << endl;
           foo.erase(-1);
           cout << foo << endl;
         }
               


.. index:: linear probing
   single: quadratic probing
   single: double hashing

Choosing the next slot
----------------------
The function ``next_slot(n)`` in the ``find`` and ``insert`` functions 
controls the sequence of positions that will be checked.
It is the implementation of the function :math:`f(n)` mentioned earlier.
Recall the find function:

.. code-block:: cpp
   :emphasize-lines: 12

   size_t find (const Key& value) const
   {
     size_t hash = std::hash<Key>()(value);
     size_t pos = hash % N;
     size_t count = 0;
     while ((table[pos].info == hash_status::DELETED ||
            (table[pos].info == hash_status::OCCUPIED 
            && (!compare(table[pos].data, value))))
         && count < N)
     {
       ++count;
       pos = (hash + next_slot(count)) % N;
     }
     if (count >= N || table[pos].info == hash_status::EMPTY) {
       return N;
     }
     return pos;
   }

On our :math:`n_{th}` try, we examine the position

.. math::

   pos_n = hash(value) + f(n)

where :math:`hash(value)` always returns the :term:`home slot` for any
hashed value.
This is the location that the value would be stored if currently unoccupied.
The ``f`` function computes an offset from the reference location.
The most common schemes for choosing the next slot are
:term:`linear probing`,
:term:`quadratic probing`, and
:term:`double hashing`.

Linear probing
   .. math::

      f(n) = n

   If a collision occurs at location ``pos``, 
   we next check locations 
   :math:`pos+1 \pmod N, pos+2 \pmod N, pos+3 \pmod N, \ldots` and so on.

   Because collisions get stored in a location originally intended for
   another hash code, values have a tendency to clump together in the
   hash table.

Quadratic probing
   .. math::

      f(n) = n^2

   If a collision occurs at location ``pos``, 
   we next check locations 
   :math:`pos+1 \pmod N, pos+4 \pmod N, pos+9 \pmod N, \ldots` and so on.

   Because the jumps between slots increases as the number of tries increases,
   this function tends to reduce clumping (and results in shorter searches).
   *``But``* it is not guaranteed to find an available empty slot if the table is
   more than half full or if ``N`` is not a prime number.

   .. note::

      Again, prime numbers!

      Remember the earlier discussion about how :math:`% N` tends to improve the
      key distribution when ``N`` is prime?
      You can see why it's part of programming "folklore" that hash tables
      should be prime-number sized, even if most programmers can't say 
      *why* that's supposed to be good.

Double hashing
   .. math::

      f(n) = n * h_2(value)

   where :math:`h_2` is an alternate hash code function.

   If a collision occurs at location ``pos``, 
   we next check locations 
   :math:`(pos+1*h_2(value)) \pmod N, pos+2*h_2(value)) \pmod N, pos+3*h_2(value)) \pmod N, \ldots` and so on.

   This also tends to reduce clumping, but, as with quadratic hashing,
   it is possible to get unlucky and miss open slots when trying to find
   a place to insert a new key.


Analysis of closed hashing
--------------------------
We define :math:`\lambda`, the :term:`load factor` of a hash table, 
as the number of items contained in the table divided by the table size.
In other words, the load factor measures what fraction of the table is full.
By definition, :math:`0 \le \lambda \le 1`.

- Given an ideal collision strategy, 
  the probability of an arbitrary cell being full is :math:`\lambda`.
- Therefore,
  the probability of an arbitrary cell being empty is :math:`1 - \lambda`.
- The average number of table elements we expect to examine before finding
  an open position is therefore :math:`\frac {1}{1-\lambda}`.

Since we never look at more than ``N`` positions,
given an ideal collision strategy, finds and inserts are on average 

.. math::

   O \left ( min \left ( \frac {1}{1-\lambda}, N \right ) \right )

The graph shows how :math:`\frac {1}{1-\lambda}` changes as
:math:`\lambda` increases.

.. plot::

   import numpy as np
   import matplotlib.pyplot as plt

   n = np.linspace(0, 1, 100)
   plt.plot(n, 1/(1-n) -1)

   plt.ylim(0,20.5)
   plt.xlim(0,0.96)

   plt.title('Collision growth vs. load factor')
   plt.xlabel('Load factor')
   plt.ylabel('Average # of collisions')
   plt.xticks(np.arange(0, 1, step=0.1))
   plt.yticks(np.arange(0, 20.5, step=2))

   plt.show()


If the table is less than half full (:math:`\lambda \lt 0.5`)
then we expect to try **on average** no more than 2 slots 
during a search or insert. 
Not too bad.
But as :math:`\lambda` gets larger,
the average number of slots examined grows toward ``N``.
As the table fills and ``sz`` approaches ``N``, the performance
degenerates toward :math:`O(N)` behavior.

Because of this, a general rule of thumb for hash tables is 
to keep them no more than half full.
At that load factor, we can treat searches and inserts as :math:`O(1)`
operations.
If we let the load factor get much higher, we start seeing :math:`O(N)`
performance.

No collision resolution scheme is truly ideal, 
so keeping the load factor low enough is even more important in practice 
than this idealized analysis indicates.

-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     `Resolving Collisions <https://www.cs.odu.edu/~zeil/cs361/f16/Public/collisions/index.html>`__,
     by Steven J. Zeil for his data structures course CS361. 


