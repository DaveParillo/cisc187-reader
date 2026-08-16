..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; std::array

The ``std::array`` class
========================
The :container:`std::array <array>` is a container that encapsulates fixed size arrays.
Since it is literally a wrapper around a raw array,
the size of a ``std::array`` must be defined when declared.

.. code-block:: cpp

   std::array <int, 12> days_per_month;

The array class is very lightweight and has very little
costs over a raw array.
Additionally, ``std::array`` provides convenience functions such as:

:container:`at() <array/operator_at>` and :container:`operator[] <array/operator_at>` 
   range checked access and unchecked access

:container:`front() <array/front>` and :container:`back() <array/back>`
   access to the first and last elements

:container:`size() <array/size>` 
   return the number of elements

:container:`empty() <array/empty>` 
   check if the container is empty

Unlike a raw array, ``std::array`` cannot infer its size if
declared with an initializer list:

.. tb-code:: cpp

   #include <array>
   #include <iostream>
   using std::cout;

   int main() {
     // compile error: array template parameter missing:
     //std::array<char> letters = {{'h', 'o', 'w', 'd', 'y', '!'}};

     std::array<char, 6> letters = {{'h', 'o', 'w', 'd', 'y', '!'}};

     cout << "The first character is: " << letters.front() << '\n';
     cout << "The last character is: " << letters.back() << '\n';

     for (const auto& c: letters) {
       cout << c;
     }
   }

Container class member type aliases
-----------------------------------

All the standard library containers, including ``std::array``, provide a
large set of member types. Standard-library types publish aliases so generic
code can ask a container, "What type of elements, sizes, references, and
iterators do you use?" without knowing its implementation.

For a particular ``std::array<T, N>``, several answers may seem self-evident:
its ``size_type`` is ``std::size_t``, its ``pointer`` is ``T*``, and its
``reference`` is ``T&``.  A generic function, however, might be given an
array, a vector, a list, or a user-defined container. It should use
``Container::size_type`` rather than assume that every container chose
``std::size_t``. The alias is part of the container's public contract, and it
keeps generic code independent of that choice.

The most commonly used ``std::array`` aliases are:

- ``value_type``: the element type, ``T``.
- ``size_type``: the unsigned type used for sizes and indexes,
  ``std::size_t``.
- ``difference_type``: the signed type used for iterator distances,
  ``std::ptrdiff_t``. For a random-access container such as an array,
  ``end() - begin()`` has this type. It is signed because reversing the order
  of the operands can produce a negative distance.
- ``reference`` and ``const_reference``: ``T&`` and ``const T&``, the types
  produced by dereferencing a mutable or const iterator.
- ``pointer`` and ``const_pointer``: ``T*`` and ``const T*``.
- ``iterator`` and ``const_iterator``: the types returned by ``begin()`` and
  ``end()``. They allow standard algorithms to traverse the container without
  knowing how it stores its elements.

``std::array`` also provides reverse-iterator aliases.  We will examine the
requirements of iterator types, and how to implement an iterator class, in the
list chapter.



-----

.. admonition:: More to Explore

   - :cpp:`Containers library <container>`
   - :iterator:`std::iterator_traits <iterator_traits>`
