..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
   Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. _sort_bubble:

Bubble sort
===========
The **bubble sort** makes multiple passes through an array. It compares
adjacent items and exchanges those that are out of order. Each pass
through the array places the next largest value in its proper place. In
essence, each item "bubbles" up to the location where it belongs.

:ref:`Figure 1 <fig_bubblepass>` shows the first pass of a bubble sort.
Shaded items are being compared to see if they are out of order. If there are
*n* items in the array, then there are :math:`n-1` pairs of items that
need to be compared on the first pass. It is important to note that once
the largest value in the array is part of a pair, it will continually be
moved along until the pass is complete.

.. _fig_bubblepass:

.. figure:: figures/bubblepass.png
   :align: center

   Figure 1: ``bubble_sort``: The First Pass

.. tabbed:: lst_bubble_sort

   .. tab:: Bubble sort


      At the start of the second pass, the largest value is now in place.
      There are :math:`n-1` items left to sort, meaning that there will be
      :math:`n-2` pairs. Since each pass places the next largest value in
      place, the total number of passes necessary will be :math:`n-1`. After
      completing the :math:`n-1` passes, the smallest item must be in the
      correct position with no further processing required. The 'Run It' tab
      shows the complete ``bubble_sort`` function. It takes the array as a
      parameter, and modifies it by swapping items as necessary.

      Typically, swapping two elements in an array requires a temporary storage location (an
      additional memory location). A code fragment such as

      .. code-block:: cpp

         temp = alist[i];
         alist[i] = alist[j];
         alist[j] = temp;

      will exchange the `ith` and `jth` items in the array. Without the
      temporary storage, one of the values would be overwritten.

      .. note::

         This exchange is referred to as the *swap idiom* and occurs
         frequently.

         :algorithm:`std::swap <swap>` is part of the standard library
         and many swap specializations are defined to make swap
         efficient for STL types.

   .. tab:: Run it

      .. activecode:: lst_bubble_cpp
         :caption: The Bubble Sort
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <vector>
         using std::vector;
 
         // function goes through list sorting adjacent values as it bubbles 
         // the largest value to the top.
         vector<int> bubble_sort(vector<int> data) {
           for (int passnum = data.size()-1; passnum > 0; --passnum) {
             for (int i = 0; i < passnum; ++i) {
               if (data[i] > data[i+1]) {
                 // could be replaced with std::swap
                 int temp = data[i];
                 data[i] = data[i+1];
                 data[i+1] = temp;
               }
             }
           }
           return data;
         }

         int main() {
           vector<int> data = {54,26,93,17,77,31,44,55,20};

           for (const auto& value: bubble_sort(data)) {
             std::cout << value << ' ';
           }
           return 0;
         }

The following animation shows bubble sort in action.
The values being sorted are bars of various heights.
When bar colors change to red,
this indicates these are the two values compared by bubble sort.

To start the animation, press **Initialize**.

.. animation:: bubble_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: BubbleSortModel
   :viewer: BarViewer

To analyze the bubble sort, we should note that regardless of how the
items are arranged in the initial array, :math:`n-1` passes will be
made to sort an array of size *n*. :ref:`Table 1 <tbl_bubbleanalysis>` shows the number
of comparisons for each pass. The total number of comparisons is the sum
of the first :math:`n-1` integers. Recall that the sum of the first
*n* integers is :math:`\frac{1}{2}n^{2} + \frac{1}{2}n`. The sum of
the first :math:`n-1` integers is
:math:`\frac{1}{2}n^{2} + \frac{1}{2}n - n`, which is
:math:`\frac{1}{2}n^{2} - \frac{1}{2}n`. This is still
:math:`O(n^{2})` comparisons. In the best case, if the array is already
ordered, no exchanges will be made. However, in the worst case, every
comparison will cause an exchange. On average, we exchange half of the
time.

.. _tbl_bubbleanalysis:

.. table:: **Table 1: Comparisons for Each Pass of Bubble Sort**

    ================= ==================
    **Pass**          **Comparisons**
    ================= ==================
             1         :math:`n-1`
             2         :math:`n-2`
             3         :math:`n-3`
             ...       ...
       :math:`n-1`     :math:`1`
    ================= ==================

.. tabbed:: lst_shortbubble

   .. tab:: Short Bubble

      A bubble sort is often considered the most inefficient sorting method
      since it must exchange items before the final location is known. These
      “wasted” exchange operations are very costly. However, because the
      bubble sort makes passes through the entire unsorted portion of the
      array, it has the capability to do something most sorting algorithms
      cannot. In particular, if during a pass there are no exchanges, then we
      know that the array must be sorted. A bubble sort can be modified to stop
      early if it finds that the array has become sorted. This means that for
      arrays that require just a few passes, a bubble sort may have an
      advantage in that it will recognize the sorted array and stop.
      This modification is often referred to as the **short bubble**.

   .. tab:: Run It

      .. activecode:: lst_shortbubbles_cpp
         :caption: The 'Short' Bubble Sort
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <utility>
         #include <vector>
         using std::vector;
 
         vector<int> short_bubble(vector<int> data) {
           bool exchanges = true;
           int passnum = data.size();
           while (passnum > 0 && exchanges) {
             exchanges = false;
             for (int i = 0; i < passnum; ++i) {
               if (data[i] > data[i+1]) {
                 std::swap(data[i], data[i+1]);
               }
             }
             // decrement passnum variable so that the next pass is one less
             // than the previous: the largest value has already 'bubbled' all the way up.
             --passnum;
           }

           return data;
         }

         int main() {
           vector<int> data = {20,30,40,90,50,60,70,80,110,100};

           for (const auto& value: short_bubble(data)) {
             std::cout << value << ' ';
           }
           return 0;
         }

**Self Check**

.. tabbed:: tab_check

   .. tab:: Q1

      .. mchoice:: question_sort_1
         :correct: b
         :answer_a: [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
         :answer_b: [1, 3, 7, 9, 10, 8, 12, 13, 15, 19]
         :answer_c: [1, 7, 3, 9, 10, 13, 8, 12, 15, 19]
         :answer_d: [1, 9, 19, 7, 3, 10, 13, 15, 8, 12]
         :feedback_a:  This answer represents three swaps.  A pass means that you continue swapping all the way to the end of the list.
         :feedback_b:  Very Good
         :feedback_c: A bubble sort continues to swap numbers up to index position passnum.  But remember that passnum starts at the length of the list - 1.
         :feedback_d: You have been doing an insertion sort, not a bubble sort.

         Suppose you have the following array of numbers to sort:
         [19, 1, 9, 7, 3, 10, 13, 15, 8, 12] which array represents the partially sorted list after three complete passes of bubble sort?



.. admonition:: More to Explore

   - TBD

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/runestone/books/published/cppds>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <http://creativecommons.org/licenses/by-nc-sa/4.0/>`__,
   and 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

