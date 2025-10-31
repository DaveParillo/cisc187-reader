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

.. index::
   single: modulus

Modulus operator
================
The modulus operator returns the remainder of
an integer division.
Sometimes written :math:`n \bmod m` in mathematical expressions,
the syntax in C++ is ``n % m``.
From the definition of remainder, :math:`n \bmod m` is the integer
:math:`r` such that :math:`n = qm + r` for :math:`q` an integer,
and :math:`|r| < |m|`.

Therefore, the result of :math:`n \bmod m` must be between 0 and
:math:`m-1` when :math:`n` and :math:`m` are positive integers.
For example, :math:`5 \bmod 3 = 2`; :math:`25 \bmod 3 = 1`,
:math:`5 \bmod 7 = 5`, and :math:`5 \bmod 5 = 0`.

.. tabbed:: modulus

   .. tab:: modulus

      A common source of error is mixing up modulus and
      integer division operations.

      .. code-block:: cpp

         int quotient = 7 / 3;

         int remainder = 7 % 3;

      The first operator, integer division, yields 2.
      The second operator yields 1.
      Thus, 7 divided by 3 is 2 with 1 left over.

   .. tab:: Run It

      .. activecode:: ac_math_modulus
         :language: cpp
         :caption: Modulus Operations
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         This program shows the difference between the division operator
         and the modulus operator.
         ~~~~
         #include <iostream>
         using std::cout;

         int main () {
             int quotient = 7 / 3;
             int remainder = 7 % 3;
             cout << "quotient: " << quotient << '\n';
             cout << "remainder: " << remainder << '\n';
             return 0;
         }

The modulus operator turns out to be surprisingly useful. For example,
you can check whether one number is divisible by another: if ``x % y`` is
zero, then x is divisible by y.

Also, you can use the modulus operator to extract the rightmost digit or
digits from a number. For example, ``x % 10`` yields the rightmost digit of
x (in base 10). Similarly ``x % 100`` yields the last two digits.


.. mchoice:: mod_operator_1
   :answer_a: Use x % 2, and if the result is 0, it is odd.
   :answer_b: Use x % 2, and if the result is  1, it is odd.
   :answer_c: Use x / 2, and if the result is 0, it is odd.
   :answer_d: Use x / 2, and if the result is  1, it is odd.
   :correct: b
   :feedback_a: If you divide a number by two and it has no remainder, that means it is an even number!
   :feedback_b: If you divide a number by two and it has a remainder of one, that means it is an odd number!
   :feedback_c: Dividing a number by two won't give us the information we want.
   :feedback_d: Dividing a number by two won't give us the information we want.

   How could you detmine whether a variable ``x`` is odd?


.. dragndrop:: mod_operator_2
    :feedback: Try again!
    :match_1:  3 % 2|||1
    :match_2: 2 % 3|||2
    :match_3: 6 % 2|||0
    :match_4: 9 % 6|||3

    Match the modulo expression to its result.


.. parsonsprob:: math_cond_recc_p1
   :numbered: left
   :adaptive:

   Construct a block of code that prints the remainder of 18 when
   divided by 13.
   -----
   int main () {
   =====
    int x = 18;
    int y = 13; 
   =====
    cout << x % y;
   =====
    cout << y % x; #paired
   =====
    cout << x / y; #paired
   =====
    cout << y / x; #paired
   =====
   }


.. parsonsprob:: math_cond_recc_p2
   :numbered: left
   :adaptive:

   Construct a function that prints whether a number
   is even.
   -----
   void is_even (int number) {
   =====
   bool is_even (int number) { #distractor
   =====
    if (number % 2 == 0) {
   =====
     cout << true;
    }
   =====
    else {
   =====
     cout << false;
    }
   =====
   }


There is more than one way to assign values to :math:`q`
and :math:`r`, depending on how integer division is interpreted.
The most common mathematical definition computes the mod function as
:math:`n \bmod m = n - m\lfloor n/m\rfloor`.
In this case, :math:`-3 \bmod 5 = 2`.
However, Java and C++ compilers typically use the underlying
processor's machine instruction for computing integer arithmetic.
On many computers this is done by truncating the resulting fraction,
meaning :math:`n \bmod m = n - m (\mathrm{trunc}(n/m))`.
Under this definition, :math:`-3 \bmod 5 = -3`.
Another language might do something different.

Unfortunately, for many applications this is not what the user wants
or expects.
For example, many hash systems
will perform some computation on a record's :term:`key` value and then
take the result modulo the hash table size.
The expectation here would be that the result is a legal index into
the hash table, not a negative number.
Implementers of hash functions must either ensure that the
result of the computation is always positive, or else add the hash
table size to the result of the modulo function when that result is
negative.


.. admonition:: More to Explore

   - From cppreference.com

     - :numeric:`Common math functions <math>`
     - :cmath:`remainder` and :cmath:`remquo`
     - :cmath:`fmod`
     - :cmath:`div`

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

