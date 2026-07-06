.. Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
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

Lower Bounds
============
:term:`Big-O notation <big-O notation>` describes an upper bound.
In other words, big-O notation states a claim about the greatest
amount of some resource (usually time) that is required by an
algorithm for some class of inputs of size :math:`n` (typically
the worst such input, the average of all possible inputs, or the best
such input).

Similar notation is used to describe the least amount of a resource
that an algorithm needs for some class of input.
Like big-O notation, this is a measure of the algorithm's
growth rate.
Like big-O notation, it works for any resource, but
we most often measure the least amount of time or storage required.
And again, like big-O notation, we are measuring the resource
required for some particular class of inputs: the worst-, average-,
or best-case input of size :math:`n`.
   
The :term:`lower bound` for an algorithm
(or a problem, as explained later) 
is denoted by the symbol :math:`\Omega`, pronounced "big-Omega" or
just "Omega".
The following definition for :math:`\Omega` is symmetric with the
definition of big-O.

   For :math:`\mathbf{T}(n)` a non-negatively valued function,
   :math:`\mathbf{T}(n)` is in set :math:`\Omega(g(n))` if there exist
   two positive constants :math:`c` and :math:`n_0` such that
   :math:`\mathbf{T}(n) \geq c g(n)` for all :math:`n > n_0`.

.. topic:: Example

   Assume :math:`\mathbf{T}(n) = c_1 n^2 + c_2 n` for :math:`c_1` and
   :math:`c_2 > 0`. 
   Then,

   .. math::

      c_1 n^2 + c_2 n \geq c_1 n^2

   for all :math:`n > 1`.
   So, :math:`\mathbf{T}(n) \geq c n^2` for :math:`c = c_1` and
   :math:`n_0 = 1`.
   Therefore, :math:`\mathbf{T}(n)` is in :math:`\Omega(n^2)` by the
   definition. 

It is also true that the equation of the example above
is in :math:`\Omega(n)`.
However, as with big-O notation, we wish to get the "tightest"
(for :math:`\Omega` notation, the largest) bound possible.
Thus, we prefer to say that this running time is in :math:`\Omega(n^2)`.

Recall the sequential search algorithm to find a value :math:`K`
within an array of integers.
In the average and worst cases this algorithm is in :math:`\Omega(n)`,
because in both the average and worst cases we must examine
*at least* :math:`cn` values (where :math:`c` is 1/2 in the average
case and 1 in the worst case).

.. admonition:: An alternate definition

   An alternate (non-equivalent) definition for :math:`\Omega` is

      :math:`\mathbf{T}(n)` is in the set :math:`\Omega(g(n))` if
      there exists a positive constant :math:`c` such that
      :math:`\mathbf{T}(n) \geq c g(n)` for an infinite number of
      values for :math:`n`.

   This definition says that for an "interesting" number of
   cases, the algorithm takes at least :math:`c g(n)` time.
   Note that this definition is *not* symmetric with the
   definition of big-O.
   For :math:`g(n)` to be a lower bound,
   this definition *does not* require that
   :math:`\mathbf{T}(n) \geq c g(n)` for
   all values of :math:`n` greater than some constant.
   It only requires that this happen often enough, in particular
   that it happen for an infinite number of values for :math:`n`.
   Motivation for this alternate definition can be found in the
   following example.

   Assume a particular algorithm has the following behavior:


   .. math::

      \mathbf{T}(n) = \left\{ \begin{array}{ll}
      n  & \mbox{for all odd}\ n \geq 1\\
      n^2/100 & \mbox{for all even}\ n \geq 0
      \end{array}
      \right.

   From this definition, :math:`n^2/100 \geq \frac{1}{100} n^2`
   for all even :math:`n \geq 0`.
   So, :math:`\mathbf{T}(n) \geq c n^2` for an infinite number of
   values of :math:`n` (i.e., for all even :math:`n`)
   for :math:`c = 1/100`.
   Therefore, :math:`\mathbf{T}(n)` is in :math:`\Omega(n^2)` by
   the definition. 

   For this equation for :math:`\mathbf{T}(n)`, it is true that
   all inputs of size :math:`n` take at least :math:`cn` time.
   But an infinite number of inputs of size :math:`n` take
   :math:`cn^2` time, so we would like to say that the algorithm
   is in :math:`\Omega(n^2)`. 
   Unfortunately, using our first definition will
   yield a lower bound of :math:`\Omega(n)` because it is not
   possible to pick constants :math:`c` and :math:`n_0` such that
   :math:`\mathbf{T}(n) \geq c n^2` for all :math:`n>n_0`.
   The alternative definition does result in a lower
   bound of :math:`\Omega(n^2)` for this algorithm, which seems to
   fit common sense more closely.
   Fortunately, few real algorithms or computer programs display
   the pathological behavior of this example.
   Our first definition for :math:`\Omega` generally yields the
   expected result.

   Clearly asymptotic bounds notation is not a law of nature.
   It is merely a powerful modeling tool used to describe the
   behavior of algorithms.


Theta Notation
==============
The definitions for big-O and :math:`\Omega` give us ways to
describe the upper bound for an algorithm (if we can find an equation
for the maximum cost of a particular class of inputs of size
:math:`n`) and the lower bound for an algorithm
(if we can find an equation for the minimum cost for
a particular class of inputs of size :math:`n`).
When the upper and lower bounds are the same within a constant factor,
we indicate this by using :math:`\Theta` (big-Theta) notation.
An algorithm is said to be :math:`\Theta(h(n))` if it is in
:math:`O(h(n))` *and* it is in :math:`\Omega(h(n))`.
Note that we drop the word "in" for :math:`\Theta` notation,
because there is a strict equality for two equations with the
same :math:`\Theta`.
In other words, if :math:`f(n)` is :math:`\Theta(g(n))`, then
:math:`g(n)` is :math:`\Theta(f(n))`.

Because the sequential search algorithm is both in :math:`O(n)` and in
:math:`\Omega(n)` in the average case, we say it is :math:`\Theta(n)`
in the average case.

Given an algebraic equation describing the time requirement for
an algorithm, the upper and lower bounds always meet.
That is because in some sense we have a perfect analysis for the
algorithm, embodied by the running-time equation.
For many algorithms (or their instantiations as programs), it is easy
to come up with the equation that defines their runtime behavior.
The analysis for most commonly used algorithms is well understood and
we can almost always give a :math:`\Theta` analysis for them.
However, the class of NP-Complete
problems all have no definitive :math:`\Theta` analysis, just some
unsatisfying big-O and :math:`\Omega` analyses.

Even some "simple" programs are hard to analyze.
Consider the *Collatz Conjecture*.
The Collatz Conjecture or 3x+1 problem can be summarized as follows:

   Take any positive integer :math:`n`. 
   If :math:`n` is even, divide :math:`n` by 2.
   If :math:`n` is odd, multiply :math:`n` by 3 and add 1.
   Repeat the process indefinitely.
   The conjecture states that no matter which number you start with,
   you will always reach 1 eventually.

Nobody currently knows the true upper or lower bounds for the
conjecture, because it is unknown if it is true.

.. code-block:: bash

   while n > 1
      if n is odd
         n ← 3*n + 1
      else
         n ← n / 2
      done if
   done while

While some textbooks and programmers will casually say that an
algorithm is "order of" or "big-O" of some cost function,
it is generally better to use :math:`\Theta` notation rather than
big-O notation whenever we have sufficient knowledge about an
algorithm to be sure that the upper and lower bounds indeed match.
We will use :math:`\Theta` notation in preference to 
big-O notation whenever our state of knowledge makes that possible.
Limitations on our ability to analyze certain algorithms may require
use of big-O or :math:`\Omega` notations.
In rare occasions when the discussion is explicitly about the upper or 
lower bound of a problem or algorithm, the corresponding notation will
be used in preference to :math:`\Theta` notation.

Classifying Functions
---------------------
Given functions :math:`f(n)` and :math:`g(n)` whose growth rates are
expressed as algebraic equations, we might like to determine if one
grows faster than the other.
The best way to do this is to take the limit of the two
functions as :math:`n` grows towards infinity,

.. math::

   \lim_{n \rightarrow \infty} \frac{f(n)}{g(n)}.

If the limit goes to :math:`\infty`, then :math:`f(n)` is in
:math:`\Omega(g(n))` because :math:`f(n)` grows faster.
If the limit goes to zero, then :math:`f(n)` is in :math:`O(g(n))`
because :math:`g(n)` grows faster.
If the limit goes to some constant other than zero, then
:math:`f(n) = \Theta(g(n))` because both grow at the same rate.

.. topic:: Example

   If :math:`f(n) = n^2` and :math:`g(n) = 2n\log n`, is :math:`f(n)` in
   :math:`O(g(n))`, :math:`\Omega(g(n))`, or :math:`\Theta(g(n))`?
   Since

   .. math::

      \frac{n^2}{2n\log n} = \frac{n}{2\log n},

   we easily see that

   .. math::

      \lim_{n \rightarrow \infty} \frac{n^2}{2n\log n} = \infty

   because :math:`n` grows faster than :math:`2\log n`.
   Thus, :math:`n^2` is in :math:`\Omega(2n\log n)`.

Pitfall: Confusing lower bound and best case
---------------------------------------------
A common mistake people make is confusing the lower bound and best case
cost for an algorithm.
In part this is because for simple algorithms,
they look just like the upper bound.

The lower bound represents the least cost an algorithm needs
for a problem of size :math:`n`.

In the best case, only a single element is visited.
Accordingly, the lower bound for this algorithm in the
best case is :math:`\Omega(1)`.
Even when :math:`n` grows large,
the cost for the base case is constant.

In the worst case, every element is visited.
:math:`\Omega(n)` is a lower bound for the cost of the algorithm in the
worst case because the worst case must **always**
examine :math:`n` records.

In the average case, about :math:`\frac{n}{2}` elements are visited.
The lower bound for this algorithm in the
average case is also :math:`\Omega(n)`.
As :math:`n` grows large, the denominator becomes insignificant.
No matter the value of :math:`n`,
for some constant :math:`c`, :math:`cn` is less than or equal to
the average cost of :math:`n/2`.

For this simple algorithm the upper and lower bounds are the same in the
best / average / worst case:

- :math:`O(1)` in the **best case**
- :math:`O(n)` in the **worst case**
- :math:`O(n)` in the **average case**

Then why do we have upper and lower bounds in the first place,
if they work out to be the same?

In the case of functions like sequential search that are perfectly
understood, they **are** the same.
The upper and lower bound will only be different when we are describing
what we know about an algorithm that we 
**don't know the exact cost for**.

This is what :math:`\Theta` is for.
It is a shorthand we use to say the upper and lower bounds match.
We can say the cost is :math:`\Theta` some value.

Sequential search has worst case cost :math:`\Theta(n)` because 
the upper and lower bounds are the same.

**Self Check**

.. tb-group::
   :name: tabbed_check1

   .. tb-tab:: Q1

      .. tb-choice::
         :name: mc-bigtheta1

         Determine the proper relationship between the following pair of functions.

         :math:`f(n) = \sqrt n`

         :math:`g(n) = \log n^2`

         - :math:`f(n) \mbox{ is } \Omega(g(n))`

           + correct!

         - :math:`f(n) \mbox{ is } O(g(n))`

           - :math:`\lim \frac{f(n)}{g(n)} \rightarrow 0`, then :math:`f(n)` is in :math:`O(g(n))`

         - :math:`f(n) \mbox{ is } \Theta(g(n))`

           - :math:`\lim \frac{f(n)}{g(n)} \rightarrow \mbox{constant}`, then :math:`f(n)` is in :math:`\Theta(g(n))`



   .. tb-tab:: Q2

      .. tb-choice::
         :name: mc-bigtheta2

         Determine the proper relationship between the following pair of functions.

         :math:`f(n) = \log n^2`

         :math:`g(n) = \log n + 5`

         - :math:`f(n) \mbox{ is } \Omega(g(n))`

           - :math:`\lim \frac{f(n)}{g(n)} \rightarrow \infty`, then :math:`f(n)` is in :math:`\Omega(g(n))`

         - :math:`f(n) \mbox{ is } O(g(n))`

           - :math:`\lim \frac{f(n)}{g(n)} \rightarrow 0`, then :math:`f(n)` is in :math:`O(g(n))`

         - :math:`f(n) \mbox{ is } \Theta(g(n))`

           + correct!


.. admonition:: More to explore

   - :wiki:`Collatz Conjecture <Collatz_conjecture>` on wikipedia.

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

