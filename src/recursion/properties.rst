..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   single: base case
   single: recursive case
   pair: recursion; call stack unwinding

Properties of recursive functions
=================================
All recursive algorithms must implement 3 properties:

#. A recursive algorithm must have a **base case**.

#. A recursive algorithm must change its state and move toward the base
   case.

#. A recursive algorithm must call itself.

The base case is the condition
that allows the algorithm to stop the recursion and begin
the process of returning to the original calling function.
This process is sometimes called *unwinding the stack*.
A base case is typically a
problem that is small enough to solve directly. In the ``accumulate``
algorithm the base case is an empty vector.

The second property requires modifying something in the recursive
function that on subsequent calls moves the state of the program
closer to the base case. A change of state means that some
data that the algorithm is using is modified. Usually the data that
represents our problem gets smaller in some way. In the ``accumulate``
algorithm our primary data structure is a vector, so we must focus our
state-changing efforts on the vector. Since the base case is the empty vector,
a natural progression toward the base case is to shorten the vector.

Lastly, a recursive algorithm must call itself. This is the very
definition of recursion. Recursion is a confusing concept to many
beginning programmers. As a novice programmer, you have learned that
functions are good because you can take a large problem and break it up
into smaller problems. The smaller problems can be solved by writing a
function to solve each problem. When we talk about recursion it may seem
that we are talking ourselves in circles. We have a problem to solve
with a function, but that function solves the problem by calling itself!
But the logic is not circular at all; the logic of recursion is an
elegant expression of solving a problem by breaking it down into a
smaller and easier problems.

In the remainder of this chapter we will look at more examples of
recursion. In each case we will focus on designing a solution to a
problem by using the three properties of recursive functions.


**Self Check**

.. tb-group::
   :name: tab_self_check

   .. tb-tab:: Q1

      .. tb-choice::
         :name: question_recsimp_1

         How many recursive calls are made when computing the sum of the vector {2,4,6,8,10}?

         - [ ] 6

           Good choice: our accumulate example called once for each element, plus the empty vector.
         - [ ] 5

           The last call to accumulate is always an empty vector
         - [x] 4

           the first recursive call passes the vector {4,6,8,10}, the second {6,8,10} and so on until the vector is empty.
         - [ ] 3

           This would not be enough calls to cover all the numbers on the vector

   .. tb-tab:: Q2

      .. tb-choice::
         :name: question_recsimp_2

         Suppose you are going to write a recusive function to calculate the factorial of a number.  fact(n) returns n * n-1 * n-2 * ... Where the factorial of zero is defined to be 1.  What would be the most appropriate base case?



         - [ ] n == 0

           Although this would work there are better and slightly more efficient choices. since fact(1) and fact(0) are the same.
         - [ ] n == 1

           A good choice, but what happens if you call fact(0)?
         - [ ] n &gt;= 0

           This base case would be true for all numbers greater than zero so fact of any positive number would be 1.
         - [x] n &lt;= 1

           Good, this is the most efficient, and even keeps your program from crashing if you try to compute the factorial of a negative number.

-----

.. admonition:: More to Explore

   - `Problem Solving with Algorithms and Data Structures: Recursion
     <https://runestone.academy/ns/books/published/pythonds/Recursion/toctree.html>`__
     by Brad Miller and David Ranum. Especially useful for the 'three laws of
     recursion,' stack frames, and visual examples.
   - Wikipedia:

      - :wiki:`Recursion in computer science <Recursion_%28computer_science%29>`
      - :wiki:`Recursive definition <Recursive_definition>`

