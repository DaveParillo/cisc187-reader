..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: recursion

What is Recursion?
==================
**Recursion** refers to defining something in terms of itself.
While recursion may appear in many forms (paintings and poems, 
for example), in computer science and mathematics,
objects or functions exhibit recursive behavior when they 
can be defined by two properties:

- A *base case*  -  a terminating scenario that 
  does **not** use recursion to produce an answer
- A *recursive step*  -  a set of rules that reduces all other cases 
  toward the base case

Some famous sequences in mathematics, 
such as the Fibonacci sequence are generated recursively.

Accumulating a sum
------------------
Consider a problem you are already familiar with:
computing the sum of a sequence of numbers.

- The function ``accumulate`` loops over each element
  in the vector ``values``.
- The variable ``sum`` holds the running total.
- When the loop completes, the total is returned.
- If the vector is empty, then 0 is returned.

.. tb-code::
   :name: recursion-sum

   #include <iostream>
   #include <vector>

   // iterative sum
   int accumulate(const std::vector<int>& values) {
     int sum = 0;
     for (const auto& x: values) {
       sum = sum + x;
     }
     return sum;
   }

   int main () {
     std::vector<int> values = {1,2,3,4,5,6,7,8,9,10};

     auto sum = accumulate(values);
     std::cout << "sum is: " << sum << '\n';

     return sum;
   }

The implementation details are not critical here.
We could have used a traditional ``for`` loop or a ``while`` loop
and computed the same value.
The point is that all these solutions are *iterative*.

It is possible to solve this problem without using a loop.
Actually, there is a loop of sorts, but it is the function itself that 
is used as the looping construct.
Let's pick apart accumulating the sum to see how.

Recall that addition is a *binary operation* - an operation with two operands:
a pair of numbers. We need to restate the accumulate
problem from adding a vector to adding pairs of numbers.

.. math::

    1 + 2 + 3 + 4

Can be rewritten as:

.. math::

     (1 + (2 + (3 + 4)))

Notice that the innermost set of
parentheses, :math:`(3 + 4)`, is a problem that we can solve without a
loop or any special constructs. In fact, we can use the following
sequence of simplifications to compute a final sum.

.. math::

    total = \  (1 + (2 + (3 + 4))) \\
    total = \  (1 + (2 + 7)) \\
    total = \  (1 + 9) \\
    total = \  10

How can we take this idea and turn it into a C++ program? First,
let's restate the sum problem in terms of a C++ vector. We might say 
the sum of the vector ``values`` is the sum of the first element of the
vector (``values[0]``), 
and the sum of the numbers in the rest of the vector - the range 
``values.begin()+1`` to ``values.end()``.

Instead of a local variable to accumulate the sum,
the return value of the function stores the accumulated sum.

Each return value is the current first element of the vector
plus a *slice* of the vector composed of all the 
elements after the first element.

The base case occurs when the vector is empty - 
there is nothing left to add.
We return zero since no matter what is in the vector,
adding zero does not change the final result.

If the container is not empty, then it must contain at least
one element.
The recursive case is then the first element, plus everything
after the first element (which might be nothing).


.. tb-code::
   :name: recursion-sum-recursive

   #include <iostream>
   #include <vector>

   // recursive sum
   int accumulate(const std::vector<int>& values) {
     // base case
     if (values.empty()) return 0;

     // recursive case
     auto slice = std::vector<int>(values.begin()+1, values.end());
     return values[0] + accumulate(slice);
   }

   int main () {
     std::vector<int> values = {1,2,3,4,5,6,7,8,9,10};

     auto sum = accumulate(values);
     std::cout << "sum is: " << sum << '\n';

     return sum;
   }

.. admonition:: Try This!

   Run both the iterative and recursive versions and verify
   they both produce the same results.

The recursive calls to accumulate perform in code the same steps
outlined when we grouped the addition sequence using parentheses.

-----

.. admonition:: More to Explore

   - :wiki:`Recursion <Recursion_(computer_science)>` on Wikipedia 
   - `TED: The magic of Fibonacci numbers, Arthur Benjamin <https://www.youtube.com/watch?v=SjSHVDfXHQ4>`_

