..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: algorithms; refactoring


Refactoring to Algorithms
=========================
The primary objective of refactoring is to improve code.
Those improvements might take many forms.
In this section we are going to focus on refactoring a pair
of functions that at first glance do not appear
to be doing the same thing.
However, we will see the similarities and how refactoring is accomplished,
step-by-step.

Given two functions, each sums the values provided.

The first function adds all of the integers in a raw array:

.. code-block:: cpp

    int sum(const int array[], std::size_t n) {
      int total = 0;
      for (int i = 0; i < n; ++i ) {
        total += array[i];
      }
      return total;
    }

The second adds all of the elements in a simple,
home-grown linked list.

.. code-block:: cpp

    // create a simple node in a linked list
    struct node {
      int value = 0;
      node* next = nullptr;
    };

    int sum(node* first) {
      int s = 0;
      while (first) {        // first not false or zero
        s += first->value;
        first = first->next;
      }
      return s;
    }

How can we generalize and combine these two functions into one?
We can rewrite both functions in a form of pseudo-code.

.. code-block:: cpp

   // we need a generic type 'T'
   T sum(/* data */ )                   // somehow parameterize this
   {
     T s = 0;
     while (/* not at end */ ) {        // loop through all elements
       s = s + /* get value */;         // compute sum
       /* get next data element */;
     }
     return s;
   }

We need several generic operations on **data**:

- Determine if we are not at end of data
- Get value
- Get next element

.. tb-group::
   :name: sum

   .. tb-tab:: Example

      The standard library algorithm style supports both data structures.

      Like find, we define a pair of iterators. ``first`` and ``last``.
      The iterator type should satisfy the C++20
      :cpp:`std::input_iterator <iterator/input_iterator>` concept.

      A separate template parameter for the initial sum finishes the signature.

      The accumulator type must be movable and assignable from the result of
      the operation. The operation must be invocable with the accumulator and
      a dereferenced iterator.

      The function signature becomes:

      .. literalinclude:: refactor.txt
         :language: cpp
         :lines: 12-17
         :dedent: 3

      The main loop checks whether we should continue
      and accumulates the sum:

      .. literalinclude:: refactor.txt
         :language: cpp
         :lines: 18-20
         :dedent: 5

   .. tb-tab:: Run It

      And we can use this algorithm with either a raw array or a linked list.

      .. include:: refactor.txt

Removing a final assumption
---------------------------
Can we make ``sum`` even more generic?

Sum still has a hard-coded assumption that addition (the ``operator+``
function)
is the operation that we always want to perform.

Might we want to perform **any** binary operation on a sequence?
If yes, then we can add one more template parameter allowing callers
to pass in a callable object such as a function pointer, lambda, or function
object.

.. tb-group::
   :name: accumulate

   .. tb-tab:: Example

      The function signature becomes:

      .. literalinclude:: accumulate.txt
         :language: cpp
         :start-after: // using
         :end-before: while
         :dedent: 3

      The main loop replaces the explicit ``+`` with
      a call to a provided binary operator:

      .. literalinclude:: accumulate.txt
         :language: cpp
         :start-after: while
         :end-before: ++first
         :dedent: 5

      This *could* be addition, represented by ``std::plus<>``, but can now
      support any binary operation that satisfies the callable requirements.

      A default operation can be provided with an overload that calls
      ``my_accumulate`` with :functional:`plus`.

      .. literalinclude:: accumulate.txt
         :language: cpp
         :start-after: default operation
         :end-before: main
         :dedent: 3

   .. tb-tab:: Run It

      .. include:: accumulate.txt


Note that 
we did not pass ``+`` or ``*`` to a function.
The symbol ``+`` is not a type.

The template parameter ``BinaryOp`` names the type of the callable object, and
the parameter ``op`` is an object of that type. The object must satisfy the
C++20 :cpp:`std::invocable <concepts/invocable>` concept for the accumulator
and element types.

Lambda expressions, function objects, and function pointers are all acceptable
callables. The standard library provides a large collection of
:cpp:`function objects <functional>` such as :cpp:`std::plus <functional/plus>`
and :cpp:`std::multiplies <functional/multiplies>`.


-----

.. admonition:: More to Explore

   - :guidelines:`T.2 Use templates to express algorithms that apply to many argument types <rt-algo>`
   - :algorithm:`std::accumulate <numeric/accumulate>`
   - :cpp:`std::input_iterator <iterator/input_iterator>`
   - :cpp:`std::invocable <concepts/invocable>`
   - :cpp:`std::plus <functional/plus>`
