.. Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
   and/or modify this document under the terms of the GNU Free Documentation
   License, Version 1.3 or any later version published by the Free Software
   Foundation; with Invariant Sections being Forward, and Preface,
   no Front-Cover Texts, and no Back-Cover Texts.  A copy of
   the license is included in the section entitled "GNU Free Documentation
   License".
.. This file is adapted from the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

Best, worst, and average cases
==============================
Consider the problem of finding the factorial of :math:`n`.
For any given input, there is a single output.
For example, when :math:`n=2`, then :math:`n! = 2` and
when :math:`n=3`, then :math:`n! = 6` and
when :math:`n=4`, then :math:`n! = 24`.

.. tb-group::
   :name: rs-search

   .. tb-tab:: Find max

      Compare the factorial algorithm to a sequential search algorithm.

      .. code-block:: bash

         search(array: A)
            max_value ← 1
            index  ← 2
            while index < array_size(A)
               if A[index] > A[max_value]
                  max_value ← index
               done if
            done while

            return max_index
         done search

      The algorithm operates on arrays of varying size.
      Many different array sizes may be passed to this function.

      Regardless of the input array size,
      the algorithm evaluates each storage location exactly once.

   .. tb-tab:: Run It

      tbd



Compare finding the maximum value to finding a specific value.

When looking for a value :math:`K`, we can stop searching
as soon as the desired value is found.

This differs from the find max search algorithm
in which every location must always be examined.

.. tb-group::
   :name: search2

   .. tb-tab:: Best case

      .. code-block:: bash

         search(array: A, integer: K)
            index  ← 1
            while index < array_size(A)
               if A[index] ≡ K
                  return index
               done if
            done while
            return array_size(A)
         done search

      There are many possible running times for this algorithm.
      Given the following data:

      .. graphviz::
         :align: center

         digraph c {
           graph [
              fontname = "Bitstream Vera Sans"
              ranksep=0.1
           ];
           edge[constraint=false]
           node [
              fontsize = 14
              shape = box
              style=filled
              fillcolor=lightblue
           ]
           3 [fillcolor=palegreen]
           3->1->4->5->9->2->7->8->13->21
         }

      If searching for :math:`K = 3`, we are in luck: we will find it in the
      first element we examine.
      This is the **best case**.
      We can't search for less than one location.
      In this case, we find the value in the first place we look and
      return the index ``0``.


   .. tb-tab:: Average case

      .. code-block:: bash

         search(array: A, integer: K)
            index  ← 1
            while index < array_size(A)
               if A[index] ≡ K
                  return index
               done if
            done while
            return array_size(A)
         done search

      Given random assortments of data search very many times
      on arrays of many different sizes, we can expect many different
      running times.

      .. graphviz::
         :align: center

         digraph c {
           graph [
              fontname = "Bitstream Vera Sans"
              ranksep=0.1
           ];
           edge[constraint=false]
           node [
              fontsize = 14
              shape = box
              style=filled
              fillcolor=wheat
           ]
           3->1->4->5->9
           node [fillcolor=lightblue]
           9->2->7->8->13->21

         }

      If searching for :math:`K = 9`, then we find the value after we have
      examined half of the array.
      On average, the algorithm examines :math:`\frac{n+1}{2}` values.
      This is called the **average case** for this algorithm.

   .. tb-tab:: Worst case

      .. code-block:: bash

         search(array: A, integer: K)
            index  ← 1
            while index < array_size(A)
               if A[index] ≡ K
                  return index
               done if
            done while
            return array_size(A)
         done search

      If searching for :math:`K = 72`, then we won't find the value at all.
      But we don't know this until every element has been examined.

      .. graphviz::
         :align: center

         digraph c {
           graph [
              fontname = "Bitstream Vera Sans"
              ranksep=0.1
           ];
           edge[constraint=false]
           node [
              fontsize = 14
              shape = box
              style=filled
              fillcolor=lightcoral
           ]
           3->1->4->5->9->2->7->8->13->21->null
           null [label=""]
         }

      This is the **worst case**.
      In this case, we find don't find the value and
      return the size of the container.

      Because arrays use zero-based indexing,
      the size is is always a location *past the end* of the array.
      Returning a value beyond the range searched is a standard idiom for
      "The value was not found".

When analyzing an algorithm, should we study the best, worst, or
average case?
Normally we are not interested in the best case, because this might
happen only rarely and generally is too optimistic for a fair
characterization of the algorithm's running time.
In other words, analysis based on the best case is not likely to be
representative of the behavior of the algorithm.
However, there are rare instances where a best-case analysis is
useful --- in particular, when the best case has high probability of
occurring.
The Shellsort and
Quicksort
algorithms both can take advantage of the best-case running time
of Insertion sort
to become more efficient.

How about the worst case?
The advantage to analyzing the worst case is that you know for
certain that the algorithm must perform at least that well.
This is especially important for real-time applications,
such as for the computers that monitor an air traffic control system.
Here, it would not be acceptable to use an algorithm that can handle
:math:`n` airplanes quickly enough *most of the time*, but which
fails to perform quickly enough when all :math:`n` airplanes are coming
from the same direction.

For other applications --- particularly when we wish to aggregate
the cost of running the program many times on many different inputs ---
worst-case analysis might not be a representative measure of the
algorithm's performance.
Often we prefer to know the average-case running time.
This means that we would like to know the *typical* behavior of
the algorithm on inputs of size :math:`n`.
Unfortunately, average-case analysis is not always possible.
Average-case analysis first requires that we understand how the actual
inputs to the program (and their costs) are distributed with respect
to the set of all possible inputs to the program.
For example, it was stated previously that the sequential search
algorithm on average examines half of the array values.
This is only true if the element with value :math:`K` is
equally likely to appear in any position in the array.
If this assumption is not correct, then the algorithm does *not*
necessarily examine half of the array values in the average case.

The characteristics of a data distribution have a significant effect
on many search algorithms, such as those based on
hashing and search trees such as the
binary search tree.
Incorrect assumptions about data distribution can have disastrous
consequences on a program's space or time performance.

In summary, for real-time applications
we are likely to prefer a worst-case analysis of an algorithm.
Otherwise, we often desire an average-case analysis if we know enough
about the distribution of our input to compute the average case.
If not, then we must resort to worst-case analysis.


.. admonition:: More to Explore

   - `Average time complexity <https://yourbasic.org/algorithms/amortized-time-complexity-analysis/>`__


.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

