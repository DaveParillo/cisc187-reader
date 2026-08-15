..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; array

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

All the standard library containers, including ``std::array`` provide a
large set of 'member types'.
Standard-library types publish aliases so generic code can ask an iterator,
"What kinds of values and operations do you provide?" without knowing its
implementation.
:iterator:`std::iterator_traits <iterator_traits>` and
C++20 iterator/range concepts use
these names to adapt algorithms to many iterator types uniformly.

Commonly encountered type aliases:

- ``using pointer = T*;``
  The type of a pointer to the current element. For this iterator, it is an
  ordinary raw pointer.

- ``using reference = T&;``
  The type produced by dereferencing the iterator: ``*it``.
  It is a reference to the actual element, so modifying ``*it`` modifies that
  element.

- ``using difference_type = std::ptrdiff_t;``
  A signed integer type used for distances between iterators,
  such as ``last - first``.
  It must be signed because a distance can be negative.
  The standard describes every iterator as having a signed integer-like
  difference type.

- ``using iterator_category = std::forward_iterator_tag;``
  The legacy classification used by pre-C++20 algorithms and
  ``std::iterator_traits``.
  It means that this iterator supports forward traversal and the
  multi-pass guarantee: copied iterators can be advanced independently.

- ``using iterator_concept = std::forward_iterator_tag;``
  The C++20 classification used by iterator concepts and ranges. It states the
  same capability here, but is separate because an iterator's modern concept
  classification can be more precise than its legacy category. The standard
  checks iterator_concept first, then falls back to iterator_category.

For this simple iterator, both tags are forward_iterator_tag; including both
makes it work clearly with both older algorithms and C++20 ranges.



-----

.. admonition:: More to Explore

   - :cpp:`Containers library <container>`
   - :iterator:`std::iterator_traits <iterator_traits>`

