..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
   Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, vi

.. _sort_insertion:

.. index::
   single: insertion sort
   pair: sorting algorithms; insertion sort

Insertion sort
==============
What would you do if you have a stack of phone bills from the past
two years and you want to order by date?
A fairly natural way to handle this is to look at the first two
bills and put them in order.
Then take the third bill and put it into the right position with
respect to the first two, and so on.
As you take each bill, you would add it to the sorted pile that you
have already made.
This simple approach is the inspiration for
our first sorting algorithm, called **Insertion Sort**.

Insertion Sort iterates through a list of records.
For each iteration, the current record is inserted in turn at the
correct position within a sorted list composed of those records
already processed.
Given an array named ``data`` that stores :math:`n` records,
one way to implement an insertion sort could be this.

.. code-block:: cpp

   template <class Comparable>
   void insertion_sort(Comparable* data[], int n) {
     for (int i = 1; i < n; ++i) {
       for (int j = i; (j > 0) && (*data[j] < *data[j-1]); --j) {
         swap(data, j, j-1);
        }
      }
   }

.. tb-deck::
   :name: fig_insertionsort
   :caption: Insertion sort: growing the sorted prefix

   .. tb-card::
      :caption: Start with a sorted prefix of one item.

      This sort is still :math:`O(n^{2})`, but works differently from
      the bubble sort and selection sort, since it always maintains a
      sorted subvector at the start of the container. Each new item is
      inserted into this sorted prefix, making it one item larger.

      The outlined cells show the sorted prefix. Initially, it contains
      only 54. The remaining eight items have not yet been processed.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Initially, only the first cell, containing 54, belongs to the sorted prefix.
         :highlight: data.node[a]

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
      :caption: Pass 1: insert 26.

      Since 26 is less than 54, shift 54 one position to the right and
      insert 26 at the start. The sorted prefix now contains two items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 26, the first 2 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b]

         a[26]
         b[54]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 2: insert 93.

      Since 93 is greater than 54, it is already in the correct position.
      No shifts are needed. The sorted prefix now contains three items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 93, the first 3 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]

         a[26]
         b[54]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 3: insert 17.

      Shift 93, 54, and 26 one position to the right, then insert 17 at
      the start. The sorted prefix now contains four items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 17, the first 4 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d]

         a[17]
         b[26]
         c[54]
         d[93]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 4: insert 77.

      Shift 93 one position to the right. Since 54 is less than 77,
      insert 77 between 54 and 93. The sorted prefix now contains five
      items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 77, the first 5 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d] data.node[e]

         a[17]
         b[26]
         c[54]
         d[77]
         e[93]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 5: insert 31.

      Shift 93, 77, and 54 one position to the right. Stop at 26 and
      insert 31 immediately after it. The sorted prefix now contains
      six items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 31, the first 6 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d] data.node[e] data.node[f]

         a[17]
         b[26]
         c[31]
         d[54]
         e[77]
         f[93]
         g[44]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 6: insert 44.

      Shift 93, 77, and 54 one position to the right, then insert 44
      between 31 and 54. The sorted prefix now contains seven items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 44, the first 7 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d] data.node[e] data.node[f] data.node[g]

         a[17]
         b[26]
         c[31]
         d[44]
         e[54]
         f[77]
         g[93]
         h[55]
         i[20]

   .. tb-card::
      :caption: Pass 7: insert 55.

      Shift 93 and 77 one position to the right, then insert 55 between
      54 and 77. The sorted prefix now contains eight items.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 55, the first 8 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d] data.node[e] data.node[f] data.node[g] data.node[h]

         a[17]
         b[26]
         c[31]
         d[44]
         e[54]
         f[55]
         g[77]
         h[93]
         i[20]

   .. tb-card::
      :caption: Pass 8: insert 20; the array is sorted.

      Shift every value greater than 20 one position to the right.
      Stop at 17 and insert 20 immediately after it. All nine items now
      belong to the sorted prefix, so the sort is complete.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 20, all nine cells are sorted in ascending order.
         :highlight: data.node[a] data.node[b] data.node[c] data.node[d] data.node[e] data.node[f] data.node[g] data.node[h] data.node[i]

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]


We begin by assuming that a vector with one item (position :math:`0`) is
already sorted. On each pass, one for each item 1 through :math:`n-1`,
the current item is checked against those in the already sorted subvector.
As we look back into the already sorted subvector, we shift those items
that are greater to the right. When we reach a smaller item or the end
of the subvector, the current item can be inserted.

.. tb-deck::
   :name: fig_insertionpass
   :caption: Insertion sort: the fifth pass in detail

   .. tb-card::
      :caption: Save 31 before shifting any items.

      The fifth pass starts with a sorted prefix of five items: 17, 26,
      54, 77, and 93. The next item, 31, must be inserted into that prefix.
      Save a copy of 31 so that shifting larger values cannot overwrite it.

      The separate cell holds the saved value. In the following cards,
      an empty cell marks the position available for insertion.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Before the fifth pass, the sorted prefix ends at 93; 31 is next.
         :highlight: data.node[f]

         a[17]
         b[26]
         c[54]
         d[77]
         e[93]
         f[31]
         g[44]
         h[55]
         i[20]

      .. tb-graph:: saved
         :style: array
         :align: center
         :label: Saved value
         :alt: The saved value to insert is 31.

         current[31]

   .. tb-card::
      :caption: Compare 31 with 93.

      The saved value is 31. Since 93 is greater than 31, shift 93
      one position to the right, into the empty cell. The available
      insertion position moves one cell to the left.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Compare 93 with saved value 31; the empty cell is after 93.
         :highlight: data.node[e] data.node[f]

         a[17]
         b[26]
         c[54]
         d[77]
         e[93]
         f['']
         g[44]
         h[55]
         i[20]

      .. tb-graph:: saved
         :style: array
         :align: center
         :label: Saved value
         :alt: The saved value to insert is 31.

         current[31]

   .. tb-card::
      :caption: Compare 31 with 77.

      The previous shift placed 93 in the sixth cell. Since 77 is also
      greater than 31, shift 77 one position to the right into the empty
      cell.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Compare 77 with saved value 31; the empty cell is after 77.
         :highlight: data.node[d] data.node[e]

         a[17]
         b[26]
         c[54]
         d[77]
         e['']
         f[93]
         g[44]
         h[55]
         i[20]

      .. tb-graph:: saved
         :style: array
         :align: center
         :label: Saved value
         :alt: The saved value to insert is 31.

         current[31]

   .. tb-card::
      :caption: Compare 31 with 54.

      The previous shift placed 77 immediately before 93. Since 54 is
      greater than 31, shift 54 one position to the right into the empty
      cell.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: Compare 54 with saved value 31; the empty cell is after 54.
         :highlight: data.node[c] data.node[d]

         a[17]
         b[26]
         c[54]
         d['']
         e[77]
         f[93]
         g[44]
         h[55]
         i[20]

      .. tb-graph:: saved
         :style: array
         :align: center
         :label: Saved value
         :alt: The saved value to insert is 31.

         current[31]

   .. tb-card::
      :caption: Compare 31 with 26; stop shifting.

      The previous shift placed 54 immediately before 77. Since 26 is
      less than 31, no more shifts are needed. Insert the saved value,
      31, into the empty cell between 26 and 54.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: 26 is less than saved value 31; insert 31 into the empty cell.
         :highlight: data.node[b] data.node[c]

         a[17]
         b[26]
         c['']
         d[54]
         e[77]
         f[93]
         g[44]
         h[55]
         i[20]

      .. tb-graph:: saved
         :style: array
         :align: center
         :label: Saved value
         :alt: The saved value to insert is 31.

         current[31]

   .. tb-card::
      :caption: The fifth pass is complete; six items form the sorted prefix.

      Four comparisons and three shifts made room for 31. Inserting it
      after 26 extends the sorted prefix to six items. The outlined
      cells are sorted; 44, 55, and 20 still need to be inserted on later
      passes.

      .. tb-graph:: data
         :style: array
         :align: center
         :alt: After inserting 31, the sorted prefix is 17, 26, 31, 54, 77, 93.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e] data.node[f]

         a[17]
         b[26]
         c[31]
         d[54]
         e[77]
         f[93]
         g[44]
         h[55]
         i[20]


In the following animations, yellow marks the value being inserted, red marks
a value being shifted, and gray marks the sorted prefix.

.. Sort animation assets are generated with ``generate_sort_video.py``.

.. only:: html

   .. tb-group::
      :name: insertion-sort-animations

      .. tb-tab:: Average case

         .. tb-video:: ../_static/generated/sort/insertion-sort-average.webm
            :name: insertion-sort-average-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/insertion-sort-average.png

      .. tb-tab:: Best case

         .. tb-video:: ../_static/generated/sort/insertion-sort-best.webm
            :name: insertion-sort-best-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/insertion-sort-best.png

      .. tb-tab:: Worst case

         .. tb-video:: ../_static/generated/sort/insertion-sort-worst.webm
            :name: insertion-sort-worst-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/insertion-sort-worst.png

.. only:: not html

   .. figure:: ../_static/generated/sort/insertion-sort-average.png
      :alt: Insertion sort summary for an average input.

   .. figure:: ../_static/generated/sort/insertion-sort-best.png
      :alt: Insertion sort summary for an already sorted input.

   .. figure:: ../_static/generated/sort/insertion-sort-worst.png
      :alt: Insertion sort summary for a reverse-sorted input.

.. _lst-insertion-sort-code:

Insertion sort analysis
-----------------------

.. tb-group::
   :name: lst_insertion_sort

   .. tb-tab:: Insertion Sort

      The implementation of ``insertion_sort`` 
      (:ref:`Run It <lst-insertion-sort-code>`) shows that
      there are again :math:`n-1` passes to sort *n* items. The iteration
      starts at position 1 and moves through position :math:`n-1`, as these
      are the items that need to be inserted back into the sorted subvectors.
      Line 8 performs the shift operation that moves a value up one position
      in the vector, making room behind it for the insertion.
      Remember that this
      is not a complete exchange as was performed in the previous algorithms.

      The maximum number of comparisons for an insertion sort is the sum of
      the first :math:`n-1` integers. Again, this is :math:`O(n^{2})`.
      However, in the best case, only one comparison needs to be done on each
      pass. This would be the case for an already sorted vector.

      One note about shifting versus exchanging is also important. In general,
      a shift operation requires approximately a third of the processing work
      of an exchange since only one assignment is performed. In benchmark
      studies, insertion sort will show very good performance.

   .. tb-tab:: Run It


      .. tb-code:: cpp
         :name: lst_insertion_cpp
         :caption: The Insertion Sort

         #include <iostream>
         #include <vector>
         using std::vector;

         vector<int> insertion_sort(vector<int> data) {
           for (unsigned int index=1; index<data.size(); ++index) {
             int currentvalue = data[index];
             int position = index;

             while (position>0 && data[position-1]>currentvalue) {
               data[position] = data[position-1];
               --position;
             }
             data[position] = currentvalue;
           }
           return data;
         }

         int main() {
           vector<int> data = {54, 26, 93, 17, 77, 31, 44, 55, 20};
           for (const auto& value: insertion_sort(data)) {
             std::cout << value << ' ';
           }
           std::cout << '\n';
           return 0;
         }


.. note::
   If you have not examined the previous you should.
   Many job interviews involve a 'whiteboard interview'
   that may ask you to write a bubble sort or an insertion sort.


I don't know why bubble sort in particular is such a popular question.
The bubble sort: 

- is not particularly easy to memorize
- is not an obvious solution to the sorting problem
- performs rather badly - it's average performance is n-squared!

.. tb-group::
   :name: stl_exchange_sort

   .. tb-tab:: Exchange Sorts

      If sorting does get asked and you can get past these points with a future employer,
      you might score some points with the following examples, which:

      - are far easier to memorize and explain: the actual sort is only 2 lines
      - even though still n-squared, is typically better in practice than bubble sort
      - demonstrates familiarity with the standard library.


      .. tb-code:: cpp
         :name: stl_exchange_sorts
         :caption: Standard Library Exchange Sorts

         #include <algorithm>
         #include <iostream>
         #include <iterator>
         #include <numeric> 
         #include <vector>
         #include <random>

         #define RandomAccessIterable typename
         template <RandomAccessIterable It> void print(const It begin, const It end, const char* msg);
         template <RandomAccessIterable It> void selection_sort(It begin, It end);
         template <RandomAccessIterable It> void insertion_sort(It begin, It end);

         int main() {
             std::vector<int> v(20);
             std::iota(v.begin(), v.end(), -10);
             auto generator = std::mt19937{std::random_device{}()};
             std::shuffle(v.begin(), v.end(), generator);

             print (v.begin(), v.end(), "before:         \t");
             selection_sort(v.begin(), v.end());
             print (v.begin(), v.end(), "selection sort: \t");

             std::shuffle(v.begin(), v.end(), generator);
             print (v.begin(), v.end(), "before:         \t");
             insertion_sort(v.begin(), v.end());
             print (v.begin(), v.end(), "insertion sort: \t");
         }

         template <RandomAccessIterable It> 
         void selection_sort(It begin, It end) {
             for (auto i = begin; i != end; ++i) {
                 std::iter_swap(i, std::min_element(i, end));
                 //print (begin, end, "\t");
             }
         }

         template <RandomAccessIterable It> 
         void insertion_sort(It begin, It end) {
             for (auto i = begin; i != end; ++i) {
                 std::rotate(std::upper_bound(begin, i, *i), i, std::next(i));
                 //print (begin, end, "\t");
             }
         }

         template <RandomAccessIterable It> 
         void print(const It begin, const It end, const char* msg) {
             // not very pretty
             // avoids hardcoded ostream_iterator<int>
             using os_iter = std::ostream_iterator<typename std::iterator_traits<It>::value_type>;

             std::cout << msg;
             std::copy(begin, end, os_iter(std::cout, " "));
             std::cout << '\n';
         }

One nice feature of the selection sort implemented using
:algorithm:`iter_swap` and :algorithm:`min_element` is that the
``min_element`` function takes a custom comparator.

This means that while the default behavior is to sort ascending since the
default comparator is :functional:`std::less <less>` any other binary
predicate operation could be passed in.

.. cpp:: 20

   If your compiler supports C++20 :cpp:`ranges`, then you could use the ranges versions
   of ``min_element`` and ``iter_swap`` and use a range-for loop.

.. admonition:: Try This!

   Modify the ``selection_sort`` template to take an optional comparison function
   that changes the sort order.


**Self Check**

.. tb-group::
   :name: tab_check

   .. tb-tab:: Q1

      .. tb-choice::
         :name: question_sort_3

         Suppose you have the following list of numbers to sort:
         [15, 5, 4, 18, 12, 19, 14, 10, 8, 20] which list represents the partially sorted list after three complete passes of insertion sort?

         - [ ] [4, 5, 12, 15, 14, 10, 8, 18, 19, 20]

           This is the result of bubble sort.
         - [ ] [15, 5, 4, 10, 12, 8, 14, 18, 19, 20]

           This is the result of selection sort.
         - [x] [4, 5, 15, 18, 12, 19, 14, 10, 8, 20]

           Insertion sort works at the start of the list.  Each pass produces a longer sorted list.
         - [ ] [15, 5, 4, 18, 12, 19, 14, 8, 10, 20]

           Insertion sort works on the front of the list not the end.

.. admonition:: More to Explore

   - `Top 5 beautiful C++ algorithms <https://www.cppstories.com/2014/12/top-5-beautiful-c-std-algorithms/>`__
   - :wiki:`Insertion sort <Insertion_sort>`
   - `Insertion Sort visualization <https://visualgo.net/en/sorting>`__
   - :cpp:`C++ std::ranges::lower_bound <algorithm/ranges/lower_bound>`

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/ns/books/published/cppds/index.html?mode=browsing>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__,
   and 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.
