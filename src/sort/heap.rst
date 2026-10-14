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

.. index::
   single: heap sort
   pair: sorting algorithms; heap sort
   pair: heap sort; heap property

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

Heap sort walkthrough
---------------------

To sort in ascending order, first build a **max-heap**, where every
parent is at least as large as its children. Then repeatedly exchange
the root (the largest remaining value) with the last active heap item,
shrink the heap by one, and **sift down** the replacement root. Sifting
down exchanges a parent with its larger child until the heap property
holds again or the value reaches a leaf.

The following stack uses our familiar array
``[54, 26, 93, 17, 77, 31, 44, 55, 20]``. Each scene shows the active
heap as a tree and the full array below it. Outlined nodes and cells
mark the values being compared or exchanged. The ``last_heap`` arrow
marks the last active cell, and the ``sorted`` arrow marks the start
of the sorted suffix. Values in that suffix remain in the array but
are excluded from the tree and all later heap operations.

.. tb-stack::
   :name: heap-sort-process
   :caption: Heap sort: build a max-heap, extract the maximum, and sift down

   .. tb-scene::
      :caption: Begin with the original array.

      The tree and array show the same nine values. The root is at index 0;
      its children are at indices 1 and 2. For a parent at index ``p``,
      the children are at ``2*p + 1`` and ``2*p + 2``, when those indices
      are within the active heap. This complete tree is not yet a max-heap.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Begin with the original array. Active heap shown as a tree.

         a[54] -left-> b[26]
         a -right-> c[93]
         b -left-> d[17]
         b -right-> e[77]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[55]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Begin with the original array. Array: 54, 26, 93, 17, 77, 31, 44,
            55, 20.
         :indicators: last_heap=i

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
      :caption: Build the heap: exchange 17 with its larger child, 55.

      Build a max-heap from the bottom up. Indices 4 through 8 are leaves,
      so their one-item subtrees already satisfy the heap property. Start
      with the last parent, index 3. Its children are 55 and 20. Exchange
      17 with the larger child, 55. The value 17 reaches a leaf, ending
      this sift-down.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Build the heap: exchange 17 with its larger child, 55. Active
            heap shown as a tree.
         :highlight: heap.node[d] heap.node[h]

         a[54] -left-> b[26]
         a -right-> c[93]
         b -left-> d[55]
         b -right-> e[77]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Build the heap: exchange 17 with its larger child, 55. Array: 54,
            26, 93, 55, 77, 31, 44, 17, 20.
         :highlight: data.node[d] data.node[h]
         :indicators: last_heap=i

         a[54]
         b[26]
         c[93]
         d[55]
         e[77]
         f[31]
         g[44]
         h[17]
         i[20]

   .. tb-scene::
      :caption: Check the parent at index 2: keep 93 in place.

      Move left to index 2. Its children are 31 and 44. Since 93 is
      already greater than both children, this subtree needs no exchange.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Check the parent at index 2: keep 93 in place. Active heap shown
            as a tree.
         :highlight: heap.node[c] heap.node[f] heap.node[g]

         a[54] -left-> b[26]
         a -right-> c[93]
         b -left-> d[55]
         b -right-> e[77]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Check the parent at index 2: keep 93 in place. Array: 54, 26, 93,
            55, 77, 31, 44, 17, 20.
         :highlight: data.node[c] data.node[f] data.node[g]
         :indicators: last_heap=i

         a[54]
         b[26]
         c[93]
         d[55]
         e[77]
         f[31]
         g[44]
         h[17]
         i[20]

   .. tb-scene::
      :caption: Build the heap: exchange 26 with its larger child, 77.

      At index 1, compare 26 with children 55 and 77. Exchange 26 with
      77, the larger child. The value 26 reaches a leaf. Choosing the
      larger child ensures that the new parent is at least as large as
      both children.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Build the heap: exchange 26 with its larger child, 77. Active
            heap shown as a tree.
         :highlight: heap.node[b] heap.node[e]

         a[54] -left-> b[77]
         a -right-> c[93]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Build the heap: exchange 26 with its larger child, 77. Array: 54,
            77, 93, 55, 26, 31, 44, 17, 20.
         :highlight: data.node[b] data.node[e]
         :indicators: last_heap=i

         a[54]
         b[77]
         c[93]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[20]

   .. tb-scene::
      :caption: Build the heap: exchange 54 with its larger child, 93.

      Finally, sift down from the root. Compare 54 with children 77 and
      93, then exchange it with 93. Continue checking 54 at index 2.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Build the heap: exchange 54 with its larger child, 93. Active
            heap shown as a tree.
         :highlight: heap.node[a] heap.node[c]

         a[93] -left-> b[77]
         a -right-> c[54]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Build the heap: exchange 54 with its larger child, 93. Array: 93,
            77, 54, 55, 26, 31, 44, 17, 20.
         :highlight: data.node[a] data.node[c]
         :indicators: last_heap=i

         a[93]
         b[77]
         c[54]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[20]

   .. tb-scene::
      :caption: The max-heap is ready; 93 is at the root.

      At index 2, 54 is greater than its children, 31 and 44, so stop.
      Every parent is now at least as large as its children, and the root
      holds the maximum value, 93. Building the heap does not sort the
      array: for example, 77 still appears before 54.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: The max-heap is ready; 93 is at the root. Active heap shown as a
            tree.
         :highlight: heap.node[c] heap.node[f] heap.node[g]

         a[93] -left-> b[77]
         a -right-> c[54]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: The max-heap is ready; 93 is at the root. Array: 93, 77, 54, 55,
            26, 31, 44, 17, 20.
         :highlight: data.node[c] data.node[f] data.node[g]
         :indicators: last_heap=i

         a[93]
         b[77]
         c[54]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[20]

   .. tb-scene::
      :caption: Exchange the maximum, 93, with the last heap value, 20.

      Exchange the root at index 0 with the last active item at index 8.
      The maximum value, 93, is now in its final array position. The
      replacement root, 20, may violate the heap property.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (9 items)
         :alt: Exchange the maximum, 93, with the last heap value, 20. Active
            heap shown as a tree.
         :highlight: heap.node[a] heap.node[i]

         a[20] -left-> b[77]
         a -right-> c[54]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]
         d -right-> i[93]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange the maximum, 93, with the last heap value, 20. Array:
            20, 77, 54, 55, 26, 31, 44, 17, 93.
         :highlight: data.node[a] data.node[i]
         :indicators: last_heap=i

         a[20]
         b[77]
         c[54]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[93]

   .. tb-scene::
      :caption: Shrink the active heap to eight items.

      Exclude index 8 from the heap. The value 93 stays in the array,
      but disappears from the active tree. The sorted suffix begins at
      index 8, and the last active heap item is now at index 7.
      Only the active heap participates in the next sift-down.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (8 items)
         :alt: Shrink the active heap to eight items. Active heap shown as a
            tree.
         :highlight: heap.node[a]

         a[20] -left-> b[77]
         a -right-> c[54]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Shrink the active heap to eight items. Array: 20, 77, 54, 55, 26,
            31, 44, 17, 93.
         :highlight: data.node[a]
         :indicators: last_heap=h sorted=i

         a[20]
         b[77]
         c[54]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[93]

   .. tb-scene::
      :caption: Restore the heap: exchange 20 with its larger child, 77.

      The root's children are 77 and 54. Exchange 20 with 77, then
      continue sifting 20 down from index 1. The sorted value 93 stays
      in place.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (8 items)
         :alt: Restore the heap: exchange 20 with its larger child, 77. Active
            heap shown as a tree.
         :highlight: heap.node[a] heap.node[b]

         a[77] -left-> b[20]
         a -right-> c[54]
         b -left-> d[55]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Restore the heap: exchange 20 with its larger child, 77. Array:
            77, 20, 54, 55, 26, 31, 44, 17, 93.
         :highlight: data.node[a] data.node[b]
         :indicators: last_heap=h sorted=i

         a[77]
         b[20]
         c[54]
         d[55]
         e[26]
         f[31]
         g[44]
         h[17]
         i[93]

   .. tb-scene::
      :caption: Continue sifting down: exchange 20 with 55.

      At index 1, the children are 55 and 26. Exchange 20 with the
      larger child, 55, and continue from index 3.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (8 items)
         :alt: Continue sifting down: exchange 20 with 55. Active heap shown as
            a tree.
         :highlight: heap.node[b] heap.node[d]

         a[77] -left-> b[55]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Continue sifting down: exchange 20 with 55. Array: 77, 55, 54,
            20, 26, 31, 44, 17, 93.
         :highlight: data.node[b] data.node[d]
         :indicators: last_heap=h sorted=i

         a[77]
         b[55]
         c[54]
         d[20]
         e[26]
         f[31]
         g[44]
         h[17]
         i[93]

   .. tb-scene::
      :caption: Stop at 20; the eight-item max-heap is restored.

      At index 3, the only active child is 17 at index 7. The value 20
      is greater than 17, so stop. Index 8 holds the sorted value 93
      and is outside the heap. The new maximum, 77, is at the root.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (8 items)
         :alt: Stop at 20; the eight-item max-heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[d] heap.node[h]

         a[77] -left-> b[55]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]
         d -left-> h[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Stop at 20; the eight-item max-heap is restored. Array: 77, 55,
            54, 20, 26, 31, 44, 17, 93.
         :highlight: data.node[d] data.node[h]
         :indicators: last_heap=h sorted=i

         a[77]
         b[55]
         c[54]
         d[20]
         e[26]
         f[31]
         g[44]
         h[17]
         i[93]

   .. tb-scene::
      :caption: Place 77 at index 7; shrink the heap to seven items.

      Repeat the extraction: exchange root 77 with the last active
      value, 17, then exclude index 7 from the heap. The sorted suffix
      is now [77, 93]. Sift the replacement root, 17, down within
      indices 0 through 6.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (7 items)
         :alt: Place 77 at index 7; shrink the heap to seven items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[17] -left-> b[55]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 77 at index 7; shrink the heap to seven items. Array: 17,
            55, 54, 20, 26, 31, 44, 77, 93.
         :highlight: data.node[a] data.node[h]
         :indicators: last_heap=g sorted=h

         a[17]
         b[55]
         c[54]
         d[20]
         e[26]
         f[31]
         g[44]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Restore the heap: exchange 17 with 55.

      The root's children are 55 and 54. Exchange 17 with the larger
      child, 55. Continue sifting 17 down from index 1.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (7 items)
         :alt: Restore the heap: exchange 17 with 55. Active heap shown as a
            tree.
         :highlight: heap.node[a] heap.node[b]

         a[55] -left-> b[17]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[26]
         c -left-> f[31]
         c -right-> g[44]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Restore the heap: exchange 17 with 55. Array: 55, 17, 54, 20, 26,
            31, 44, 77, 93.
         :highlight: data.node[a] data.node[b]
         :indicators: last_heap=g sorted=h

         a[55]
         b[17]
         c[54]
         d[20]
         e[26]
         f[31]
         g[44]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Exchange 17 with 26; the seven-item heap is restored.

      At index 1, the children are 20 and 26. Exchange 17 with 26.
      The value 17 reaches a leaf, so stop. The next maximum, 55,
      is now at the root.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (7 items)
         :alt: Exchange 17 with 26; the seven-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[b] heap.node[e]

         a[55] -left-> b[26]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[17]
         c -left-> f[31]
         c -right-> g[44]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 17 with 26; the seven-item heap is restored. Array: 55,
            26, 54, 20, 17, 31, 44, 77, 93.
         :highlight: data.node[b] data.node[e]
         :indicators: last_heap=g sorted=h

         a[55]
         b[26]
         c[54]
         d[20]
         e[17]
         f[31]
         g[44]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 55 at index 6; shrink the heap to six items.

      Exchange root 55 with the last active value, 44, and exclude
      index 6. The sorted suffix is [55, 77, 93]. The replacement
      root, 44, must be checked against children 26 and 54.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (6 items)
         :alt: Place 55 at index 6; shrink the heap to six items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[44] -left-> b[26]
         a -right-> c[54]
         b -left-> d[20]
         b -right-> e[17]
         c -left-> f[31]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 55 at index 6; shrink the heap to six items. Array: 44, 26,
            54, 20, 17, 31, 55, 77, 93.
         :highlight: data.node[a] data.node[g]
         :indicators: last_heap=f sorted=g

         a[44]
         b[26]
         c[54]
         d[20]
         e[17]
         f[31]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Exchange 44 with 54; the six-item heap is restored.

      Exchange 44 with the larger child, 54. At index 2, its only
      active child is 31 at index 5. Since 44 is greater than 31,
      stop. The value 55 at index 6 is already sorted and cannot
      participate in this comparison.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (6 items)
         :alt: Exchange 44 with 54; the six-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[a] heap.node[c]

         a[54] -left-> b[26]
         a -right-> c[44]
         b -left-> d[20]
         b -right-> e[17]
         c -left-> f[31]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 44 with 54; the six-item heap is restored. Array: 54,
            26, 44, 20, 17, 31, 55, 77, 93.
         :highlight: data.node[a] data.node[c]
         :indicators: last_heap=f sorted=g

         a[54]
         b[26]
         c[44]
         d[20]
         e[17]
         f[31]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 54 at index 5; shrink the heap to five items.

      Exchange root 54 with the last active value, 31, then exclude
      index 5. The sorted suffix is [54, 55, 77, 93]. Compare the
      replacement root, 31, with children 26 and 44.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (5 items)
         :alt: Place 54 at index 5; shrink the heap to five items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[31] -left-> b[26]
         a -right-> c[44]
         b -left-> d[20]
         b -right-> e[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 54 at index 5; shrink the heap to five items. Array: 31,
            26, 44, 20, 17, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[f]
         :indicators: last_heap=e sorted=f

         a[31]
         b[26]
         c[44]
         d[20]
         e[17]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Exchange 31 with 44; the five-item heap is restored.

      Exchange 31 with the larger child, 44. The value 31 reaches a
      leaf in the active heap, so stop. The root now holds the next
      maximum, 44.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (5 items)
         :alt: Exchange 31 with 44; the five-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[a] heap.node[c]

         a[44] -left-> b[26]
         a -right-> c[31]
         b -left-> d[20]
         b -right-> e[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 31 with 44; the five-item heap is restored. Array: 44,
            26, 31, 20, 17, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[c]
         :indicators: last_heap=e sorted=f

         a[44]
         b[26]
         c[31]
         d[20]
         e[17]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 44 at index 4; shrink the heap to four items.

      Exchange root 44 with the last active value, 17, then exclude
      index 4. The sorted suffix is [44, 54, 55, 77, 93]. Compare the
      replacement root, 17, with children 26 and 31.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (4 items)
         :alt: Place 44 at index 4; shrink the heap to four items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[17] -left-> b[26]
         a -right-> c[31]
         b -left-> d[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 44 at index 4; shrink the heap to four items. Array: 17,
            26, 31, 20, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[e]
         :indicators: last_heap=d sorted=e

         a[17]
         b[26]
         c[31]
         d[20]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Exchange 17 with 31; the four-item heap is restored.

      Exchange 17 with the larger child, 31. The value 17 reaches a
      leaf, so stop. The remaining active values form a max-heap
      with 31 at the root.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (4 items)
         :alt: Exchange 17 with 31; the four-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[a] heap.node[c]

         a[31] -left-> b[26]
         a -right-> c[17]
         b -left-> d[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 17 with 31; the four-item heap is restored. Array: 31,
            26, 17, 20, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[c]
         :indicators: last_heap=d sorted=e

         a[31]
         b[26]
         c[17]
         d[20]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 31 at index 3; shrink the heap to three items.

      Exchange root 31 with the last active value, 20, then exclude
      index 3. The sorted suffix is [31, 44, 54, 55, 77, 93]. The
      replacement root, 20, has children 26 and 17.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (3 items)
         :alt: Place 31 at index 3; shrink the heap to three items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[20] -left-> b[26]
         a -right-> c[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 31 at index 3; shrink the heap to three items. Array: 20,
            26, 17, 31, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[d]
         :indicators: last_heap=c sorted=d

         a[20]
         b[26]
         c[17]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Exchange 20 with 26; the three-item heap is restored.

      Exchange 20 with the larger child, 26. The value 20 reaches a
      leaf, so stop. The next maximum is 26.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (3 items)
         :alt: Exchange 20 with 26; the three-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[a] heap.node[b]

         a[26] -left-> b[20]
         a -right-> c[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 20 with 26; the three-item heap is restored. Array: 26,
            20, 17, 31, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[b]
         :indicators: last_heap=c sorted=d

         a[26]
         b[20]
         c[17]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 26 at index 2; shrink the heap to two items.

      Exchange root 26 with the last active value, 17, then exclude
      index 2. The sorted suffix is [26, 31, 44, 54, 55, 77, 93]. The
      replacement root, 17, has just one active child, 20.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (2 items)
         :alt: Place 26 at index 2; shrink the heap to two items. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[17] -left-> b[20]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 26 at index 2; shrink the heap to two items. Array: 17, 20,
            26, 31, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[c]
         :indicators: last_heap=b sorted=c

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
      :caption: Exchange 17 with 20; the two-item heap is restored.

      Exchange 17 with its only child, 20. The heap property holds
      again, with 20 at the root.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (2 items)
         :alt: Exchange 17 with 20; the two-item heap is restored. Active heap
            shown as a tree.
         :highlight: heap.node[a] heap.node[b]

         a[20] -left-> b[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Exchange 17 with 20; the two-item heap is restored. Array: 20,
            17, 26, 31, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[b]
         :indicators: last_heap=b sorted=c

         a[20]
         b[17]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

   .. tb-scene::
      :caption: Place 20 at index 1; only 17 remains in the heap.

      Exchange root 20 with the last active value, 17, then exclude
      index 1. A one-item heap needs no sift-down. The remaining value,
      17, must be the smallest and is already in its final position.

      .. tb-graph:: heap
         :style: tree
         :align: center
         :label: Active heap (1 item)
         :alt: Place 20 at index 1; only 17 remains in the heap. Active heap
            shown as a tree.
         :highlight: heap.node[a]

         a[17]

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: Place 20 at index 1; only 17 remains in the heap. Array: 17, 20,
            26, 31, 44, 54, 55, 77, 93.
         :highlight: data.node[a] data.node[b]
         :indicators: last_heap=a sorted=b

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
      :caption: The array is sorted in ascending order.

      Treat the final value, 17, as sorted too. The active heap is empty,
      and the full array is [17, 20, 26, 31, 44, 54, 55, 77, 93].
      Each extraction placed the largest remaining value immediately
      before the sorted suffix. All exchanges took place in the original
      array; the tree was another view of those same values.

      .. tb-graph:: data
         :style: array
         :align: center
         :label: Array
         :show-indices:
         :alt: The array is sorted in ascending order. Array: 17, 20, 26, 31,
            44, 54, 55, 77, 93.
         :indicators: sorted=a

         a[17]
         b[20]
         c[26]
         d[31]
         e[44]
         f[54]
         g[55]
         h[77]
         i[93]

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
