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

.. _sort_merge:

.. index::
   single: merge sort
   pair: sorting algorithms; merge sort
   pair: merge sort; divide and conquer

Merge sort
==========
We now turn our attention to using a :term:`divide and conquer` strategy as a
way to improve the performance of sorting algorithms. The first
algorithm we will study is the **merge sort**. Merge sort is a recursive
algorithm that continually splits a vector in half. If the vector is empty
or has one item, it is sorted by definition (the base case). If the vector
has more than one item, we split the vector and recursively invoke a merge
sort on both halves. Once the two halves are sorted, the fundamental
operation, called a **merge**, is performed. Merging is the process of
taking two smaller sorted vectors and combining them together into a
single, sorted, new vector. The :ref:`following sequence <fig_mergesortA>`
shows the recursive splits and the :ref:`merge process <fig_mergesortB>`
for our familiar example array.

.. tb-stack::
   :name: merge-sort-process
   :caption: Merge sort: split, sort, and merge

   .. tb-scene::
      :name: fig_mergesortA
      :caption: Begin with the original array.

      Merge sort splits an array, sorts its left half recursively, then
      sorts its right half and merges the results.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}

   .. tb-scene::
      :caption: Split into a four-item left half and a five-item right half.

      Because there are 9 elements, the split is an an array of size 4 and
      and array of size 5.
      We continue down the left half of the array.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Split the left half into two pairs.

      The left half splits into [54, 26] and [93, 17].

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [54, 26]}
         left_right{"type": "array", "values": [93, 17]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :caption: Reach the first two base cases.

      Each one-item array is already sorted.
      The parent array will be filled by merging them.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [54, 26]}
         left_right{"type": "array", "values": [93, 17]}
         left_left_left{"type": "array", "values": [54]}
         left_left_right{"type": "array", "values": [26]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right
         left_left -left-> left_left_left
         left_left -right-> left_left_right

   .. tb-scene::
      :caption: Merge the first two leaves: compare 54 and 26.

      To merge two sorted arrays, write the minimum value to parent
      position 0, then repeatedly write the minimum remaining value to
      the next position. The first remaining value in each sorted input
      is its minimum, so compare those values.

      Each write replaces the value already in that parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left_left_left].slot[0]
            merge.node[left_left_right].slot[0]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [54, 26]}
         left_right{"type": "array", "values": [93, 17]}
         left_left_left{"type": "array", "values": [54]}
         left_left_right{"type": "array", "values": [26]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right
         left_left -left-> left_left_left
         left_left -right-> left_left_right

      .. tb-pointer:: parent
         :at: merge.node[left_left].slot[0]

   .. tb-scene::
      :caption: Move 26; then move the minimum remaining value, 54.

      Move 26 to parent position 0.
      The minimum remaining value is 54, the only value left.
      Move it to parent position 1.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left_left].slot[0]
            merge.node[left_left_left].slot[0]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [26, 26]}
         left_right{"type": "array", "values": [93, 17]}
         left_left_left{"type": "array", "values": [54]}
         left_left_right{"type": "array", "values": [""]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right
         left_left -left-> left_left_left
         left_left -right-> left_left_right

   .. tb-scene::
      :caption: Merge the first pair; split the second pair.

      Now split the waiting pair [93, 17] into [93] and [17]. These
      are also sorted base cases.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left_right_left].slot[0]
            merge.node[left_right_right].slot[0]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [26, 54]}
         left_right{"type": "array", "values": [93, 17]}
         left_right_left{"type": "array", "values": [93]}
         left_right_right{"type": "array", "values": [17]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right
         left_right -left-> left_right_left
         left_right -right-> left_right_right

   .. tb-scene::
      :caption: Both pairs in the left half are sorted.

      Merge [93] and [17] by moving 17 before 93. The left half now
      has two sorted child arrays, [26, 54] and [17, 93], ready to merge.
      The right half still waits.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [26, 54]}
         left_right{"type": "array", "values": [17, 93]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :name: fig_mergesortB
      :caption: Merge the two sorted pairs: compare 26 and 17.

      Compare the first remaining value of each sorted child: 26 and 17.
      The smaller value, 17, is the value to move to output position 0.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left_left].slot[0]
            merge.node[left_right].slot[0]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [54, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [26, 54]}
         left_right{"type": "array", "values": [17, 93]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :caption: Move 17; compare 26 and 93.

      Move 17 to output position 0 and advance in the right input.
      Since 26 is less than 93 move 26 to parent position 1.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left].slot[0]
            merge.node[left_left].slot[0]
            merge.node[left_right].slot[1]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": [26, 54]}
         left_right{"type": "array", "values": ["", 93]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :caption: Move 26; compare 54 and 93.

      Move 26 to output position 1 and advance in the left input.
      Compare 54 with 93. Move 54 to position 2 because it is smaller.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left].slot[1]
            merge.node[left_left].slot[1]
            merge.node[left_right].slot[1]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 93, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": ["", 54]}
         left_right{"type": "array", "values": ["", 93]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :caption: Move 54; the left input is exhausted.

      Move 54 to output position 2. The left input is now empty,
      so no further comparison is needed. Move the remaining 93
      from the right input to output position 3.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left].slot[2]
            merge.node[left_right].slot[1]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 17]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         left_left{"type": "array", "values": ["", ""]}
         left_right{"type": "array", "values": ["", 93]}

         root -left-> left
         root -right-> right
         left -left-> left_left
         left -right-> left_right

   .. tb-scene::
      :caption: The left half is sorted.

      Copying 93 to position 3 completes the left half of the array.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Split the right half.

      Split the right half into [77, 31] and [44, 55, 20].
      The lengths differ by one, as in the initial split.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         right_left{"type": "array", "values": [77, 31]}
         right_right{"type": "array", "values": [44, 55, 20]}

         root -left-> left
         root -right-> right
         right -left-> right_left
         right -right-> right_right

   .. tb-scene::
      :caption: Sort the right pair; split the remaining three items.

      The same base-case splits and merge sort [77, 31] into [31, 77].
      We omit those repeated intermediate scenes.

      Split [44, 55, 20] into [44] and [55, 20]. The one-item array
      [44] is sorted; the other child still needs splitting.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         right_left{"type": "array", "values": [31, 77]}
         right_right{"type": "array", "values": [44, 55, 20]}
         right_right_left{"type": "array", "values": [44]}
         right_right_right{"type": "array", "values": [55, 20]}

         root -left-> left
         root -right-> right
         right -left-> right_left
         right -right-> right_right
         right_right -left-> right_right_left
         right_right -right-> right_right_right

   .. tb-scene::
      :caption: Combine the three-item branch.

      Merge [55] and [20] into [20, 55], then merge that result
      with [44] to obtain [20, 44, 55]. These merges follow the same
      front-value comparisons shown earlier, so we summarize them.

      The sorted arrays are ready to merge.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [77, 31, 44, 55, 20]}
         right_left{"type": "array", "values": [31, 77]}
         right_right{"type": "array", "values": [20, 44, 55]}

         root -left-> left
         root -right-> right
         right -left-> right_left
         right -right-> right_right

   .. tb-scene::
      :caption: The right half is sorted.

      Merge [31, 77] and [20, 44, 55] to obtain [20, 31, 44, 55, 77].
      Both halves of the original array are now sorted and ready for the final
      merge.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [20, 31, 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Begin the final merge.

      Merge the two sorted halves into the root array. First compare
      17 and 20; choose 17 for root position 0. Continue writing the
      smaller front value to the next root position, just as in the
      detailed merge of the left half.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[left].slot[0]
            merge.node[right].slot[0]

         root{"type": "array", "values": [54, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": [17, 26, 54, 93]}
         right{"type": "array", "values": [20, 31, 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 17; compare 26 and 20.

      Move 17 from left position 0 to parent position 0.
      Its source cell is now empty.
      Compare the remaining front values, 26 and 20; choose 20 next.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[0]
            merge.node[left].slot[1]
            merge.node[right].slot[0]

         root{"type": "array", "values": [17, 26, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": ["", 26, 54, 93]}
         right{"type": "array", "values": [20, 31, 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 20; compare 26 and 31.

      Move 20 from right position 0 to parent position 1.
      Its source cell is now empty.
      Compare 26 and 31; choose 26 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[1]
            merge.node[left].slot[1]
            merge.node[right].slot[1]

         root{"type": "array", "values": [17, 20, 93, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": ["", 26, 54, 93]}
         right{"type": "array", "values": ["", 31, 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 26; compare 54 and 31.

      Move 26 from left position 1 to parent position 2.
      Its source cell is now empty.
      Compare 54 and 31; choose 31 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[2]
            merge.node[left].slot[2]
            merge.node[right].slot[1]

         root{"type": "array", "values": [17, 20, 26, 17, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": ["", "", 54, 93]}
         right{"type": "array", "values": ["", 31, 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 31; compare 54 and 44.

      Move 31 from right position 1 to parent position 3.
      Its source cell is now empty.
      Compare 54 and 44; choose 44 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[3]
            merge.node[left].slot[2]
            merge.node[right].slot[2]

         root{"type": "array", "values": [17, 20, 26, 31, 77, 31, 44, 55, 20]}
         left{"type": "array", "values": ["", "", 54, 93]}
         right{"type": "array", "values": ["", "", 44, 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 44; compare 54 and 55.

      Move 44 from right position 2 to parent position 4.
      Its source cell is now empty.
      Compare 54 and 55; choose 54 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[4]
            merge.node[left].slot[2]
            merge.node[right].slot[3]

         root{"type": "array", "values": [17, 20, 26, 31, 44, 31, 44, 55, 20]}
         left{"type": "array", "values": ["", "", 54, 93]}
         right{"type": "array", "values": ["", "", "", 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 54; compare 93 and 55.

      Move 54 from left position 2 to parent position 5.
      Its source cell is now empty.
      Compare 93 and 55; choose 55 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[5]
            merge.node[left].slot[3]
            merge.node[right].slot[3]

         root{"type": "array", "values": [17, 20, 26, 31, 44, 54, 44, 55, 20]}
         left{"type": "array", "values": ["", "", "", 93]}
         right{"type": "array", "values": ["", "", "", 55, 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 55; compare 93 and 77.

      Move 55 from right position 3 to parent position 6.
      Its source cell is now empty.
      Compare 93 and 77; choose 77 for the next parent position.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[6]
            merge.node[left].slot[3]
            merge.node[right].slot[4]

         root{"type": "array", "values": [17, 20, 26, 31, 44, 54, 55, 55, 20]}
         left{"type": "array", "values": ["", "", "", 93]}
         right{"type": "array", "values": ["", "", "", "", 77]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 77; the right input is exhausted.

      Move 77 from right position 4 to parent position 7.
      Its source cell is now empty.
      The right input is exhausted. Move the only remaining value, 93,
      to parent position 8; no further comparison is needed.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[7]
            merge.node[left].slot[3]

         root{"type": "array", "values": [17, 20, 26, 31, 44, 54, 55, 77, 20]}
         left{"type": "array", "values": ["", "", "", 93]}
         right{"type": "array", "values": ["", "", "", "", ""]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: Move 93; both inputs are exhausted.

      Move 93 from left position 3 to parent position 8.
      Its source cell is now empty.
      Both input arrays are now empty. Every value has moved into the parent.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.
         :highlight: merge.node[root].slot[8]

         root{"type": "array", "values": [17, 20, 26, 31, 44, 54, 55, 77, 93]}
         left{"type": "array", "values": ["", "", "", ""]}
         right{"type": "array", "values": ["", "", "", "", ""]}

         root -left-> left
         root -right-> right

   .. tb-scene::
      :caption: The final merge completes the sorted array.

      Every item is now in order.

      .. tb-graph:: merge
         :style: tree
         :align: center
         :show-indices:
         :alt: Merge-sort arrays and their parent-child relationships.

         root{"type": "array", "values": [17, 20, 26, 31, 44, 54, 55, 77, 93]}
         left{"type": "array", "values": ["", "", "", ""]}
         right{"type": "array", "values": ["", "", "", "", ""]}

         root -left-> left
         root -right-> right

.. tb-group::
   :name: lst_merge

   .. tb-tab:: Merge Sort

      The ``merge_sort`` function begins by checking the base case.
      If the length of the vector is less than or equal to one, 
      then we already have a sorted vector and no more processing is needed.
      If the length is greater than one,
      then we extract the left and right halves.
      It is important to note that the vector may not have an even
      number of items. That does not matter, as the lengths will differ by at
      most one.

      Once the ``merge_sort`` function is invoked on the left half and the
      right half (lines 23-24), it is assumed they are sorted. The rest of the
      function is responsible for merging the two smaller sorted
      vectors into a larger sorted vector. Notice that the merge operation places
      the items back into the original vector (``data``) one at a time by
      repeatedly taking the smallest item from the sorted vectors.

      The print function shows the vector contents at the start of
      each invocation. There is also a print call at the end to show
      the merging process. The output shows the result of executing the
      function on our example vector. 

      Note that the vector with 44, 55, and 20
      will not divide evenly. The first split gives [44] and the second gives
      [55,20]. It is easy to see how the splitting process eventually yields a
      vector that can be immediately merged with other sorted vectors.

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: lst_merge_cpp
         :caption: The Merge Sort

         #include <iostream>
         #include <string>
         #include <vector>
         using std::cout;
         using std::vector;

         void print(const vector<int>& data) {
            for (const auto& value: data) {
               cout << value << ' ';
            }
            cout << '\n';
         }

         vector<int> merge_sort(vector<int> data) {
            cout << "Splitting ";
            print(data);
            if (data.size() > 1) {
               int mid = data.size() / 2;
               // split data into 2 halves
               vector<int> left(data.begin(),data.begin()+mid);
               vector<int> right(data.begin()+mid,data.end());

               left = merge_sort(left);
               right = merge_sort(right);

               int i = 0, j = 0, k = 0;
               while (i < int(left.size()) && j < int(right.size())) {
                  if(left[i] < right[j]) {
                     data[k] = left[i];
                     ++i;
                  } else {
                     data[k] = right[j];
                     ++j;
                  }
                  ++k;
               }
               while(i < int(left.size())) {
                  data[k] = left[i];
                  ++i;
                  ++k;
               }
               while(j < int(right.size())) {
                  data[k] = right[j];
                  ++j;
                  ++k;
               }
            }
            cout << "Merging ";
            print(data);

            return data;
         }

         int main() {
           vector<int> data = {54, 26, 93, 17, 77, 31, 44, 55, 20};
           print(merge_sort(data));
           return 0;
         }


In the following animations, purple marks a range being split, teal marks the
range being merged, yellow marks the target slot currently filled, and gray
marks merged ranges.

.. Sort animation assets are generated with ``generate_sort_video.py``.

.. only:: html

   .. tb-group::
      :name: merge-sort-animations

      .. tb-tab:: Average case

         .. tb-video:: ../_static/generated/sort/merge-sort-average.webm
            :name: merge-sort-average-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/merge-sort-average.png

      .. tb-tab:: Best case

         .. tb-video:: ../_static/generated/sort/merge-sort-best.webm
            :name: merge-sort-best-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/merge-sort-best.png

      .. tb-tab:: Worst case

         .. tb-video:: ../_static/generated/sort/merge-sort-worst.webm
            :name: merge-sort-worst-video
            :width: 660
            :height: 385
            :thumbnail: ../_static/generated/sort/merge-sort-worst.png

.. only:: not html

   .. figure:: ../_static/generated/sort/merge-sort-average.png
      :alt: Merge sort summary for an average input.

   .. figure:: ../_static/generated/sort/merge-sort-best.png
      :alt: Merge sort summary for an already sorted input.

   .. figure:: ../_static/generated/sort/merge-sort-worst.png
      :alt: Merge sort summary for a reverse-sorted input.

Merge sort analysis
-------------------

In order to analyze the ``merge_sort`` function, we need to consider the
two distinct processes that make up its implementation. 
First, the vector is split into halves.
We already computed (in a binary search) that we can divide a vector in half 
:math:`\log n` times where *n* is the length of the vector.
The second process is the merge.
Each item in the vector will eventually be processed and 
placed on the sorted vector. 
So the merge operation which results in a vector of size *n* requires *n*
operations. 
The result of this analysis is that :math:`\log n` splits,
each of which costs :math:`n` for a total of :math:`n\log n` operations. 
A merge sort is an :math:`O(n \cdot log n)` algorithm and even better,
it is also :math:`\Omega(n \cdot log n)` in the worst case.


Recall that the slicing operator is :math:`O(k)` where k is the size
of the slice. In order to guarantee that ``merge_sort`` will be
:math:`O(n \cdot log n)` we will need to remove the slice operator. Again,
this is possible if we simply pass the starting and ending indices along
with the vector when we make the recursive call. We leave this as an
exercise.

It is important to notice that the ``merge_sort`` function requires extra
space to hold the two halves as they are extracted with the slicing
operations. This additional space can be a critical factor if the vector
is large and can make this sort problematic when working on large data sets.

**Self Check**

.. tb-group::
   :name: tab_check

   .. tb-tab:: Q1

      .. tb-choice::
         :name: question_sort_5

         Given the following list of numbers: [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] which answer illustrates the list to be sorted after 3 recursive calls to mergesort?

         - [ ] [16, 49, 39, 27, 43, 34, 46, 40]

           This is the second half of the list.
         - [x] [21,1]

           Yes, mergesort will continue to recursively move toward the beginning of the list until it hits a base case.
         - [ ] [21, 1, 26, 45]

           Remember mergesort doesn't work on the right half of the list until the left half is completely sorted.
         - [ ] [21]

           This is the list after 4 recursive calls

   .. tb-tab:: Q2

      .. tb-choice::
         :name: question_sort_6

         Given the following list of numbers: [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] which answer illustrates the first two lists to be merged?



         - [ ] [21, 1] and [26, 45]

           The first two lists merged will be base case lists, we have not yet reached a base case.
         - [ ] [[1, 2, 9, 21, 26, 28, 29, 45] and [16, 27, 34, 39, 40, 43, 46, 49]

           These will be the last two lists merged
         - [x] [21] and [1]

           The lists [21] and [1] are the first two base cases encountered by mergesort and will therefore be the first two lists merged.
         - [ ] [9] and [16]

           Although 9 and 16 are next to each other they are in different halves of the list starting with the first split.

.. admonition:: More to Explore

   - `OpenDSA: Mergesort Concepts <https://opendsa.cs.vt.edu/ODSA/Books/Everything/html/Mergesort.html>`__
   - :cpp:`C++ std::inplace_merge <algorithm/inplace_merge>`
   - `Merge Sort visualization <https://visualgo.net/en/sorting>`__

.. topic:: Acknowledgements

   This section is adapted from 
   `Problem Solving with Algorithms and Data Structures using C++ <https://runestone.academy/ns/books/published/cppds/index.html?mode=browsing>`__,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__.
