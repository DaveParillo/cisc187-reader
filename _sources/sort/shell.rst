..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
   Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
   This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http

.. _sort_shell:

Shell sort
==========
The **shell sort**, sometimes called the “diminishing increment sort,”
improves on the :ref:`insertion sort<sort_insertion>` by breaking the original vector into a
number of smaller subvectors, each of which is sorted using an insertion
sort. The unique way that these subvectors are chosen is the key to the
shell sort. Instead of breaking the vector into subvectors of contiguous
items, the shell sort uses an increment ``i``, sometimes called the
**gap**, to create a subvector by choosing all items that are ``i`` items
apart.

This can be seen in :ref:`Figure 6 <fig_incrementsA>`. This vector has nine items. If
we use an increment of three, there are three subvectors, each of which
can be sorted by an insertion sort. After completing these sorts, we get
the vector shown in :ref:`Figure 7 <fig_incrementsB>`. Although this vector is not
completely sorted, something very interesting has happened. By sorting
the subvectors, we have moved the items closer to where they actually
belong.

.. _fig_incrementsA:


.. figure:: figures/shellsortA.png
   :align: center

   Figure 6: A Shell Sort with Increments of Three


.. _fig_incrementsB:

.. figure:: figures/shellsortB.png
   :align: center

   Figure 7: A Shell Sort after Sorting Each subvector


:ref:`Figure 8 <fig_incrementsC>` shows a final insertion sort using an increment of
one; in other words, a standard :ref:`insertion sort<sort_insertion>`.
Note that by performing the earlier subvector sorts, we have now reduced
the total number of shifting operations necessary to put the vector in its final order.
For this case, we need only four more shifts to complete the process.

.. _fig_incrementsC:

.. figure:: figures/shellsortC.png
   :align: center

   Figure 8: ShellSort: A Final Insertion Sort with Increment of 1


.. _fig_incrementsD:

.. figure:: figures/shellsortD.png
   :align: center

   Figure 9: Initial Subvectors for a Shell Sort

.. tabbed:: _lst_shell

   .. tab:: Shell Sort

      We said earlier that the way in which the increments are chosen is the
      unique feature of the shell sort. The function shown in :ref:`ActiveCode 1 <lst_shell_cpp>`
      uses a different set of increments. In this case, we begin with
      :math:`\frac {n}{2}` subvectors. On the next pass,
      :math:`\frac {n}{4}` subvectors are sorted. Eventually, a single vector is
      sorted with the basic insertion sort. :ref:`Figure 9 <fig_incrementsD>` shows the
      first subvectors for our example using this increment.

      The following invocation of the ``shell_sort`` function shows the
      partially sorted vectors after each increment, with the final sort being
      an insertion sort with an increment of one.

   .. tab:: Run It

      .. activecode:: lst_shell_cpp
         :caption: The Shell Sort
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

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

The following animation shows the shell sort in action.

.. animation:: shell_anim
   :modelfile: sortmodels.js
   :viewerfile: sortviewers.js
   :model: ShellSortModel
   :viewer: BarViewer

At first glance you may think that a shell sort cannot be better than an
insertion sort, since it does a complete insertion sort as the last
step. It turns out, however, that this final insertion sort does not
need to do very many comparisons (or shifts) since the list has been
pre-sorted by earlier incremental insertion sorts, as described above.
In other words, each pass produces a list that is “more sorted” than the
previous one. This makes the final pass very efficient.

Although a general analysis of the shell sort is well beyond the scope
of this text, we can say that it tends to fall somewhere between
:math:`O(n)` and :math:`O(n^{2})`, based on the behavior described above. 
For the increments shown in :ref:`Listing 5 <lst_shell_cpp>`, 
the performance is :math:`O(n^{2})`.
By changing the increment, for example using
:math:`2^{k}-1` (1, 3, 7, 15, 31, and so on), a shell sort can perform
at :math:`O(n^{\frac {3}{2}})`.


**Self Check**

.. tabbed:: tab_check

   .. tab:: Q1

      .. mchoice:: question_sort_4
         :correct: a
         :answer_a: [5, 3, 8, 7, 16, 19, 9, 17, 20, 12]
         :answer_b: [3, 7, 5, 8, 9, 12, 19, 16, 20, 17]
         :answer_c: [3, 5, 7, 8, 9, 12, 16, 17, 19, 20]
         :answer_d: [5, 16, 20, 3, 8, 12, 9, 17, 20, 7]
         :feedback_a:  Each group of numbers represented by index positions 3 apart are sorted correctly.
         :feedback_b:  This solution is for a gap size of two.
         :feedback_c: This is list completely sorted, you have gone too far.
         :feedback_d: The gap size of three indicates that the group represented by every third number e.g. 0, 3, 6, 9  and 1, 4, 7 and 2, 5, 8 are sorted not groups of 3.

         Given the following list of numbers:  [5, 16, 20, 12, 3, 8, 9, 17, 19, 7],
         which answer illustrates the contents of the list after all swapping is complete for a gap size of 3?


.. admonition:: More to Explore

   - TBD

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/runestone/books/published/cppds>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <http://creativecommons.org/licenses/by-nc-sa/4.0/>`__.

