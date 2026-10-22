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

.. _sort_radix:

.. index::
   single: radix sort
   pair: sorting algorithms; radix sort
   pair: radix sort; digit sorting

Radix sort
==========
Consider a sequence of records with keys in the range 0 to 99.
If we have ten bins available, we can first assign records to bins by
taking their key value modulo 10.
Thus, every key will be assigned to the
bin matching its rightmost decimal digit.
We can then take these records from the bins **in order**,
and reassign them to the bins
on the basis of their leftmost (10's place) digit.
We will define values in the range 0 to 9 to have a leftmost digit of
0.
In other words, assign the :math:`i`'th record from array ``A`` to
a bin using the formula ``A[i]/10``.
If we now gather the values from
the bins **in order**, the result is a sorted list.

In this example, we have :math:`r=10` bins and key values in
the range 0 to :math:`r^2-1`.
The total computation is :math:`\Theta(n)`, because we look at each
record and each bin a constant number of times.
This is a great improvement over the simple Binsort where the number
of bins must be as large as the key range.
Note that the example uses :math:`r = 10` so as
to make the bin computations easy to visualize:
Records were placed into bins based on the value of first the
rightmost and then the leftmost decimal digits.
Any number of bins would have worked if we interpret the key values in
terms of the corresponding base.
This is an example of a *Radix Sort*, so called because the
bin computations are based on the :term:`radix` or the
:term:`base` of the key values.
This sorting algorithm can be extended to any number of
keys in any key range.
We simply assign records to bins based on the
keys' digit values working from the rightmost digit to the leftmost.
If there are :math:`k` digits, then this requires that we assign keys to
bins :math:`k` times.

Radix sort walkthrough
----------------------

The following example shows the first pass using our familiar array
``[54, 26, 93, 17, 77, 31, 44, 55, 20]``. Values enter ten digit bins
and are collected into an output array.
Input and Output read from top to bottom. The Bins heading
labels the least-significant digits, 0 through 9, down the left side
of the bin table. Values follow their bin's digit in arrival order
from left to right.
This **stability** is essential: each later pass must preserve the
ordering established by earlier passes among values with equal digits.

.. tb-deck::
   :name: radix-sort-math-first-pass
   :caption: Radix sort pass 1: Least signifigant digit

   .. tb-card::
      :caption: Begin pass 1 with ten empty bins and an empty output array.

      Read Input from top to bottom. For each value, compute
      ``value % 10`` and append it to that digit's bin.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         3 & & \\
         4 & & \\
         5 & & \\
         6 & & \\
         7 & & \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 54 to bin 4.

      Read 54 at input index 0. Since ``54 % 10 == 4``, append 54 to
      bin 4.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         \boxed{54} \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         3 & & \\
         \boxed{4} &
            \boxed{54} &
             \\
         5 & & \\
         6 & & \\
         7 & & \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 26 to bin 6.

      Read 26 at input index 1. Since ``26 % 10 == 6``, append 26 to
      bin 6.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         \boxed{26} \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         3 & & \\
         4 & 54 & \\
         5 & & \\
         \boxed{6} &
            \boxed{26} &
             \\
         7 & & \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 93 to bin 3.

      Read 93 at input index 2. Since ``93 % 10 == 3``, append 93 to
      bin 3.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         \boxed{93} \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         \boxed{3} &
            \boxed{93} &
             \\
         4 & 54 & \\
         5 & & \\
         6 & 26 & \\
         7 & & \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 17 to bin 7.

      Read 17 at input index 3. Since ``17 % 10 == 7``, append 17 to
      bin 7.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         \boxed{17} \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & \\
         5 & & \\
         6 & 26 & \\
         \boxed{7} &
            \boxed{17} &
             \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 77 to bin 7.

      Read 77 at input index 4. Since ``77 % 10 == 7``, append 77
      after 17 in bin 7.
      Values with the same ones digit share a bin.
      Keep [17, 77] in arrival order; the tens digit
      will be considered on the next pass.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         \boxed{77} \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & \\
         5 & & \\
         6 & 26 & \\
         \boxed{7} &
            17 &
            \boxed{77} \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 31 to bin 1.

      Read 31 at input index 5. Since ``31 % 10 == 1``, append 31 to
      bin 1.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         \boxed{31} \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         \boxed{1} &
            \boxed{31} &
             \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & \\
         5 & & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 44 to bin 4.

      Read 44 at input index 6. Since ``44 % 10 == 4``, append 44
      after 54 in bin 4. Keep [54, 44] in arrival order, even though
      44 is numerically smaller than 54.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         \boxed{44} \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         \boxed{4} &
            54 &
            \boxed{44} \\
         5 & & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 55 to bin 5.

      Read 55 at input index 7. Since ``55 % 10 == 5``, append 55 to
      bin 5.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         \boxed{55} \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         \boxed{5} &
            \boxed{55} &
             \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Append 20 to bin 0.

      Read 20 at input index 8. Since ``20 % 10 == 0``, append 20 to
      bin 0. All nine input values are now assigned to bins.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         \boxed{20}
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         \boxed{0} &
            \boxed{20} &
             \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Distribution is complete; collect bins in digit order.

      Visit bins 0 through 9 from top to bottom. Copy each bin's values
      from left to right into the next unused Output positions.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 20 from bin 0 to output index 0.

      Bin 0 contains [20]. Copy 20 to output index 0. The first output
      value has the smallest ones digit, even though it is not the
      smallest number in the input.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         \boxed{0} &
            \boxed{20} &
             \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         \boxed{20} \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 31 from bin 1 to output index 1.

      Bin 1 contains [31]. Copy 31 to output index 1.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         \boxed{1} &
            \boxed{31} &
             \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         \boxed{31} \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 93 from bin 3 to output index 2.

      Bin 2 contains no values, so nothing is copied to Output.

      Bin 3 contains [93], so copy 93 to output
      index 2. A large number can appear early in the output because
      this pass considers only its ones digit.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         \boxed{3} &
            \boxed{93} &
             \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         \boxed{93} \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 54 from bin 4 to output index 3.

      Bin 4 contains [54, 44]. Copy values in order. 54 first.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         \boxed{4} &
            \boxed{54} &
            44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         \boxed{54} \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 44 from bin 4 to output index 4.

      Copy bin 4's next value, 44, to output index 4.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         \boxed{4} &
            54 &
            \boxed{44} \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         \boxed{44} \\
         \varnothing \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 55 from bin 5 to output index 5.

      Copy 55 to output index 5 next.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         \boxed{5} &
            \boxed{55} &
             \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         \boxed{55} \\
         \varnothing \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 26 from bin 6 to output index 6.

      Copy 26 to output index 6.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         \boxed{6} &
            \boxed{26} &
             \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         \boxed{26} \\
         \varnothing \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 17 from bin 7 to output index 7.

      Bin 7 contains two values. Copy 17 first.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         \boxed{7} &
            \boxed{17} &
            77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         26 \\
         \boxed{17} \\
         \varnothing
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy 77 from bin 7 to output index 8.

      Copy bin 7's next value, 77, to output index 8.
      Bins 8 and 9 are empty, so collection is complete.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         \boxed{7} &
            17 &
            \boxed{77} \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         26 \\
         17 \\
         \boxed{77}
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Pass 1 is complete; the output is ordered by ones digit.

      Output is [20, 31, 93, 54, 44, 55, 26, 17, 77]. Its ones digits
      are [0, 1, 3, 4, 4, 5, 6, 7, 7]. The pairs [54, 44] and [17, 77]
      retain their input order. This completes collection for the first
      pass, but the values are not yet in numerical order.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         54 \\
         26 \\
         93 \\
         17 \\
         77 \\
         31 \\
         44 \\
         55 \\
         20
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         26 \\
         17 \\
         77
         \end{bmatrix}
         \end{array}
         \end{array}

   .. tb-card::
      :caption: Copy Output to Input to finish the first pass.

      Copy the completed Output sequence back to Input. The next pass
      will process these values by their tens digit. Preserving each bin's
      arrival order on that pass will retain the ones-digit ordering
      established here. The bin contents shown are the record of this
      completed first pass.

      .. math::

         \begin{array}{ccccc}
         \begin{array}{c}
         \text{Input} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         26 \\
         17 \\
         77
         \end{bmatrix}
         \end{array}
         & \Longrightarrow &
         \begin{array}{c|ll}
         \text{Bins} & & \\[1ex]
         0 & 20 & \\
         1 & 31 & \\
         2 & & \\
         3 & 93 & \\
         4 & 54 & 44 \\
         5 & 55 & \\
         6 & 26 & \\
         7 & 17 & 77 \\
         8 & & \\
         9 & &
         \end{array}
         & \Longrightarrow &
         \begin{array}{c}
         \text{Output} \\[1ex]
         \begin{bmatrix}
         20 \\
         31 \\
         93 \\
         54 \\
         44 \\
         55 \\
         26 \\
         17 \\
         77
         \end{bmatrix}
         \end{array}
         \end{array}

Array-based Radix Sort
----------------------

As with :ref:`Merge sort <sort_merge>`, an efficient implementation of Radix Sort is
somewhat difficult to achieve.
In particular, we would prefer to sort an array of values and avoid
processing linked lists.
If we knew how  many values would be in each bin, then an auxiliary
array of size :math:`r` can be used to define these lengths and guide
us to were each one starts in the output array.
For example, if during the first pass the 0 bin will receive three
records and the 1 bin will receive five records, then we could simply
reserve the first three array positions for the 0 bin and the next
five array positions for the 1 bin.
Exactly this approach is taken by the following implementation.
At the end of each pass, the records are copied back to the original
array.

.. code-block:: cpp

   static void radixsort(int A[], int k, int r, int n) {
     int B[n];
     int count[r];
     int i, j, rtok;
  
     for (i = 0, rtok = 1; i < k; i++, rtok *= r) {  // For k digits
       for (j = 0; j < r; j++) count[j] = 0;  // Initialize count
    
       // Count the number of records for each bin on this pass
       for (j = 0; j < n; j++) count[(A[j]/rtok)%r]++;
    
       // count[j] will be index in B for last slot of bin j.
       // First, reduce count[0] because indexing starts at 0, not 1
       count[0] = count[0] - 1;
       for (j = 1; j < r; j++) count[j] = count[j-1] + count[j];
      
       // Put records into bins, working from bottom of bin
       // Since bins fill from bottom, j counts downwards
       for (j  = n-1; j >= 0; j--) {
         B[count[(A[j]/rtok)%r]] = A[j];
         count[(A[j]/rtok)%r] = count[(A[j]/rtok)%r] - 1;
       }
       for (j = 0; j < n; j++) A[j] = B[j];  // Copy B back
     }
   }

The first inner ``for`` loop initializes array ``count``.
The second loop counts the number of records to be assigned to each
bin.
The third loop sets the values in ``count`` to their proper
indices within array ``B``.
Note that the index stored in ``count[j]``
is the *last* index for bin ``j``; bins are filled
from high index to low index.
The fourth loop assigns the records to the bins (within
array ``B``).
The final loop simply copies the records back to
array ``A`` to be ready for the next pass.
Variable ``rtoi`` stores :math:`r^i` for use in bin computation
on the :math:`i`'th iteration.

Radix sort analysis
-------------------
**Is it really a reasonable assumption to treat** :math:`k` **as a
constant?**
Or is there some relationship between :math:`k` and :math:`n`?
If the key range is limited and duplicate key values are common,
there might be no relationship between :math:`k` and :math:`n`.
To make this distinction more clear, use :math:`N` to denote the
number of distinct key values used by the :math:`n` records.
Thus, :math:`N \leq n`.
Because it takes a minimum of :math:`\log_r N` base :math:`r` digits
to represent :math:`N` distinct key values, we know that
:math:`k \geq \log_r N`.

Now, consider the situation in which no keys are duplicated.
If there are :math:`n` unique keys then :math:`n = N`.
It would require :math:`n` distinct values to represent them.
So now it takes a minimum of :math:`\log_r n` base :math:`r` digits to
represent the :math:`n` distinct key values.
This means that :math:`k \geq \log_r n`.
Because it requires *at least* :math:`\log n` digits
to distinguish between the :math:`n` distinct keys
(within a constant factor -- meaning, the number of digits is
:math:`\Omega(\log n)`),
:math:`k` is in :math:`\Omega(\log n)`.
**This means that Radix Sort requires**
:math:`\Omega(n \log n)`  
**time to process** :math:`n` **distinct key values.**

Of course the key range could be much bigger
:math:`\log_r n` bits is merely the best case possible for :math:`n`
distinct values.
Thus, the :math:`\log_r n` estimate for :math:`k` could be overly
optimistic.
The bottom line of this analysis is that, for the general case of
:math:`n` distinct key values, Radix Sort is at best a
:math:`\Omega(n \log n)` sorting algorithm.

Radix Sort's running time can be much improved (by a constant factor)
if we make base :math:`r` be as large as possible.
This is simplest if we think about integer key values.
Set :math:`r = 2^i` for some :math:`i`.
In other words, the value of :math:`r` is related to the
number of bits of the key processed on each pass.
Each time the number of bits is doubled, the number of passes is cut
in half.
When processing an integer key value, setting :math:`r = 256` allows
the key to be processed one byte at a time.
Processing a 32-bit integer key requires only four passes.
It is not unreasonable on most computers to use
:math:`r = 2^{16} = 64\mbox{K}`, resulting in only two passes for a
32-bit key.
Of course, this requires a ``count`` array of size 64K.
Performance will be good
only if the number of records is about 64K or greater.
In other words, the number of records must be large compared to the
key size for Radix Sort to be efficient.
In many sorting applications, Radix Sort can be tuned in this way to
give better performance.

Radix Sort depends on the ability to make a fixed number of multiway
choices based on a digit value, as well as random access to the bins.
Thus, Radix Sort might be difficult to implement for certain key
types.
For example, if the keys are real numbers or arbitrary length strings,
then some care will be necessary in implementation.
In particular, Radix Sort will need to be careful about deciding when
the "last digit" has been found to distinguish among real numbers,
or the last character in variable length strings.


.. admonition:: More to Explore

   - `Radix Sort visualization <https://visualgo.net/en/sorting>`__
   - :wiki:`Radix sort <Radix_sort>`
   - :wiki:`Counting sort <Counting_sort>`

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.
