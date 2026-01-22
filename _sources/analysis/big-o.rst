.. Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
   and/or modify this document under the terms of the GNU Free Documentation
   License, Version 1.3 or any later version published by the Free Software
   Foundation; with Invariant Sections being Forward, and Preface,
   no Front-Cover Texts, and no Back-Cover Texts.  A copy of
   the license is included in the section entitled "GNU Free Documentation
   License".

.. This file is adapted from Problem Solving with Algorithms and Data Structures using C++
   Copyright (C)  Brad Miller, David Ranum, and Jan Pearce
   This work is licensed under the Creative Commons 
   Attribution-NonCommercial-ShareAlike 4.0 International License.
   To view a copy of this license, visit 
   https://creativecommons.org/licenses/by-nc-sa/4.0/.

.. index::
   single: big-O notation
   single: upper bounds

.. _analysis_big_o:

Asymptotic Analysis and Upper Bounds
====================================
Recall our growth rates from a little while ago.

.. plot::

   import numpy as np
   import matplotlib.pyplot as plt
   from scipy.special import gamma

   n = np.linspace(1, 20, 1000)
   plt.plot(n,gamma(n+1))
   plt.plot(n, 2**n)
   plt.plot(n, 2*n**2)
   plt.plot(n, 5*n*np.log2(n))
   plt.plot(n, 20*n, '--')
   plt.plot(n, 10*n, '--')

   plt.ylim(0,500)
   plt.xlim(0,15)

   plt.text(6,  450,'n!')
   plt.text(8, 450, '$2^n$')
   plt.text(13, 450, '$2n^2$')
   plt.text(12, 200, '$5n\cdot\log_{2}(n)$')
   plt.text(14, 300, '$20n$')
   plt.text(14, 120, '$10n$')

   plt.title('Growth Rates')
   plt.xlabel('Input size (n)')
   plt.ylabel('Cost')

   plt.show()

Despite the larger constant for the curve labeled :math:`10 n` in
the figure above, :math:`2 n^2` crosses it at the
relatively small value of :math:`n = 5`.
What if we double the value of the constant in front of the linear
equation?
As shown in the graph, :math:`20 n` is surpassed by :math:`2 n^2`
once :math:`n = 10`.
The additional factor of two for the linear :term:`growth rate` does
not much matter.
It only doubles the :math:`x`-coordinate for the intersection point.
In general, changes to a constant factor in either equation only
shift *where* the two curves cross, not *whether*
the two curves cross.

When you buy a faster computer or a faster compiler,
the new problem size that can be run in a given amount of time for a
given growth rate is
larger by the same factor, regardless of the constant on the
running-time equation.
The time curves for two algorithms with different growth rates
still cross, regardless of their running-time equation constants.
For these reasons, we usually ignore the constants when we want an
estimate of the growth rate for the running time or other resource
requirements of an algorithm.
This simplifies the analysis and keeps us thinking about the most
important aspect: the growth rate.
This is called :term:`asymptotic algorithm analysis`.
To be precise, asymptotic analysis refers to the study of an
algorithm as the input size "gets big" or reaches
a limit (in the calculus sense).
However, it has proved to be so useful to ignore all constant factors
that asymptotic analysis is used for most algorithm comparisons.

Big-O Notation
--------------
When trying to characterize an algorithm’s efficiency in terms of
execution time, independent of any particular program or computer, it is
important to quantify the number of operations or steps that the
algorithm will require. If each of these steps is considered to be a
basic unit of computation, then the execution time for an algorithm can
be expressed as the number of steps required to solve the problem.
Deciding on an appropriate basic unit of computation can be a
complicated problem and will depend on how the algorithm is implemented.

Consider the problem of accumulating a sum.
The idea of a simple loop to add values should be familiar.

.. code-block:: bash

   accumulate1(int: N)
      sum ← 0
      count  ← N
      while count > 0
         sum ← sum + count
         count ← count - 1
      done while
      return sum
   done accumulate

Compare the previous algorithm to this one:

.. code-block:: bash

   accumulate2(int: N)
      if N ≡ 0 return N
      return N + accumulate(N-1)
   done accumulate


Are both implementations valid?

Is one more efficient than the other?

How do we characterize functions that appear to be different
and compare them using a consistent yardstick?
Asymptotic analysis to the rescue.

A good basic unit of computation for comparing the summation algorithms
shown earlier might be to count the number of assignment statements
performed to compute the sum. In the function ``accumulate1``, the number of
assignment statements is 2 --- assigning ``0`` to ``sum`` and 
assigning ``N`` to ``count``,
plus the value of *n* (the number of times we perform
:math:`sum=sum+count` and :math:`count=count-1`).
We can denote this by a function, call it ``T``,
where :math:`T(n)=2 + 2n`. 
The parameter *n* is often referred to as
the “size of the problem,” and we can read this as “T(n) is the time
it takes to solve a problem of size n, namely 2+2n steps.”

In the summation functions given above, it makes sense to use the number
of terms in the summation to denote the size of the problem. We can then
say that the sum of the first 100,000 integers is a bigger instance of
the summation problem than the sum of the first 1,000. Because of this,
it might seem reasonable that the time required to solve the larger case
would be greater than for the smaller case. Our goal then is to show how
the algorithm’s execution time changes with respect to the size of the
problem.

Computer scientists prefer to take this analysis technique one step further.
It turns out that the exact number of operations is not as important as
determining the most dominant part of the :math:`T(n)` function. 
In other words, as the problem gets larger, some portion of the :math:`T(n)`
function tends to overpower the rest. 
This dominant term is what, in the end,
is used for comparison.
The **order of magnitude** function describes the part
of :math:`T(n)` that increases the fastest as the value of *n* increases. 
Order of magnitude is often called **Big-O notation** (for “order”) and
written as :math:`O(f(n))`.
It provides a useful approximation to the actual number of
steps in the computation. The function :math:`f(n)` provides a simple
representation of the dominant part of the original :math:`T(n)`.

In the above example, :math:`T(n)=2+2n`. As *n* gets large, the
constants will become less and less significant to the final result. If
we are looking for an approximation for :math:`T(n)`, then we can drop
them and simply say that the running time is :math:`O(n)`. It is
important to note that the constants are certainly significant for
:math:`T(n)`. However, as *n* gets large, our approximation will be
just as accurate without it.

.. admonition:: Try This!

   Prove to yourself that the recursive version of the summation
   in ``accumulate2`` has the same :math:`O(n)` performance as
   ``accumulate1``.


.. topic:: Example

   Suppose that for some algorithm, the exact number of
   steps is :math:`T(n)=5n^{2}+27n+1005`. When *n* is small, say 1 or 2,
   the constant 1005 seems to be the dominant part of the function.
   However, as *n* gets larger, the :math:`n^{2}` term becomes the most
   important. In fact, when *n* is really large, the other two terms become
   insignificant in the role that they play in determining the final
   result. Again, to approximate :math:`T(n)` as *n* gets large, we can
   ignore the other terms and focus on :math:`5n^{2}`. In addition, the
   coefficient :math:`5` becomes insignificant as *n* gets large. We
   would say then that the function :math:`T(n)` has an order of
   magnitude :math:`f(n)=n^{2}`, or simply that it is :math:`O(n^{2})`.


**Self Check**

.. tabbed:: tabbed_check1

   .. tab:: Q1

      .. mchoice:: bigo3
         :answer_a: O(2n)
         :answer_b: O(n)
         :answer_c: O(3n<sup>2</sup>)
         :answer_d: O(n<sup>2</sup>)
         :answer_e: More than one of the above
         :correct: d
         :feedback_a: No, 3n<sup>2</sup> dominates 2n. Try again.
         :feedback_b: No, n<sup>2</sup> dominates n. Try again.
         :feedback_c: No, the 3 should be omitted because n<sup>2</sup> dominates.
         :feedback_d: Right!
         :feedback_e: No, only one of them is correct. Try again.


         If the exact number of steps is :math:`T(n)=2n+3n^{2}-1` what is the Big O?

   .. tab:: Q2

      .. parsonsprob:: parsonsBigO

         Without looking at the graph above, from top to bottom order the following from most to least efficient.
         -----
         constant
         logarithmic
         linear
         log linear
         quadratic
         cubic
         exponential

   .. tab:: Q3

      .. mchoice:: crossoverefficiency
         :answer_a: Algorithm 1 will require a greater number of steps to complete than Algorithm 2
         :answer_b: Algorithm 2 will require a greater number of steps to complete than Algorithm 1
         :answer_c: Algorithm 1 will require a greater number of steps to complete than Algorithm 2 until they reach the crossover point
         :answer_d: Algorithm 1 and 2 will always require the same number of steps to complete
         :correct: c
         :feedback_a: This could be true depending on the input, but consider the broader picture
         :feedback_b: This could be true depending on the input, but consider the broader picture
         :feedback_c: Correct!
         :feedback_d: No, the efficiency of both will depend on the input

         Which of the following statements is true about the two algorithms?
         Algorithm 1: 100n + 1
         Algorithm 2: n^2 + n + 1


Using summation facts
---------------------
Sometimes we can combine our knowledge of
asymptotic analysis and math facts to make algorithms more
efficient.

.. tabbed:: tabbed_summation_facts

   .. tab:: Sum

      Starting with the original accumulate algortihm.

      .. code-block:: bash

         accumulate1(int: N)
            sum ← 0
            count  ← N
            while count > 0
               sum ← sum + count
               count ← count - 1
            done while
            return sum
         done accumulate

      When we discussed :doc:`../math/summations`,
      we saw that is loop is equivalent to

      .. math::

         \sum_{k = 1}^{n} k = \frac{n (n+1)}{2}.

      We can use this fact to transform
      our :math:`O(n)` algorithm into :math:`O(1)`.
      The cost of :math:`O(1)` algorithms is *constant*.
      :term:`Constant time <constant time>` algorithms do not grow
      more expensive as the size of :math:`n` grows large.

   .. tab:: Run It

      .. activecode:: ac_analysis_accumulate_bigo
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <ctime>
         #include <iostream>

         clock_t start() {
            return clock();
         }
         void time_since(clock_t start) {
            clock_t end = clock();
            double elapsed_secs = double(end - start) / CLOCKS_PER_SEC;
            std::cout << std::fixed
                      << " took "<< elapsed_secs << " seconds\n";
         }

         long accumulate1(long n){
            long sum = 0;
            for (long i = n; i > 0; --i){
                sum = sum + i;
            }
            return sum;
         }

         long accumulate2(long n){
             return (n*(n+1))/2;
         }

         int main(){

             for (int N=1000; N<1e6; N*=10) {
                clock_t begin = clock();
                std::cout << "N: " << N 
                          << ", Sum1 = " << accumulate1(N) << '\t';
                time_since(begin);
             }

             for (int N=1000; N<1e6; N*=10) {
                clock_t begin = clock();
                std::cout << "N: " << N 
                          << ", Sum2 = " << accumulate2(N) << '\t';
                time_since(begin);
             }

             return 0;
         }

There are two important things to notice about this output. 
First, the times
recorded above are shorter than any of the previous examples. Second, they are
very consistent no matter what the value of :math:`n`. 
It appears that ``accumulate2`` is
hardly impacted by the number of integers being added.

But what does this benchmark really tell us? Intuitively, we can see that the
iterative solutions seem to be doing more work since some program steps are
being repeated. 
This is likely the reason it is taking longer. Also, the time required for 
the iterative solution seems to increase as we increase the value of :math:`n`.
However, there is a problem.
If we run the same function on a different
computer or used a different programming language, we would get
different results. It could take even longer to perform ``accumulate2`` 
if the computer were older.

Asymptotic analysis gives us the tools to definitively state,
without resorting to measuring execution time,
that the ``accumulate2`` runs in :term:`constant time`,
while the ``accumulate1`` function runs in :math:`O(n)` time.

Pitfall: Confusing upper bound and worst case
---------------------------------------------
A common mistake people make is confusing the upper bound and worst case
cost for an algorithm.
The upper bound represents the highest growth rate an
algorithm may have for size :math:`n`.
The sequential search algorithm we discussed in :doc:`cases`
involved 3 key input cases:

#. When the target value was in the first element (base case)
#. When the target value was not found (worst case)
#. The average cost for all possible locations,
   which works out to :math:`n/2`

In the best case, only a single element is visited.
Accordingly, the upper bound for this algorithm in the
best case is :math:`O(1)`.
Even when :math:`n` grows large,
the cost for the base case is constant.

In the worst case, every element is visited.
Accordingly, the upper bound for this algorithm in the
worst case is :math:`O(n)`.
No matter the value of :math:`n`,
for some constant :math:`c`, :math:`cn` is bigger than :math:`n`.

In the average case, about :math:`\frac{n}{2}` elements are visited.
The upper bound for this algorithm in the
average case is also :math:`O(n)`.
As :math:`n` grows large, the denominator becomes insignificant.
No matter the value of :math:`n`,
for some constant :math:`c`, :math:`cn` is bigger than :math:`n/2`.

Therefore, question we should always consider is:
*what is the upper bound of our algorithm in the best / average / worst case*?
And the answer should be (sequential search):

- :math:`O(1)` in the **best case**
- :math:`O(n)` in the **worst case**
- :math:`O(n)` in the **average case**


.. admonition:: More to Explore

   - TBD

.. topic:: Acknowledgements

   This section is adapted from 
   Problem Solving with Algorithms and Data Structures using C++,
   by Brad Miller and David Ranum, Luther College, and Jan Pearce, Berea College
   released under the 
   `CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__.

