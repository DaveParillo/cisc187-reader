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

Radix Sort Analysis
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

   - TBD

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.
