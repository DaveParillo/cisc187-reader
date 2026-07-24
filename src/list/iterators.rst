..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| replace:: --

.. index::
   single: iterable types

Iterable Types
==============
How can we visit each :term:`element` in a :term:`container`
without depending on the container's storage details?
For example, an array stores elements contiguously, while a list stores
elements in separate nodes. Both can still be visited in order.

Positional indexing
-------------------
An indexed loop works when the container provides positional access through
``operator[]``. An array is one example:

.. tb-code:: cpp
   :name: iterators_indexed_array_ac

   #include <array>
   #include <cstddef>
   #include <iostream>
   #include <string>

   int main() {
     const std::array<std::string, 3> names = {"Alice", "Bob", "Clara"};

     for (std::size_t i = 0; i < names.size(); ++i) {
       std::cout << names[i] << '\n';
     }
   }

The loop above depends on two operations: ``size()`` and ``operator[]``.
``std::list`` does not provide positional access through either ``operator[]``
or ``at()``. A loop that assumes an integer position therefore cannot be
adapted to a list by changing only the container type.

``std::set`` also has no positional indexing. ``std::map`` is different:
it provides ``operator[]`` for lookup by key, not for locating an element by
position. For example, ``records[42]`` asks for the value associated with key
``42``; it does not mean the forty-third element.

Range-based for loops
---------------------
The :lang:`range-based for loop <range-for>` avoids explicit indexing.
The same loop syntax works for standard containers with ``begin()`` and
``end()``, including both arrays and lists:

.. tb-code:: cpp
   :name: iterators_range_for_ac

   #include <array>
   #include <iostream>
   #include <list>
   #include <string>

   int main() {
     const std::array<std::string, 3> names = {"Alice", "Bob", "Clara"};
     const std::list<int> ages = {27, 3, 1};

     std::cout << "names:";
     for (const auto& name : names) {
       std::cout << ' ' << name;
     }
     std::cout << '\n';

     std::cout << "ages:";
     for (const auto& age : ages) {
       std::cout << ' ' << age;
     }
     std::cout << '\n';
   }

The declaration ``const auto&`` binds a reference to each existing element,
so the loop does not copy the element. The ``const`` prevents the loop body
from changing the container's elements. Use ``auto&`` when modification is
intended, or ``auto`` when an independent copy is useful.

The range-based loop hides the iterator syntax, but it still relies on the
same operations: obtain a beginning position, compare it with the end
position, dereference the current position, and advance to the next one.
We say that containers supporting this interface are :term:`iterable`.

-----

.. admonition:: More to Explore

  - :cpp:`Iterator Library <iterator>` at cppreference.com
  - :cpp:`C++ Concepts: Iterator <named_req/Iterator>`
