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

.. index:: logarithms

Logarithms
==========
The logarithm of base :math:`b` for value :math:`y` is the
power to which :math:`b` is raised to get :math:`y`.
Normally, this is written as :math:`\log_b y = x`.
Thus, if :math:`\log_b y = x` then :math:`b^x = y`,
and :math:`b^{log_b y} = y`.

Logarithms have the following properties, for any positive values of
:math:`m`, :math:`n`, and :math:`r`, and any positive integers
:math:`a` and :math:`b`. 

#) :math:`\log (nm) = \log n + \log m`.

#) :math:`\log (n/m) = \log n - \log m`.

#) :math:`\log (n^r) = r \log n`.

#) :math:`\log_a n = \log_b n / \log_b a`.

The first two properties state that the logarithm
of two numbers multiplied (or divided) can be found by adding
(or subtracting) the logarithms of the two numbers. [#]_
Property (3) is simply an extension of property (1).
Property (4) tells us that, for variable :math:`n` and any two integer
constants :math:`a` and :math:`b`, :math:`\log_a n` and
:math:`\log_b n` differ by the constant factor :math:`\log_b a`,
regardless of the value of :math:`n`.
Most runtime analyses we use are of a type that ignores
constant factors in costs.
Property (4) says that such analyses need not be concerned with the
base of the logarithm, because this can change the total cost only by
a constant factor.

.. tabbed:: math_logs

   .. tab:: log base 2

      C and C++ have always included functions to compute :math:`\log_e`
      and :math:`\log_{10}`. New in C++11 is a function specifically
      for base 2.
      As we will see, base 2 logarithms are used frequently and it is
      convenient to not have to perform change in base calculations
      when :math:`\log_2` is needed.

      .. code-block:: cpp

         double x = std::log(1000);  // natural log of 1000

         double x = std::log10(1000);  // base 10 log of 1000

         double x = std::log2(1000);  // base 2 log of 1000

      In this course, nearly all logarithms used have a base of two.
      This is because data structures and algorithms most often divide
      things in half, or store codes with binary bits.
      Whenever you see the notation :math:`\log n` in this text,
      either :math:`\log_2 n` is meant or else the term is being used
      asymptotically and so the actual base does not matter.
      For logarithms using any base other than two, we will show the base
      explicitly.

   .. tab:: Run It

      .. activecode:: ac_math_log2
         :language: cpp
         :caption: Log Operations
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <cmath>
         int main()
         {
             std::cout << "log(1) = " << std::log(1) << '\n'
                       << "base-5 logarithm of 125 = " << std::log(125)/std::log(5) << '\n';

             std::cout << "log2(65536) = " << std::log2(65536) << '\n'
                 << "log2(0.125) = " << std::log2(0.125) << '\n'
                 << "log2(0x020f) = " << std::log2(0x020f)
                 << " (highest set bit is in position 9)\n"
                 << "base-5 logarithm of 125 = " << std::log2(125)/std::log2(5) << '\n';

             // special values
             std::cout << "log2(1) = " << std::log2(1) << '\n'
                       << "log2(+Inf) = " << std::log2(INFINITY) << '\n';

         }

.. topic:: Example

   Many programs require an encoding for a collection of objects.
   What is the minimum number of bits needed to represent :math:`n`
   distinct code values?
   The answer is :math:`\lceil \log_2 n \rceil` bits.
   For example, if you have 1000 codes to store, you will require at
   least :math:`\lceil \log_2 1000 \rceil = 10` bits to have 1000
   different codes (10 bits provide 1024 distinct code values).

.. topic:: Example

   Consider the binary search 
   algorithm for finding a given value within an array sorted by value
   from lowest to highest.

   Binary search first looks at the middle element
   and determines if the value being searched for is in the upper half
   or the lower half of the array.
   The algorithm then continues splitting the appropriate
   subarray in half until the desired value is found.
   How many times can an array of size \(n\) be split in half until
   only one element remains in the final subarray?
   The answer is :math:`\lceil \log_2 n \rceil` times.

A useful identity to know is:

.. math::

   2^{\log n} = n

To give some intuition for why this is true:
What does it mean to take the log (base 2) of :math:`n`?
If :math:`\log_2 n = x`, then :math:`x` is the power to which you need
to raise 2 to get back to :math:`n`.
So of course, :math:`2^{\log n} = n` when the base of the log is 2.

When discussing logarithms, exponents often lead to confusion.
Property (3) tells us that :math:`\log n^2 = 2 \log n`.
How do we indicate the square of the logarithm (as opposed to the
logarithm of :math:`n^2`)?
This could be written as :math:`(\log n)^2`, but it is traditional to
use :math:`\log^2 n`.
On the other hand, we might want to take the logarithm of the
logarithm of :math:`n`.
This is written :math:`\log \log n`.

A special notation is used in the rare case when we need to know how
many times we must take the log of a number before we reach a
value :math:`\leq 1`.
This quantity is written :math:`\log^* n`.
For example, :math:`\log^* 1024 = 4` because
:math:`\log 1024 = 10`, :math:`\log 10 \approx 3.33`,
:math:`\log 3.33 \approx 1.74`,
and :math:`\log 1.74 < 1`, which is a total of 4 log operations.

**Self Check**

.. tabbed:: math_log_check

   .. tab:: Q1

      .. fillintheblank:: fitb_math_log1
         :casei:

         Simplify the following expression into the form :math:`log(c)`:
         :math:`\log(15) - \log(3)`

         - :log\(5\): Good job.
           :log\(15/3\): Close. This expression can be even simpler.
           :0.69 0.05: This is a numeric approximation of the base 10 log, not a simplification.
           :1.69 0.05: This is a numeric approximation of the natural log, not a simplification.
           :x: Use the rule :math:`\log(a)−\log(b)=\log(\frac{a}{b})`


   .. tab:: Q2

      .. fillintheblank:: fitb_math_log2
         :casei:

         Simplify the following expression into the form :math:`log(c)`:
         :math:`\log(3) + \log(4)`

         - :log\(12\): Good job.
           :log\(3\*4\): Close. This expression can be even simpler.
           :1.07 0.05: This is a numeric approximation of the base 10 log, not a simplification.
           :2.48 0.05: This is a numeric approximation of the natural log, not a simplification.
           :x: Use the rule :math:`\log(a)+\log(b)=\log(a*b)`


   .. tab:: Q3

      .. fillintheblank:: fitb_math_log3
         :casei:

         Solve the following expression:
         :math:`\log_{729}(9)`

         - :1/3: Good job.
           :0.33 0.05: This is a numeric approximation not an exact solution. Note the cube root of 729 is 9.
           :x: Use the rule if :math:`b^y = x`, then :math:`\log_bx = y`


.. admonition:: More to Explore

   - From cppreference.com

     - :cmath:`log`, :cmath:`log`, and :cmath:`log2`


.. topic:: Footnotes

   .. [#] These properties are the idea behind the slide rule.
          Adding two numbers can be viewed as joining two lengths
          together and measuring their combined length.
          Multiplication is not so easily done.
          However, if the numbers are first converted to the lengths of
          their logarithms, then those lengths can be added and the
          inverse logarithm of the resulting length gives the answer for
          the multiplication (this is simply logarithm property (1)).
          A slide rule measures the length of the logarithm for the
          numbers, lets you slide bars representing these lengths to add
          up the total length, and finally converts this total length to
          the correct numeric answer by taking the inverse of the
          logarithm for the result. 

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

