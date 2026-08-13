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

.. _sort_heap:

Heap sort
=========
Our discussion of Quicksort began by considering the practicality of
using a BST for sorting.
The BST requires more space than the other sorting methods and will
be slower than Quicksort or Mergesort due to the relative expense of
inserting values into the tree.
There is also the possibility that the BST might be unbalanced,
leading to a :math:`\Theta(n^2)` worst-case running time.
Subtree balance in the BST is closely related to Quicksort's partition
step.
Quicksort's pivot serves roughly the same purpose as the BST root
value in that the left partition (subtree) stores values less than
the pivot (root) value, while the right partition (subtree) stores
values greater than or equal to the pivot (root).

A good sorting algorithm can be devised based on a tree structure more
suited to the purpose.
In particular, we would like the tree to be balanced, space efficient,
and fast.
The algorithm should take advantage of the fact that sorting is a
special-purpose application in that all of the values to be stored are
available at the start.
This means that we do not necessarily need to insert one value at a
time into the tree structure.

Heapsort is based on the heap data structure.
Heapsort has all of the advantages just listed.
The complete binary tree is balanced, its array representation is
space efficient, and we can load all values into the tree at once,
taking advantage of the efficient ``buildheap`` function.

Heap sort analysis
------------------

The asymptotic performance of Heapsort when all of the records have
unique key values is :math:`\Theta(n \log n)` in the best, average,
and worst cases.
It is not as fast as Quicksort in the average case (by a constant
factor), but Heapsort has special properties that will make it
particularly useful for
external sorting algorithms - 
used when sorting data sets too large to fit in main memory.

The following animations show heap sort in action. Yellow marks the active
root or subtree parent, red marks compared or exchanged values, teal marks the
active heap boundary, purple marks the completed max heap, and gray marks the
sorted suffix.

.. Sort animation assets are generated with ``generate_sort_video.py``.

.. only:: html

   .. tb-group::
      :name: heap-sort-animations

      .. tb-tab:: Average case

         .. tb-video:: ../_static/generated/sort/heap-sort-average.webm
            :name: heap-sort-average-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/heap-sort-average.png

      .. tb-tab:: Best case

         .. tb-video:: ../_static/generated/sort/heap-sort-best.webm
            :name: heap-sort-best-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/heap-sort-best.png

      .. tb-tab:: Worst case

         .. tb-video:: ../_static/generated/sort/heap-sort-worst.webm
            :name: heap-sort-worst-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/heap-sort-worst.png

.. only:: not html

   .. figure:: ../_static/generated/sort/heap-sort-average.png
      :alt: Heap sort summary for an average input.

   .. figure:: ../_static/generated/sort/heap-sort-best.png
      :alt: Heap sort summary for an already sorted input.

   .. figure:: ../_static/generated/sort/heap-sort-worst.png
      :alt: Heap sort summary for a reverse-sorted input.




.. admonition:: More to Explore

   - :cpp:`C++ heap operations <algorithm/make_heap>`
   - :wiki:`Heapsort <Heapsort>`

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.
