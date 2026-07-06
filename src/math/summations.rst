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

.. index:: summation

Summations
==========
Most programs contain loop constructs.
When analyzing running time costs for programs with loops, we
need to add up the costs for each time the loop is executed.
This is an example of a *summation*.
Summations are simply the sum of costs for some function applied to a
range of values.
Summations are typically written with the following "Sigma"
notation:

.. math::

   \sum_{k=1}^{n} f(k)

This notation indicates that we are adding the result of
:math:`f(k)` over some range of (integer) values.

The expression parameter and its initial value are indicated
below the :math:`\sum` symbol.
Here, the notation :math:`k=1` indicates that the parameter is
:math:`k` and that it begins with the value 1.
At the top of the :math:`\sum` symbol is the expression :math:`n`.
This indicates the maximum value for the parameter :math:`k`.
Thus, this notation means to sum the values of :math:`f(k)` as
:math:`k` ranges across the integers from 1 through :math:`n`.
In other words, 

.. math::

   \sum_{k=1}^{n} f(k)

is simply a way to express the sum

.. math::

   f(1) + f(2) + \cdots + f(n-1) + f(n)

Given a summation, you often wish to replace it with an algebraic
equation with the same value as the summation.
This is known as a *closed-form solution*,
and the process of replacing the summation with its closed-form
solution is known as solving the summation.

A closed form is an expression that can be computed by applying 
a fixed number of familiar operations to the arguments.
For example, the expression :math:`2 + 4 + \cdots + 2n` is not a
closed form, but the expression :math:`n(n+1)` is a closed form.

For example, the summation
:math:`\sum_{k=1}^{n} 1`
is simply the constant expression "1" added :math:`n` times
(remember that :math:`k` ranges from 1 to :math:`n`).
Because the sum of :math:`n` 1s is :math:`n`,
the closed-form solution is :math:`n`.
In other words, a summation of a constant expression is
equivalent to counting by the constant value "math"`n` times,
or multiplying the constant by :math:`n`.

Summation facts
---------------

+------------------------------+--------------------------------+
| **Fact 1**                   | **Fact 2**                     |
|                              |                                |
| .. math::                    | .. math::                      |
|                              |                                |
|    \sum ca_k = c\sum a_k     |    \sum (a_k + b_k) =          |
|                              |    \sum a_k + \sum b_k         |
+------------------------------+--------------------------------+
| **Fact 3**                   | **Fact 4**                     |
|                              |                                |
| .. math::                    | .. math::                      |
|                              |                                |
|    \sum a_kx^{i+k} =         |    \sum_{k = m}^{n} a_{k+i} =  |
|    x^i \sum a_kx^k           |    \sum_{k = m+i}^{n+i} a_{k}  |    
+------------------------------+--------------------------------+


+------------------------------------------------------------------------+
| **Collapsing sums (Fact 5)**                                           |
+--------------------------------+-----+---------------------------------+
|                                |     |                                 |
| .. math::                      |     | .. math::                       |
|                                | and |                                 |
|   \sum_{k = 1}^{n}             |     |    \sum_{k = 1}^{n}             |
|   (a_k - a_{k-1}) = a_n - a_0  |     |     (a_{k-1} - a_k) = a_0 - a_n |
+--------------------------------+-----+---------------------------------+


.. tb-group::
   :name: tab_useful_forms

   .. tb-tab:: Useful forms

      Here is a list of useful summations, along with their closed-form solutions.

      .. math::

         \sum_{k = 1}^{n} k = \frac{n (n+1)}{2}.

      .. math::

         \sum_{k = 1}^{n} k^2 = \frac{2 n^3 + 3 n^2 + n}{6} =
         \frac{n(2n + 1)(n + 1)}{6}.

      .. math::

         \sum_{k = 1}^{\log n} n = n \log n.

      .. math::
         :label: semi

         \sum_{k=0}^{n} a^k = \frac{a^{n+1} - 1}{a - 1}\ \mbox{where}
         \ a \neq 1.

   .. tb-tab:: Special cases

      As special cases to :eq:`semi`, we have the following two:

      .. math::
         :label: case1

         \sum_{k = 1}^{n} \frac{1}{2^k} = 1 - \frac{1}{2^n},

      .. math::
         :label: case2

         \sum_{k = 0}^{n} 2^k = 2^{n+1} - 1.

      As a corollary to equation :eq:`case2`,

      .. math::

         \sum_{k = 0}^{\log n} 2^k = 2^{\log n + 1} - 1 = 2n - 1.

      Finally,

      .. math::
         :label: power

         \sum_{k=1}^{n} \frac{k}{2^k} = 2 - \frac{n+2}{2^n}.

      Most of these equalities can be proved using a
      :term:`proof by induction`.
      Unfortunately, induction does not help us derive a closed-form
      solution.
      Induction only confirms when a proposed closed-form solution is
      correct.

.. topic:: Example

   Find a closed form for the expression :math:`\sum_{k=2}^{n} (k-1) 2^{k+1}`.

   **Solution:**

   .. math::

      \sum_{k=2}^{n} (k-1) 2^{k+1} &= \sum_{k=1}^{n-1} k2^{k+2} \qquad \text{Fact 4} \\
                                   &= 2^2 \sum_{k=1}^{n-1} k2^k \qquad \text{Fact 3} \\
                                   &= 2^2 \left(2 - n2^n + (n-1)2^{n+1}\right) \qquad \text{Form 5} \\
                                   &= 2^3 - (2 - n)2^{n+2}


.. topic:: Example

   Use summation facts and forms to prove :math:`2 + 3 + \cdots + n = \frac{(n-1)(n+2)}{2}`.

   **Solution:**

   .. math::

      2 + 3 + \cdots + n &= \sum_{k=2}^{n} k \\
                         &= \sum_{k=1}^{n-1}(k+1) \\
                         &= \sum_{k=1}^{n-1}k + \sum_{k=1}^{n-1}1 \\
                         &= \frac{(n-1)(n)}{2} + (n-1) \\
                         &= \frac{(n-1)(n+2)}{2}


.. topic:: Example

   Use summation facts and forms to find a closed form for :math:`3 + 7 + \cdots + (3+4n)`.

   **Solution:**

   .. math::

      \sum_{k=0}^{n}(3+4k) &= \sum_{k=0}^{n} 3 + \sum_{k=0}^{n} 4k \\
                           &= \sum_{k=0}^{n} 3 + 4 \sum_{k-0}^{n} k \\
                           &= 3(n+1) + \frac{4n(n+1)}{2} \\
                           &= (3+2n)(n+1) 


.. topic:: Example

   Let *count(n)* be the number of times ``func()`` is executed by the following
   algorithm as a function of :math:`n`,
   where :math:`n \in \mathbb{N}`. 
   Find a closed for for *count(n)*.

   .. code-block:: cpp

      int i = 1;
      while (i < n) {
         i = i + 2;
         for (int j = 1; j <= i; ++j) {
            func();
         }
      }

   **Solution:**

   Each time through the while loop, ``i`` is incremented by 2.
   So the values of ``i`` at the start of the for loop are
   :math:`3, 5, \cdots, (2k+1)`, where
   :math:`i = 2k + 1 \ge n`
   represents the stopping point for the while loop.
   So we have:

   .. math::

      \textit{count(n)} &= 3+5+ \cdots + (2k+1) \\
                        &= \sum_{i=1}^{k}(2i+1) \\
                        &= 2 \sum_{i=1}^{k}i + \sum_{i=1}^{k}1 \\
                        &= \frac{2k(k+1)}{2} + k \\
                        &= k(k+1) + k \\
                        &= k(k+2)

   In order to write *count(n)* in terms of :math:`n`,
   we need to do a bit more work.
   Since :math:`2k +1 \ge n` is the stopping point for the while loop
   it follows that :math:`2k - 1 \lt n` is the last time the 
   while condition is ``true``.
   In otherwords, we have the inequality
   :math:`2k-1 \lt n \le 2k+1`.
   Solving for :math:`k`, we have :math:`2k - 2 \lt n-1 \le 2k`,
   which gives :math:`k-1 \lt (n-1)/2 \le k`.
   Therefore, :math:`k = \lceil (n-1)/2 \rceil`.
   Now we can write *count(n)* in terms of :math:`n` as:

   .. math::

      \textit{count(n)} &= k(k+2) \\
                        &= \Bigg \lceil \frac{n-1}{2} \Bigg \rceil \left(\Bigg \lceil \frac{n-1}{2} \Bigg \rceil + 2\right)
      

Approximating Sums
------------------
Not all sums have closed forms.
In those cases, we can try to find a suitable approximation.
For example, consider the following sum:

.. math::

   {\cal H}_n &= 1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} \\
              &= \sum_{k=1}^{n} \frac{1}{k}


This is called the *Harmonic Series* and it has no closed form.
It is closely approximated by :math:`\ln{n}` because the definite integral
of :math:`1/x` from 1 to *n* is :math:`\ln{n}`.
The constant known as Euler's constant :math:`(\gamma)` with a value 
close to 0.577, approximates the difference between
:math:`{\cal H}_n` and :math:`\ln{n}` when :math:`n` is large.

.. math::

   {\cal H}_{10} - \ln{10} \approx 2.93 - 2.31 = 0.62 \\
   {\cal H}_{20} - \ln{20} \approx 3.00 - 2.60 = 0.60 \\
   {\cal H}_{40} - \ln{40} \approx 4.28 - 3.69 = 0.59


.. admonition:: More to Explore

   - :wiki:`Geometric series <Geometric_series>`
   - `700 years of secrets of the Sum of Sums <https://www.youtube.com/watch?v=vQE6-PLcGwU>`__


.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.
