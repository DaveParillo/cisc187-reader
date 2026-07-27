..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: algorithms

Background
==========

Recall from :doc:`../class-IV-templates/containers` that a container
is a generic collection.
Containers allow us to store data using *well-known* data structures.
The standard library containers provide reusable interfaces and behavior that
we can use directly or study when designing custom containers.

Recall from :doc:`../list/iterators` that an iterator
is a :term:`type` that performs operations that *feel* like a pointer.
Although an iterator allows syntax very similar to a pointer,
it is not a pointer.
Each container is responsible for its own iterators.
When a container is created, it has the ability to create an iterator
that knows how to visit elements of the type stored in the container.

Now that we have these two tools in the standard library,
we want to use them to solve problems.
It turns out that many programming tasks fall into basic groups:

- find
- copy
- sum
- count
- sort

These are all *actions* that we perform on *sequences*.
The goal of standard library algorithms is to define these actions in a generic
way. They satisfy this goal using small,
reusable functions that avoid writing repetitive code
and define a consistent, portable interface.

The :term:`abstractions <abstraction>` in the standard library are primarily
concerned with performing actions on data accessed through iterator ranges.
Consider that counting elements in a :term:`list` is not very different
from counting elements in a :term:`vector`.


.. index:: ISO C++ standard
   single: for_each
   single: count(_if)
   single: find(_if)
   single: search
   single: copy(_if)
   single: move
   single: transform
   single: generate
   single: is_partitioned
   single: partition_copy
   single: stable_partition
   single: is_sorted
   single: sort
   single: stable_partition
   single: lower_bound
   single: binary_search
   single: equal_range
   single: merge
   single: includes
   single: set_difference
   single: set_union
   single: is_heap
   single: make_heap
   single: sort_heap
   single: max
   single: min
   single: max_element
   single: clamp
   single: equal
   single: lexicographical_compare
   single: is_permutation
   single: next_permutation
   single: iota
   single: accumulate
   single: inner_product
   single: reduce
   single: uninitialized_copy
   single: uninitialized_fill
   single: destroy

Standard library algorithms at a glance
---------------------------------------
The standard library algorithms are part of the
`ISO C++ Standard <https://isocpp.org/std/the-standard>`__.
The library provides algorithms for searching, counting, comparing, rearranging,
sorting, and manipulating ranges. The set of available algorithms grows as new
C++ standards add capabilities and new overloads.

The algorithms are organized into broad categories:

.. list-table::
   :header-rows: 1

   * - Algorithm operations
     - Example algorithms
   * - Non-modifying sequence operations
     - :algorithm:`for_each`, :algorithm:`count_if <count>`,
       :algorithm:`find_if <find>`, :algorithm:`search`
   * - Modifying sequence operations
     - :algorithm:`copy_if <copy>`, :algorithm:`move`,
       :algorithm:`swap`, :algorithm:`transform`
   * - Partitioning operations
     - :algorithm:`is_partitioned`, :algorithm:`partition_copy`,
       :algorithm:`stable_partition`
   * - Sorting operations
     - :algorithm:`is_sorted`, :algorithm:`sort`, :algorithm:`stable_sort`
   * - Binary search operations
     - :algorithm:`lower_bound`, :algorithm:`binary_search`,
       :algorithm:`equal_range`
   * - Set operations
     - :algorithm:`merge`, :algorithm:`includes`,
       :algorithm:`set_difference`, :algorithm:`set_union`
   * - Heap operations
     - :algorithm:`is_heap`, :algorithm:`make_heap`,
       :algorithm:`sort_heap`
   * - Min/max operations
     - :algorithm:`max`, :algorithm:`min`,
       :algorithm:`max_element`, :algorithm:`clamp`
   * - Comparison operations
     - :algorithm:`equal`, :algorithm:`lexicographical_compare`
   * - Permutation operations
     - :algorithm:`is_permutation`, :algorithm:`next_permutation`
   * - Numeric operations
     - :algorithm:`iota`, :algorithm:`accumulate`,
       :algorithm:`inner_product`, :algorithm:`reduce`
   * - Uninitialized memory operations
     - :memory:`uninitialized_copy`, :memory:`uninitialized_fill`,
       :memory:`destroy`


Numeric algorithms are grouped together because they combine or generate
values, but several other standard algorithms also perform arithmetic as part
of their work. The categories above are a guide for finding related
operations, not an exhaustive classification of every algorithm.

.. index:: 
   pair: algorithms; loops


Standard library algorithms and loops
-------------------------------------
Many standard library algorithms are reusable patterns for traversing a range.
They often take a range of elements and an operation that is performed on each
element, although some algorithms do more than a simple loop or have optimized
implementations.
Structurally, this makes them similar to loops.

Most tasks you've written so far could be rewritten using algorithms.

One way to think about standard library algorithms is to consider them
*named loops*.
That is, a loop that is important and general enough
to justify getting named and encapsulated in its own function.

:algorithm:`iota` is a standard library algorithm that fills a range
``[first, last)``
with sequentially increasing values.
This is the sort of algorithm that occurs often enough that it was decided
to include it in the standard library 
(but not until C++11).

The example below shows a possible implementation.

.. tb-group::
   :name: iota

   .. tb-tab:: Example: iota

      The parameter ``value`` defines the start value.
      This value is assigned to ``first``,
      and both ``first`` and ``value`` are incremented.

      .. literalinclude:: iota.txt
         :language: cpp
         :start-at: template
         :end-before: void print
         :dedent: 3
         :linenos:

   .. tb-tab:: Run It

      .. include:: iota.txt

Why prefer algorithms to hand-written loops?

- Reuse and clarity

  An algorithm gives a common name to a well-defined operation. It can make
  the intent of the code easier to recognize and avoids repeating the same
  loop structure in multiple places. Standard implementations are also
  carefully designed and may take advantage of library- or platform-specific
  optimizations, but an algorithm call is not automatically faster than an
  equivalent hand-written loop.

- Correctness

  Writing loops exposes more bookkeeping details than an algorithm call.
  As a programmer you have to worry about initializing the loop,
  incrementing the loop, terminating the loop as well as the loop body.

  When calling an algorithm, you still need to provide a valid range, the
  required iterator category, suitable predicates, and any required output
  range. The algorithm handles the traversal and its documented edge cases,
  but it cannot make an invalid range or invalid predicate safe.

  Often you don't even need to care about the body - the algorithm takes care
  of all the details for you. Sometimes a lambda or function pointer is expected.

  Standard library implementations receive extensive review and testing.
  Using them avoids maintaining another copy of a common operation, provided
  the caller follows the algorithm's documented contract.


- Maintainability

  Algorithm calls result in clearer code.
  The standard library is designed around a simple, consistent set of
  interfaces.
  The more you use these interfaces, the more consistently
  your own code will be structured.

  When combined together, algorithms can eliminate code that would otherwise
  need to be written and can make the result more straightforward than a
  collection of explicit loops.

  Code you use from the standard libray is code you don't need to maintain.
  The less code you have to maintain, the cheaper and easier it is to maintain.


-----

.. admonition:: More to Explore

  - From cppreference.com

    - Overview of the :cpp:`algorithms <algorithm>` library
    - :algorithm:`std::iota <iota>`
    - :cpp:`C++20 Ranges Library <ranges>`
