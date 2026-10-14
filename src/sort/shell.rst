..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the Runestone eTextbook project. See
   Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http

.. _sort_shell:

.. index::
   single: Shellsort
   pair: sorting algorithms; Shellsort
   pair: Shellsort; gap sequence

Shellsort
==========

Shellsort was named for its inventor, D.L. Shell, who published it in 1959.
When properly implemented, Shellsort will give much better performance than any
of the :math:`O(n^{2})` sorts like :ref:`insertion sort<sort_insertion>` or
:ref:`selection sort<sort_selection>`.
But it is also a bit more complicated than those simple :math:`O(n^{2})` sorts.
Unlike insertion sort and selection sort, there is no real-life intuition to
inspire Shellsort -- nobody will use Shellsort to sort their Bridge hand or
organize their bills.

The key idea behind Shellsort is to exploit the best-case performance of insertion sort.
Recall that when a list is sorted or nearly sorted, insertion sort runs in linear time.
So Shellsort’s strategy is to quickly make the list "mostly sorted",
so that a final insertion sort can finish the job.

Shellsort does what most good sorts do:
Break the input into pieces, sort the pieces, then recombine them.
But Shellsort does this in an unusual way, breaking its input into "virtual"
sublists that are often not contiguous.

Shellsort uses an **increment**, sometimes called the **gap**,
to create a sublist by choosing all items that are ``gap`` items apart.
Each such sublist is sorted using an insertion sort.
Another group of sublists is then chosen and sorted, and so on.

The :ref:`following sequence <fig_incrementsA>` uses a vector with nine
items and a gap of three. This creates three sublists, each sorted using
insertion sort. The :ref:`last scene <fig_incrementsB>` shows the values
in their positions after one pass through all three sublists.

.. tb-stack::
   :name: shell-gap-three
   :caption: Shellsort: one pass with a gap of three

   .. tb-scene::
      :name: fig_incrementsA
      :caption: Gap 3: sort sublist 1 at positions 0, 3, and 6.

      A gap of three creates three sublists. Their positions are fixed;
      values move only between positions in the same sublist during this
      pass. The outlined cells contain sublist 1: [54, 17, 44].

      Use insertion sort within this sublist. Insert 17 before 54, then
      insert 44 between 17 and 54. Its sorted values are [17, 44, 54].

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Before the gap-three pass, sublist 1 occupies positions 0, 3,
            and 6.
         :highlight: data.node[a] data.node[d] data.node[g]

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

      .. list-table:: Sublists before the gap-three pass
         :header-rows: 1

         * - Sublist
           - Zero-based positions
           - Original values in position order
         * - 1
           - 0, 3, 6
           - 54, 17, 44
         * - 2
           - 1, 4, 7
           - 26, 77, 55
         * - 3
           - 2, 5, 8
           - 93, 31, 20

   .. tb-scene::
      :caption: Sublist 1 is sorted in positions 0, 3, and 6.

      The values [17, 44, 54] now occupy positions 0, 3, and 6,
      respectively. Positions belonging to sublists 2 and 3 are unchanged.
      Only sublist 1 has been sorted so far.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: After sorting sublist 1, positions 0, 3, and 6 contain 17, 44,
            and 54.
         :highlight: data.node[a] data.node[d] data.node[g]

         a[17]
         b[26]
         c[93]
         d[44]
         e[77]
         f[31]
         g[54]
         h[55]
         i[20]

   .. tb-scene::
      :caption: Sort sublist 2 at positions 1, 4, and 7.

      The outlined cells contain sublist 2: [26, 77, 55]. Its positions
      are one cell to the right of those in sublist 1.

      Use insertion sort within this sublist. Leave 77 after 26, then
      insert 55 between them. Its sorted values are [26, 55, 77].

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Sublist 2 contains 26, 77, and 55 at positions 1, 4, and 7.
         :highlight: data.node[b] data.node[e] data.node[h]

         a[17]
         b[26]
         c[93]
         d[44]
         e[77]
         f[31]
         g[54]
         h[55]
         i[20]

   .. tb-scene::
      :caption: Sublist 2 is sorted in positions 1, 4, and 7.

      The values [26, 55, 77] now occupy positions 1, 4, and 7,
      respectively. Sublist 1 retains its sorted values, and sublist 3
      has not yet been processed.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: After sorting sublist 2, positions 1, 4, and 7 contain 26, 55,
            and 77.
         :highlight: data.node[b] data.node[e] data.node[h]

         a[17]
         b[26]
         c[93]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[20]

   .. tb-scene::
      :caption: Sort sublist 3 at positions 2, 5, and 8.

      The outlined cells contain sublist 3: [93, 31, 20]. Its positions
      are two cells to the right of those in sublist 1.

      Use insertion sort within this sublist. Insert 31 before 93, then
      insert 20 before both of them. Its sorted values are [20, 31, 93].

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Sublist 3 contains 93, 31, and 20 at positions 2, 5, and 8.
         :highlight: data.node[c] data.node[f] data.node[i]

         a[17]
         b[26]
         c[93]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[20]

   .. tb-scene::
      :caption: Sublist 3 is sorted in positions 2, 5, and 8.

      The values [20, 31, 93] now occupy positions 2, 5, and 8,
      respectively. Sublists 1 and 2 retain their sorted values.
      The pass through all three sublists is complete.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: After sorting sublist 3, positions 2, 5, and 8 contain 20, 31,
            and 93.
         :highlight: data.node[c] data.node[f] data.node[i]

         a[17]
         b[26]
         c[20]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :name: fig_incrementsB
      :caption: The gap-three pass is complete.

      All three sublists are sorted within their original positions.
      Reading across the array gives [17, 26, 20, 44, 55, 31, 54, 77, 93].

      The whole array is still not sorted: 26 precedes 20, and 55 precedes
      31. Sorting the sublists has moved values closer to their final
      positions. A later pass with a gap of one will finish the sort.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: After the gap-three pass: 17, 26, 20, 44, 55, 31, 54, 77, 93.

         a[17]
         b[26]
         c[20]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

      .. list-table:: Sorted sublists after the gap-three pass
         :header-rows: 1

         * - Sublist
           - Zero-based positions
           - Sorted values in position order
         * - 1
           - 0, 3, 6
           - 17, 44, 54
         * - 2
           - 1, 4, 7
           - 26, 55, 77
         * - 3
           - 2, 5, 8
           - 20, 31, 93


The :ref:`gap-one sequence <fig_incrementsC>` shows the final pass of the
previous example: a standard :ref:`insertion sort <sort_insertion>`.
Sorting the gap-three sublists first reduces the shifting needed to put
the whole array in order. This final pass requires only four shifts.

.. tb-stack::
   :name: fig_incrementsC
   :caption: Shellsort: the final pass with a gap of one

   .. tb-scene::
      :caption: Gap 1: start with the array from the gap-three pass.

      A gap of one makes the whole array a single sublist. Finish with
      a standard insertion sort, starting with 17 as the sorted prefix.
      The outlined cells mark that prefix as it grows.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 1 cells form the sorted prefix.
         :highlight: data.node[a]

         a[17]
         b[26]
         c[20]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 26: no shifts.

      Since 26 is greater than 17, leave it in place. The sorted prefix
      now contains two items.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 2 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b]

         a[17]
         b[26]
         c[20]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 20: shift 26 once.

      Save 20, shift 26 one cell to the right, and insert 20 after 17.
      The sorted prefix now contains three items. This is the first of
      four shifts needed to finish the sort.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 3 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]

         a[17]
         b[20]
         c[26]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 44: no shifts.

      Since 44 is greater than 26, leave it in place. The sorted prefix
      now contains four items.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 4 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d]

         a[17]
         b[20]
         c[26]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 55: no shifts.

      Since 55 is greater than 44, leave it in place. The sorted prefix
      now contains five items.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 5 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e]

         a[17]
         b[20]
         c[26]
         d[44]
         e[55]
         f[31]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 31: shift 55 and 44.

      Save 31, shift 55 and 44 one cell to the right, then insert 31
      after 26. The sorted prefix now contains six items. These two
      shifts bring the total to three.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 6 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e] data.node[f]

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[55]
         g[54]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 54: shift 55 once.

      Save 54, shift 55 one cell to the right, and insert 54 after 44.
      The sorted prefix now contains seven items. This fourth shift is
      the last one needed.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 7 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e] data.node[f]
            data.node[g]

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 77: no shifts.

      Since 77 is greater than 55, leave it in place. The sorted prefix
      now contains eight items.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 8 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e] data.node[f]
            data.node[g] data.node[h]

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Insert 93: the array is sorted.

      Since 93 is greater than 77, leave it in place. All nine items
      now belong to the sorted prefix. The gap-one pass needed only
      four shifts: one for 20, two for 31, and one for 54.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-one pass: the first 9 cells form the sorted prefix.
         :highlight: data.node[a] data.node[b] data.node[c]
            data.node[d] data.node[e] data.node[f]
            data.node[g] data.node[h] data.node[i]

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]


.. tb-stack::
   :name: fig_incrementsD
   :caption: Shellsort: initial sublists with a gap of four

   .. tb-scene::
      :caption: Gap 4: sublist 1 occupies positions 0, 4, and 8.

      This separate example returns to the original, unsorted array.
      The implementation below starts with a gap of :math:`9 / 2`,
      using integer division to get four. Later gaps are two and one.

      The outlined cells form sublist 1: [54, 77, 20]. They are four
      positions apart. Insertion sort will sort these values within
      positions 0, 4, and 8.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-four sublist 1 occupies positions 0, 4, 8.
         :highlight: data.node[a] data.node[e] data.node[i]

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-scene::
      :caption: Sublist 2 occupies positions 1 and 5.

      The outlined cells form sublist 2: [26, 31]. This sublist starts
      at position 1 and advances by four positions. Its values are
      already in ascending order.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-four sublist 2 occupies positions 1, 5.
         :highlight: data.node[b] data.node[f]

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-scene::
      :caption: Sublist 3 occupies positions 2 and 6.

      The outlined cells form sublist 3: [93, 44]. This sublist starts
      at position 2 and advances by four positions. Sorting it will
      place 44 at position 2 and 93 at position 6.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-four sublist 3 occupies positions 2, 6.
         :highlight: data.node[c] data.node[g]

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

   .. tb-scene::
      :caption: Sublist 4 occupies positions 3 and 7.

      The outlined cells form sublist 4: [17, 55]. This sublist starts
      at position 3 and advances by four positions. Its values are
      already in ascending order.

      These four sublists cover every position in the original array.
      The table summarizes their positions and values before sorting.

      .. tb-graph:: data
         :style: array
         :align: center
         :show-indices:
         :alt: Gap-four sublist 4 occupies positions 3, 7.
         :highlight: data.node[d] data.node[h]

         a[54]
         b[26]
         c[93]
         d[17]
         e[77]
         f[31]
         g[44]
         h[55]
         i[20]

      .. list-table:: Initial sublists with a gap of four
         :header-rows: 1

         * - Sublist
           - Zero-based positions
           - Original values in position order
         * - 1
           - 0, 4, 8
           - 54, 77, 20
         * - 2
           - 1, 5
           - 26, 31
         * - 3
           - 2, 6
           - 93, 44
         * - 4
           - 3, 7
           - 17, 55

.. _lst-shell-sort-code:

.. tb-group::
   :name: lst-shell

   .. tb-tab:: Shell Sort

      We said earlier that the way in which the increments are chosen is the
      unique feature of the Shellsort. The function shown in the
      :ref:`Run It <lst-shell-sort-code>` section.
      uses a different set of increments. In this case, we begin with
      :math:`\frac {n}{2}` sublists. On the next pass,
      :math:`\frac {n}{4}` sublists are sorted. Eventually, a single vector is
      sorted with the basic insertion sort. The
      :ref:`gap-four scenes <fig_incrementsD>` show the first sublists
      for our example using this increment.

      The following invocation of the ``shell_sort`` function shows the
      partially sorted vectors after each increment, with the final sort being
      an insertion sort with an increment of one.

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: lst_shell_cpp
         :caption: The Shell Sort

         #include <iostream>
         #include <string>
         #include <vector>
         using std::vector;

         void print(const vector<int>& data, const std::string& comment) {
            for (const auto& value: data) {
               std::cout << value << ' ';
            }
            std::cout << comment << '\n';
         }

         vector<int> gap_insertion_sort(vector<int> data, int start, int gap) {
            for (int i = start+gap; i < int(data.size()); i += gap) {
               int value = data[i];
               int pos = i;

               while (pos >= gap && data[pos-gap] > value) {
                  data[pos] = data[pos-gap];
                  pos -= gap;
               }
               data[pos] = value;
            }
            return data;
         }

         vector<int> shell_sort(vector<int> data) {
            int pivot = data.size() / 2;
            while (pivot > 0) {
               for (int start = 0; start < pivot; ++start) {
                  data = gap_insertion_sort(data, start, pivot);
               }
               std::string text = ": pivot = ";
               text.append(std::to_string(pivot));
               print(data, text);
               pivot /= 2;
            }
            return data;
         }

         int main() {
           vector<int> data = {54, 26, 93, 17, 77, 31, 44, 55, 20};
           print(shell_sort(data), ": done");
           return 0;
         }

The following animations show the Shellsort in action. Teal marks the
current gap group, yellow marks the value being inserted, red marks a shifted
comparison, and gray marks the final sorted state.

.. Sort animation assets are generated with ``generate_sort_video.py``.

.. only:: html

   .. tb-group::
      :name: shell-sort-animations

      .. tb-tab:: Average case

         .. tb-video:: ../_static/generated/sort/shell-sort-average.webm
            :name: shell-sort-average-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/shell-sort-average.png

      .. tb-tab:: Best case

         .. tb-video:: ../_static/generated/sort/shell-sort-best.webm
            :name: shell-sort-best-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/shell-sort-best.png

      .. tb-tab:: Worst case

         .. tb-video:: ../_static/generated/sort/shell-sort-worst.webm
            :name: shell-sort-worst-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/shell-sort-worst.png

.. only:: not html

   .. figure:: ../_static/generated/sort/shell-sort-average.png
      :alt: Shellsort summary for an average input.

   .. figure:: ../_static/generated/sort/shell-sort-best.png
      :alt: Shellsort summary for an already sorted input.

   .. figure:: ../_static/generated/sort/shell-sort-worst.png
      :alt: Shellsort summary for a reverse-sorted input.

Shellsort analysis
-------------------

At first glance you may think that a Shellsort cannot be better than an
insertion sort, since it does a complete insertion sort as the last
step. It turns out, however, that this final insertion sort does not
need to do very many comparisons (or shifts) since the list has been
pre-sorted by earlier incremental insertion sorts, as described above.
In other words, each pass produces a list that is "more sorted" than the
previous one. This makes the final pass very efficient.

Although a general analysis of the Shellsort is well beyond the scope
of this text, we can say that it tends to fall somewhere between
:math:`O(n)` and :math:`O(n^{2})`, based on the behavior described above. 
For the increments shown in the :ref:`Run It <lst-shell-sort-code>` section 
the performance is :math:`O(n^{2})`.

Some choices for the series of increments will make Shellsort run more
efficiently than others.
In particular, the choice of increments described above
:math:`(\frac{N}{2^{k}},\ldots,4,2,1)`
turns out to be relatively inefficient.
Notice for example that all records in a given 8 increment sublist are also
part of some 4 increment sublist,
which are all in turn records of the same 2 increment sublist.
So there is no "crossover" between sublists as the increments reduce.
By changing the increment, for example using
:math:`(2^{k}-1,\ldots,31,15,7,3,1)` a shell sort can perform
at :math:`O(n^{\frac {3}{2}})`.

Shellsort is not so much worse than the asymptotically better sorts to be
presented later, whenever :math:`n` is of medium size (though it tends to be a
little slower than these other algorithms if they are well implemented).
Shellsort illustrates how we can sometimes exploit the special properties of an
algorithm (like insertion sort) even if in general that algorithm is
unacceptably slow.

**Self Check**

.. tb-group::
   :name: tab_check

   .. tb-tab:: Q1

      .. tb-choice::
         :name: question_sort_4

         Given the following list of numbers:  [5, 16, 20, 12, 3, 8, 9, 17, 19, 7],
         which answer illustrates the contents of the list after all swapping is complete for a gap size of 3?


         - [x] [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]

           Each group of numbers represented by index positions 3 apart are sorted correctly.
         - [ ] [3, 7, 5, 8, 9, 12, 19, 16, 20, 17]

           This solution is for a gap size of two.
         - [ ] [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]

           This is list completely sorted, you have gone too far.
         - [ ] [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]

           The gap size of three indicates that the group represented by every third number e.g. 0, 3, 6, 9  and 1, 4, 7 and 2, 5, 8 are sorted not groups of 3.

.. admonition:: More to Explore

   - `OpenDSA: Shellsort <https://opendsa.cs.vt.edu/ODSA/Books/Everything/html/Shellsort.html>`__
   - :wiki:`Shellsort <Shellsort>` and 
     :wiki:`Shellsort gap sequences <Shellsort#Gap_sequences>`

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/ns/books/published/cppds/index.html?mode=browsing>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__.
