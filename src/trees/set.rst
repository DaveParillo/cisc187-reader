..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: associative containers; set

The set class
=============
A :term:`set` refers to any data structure in which
every member of the set is unique.
The integers define a set, because every number is unique.
The values ``{3, 1, 4, 1, 5, 9}`` do **not** define a proper set,
because the value ``1`` is repeated.

In C++, a :container:`std::set <set>` keeps its elements ordered according to
its comparison object. By default, that comparison uses ``operator<``.
Like ``std::vector``, a ``set`` is a generic class
and declarations must include the object :term:`type`
stored in the class:

.. code-block:: cpp
   :name: set-common

   #include <iostream>
   #include <set>

   std::set<int> sample_set() {
     return {2, 7, 1, 8, 4, 5, 9};
   }

The following example initializes a set with values and prints the set.
Without running the code first, what do you think will be stored in ``x`` after
initialization?

.. tb-reveal::
   :name: reveal_init

   The two defining characteristics of a ``set`` are:

   - A ``set`` is sorted.
   - A ``set`` may contain only unique values.

   Defining a set with repeated values is not an error.
   Equivalent values after the first are ignored.

   When initialized, ``x`` will contain: ``1 2 4 5 7 8 9``


.. tb-code:: cpp
   :name: set_initialization_ac

   #include <iostream>
   #include <set>

   int main() {
     std::set<int> x {2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9};
     for (const auto value : x) {
       std::cout << value << ' ';
     }
     std::cout << '\n';
   }

Like the sequence containers, each element in a set can be visited one at a
time using a :lang:`range-for` loop. The preceding complete example uses that
loop to display the sorted values.

Because ``set`` does not provide ``operator[]``, an index-based loop is not
the appropriate way to visit its elements. Use a range-for loop or an
iterator instead.


Sets can contain any key type for which the set's comparison object defines a
:req:`strict weak ordering <Compare>`. The default comparison object uses
``operator<``, but a caller can provide a different comparator instead. The
key type does not have to overload ``operator<`` when a custom comparator is
provided.

For example, this complete program stores the values in descending order:

.. tb-code:: cpp
   :name: set_custom_compare_ac
   :run-before: set-common

   struct descending {
     bool operator()(int lhs, int rhs) const {
       return lhs > rhs;
     }
   };

   int main() {
     std::set<int, descending> x {2, 7, 1, 8, 4, 5, 9};
     for (const auto value : x) {
       std::cout << value << ' ';
     }
     std::cout << '\n';
   }

The keys in a ``std::set`` are treated as constant while they are in the
container. Changing a key through an iterator could violate the ordering
invariant, so dereferencing a set iterator produces a ``const`` reference.

For an ordered ``set``, search, insertion, and erasure take :math:`O(\log N)`
time. The container uses :math:`O(N)` storage. Unordered containers have
average constant-time lookup, insertion, and erasure, but their worst-case
time is :math:`O(N)`.

Use :container:`set::insert <set/insert>` to add a new element to a ``set``.
The function returns a pair containing an iterator to the equivalent element
and a Boolean that is true only when a new element was inserted.

.. tb-code:: cpp
   :name: set_insert_ac

   #include <iostream>
   #include <set>

   int main() {
     auto x = std::set<int> {2, 7, 1, 8, 4, 5, 9};
     auto inserted = x.insert(6);
     auto duplicate = x.insert(8);

     std::cout << std::boolalpha
               << "inserted 6: " << inserted.second << '\n'
               << "value at returned position: " << *inserted.first << '\n'
               << "inserted duplicate 8: " << duplicate.second << '\n';
   }

Because a ``set`` is not an indexed container, looking up a value is a search.
The :container:`set::find <set/find>` function returns an :term:`iterator` to
the element with a specific key, or ``end()`` when the key is absent:

.. tb-code:: cpp
   :name: set_find_ac

   #include <iostream>
   #include <set>

   int main() {
     auto x = std::set<int> {2, 7, 1, 8, 4, 5, 9};
     const auto it = x.find(8);
     if (it != x.end()) {
       std::cout << "found: " << *it << '\n';
     }
   }

.. cpp:: 20

   C++20 added :container:`set::contains <set/contains>` for membership
   checks. It returns a Boolean and avoids creating an iterator when the
   position is not needed.

   .. tb-code:: cpp
      :name: set_contains_ac

      #include <iostream>
      #include <set>

      int main() {
        const auto x = std::set<int> {2, 7, 1, 8, 4, 5, 9};
        std::cout << std::boolalpha
                  << x.contains(8) << ' '
                  << x.contains(3) << '\n';
      }

The :container:`set::erase <set/erase>` function removes an element from a
``set``. When given an iterator, it removes the element at that position and
does not invalidate iterators to other elements:

.. tb-code:: cpp
   :name: set_erase_ac

   #include <iostream>
   #include <set>

   int main() {
     auto x = std::set<int> {2, 7, 1, 8, 4, 5, 9};
     const auto it = x.find(8);
     if (it != x.end()) {
       x.erase(it);
     }

     std::cout << std::boolalpha
               << (x.find(8) == x.end()) << '\n';
   }

.. cpp:: 20

   C++20 also provides :algorithm:`std::erase_if <erase_if>` for removing
   every element that satisfies a predicate. This is useful when the value
   to remove is described by a condition rather than a single key.

   .. tb-code:: cpp
      :name: set_erase_if_ac

      #include <iostream>
      #include <set>

      int main() {
        auto x = std::set<int> {2, 7, 1, 8, 4, 5, 9};
        std::erase_if(x, [](int value) { return value % 2 == 0; });

        for (const auto value : x) {
          std::cout << value << ' ';
        }
        std::cout << '\n';
      }

.. index:: multiset, unordered_set, unordered_multiset

Variations on ``std::set``
--------------------------
The standard library provides related ordered and unordered containers:

:container:`multiset`
   A ``set`` in which duplicate keys are allowed.

:container:`unordered_set`
   A container of unique objects organized by a :term:`hash function`, not by
   sorted order.
   Added in C++11.

   A key type needs a hash function and an equality predicate. The standard
   library provides these for many built-in and library types. For a user type,
   provide a ``std::hash<Key>`` specialization or a custom hash object, and
   provide equality through ``operator==`` or a custom equality object.
     
:container:`unordered_multiset`
   An ``unordered_set`` in which duplicate keys are allowed.
  

-----

.. admonition:: More to Explore

   - :cpp:`Standard library containers <container>`
   - :container:`std::set <set>`
   - :container:`std::unordered_set <unordered_set>`
