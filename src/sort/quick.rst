..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
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

.. _sort_quick:

.. index::
   single: quick sort
   pair: sorting algorithms; quick sort
   pair: quick sort; pivot
   pair: quick sort; partitioning

Quick sort
==========
The **quick sort** uses divide and conquer to gain the same advantages
as the merge sort, while not using additional storage. As a trade-off,
however, it is possible that the list may not be divided in half. When
this happens, we will see that performance is diminished.

A quick sort first selects a value, which is called the **pivot value**.
Although there are many different ways to choose the pivot value, we
will simply use the first item in the list. The role of the pivot value
is to assist with splitting the list. The actual position where the
pivot value belongs in the final sorted list, commonly called the
**split point**, will be used to divide the list for subsequent calls to
the quick sort.

The :ref:`following sequence <fig_splitvalue>` shows how partitioning
places the first pivot, 54, at its split point. The
:ref:`marker scans and exchanges <fig_partitionA>` lead to a
:ref:`completed partition <fig_partitionB>` ready for recursive sorting.

.. tb-deck::
   :name: quick-sort-process
   :caption: Quick sort: choose a pivot, partition, and recurse

   .. tb-card::
      :name: fig_splitvalue
      :caption: Choose 54 as the first pivot.

      The first item, 54, is the pivot value. Partitioning will find its
      split point and exchange items so that smaller values lie to its left
      and larger values lie to its right.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Choose 54 as the first pivot.
         :highlight: data.node[a]
         :indicators: pivot=a
         :show-indices:

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :name: fig_partitionA
      :caption: Start the left and right markers.

      Set ``leftmark`` to position 1 and ``rightmark`` to position 8.
      These markers scan toward each other through the items after the pivot.

      Advance ``leftmark`` past values less than or equal to the pivot.
      Move ``rightmark`` left past values greater than or equal to the pivot.
      Each scan stops if the markers cross. Equal values may end up on either
      side of the pivot.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Start the left and right markers.
         :highlight: data.node[b] data.node[i]
         :indicators: pivot=a leftmark=b rightmark=i
         :show-indices:

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Move leftmark past 26; stop at 93.

      At position 1, 26 is less than 54, so advance ``leftmark`` to
      position 2. Stop there because 93 is greater than the pivot.
      This value belongs on the right side of the eventual split point.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Move leftmark past 26; stop at 93.
         :highlight: data.node[c]
         :indicators: pivot=a leftmark=c rightmark=i
         :show-indices:

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Stop rightmark at 20.

      At position 8, 20 is less than 54, so ``rightmark`` stops immediately.
      The markers have not crossed: position 2 is before position 8.
      The values 93 and 20 are on the wrong sides and must be exchanged.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Stop rightmark at 20.
         :highlight: data.node[c] data.node[i]
         :indicators: pivot=a leftmark=c rightmark=i
         :show-indices:

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Exchange 93 and 20.

      Exchange the values at positions 2 and 8. Position 2 now holds 20,
      and position 8 holds 93. Keep the pivot at position 0 and resume the
      scans from the current marker positions.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Exchange 93 and 20.
         :highlight: data.node[c] data.node[i]
         :indicators: pivot=a leftmark=c rightmark=i
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[93]

   .. tb-card::
      :caption: Move leftmark past 20 and 17; stop at 77.

      The values 20 at position 2 and 17 at position 3 are less than 54.
      Advance ``leftmark`` past both to position 4. Stop at 77 because it
      is greater than the pivot.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Move leftmark past 20 and 17; stop at 77.
         :highlight: data.node[e]
         :indicators: pivot=a leftmark=e rightmark=i
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[93]

   .. tb-card::
      :caption: Move rightmark past 93 and 55; stop at 44.

      The values 93 at position 8 and 55 at position 7 are greater than 54.
      Move ``rightmark`` left past both to position 6. Stop at 44 because
      it is less than the pivot. The markers have not crossed, so exchange
      77 and 44.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Move rightmark past 93 and 55; stop at 44.
         :highlight: data.node[e] data.node[g]
         :indicators: pivot=a leftmark=e rightmark=g
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[93]

   .. tb-card::
      :caption: Exchange 77 and 44.

      Exchange the values at positions 4 and 6. Position 4 now holds 44,
      and position 6 holds 77. Resume both scans to find the split point.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Exchange 77 and 44.
         :highlight: data.node[e] data.node[g]
         :indicators: pivot=a leftmark=e rightmark=g
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[44]
         f[31]
         g[77]
         h[55]
         i[93]

   .. tb-card::
      :caption: Move leftmark past 44 and 31; stop at 77.

      The values 44 at position 4 and 31 at position 5 are less than 54.
      Advance ``leftmark`` to position 6 and stop at 77. Both markers now
      point to position 6; they have met but have not yet crossed.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Move leftmark past 44 and 31; stop at 77.
         :highlight: data.node[g]
         :indicators: pivot=a leftmark=g rightmark=g
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[44]
         f[31]
         g[77]
         h[55]
         i[93]

   .. tb-card::
      :caption: Move rightmark left; the markers cross.

      At position 6, 77 is greater than 54, so move ``rightmark`` left to
      position 5, which holds 31. Now ``rightmark`` is less than ``leftmark``:
      5 is less than 6. Stop scanning without another exchange between the
      markers. Position 5 is the split point.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Move rightmark left; the markers cross.
         :highlight: data.node[f] data.node[g]
         :indicators: pivot=a leftmark=g rightmark=f
         :show-indices:

         a[54]
         b[26]
         c[20]
         d[17]
         e[44]
         f[31]
         g[77]
         h[55]
         i[93]

   .. tb-card::
      :name: fig_partitionB
      :caption: Exchange the pivot with 31 at the split point.

      Exchange the pivot at position 0 with 31 at position 5. The pivot
      value 54 is now at its final sorted position.

      Positions 0 through 4 contain [31, 26, 20, 17, 44], all less than 54.
      Positions 6 through 8 contain [77, 55, 93], all greater than 54.
      The two ranges are partitioned, but are not yet sorted.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Exchange the pivot with 31 at the split point.
         :highlight: data.node[a] data.node[f]
         :indicators: pivot=f
         :show-indices:

         a[31]
         b[26]
         c[20]
         d[17]
         e[44]
         f[54]
         g[77]
         h[55]
         i[93]

   .. tb-card::
      :caption: Recursively sort the ranges on either side of 54.

      Apply quick sort to positions 0 through 4, then to positions 6
      through 8. Each recursive call selects the first item of its range
      as a pivot and repeats the same partition process.

      These ranges stay in the original array. Exclude position 5 from
      both calls because 54 is already in place. A range with zero or one
      item is sorted by definition and needs no partition. Continuing the
      recursion produces [17, 20, 26, 31, 44, 54, 55, 77, 93].

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Recursively sort the ranges on either side of 54.
         :highlight: data.node[f]
         :indicators: pivot=f
         :show-indices:

         a[31]
         b[26]
         c[20]
         d[17]
         e[44]
         f[54]
         g[77]
         h[55]
         i[93]


.. tb-group::
   :name: lst_quick_sort

   .. tb-tab:: Quick Sort

      The ``partition`` function implements the process described earlier.
      The following program sorts the 
      list that was used in the example above.

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: lst_quick_cpp
         :caption: The Quick Sort

         #include <iostream>
         #include <string>
         #include <utility>
         #include <vector>
         using std::vector;

         void print(const vector<int>& data) {
            for (const auto& value: data) {
               std::cout << value << ' ';
            }
            std::cout << '\n';
         }

         template <typename RandomIt>
         RandomIt partition(RandomIt first, RandomIt last) {
            if (first == last) return first;

            auto pivotvalue = *first;
            RandomIt leftmark  = first + 1;
            RandomIt rightmark = last - 1;
            bool done = false;
            while (!done) {
               while(leftmark <= rightmark &&
                     *leftmark <= pivotvalue) {
                 ++leftmark;
               }
               while(rightmark >= leftmark &&
                     *rightmark >= pivotvalue) {
                 --rightmark;
               }
               if(rightmark<leftmark) {
                  done = true;
               } else {
                  std::swap(*rightmark, *leftmark);
               }
            }
            std::swap(*rightmark, *first); //*
            return rightmark;
         }

         template <typename RandomIt>
         void quick_sort(RandomIt first, RandomIt last)
         {
            if (std::distance(first, last) > 1) {
                 RandomIt pivot = partition(first, last);
                 quick_sort(first, pivot);
                 quick_sort(pivot + 1, last);
            }
         }

         int main() {
           vector<int> data = {54, 26, 93, 17, 77, 31, 44, 55, 20};
           quick_sort(data.begin(), data.end());
           print(data);
           return 0;
         }


The following animations show quick sort in action. Yellow marks the current
pivot, red marks values being compared or exchanged, teal marks a scan
boundary, and gray marks pivot values that have been placed.

.. Sort animation assets are generated with ``generate_sort_video.py``.

.. only:: html

   .. tb-group::
      :name: quick-sort-animations

      .. tb-tab:: Average case

         .. tb-video:: ../_static/generated/sort/quick-sort-average.webm
            :name: quick-sort-average-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/quick-sort-average.png

      .. tb-tab:: Best case

         .. tb-video:: ../_static/generated/sort/quick-sort-best.webm
            :name: quick-sort-best-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/quick-sort-best.png

      .. tb-tab:: Worst case

         .. tb-video:: ../_static/generated/sort/quick-sort-worst.webm
            :name: quick-sort-worst-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/quick-sort-worst.png

.. only:: not html

   .. figure:: ../_static/generated/sort/quick-sort-average.png
      :alt: Quick sort summary for an average input.

   .. figure:: ../_static/generated/sort/quick-sort-best.png
      :alt: Quick sort summary for an already sorted input.

   .. figure:: ../_static/generated/sort/quick-sort-worst.png
      :alt: Quick sort summary for a reverse-sorted input.

Quick sort analysis
-------------------

To analyze the ``quick_sort`` function, note that for a list of length
*n*, if the partition always occurs in the middle of the list, there
will again be :math:`\log n` divisions. In order to find the split
point, each of the *n* items needs to be checked against the pivot value. 
Therefore, the average case complexity is :math:`n\cdot \log n`. 
In addition, there is no copying of list data as in the merge sort process.

The ideal pivot selection point is the median **value** in the data set,
however the cost to find the median often exceeds the benefits for many typical
data sets.

Unfortunately, in the worst case, the split points may not be in the
middle and can be very skewed to the left or the right, leaving a very
uneven division. In this case, sorting a list of *n* items divides into
sorting a list of 0 items and a list of :math:`n-1` items. Then
sorting a list of :math:`n-1` divides into a list of size 0 and a list
of size :math:`n-2`, and so on. The result is an :math:`O(n^{2})`
sort with all of the overhead that recursion requires.
This worst case example is shown in the above code example.

A recursive :math:`O(n^{2})` algorithm makes quick sort susceptible to
stack overflow errors on very large data sets.

Quick sort therefore poses an interesting dilemma.
The quick sort average case is very fast.
It tends to be the fastest, on average, of the known :math:`O(n \cdot log{n})`
average case sorting algorithms in actual clock time.
But its worst case is just dreadful.

So the suitability of quick sort winds up coming down to a question of
how often we would actually expect to encounter the worst case or 
*nearly* worst case behavior.
That, in turn, depends upon the choice of pivot.

We mentioned earlier that there are different ways to choose the pivot
value. In particular, we can attempt to alleviate some of the potential
for an uneven division by using a technique called **median of three**.
To choose the pivot value, we will consider the first, the middle, and
the last element in the list. In our example, those are 54, 77, and 20.
Now pick the median value, in our case 54, and use it for the pivot
value (of course, that was the pivot value we used originally). The idea
is that in the case where the first item in the list does not belong
toward the middle of the list, the median of three will choose a better
"middle" value. This will be particularly useful when the original list
is somewhat sorted to begin with. We leave the implementation of this
pivot value selection as an exercise.


**Self Check**

.. tb-group::
   :name: tab_check

   .. tb-tab:: Q1

      .. tb-choice::
         :name: question_sort_7

         Given the following list of numbers
         [14, 17, 13, 15, 19, 10, 3, 16, 9, 12] which answer shows the 
         contents of the list after the second partitioning according to the
         quicksort algorithm?

         - [ ] [9, 3, 10, 13, 12]

           It's important to remember that quicksort works on the entire list and sorts it in place.
         - [ ] [9, 3, 10, 13, 12, 14]

           Remember quicksort works on the entire list and sorts it in place.
         - [ ] [9, 3, 10, 13, 12, 14, 17, 16, 15, 19]

           The first partitioning works on the entire list, and the second partitioning works on the left partition not the right.
         - [x] [9, 3, 10, 13, 12, 14, 19, 16, 15, 17]

           The first partitioning works on the entire list, and the second partitioning works on the left partition.

   .. tb-tab:: Q2

      .. tb-choice::
         :name: question_sort_8

         Given the following list of numbers 
         [1, 20, 11, 5, 2, 9, 16, 14, 13, 19] 
         what would be the first pivot value using the median of 3 method?


         - [ ] 1

           The three numbers used in selecting the pivot are 1, 9, 19.  1 is not the median, and would be a very bad choice for the pivot since it is the smallest number in the list.
         - [x] 9

           Good job.
         - [ ] 16

           although 16 would be the median of 1, 16, 19 the middle is at len(list) // 2.
         - [ ] 19

           the three numbers used in selecting the pivot are 1, 9, 19.  9 is the median.  19 would be a bad choice since it is almost the largest.

   .. tb-tab:: Q3

      .. tb-choice::
         :name: question_sort_9

         Which of the following sort algorithms are guaranteed to be 
         O(n log n) even in the worst case?

         - [ ] Shell Sort

           Shell sort is between O(n) and O(n^2)
         - [ ] Quick Sort

           Quick sort can be O(n log n), but if the pivot points are not well chosen and the list is just so, it can be O(n^2).
         - [x] Merge Sort

           Merge Sort is the only guaranteed O(n log n) even in the worst case. The cost is that merge sort uses more memory.
         - [ ] Insertion Sort

           Insertion sort is O(n^2)

   .. tb-tab:: Q4

      .. tb-match::
         :name: question_sort_10

         Match each sorting method with its appropriate estimated comparisons.

         Quick Sort
            O(n log n) or O(n^2)
         Insertion/Bubble/Merge
            O(n^2)
         Merge Sort
            O(n log n)
         Shell Sort
            between O(n) and O(n^2)

   .. tb-tab:: Q5

      .. tb-choice::
         :name: sortefficiencyrandom

         Which sort should you use for best efficiency
         if you need to sort through 100,000 random items in a list?



         - [x] Merge

           Correct!
         - [ ] Selection

           Selection sort is inefficient in large lists.
         - [ ] Bubble

           Bubble sort works best with mostly sorted lists.
         - [ ] Insertion

           Insertion sort works best with either small or mostly sorted lists.

.. admonition:: More to Explore

   - `OpenDSA: Quicksort <https://opendsa.cs.vt.edu/ODSA/Books/eu_book/html/Quicksort.html>`__
   - :cpp:`C++ std::nth_element <algorithm/nth_element>`
   - `Quick Sort visualization <https://visualgo.net/en/sorting>`__

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/ns/books/published/cppds/index.html?mode=browsing>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__.
