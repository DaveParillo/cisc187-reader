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


.. _sort_selection:

Selection sort
==============
The **selection sort** improves on the bubble sort by making only one
exchange for every pass through the first part of the vector.
We will call this a step.
In order to do this, a
selection sort looks for the largest value as it makes a partial pass and, after
completing the partial pass, places it in the proper location, ending the step.
As with a bubble
sort, after the first step, the largest item is in the correct place.
After the second step, the next largest is in place. This process
continues and requires :math:`n-1` steps to sort *n* items, since the
final item must be in place after the :math:`(n-1)` step.

.. tabbed:: lst_selection_sort

   .. tab:: Selection Sort

      On each step,
      the largest remaining item is selected and then placed in its proper
      location. The first pass places 93, the second pass places 77, the third
      places 55, and so on.

      .. animation:: selection_anim
         :modelfile: sortmodels.js
         :viewerfile: sortviewers.js
         :model: SelectionSortModel
         :viewer: BarViewer

      Yellow bars represent the current element, 
      red represents the element being looked at,
      and blue represents the last element to look at during a step.

   .. tab:: Run It

      .. activecode:: lst_selectionsortcode_cpp
         :caption: The Selection Sort
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <utility>
         #include <vector>
         using std::vector;
         
         vector<int> selection_sort(vector<int> data) {
           for (int slot = data.size()-1; slot >= 0; --slot) {
             int largest = 0;  // location of the largest element
             for (int location = 1; location < slot+1; location++) {
               if (data[location] > data[largest]) {
                 largest = location;
               }
             }
             std::swap(data[slot], data[largest]);
           }
           return data;
         }

         int main() {
           vector<int> data = {54, 26, 93, 17, 77, 31, 44, 55, 20};
           for (const auto& value: selection_sort(data)) {
             std::cout << value << ' ';
           }
           std::cout << '\n';
           return 0;
         }


You may see that the selection sort makes the same number of comparisons
as the :ref:`bubble sort<sort_bubble>` and is therefore also :math:`O(n^{2})`. 
Like the bubble sort, the selection sort makes no exchanges when the
data is already sorted ascending.
In other cases selection sort generally makes fewer exchanges
than bubble sort when presented with the same data.
Due to the smaller number of exchanges, the selection sort
typically executes faster than bubble sort.

**Self Check**

.. tabbed:: tab_check

   .. tab:: Q1

      .. mchoice:: question_sort_2
         :correct: d
         :answer_a: [7, 11, 12, 1, 6, 14, 8, 18, 19, 20]
         :answer_b: [7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
         :answer_c: [11, 7, 12, 14, 1, 6, 8, 18, 19, 20]
         :answer_d: [11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
         :feedback_a: Selection sort is similar to bubble sort (which you appear to have done) but uses fewer swaps
         :feedback_b: This looks like an insertion sort.
         :feedback_c: This one looks similar to the correct answer, however, it is not how selection sort works. With this answer, instead of swapping values through each sweep, the values have been shifted to the left to make room for the correct numbers.
         :feedback_d: Selection sort improves upon bubble sort by making fewer swaps.

         Suppose you have the following vector of numbers to sort:
         [11, 7, 12, 14, 19, 1, 6, 18, 8, 20] which vector represents the partially sorted (ascending) vector after three steps of selection sort?

.. admonition:: More to Explore

   - TBD

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/runestone/books/published/cppds>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <http://creativecommons.org/licenses/by-nc-sa/4.0/>`__.

