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

.. _exhange_costs:

Costs of Exchange Sorting
=========================
The running time for each of the sorts discussed so far is
:math:`\Theta(n^2)` in the average and worst cases.
The cost summary for the 
:ref:`Insertion Sort<sort_insertion>`,
:ref:`Bubble Sort<sort_bubble>`, and
:ref:`Selection Sort<sort_selection>` 
in terms of their required number of
comparisons and swaps in the best, average, and worst cases is shown.

.. math::

   \begin{array}{rccc}
   &\textbf{Insertion}&\textbf{Bubble}&\textbf{Selection}\\
   \textbf{Comparisons:}\\
   \textrm{Best Case}&\Theta(n)&\Theta(n^2)&\Theta(n^2)\\
   \textrm{Average Case}&\Theta(n^2)&\Theta(n^2)&\Theta(n^2)\\
   \textrm{Worst Case}&\Theta(n^2)&\Theta(n^2)&\Theta(n^2)\\
   \\
   \textbf{Swaps:}\\
   \textrm{Best Case}&0&0&\Theta(n)\\
   \textrm{Average Case}&\Theta(n^2)&\Theta(n^2)&\Theta(n)\\
   \textrm{Worst Case}&\Theta(n^2)&\Theta(n^2)&\Theta(n)\\
   \end{array}

The remaining sorting algorithms presented in this chapter are
significantly better than these three under typical conditions.
But before continuing on, it is instructive to investigate what makes
these three sorts so slow.
The crucial bottleneck is that only *adjacent* records are compared.
Thus, comparisons and moves (for Insertion and Bubble Sort) are by
single steps.
Swapping adjacent records is called an :term:`exchange`.
Thus, these sorts are sometimes referred to as an *exchange sort*.
The cost of any exchange sort can be at best the total number of
steps that the records in the array must move to reach their
"correct" location.
Recall that this is at least the number of
inversions for the record. An :index:`inversion` occurs when a
record with key value greater than the current record's key value
appears before it.


.. admonition:: More to Explore

   - Last 3 sections:

     - :ref:`Insertion Sort<sort_insertion>`,
     - :ref:`Bubble Sort<sort_bubble>`, and
     - :ref:`Selection Sort<sort_selection>` 

   - :ref:`analysis_index`

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

