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
The STL containers provide the patterns we can use to make
custom containers, if needed.

Recall from :doc:`../list/iterators` that an iterator
is a :term:`type` that performs operations that *feel* like a pointer.
Although an iterator allows syntax very similar to a pointer,
it is not a pointer.
Each container is responsible for its own iterators.
When a container is created, it has the ability to create an iterator
that knows how to visit elements of the type stored in the container.

Now that we have these two great tools in the STL,
we want to use them to solve problems.
It turns out that many programming tasks fall into basic groups:

- find
- copy
- sum
- count
- sort

These are all *actions* that we perform on *sequences*.
The goal of the STL algorithms is to define these actions in a generic way.
The STL algorithms satisfy this goal using small, 
reusable functions that avoid writing repetitive code
and define a consistent, portable interface.

The :term:`abstractions <abstraction>` in the STL are primarily
concerned with performing actions on data stored in STL containers.
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

STL Algorithms at a glance
--------------------------
The STL algorithms are part of the 
`ISO C++ Standard <https://isocpp.org/std/the-standard>`__.
Currently, it contains more than 150 algorithms for 
searching, counting, and manipulating ranges.
C++17 alone added 69 more algorithms to the library.
While most of these (but not all) were new overloads to existing algorithms,
it does demonstrate the dynamic nature of the STL and its growth.

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
     - :algorithm:`is_sorted`, :algorithm:`sort`, :algorithm:`stable_partition`
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


Notice that only a single category of algorithms is considered 'numeric'.
In C++11, only 5 algorithms specifically do numeric computations.
C++17 adds 6 more.

.. index:: 
   pair: algorithms; loops


STL algorithms and loops
------------------------
Most STL algorithms are essentially wrappers around loops.
They often take a range of elements and an operation that is performed on each element.
Structurally, this makes them similar to loops.

Most tasks you've written so far could be rewritten using algorithms.

One way to think about STL algorithms is to consider them *named loops*.
That is, a loop that is important and general enough
to justify getting named and encapsulated in its own function.

:algorithm:`iota` is a STL algorithm that fills a range ``[first, last)`` 
with sequentially increasing values.
This is the sort of algorithm that occurs often enough that it was decided
to include it in the standard library 
(but not until C++11).

.. tabbed:: iota

   .. tab:: Example: iota

      The parameter ``value`` defines the start value.
      This value is assigned to ``first``,
      and both ``first`` and ``value`` are incremented.

      .. literalinclude:: iota.txt
         :language: cpp
         :start-after: // possible
         :end-before: void print
         :dedent: 3
         :linenos:

      Note the order of operations on 5.

      - First ``first`` is dereferenced and ``value`` is assigned.
      - **Then** the iterator is incremented.

   .. tab:: Run It

      .. include:: iota.txt

      See this example running `step-by-step
      <http://www.pythontutor.com/cpp.html#code=%23include%20%3Ciomanip%3E%0A%23include%20%3Ciostream%3E%0A%23include%20%3Cvector%3E%0A%0Atemplate%3Ctypename%20ForwardIterator,%20typename%20T%3E%0Avoid%20iota%28ForwardIterator%20first,%20%0A%20%20%20%20%20%20%20%20%20%20ForwardIterator%20last,%20T%20value%29%20%7B%0A%20%20while%28first%20!%3D%20last%29%20%7B%0A%20%20%20%20*first%2B%2B%20%3D%20value%3B%0A%20%20%20%20%2B%2Bvalue%3B%0A%20%20%7D%0A%7D%0A%0Avoid%20print%28const%20std%3A%3Avector%3Cint%3E%26%20v%29%20%7B%0A%20%20for%20%28auto%20x%3A%20v%29%20%7B%0A%20%20%20%20std%3A%3Acout%20%3C%3C%20std%3A%3Asetw%283%29%20%3C%3C%20x%3B%0A%20%20%7D%0A%20%20std%3A%3Acout%20%3C%3C%20'%5Cn'%3B%0A%7D%0A%0Aint%20main%20%28%29%20%7B%0A%20%20std%3A%3Avector%3Cint%3E%20nums%2813%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Before%20iota%3A%22%3B%0A%20%20print%28nums%29%3B%0A%20%20%20%20%20%0A%20%20iota%28nums.begin%28%29,%20nums.end%28%29,%20-6%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22After%20iota%3A%20%22%3B%0A%20%20print%28nums%29%3B%0A%7D%0A&curInstr=35&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D>`__

      
Why prefer algorithms to hand-written loops?

- Efficiency, for one.

  Algorithms are often more efficient than the loops programmers produce.
  The developers of the STL have had overt 20 years to consider how to make these
  algorithms efficient.
  Many algorithms have code to handle specific edge cases your initial implementations
  might overlook.

- Correctness

  Writing loops is more subject to errors than algorithm calls.
  As a programmer you have to worry about initializing the loop,
  incrementing the loop, terminating the loop as well as the loop body.

  When calling an algorithm, you only need to get the start and end
  iterators correct.

  Often you don't even need to care about the body - the algorithm takes care
  of all the details for you. Sometimes a lambda or function pointer is expected.

  The STL implementations have been carefully reviewed and tested in
  many thousands of programs.
  It is safe to say that any STL algorithm has been tested more thoroughly
  than any comparable code you write yourself.


- Maintainability

  Algorithm calls result in clearer code.
  The STL is designed around a simple consistent set of interfaces.
  The more you use these interfaces, the more consistently
  your own code will be structured.

  When combined together, algorithms can eliminate lots of code
  you other wise would have needed to write and
  results in more straightforward than the corresponding explicit loops.

  Code you use from the STL is code you don't need to maintain.
  The less code you have to maintain, the cheaper and easier it is to maintain.


-----

.. admonition:: More to Explore

   - From cppreference.com

     - Overview of the `algorithms <http://en.cppreference.com/w/cpp/algorithm>`_ library

