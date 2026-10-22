..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: to_string

Example: Converting an Integer to a String
==========================================

Suppose you want to convert an integer to a string in some base between
binary and hexadecimal. For example, convert the integer 10 to its
string representation in decimal as ``"10"``, or to its string
representation in binary as ``"1010"``. While there are many algorithms
to solve this problem, the recursive formulation of the problem is
elegant.

Let's look at a concrete example using base 10 and the number 769.
Suppose we have a sequence of characters corresponding to the first 10
digits, like ``digits = "0123456789"``. It is easy to convert a
number less than 10 to its string equivalent by looking it up in the
sequence. For example, if the number is 9, then the string is
``digits[9]`` or ``"9"``. If we can arrange to break up the number
769 into three single-digit numbers, 7, 6, and 9, then converting it to
a string is simple. A number less than 10 sounds like a good base case.

Knowing what our base is suggests that the overall algorithm will
involve three components:

#. Reduce the original number to a series of single-digit numbers.

#. Convert the single digit-number to a string using a lookup.

#. Concatenate the single-digit strings together to form the final
   result.

The next step is to figure out how to change state and make progress
toward the base case. Since we are working with an integer, let's
consider what mathematical operations might reduce a number. The most
likely candidates are division and subtraction. While subtraction might
work, it is unclear what we should subtract from what. Integer division
with remainders gives us a clear direction. Let's look at what happens
if we divide a number by the base we are trying to convert to.

Using integer division to divide 769 by 10, we get 76 with a remainder
of 9. This gives us two good results. First, the remainder is a number
less than our base that can be converted to a string immediately by
lookup. Second, we get a number that is smaller than our original and
moves us toward the base case of having a single number less than our
base. Now our job is to convert 76 to its string representation. Again
we will use integer division plus remainder to get results of 7 and 6
respectively. Finally, we have reduced the problem to converting 7,
which we can do easily since it satisfies the base case condition of
:math:`n < base`, where :math:`base = 10`.

The following deck shows the calls and their return values. Indentation
shows the depth of each call. A waiting call keeps its own ``n`` and
``base`` while the deeper call computes the string prefix. Its remainder
identifies the character to append after that deeper call returns.

.. tb-deck::
   :name: to-string-decimal-trace
   :caption: Convert 769 to base 10: recursive calls and returns

   .. tb-card::
      :caption: Call with 769; wait to append '9'.

      Since 769 is not less than 10, use the recursive case.
      Integer division gives ``769 / 10 == 76``, so call
      ``to_string(76, 10)``. The remainder, ``769 % 10 == 9``,
      identifies the character this call will append after the prefix
      returns. No concatenation has happened yet.

      .. code-block:: text

         to_string(769, 10)  waiting to append '9'
           to_string(76, 10)   active

   .. tb-card::
      :caption: Call with 76; wait to append '6'.

      The call for 76 also uses the recursive case.
      Since ``76 / 10 == 7``, call ``to_string(7, 10)``.
      The remainder, ``76 % 10 == 6``, identifies its pending character.
      Both outer calls are now waiting for a string prefix.

      .. code-block:: text

         to_string(769, 10)  waiting to append '9'
           to_string(76, 10)   waiting to append '6'
             to_string(7, 10)    active

   .. tb-card::
      :caption: Reach the base case; return "7".

      Since ``7 < 10``, this call makes no further recursive call.
      Look up ``digits[7]`` and return the one-character string ``"7"``
      to the waiting call for 76. The outer calls have not returned yet.

      .. code-block:: text

         to_string(769, 10)  waiting to append '9'
           to_string(76, 10)   waiting to append '6'
             to_string(7, 10)    returns "7"

   .. tb-card::
      :caption: Resume the call for 76; return "76".

      The call for 76 receives the prefix ``"7"``. Append the character
      ``'6'`` to produce ``"76"``, then return that string to the call
      for 769. The completed call for 7 is no longer in the trace.

      .. code-block:: text

         to_string(769, 10)  waiting to append '9'
           to_string(76, 10)   receives "7", appends '6', returns "76"

   .. tb-card::
      :caption: Resume the call for 769; return "769".

      The original call receives the prefix ``"76"``. Append ``'9'``
      and return ``"769"``. Every call has finished, and the characters
      are in the correct order because each prefix returned before its
      pending character was appended.

      .. code-block:: text

         to_string(769, 10)  receives "76", appends '9', returns "769"

.. tb-group::
   :name: stringify

   .. tb-tab:: to_string

      .. literalinclude:: to_string.txt
         :language: cpp
         :start-after: #include <string>
         :end-before: int main
         :dedent: 3
         :linenos:
         :emphasize-lines: 3,6

      Notice that in line 3 we check for the base case where ``n``
      is less than the base we are converting to.

      When we detect the base case, that call makes no further recursive
      call and returns a one-character string built from ``digits``.

      The final return on line 6 satisfies both the second and third 
      properties of recursion - 
      by making the recursive call and by reducing the
      problem size using division.

      .. note::

         The standard library includes a set of functions called
         :string:`std::to_string<to_string>` to convert a 
         variety of numeric types into a `std::string`,
         but it does not handle arbitrary change of base.

   .. tb-tab:: Run It

      .. include:: to_string.txt


Let's trace the algorithm again; this time we will convert the number 10
to its base 2 string representation (``"1010"``).


.. tb-deck::
   :name: to-string-binary-trace
   :caption: Convert 10 to base 2: recursive calls and returns

   .. tb-card::
      :caption: Call with 10; wait to append '0'.

      Since ``10 >= 2``, use the recursive case. Integer division
      gives ``10 / 2 == 5``, so call ``to_string(5, 2)``.
      The remainder, ``10 % 2 == 0``, identifies the character to append
      after that call returns.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   active

   .. tb-card::
      :caption: Call with 5; wait to append '1'.

      Since ``5 / 2 == 2``, call ``to_string(2, 2)``.
      The remainder, ``5 % 2 == 1``, identifies this call's pending
      character. The call for 10 is still waiting.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   waiting to append '1'
             to_string(2, 2)   active

   .. tb-card::
      :caption: Call with 2; wait to append '0'.

      Since ``2 == base``, this is still the recursive case.
      Integer division gives ``2 / 2 == 1``, so call
      ``to_string(1, 2)``. The remainder, ``2 % 2 == 0``, identifies
      another pending character. Three calls are now waiting.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   waiting to append '1'
             to_string(2, 2)   waiting to append '0'
               to_string(1, 2)   active

   .. tb-card::
      :caption: Reach the base case; return "1".

      Since ``1 < 2``, look up ``digits[1]`` and return ``"1"``
      to the waiting call for 2. The base case supplies the leftmost
      character of the binary result.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   waiting to append '1'
             to_string(2, 2)   waiting to append '0'
               to_string(1, 2)   returns "1"

   .. tb-card::
      :caption: Resume the call for 2; return "10".

      The call for 2 receives ``"1"``. Append ``'0'`` to produce
      ``"10"``, the binary representation of 2, and return it to the
      waiting call for 5.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   waiting to append '1'
             to_string(2, 2)   receives "1", appends '0', returns "10"

   .. tb-card::
      :caption: Resume the call for 5; return "101".

      The call for 5 receives ``"10"``. Append ``'1'`` to produce
      ``"101"``, then return that prefix to the original call for 10.

      .. code-block:: text

         to_string(10, 2)  waiting to append '0'
           to_string(5, 2)   receives "10", appends '1', returns "101"

   .. tb-card::
      :caption: Resume the call for 10; return "1010".

      The original call receives ``"101"``. Append the final ``'0'``
      and return ``"1010"``. All four characters are now in order,
      and every call has finished.

      .. code-block:: text

         to_string(10, 2)  receives "101", appends '0', returns "1010"

The pending remainder characters belong at the right ends of their
calls' results. Each call first obtains the string for ``n / base``,
then appends the character for ``n % base``. As the calls return, the
binary result grows from ``"1"`` to ``"10"``, then ``"101"``, and
finally ``"1010"``. Appending the characters as the calls return puts
the most-significant digit first. Appending them while descending into
the recursive calls would produce the digits in reverse order.


-----

.. admonition:: More to Explore

   - `Problem Solving with Algorithms and Data Structures: Recursion
     <https://runestone.academy/ns/books/published/pythonds/Recursion/toctree.html>`__
   - :string:`std::to_string<to_string>` from `cppreference.com <https://en.cppreference.com/>`__


Content on this page is adapted from 
*Problem Solving with Algorithms and Data Structures using C++*, section 4.5.
Copyright (C)  Brad Miller, David Ranum.
under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/.

