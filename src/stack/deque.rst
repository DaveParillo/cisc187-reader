..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; deque

The deque class
===============
The :container:`deque` (double-ended queue) is an indexed sequence container that 
allows fast insertion and deletion at both its beginning and its end. 
In addition, 
insertion and deletion at either end of a ``deque`` never invalidates pointers 
or references to the rest of the elements.

It's primary role in the standard library is to function as
the default container underlying ``std::stack`` and ``std::queue``.

.. tb-group::
   :name: deque

   .. tb-tab:: std::deque

      .. literalinclude:: deque.txt
         :language: cpp
         :start-after: compileargs
         :dedent: 3
         :linenos:

   .. tb-tab:: Run It

      .. include:: deque.txt

An interesting problem that can be easily solved using the deque 
data structure is the classic palindrome problem. 
A **palindrome** is a string that reads the same forward and backward, 
for example, *radar*, *toot*, and *madam*. 
We would like to construct an algorithm to input a string of characters and 
check whether it is a palindrome.

One solution to this problem uses a deque to store the characters of the string.
First store each character in the string into a new deque.
Using the properties of the deque, we can process the characters from both ends
and compare them to each other.

Since we can remove both of them directly, 
we can compare them and continue only if they match. 
If we can keep matching first and the last items, 
we will eventually either run out of characters or 
be left with a deque of size 1 depending on whether the length of the 
original string was even or odd. In either case, 
the string must be a palindrome.


.. tb-group::
   :name: check_palindrome

   .. tb-tab:: Check Palindrome

      .. literalinclude:: palindrome.txt
         :language: cpp
         :start-after: #include <iostream>
         :end-before: int main
         :dedent: 3
         :linenos:

   .. tb-tab:: Run It

      .. include:: palindrome.txt

.. index:: std::equal

A moment of full disclosure:
even though it is possible to use a deque to determine if a string is a
palindrome or not, it's far from the simplest or most efficient
solution tot he the problem.
Simply checking the string characters directly is better:

.. tb-group::
   :name: is_palindrome

   .. tb-tab:: Is Palindrome

      .. literalinclude:: is_palindrome.txt
         :language: cpp
         :start-after: compileargs
         :end-before: int main
         :dedent: 3
         :linenos:

      The STL provides the :algorithm:`equal` template which allows
      comparing the values in a pair ranges.

      The first `begin` and `end` define a range of values to be compared.
      The second `begin` defines the start of the second range of values.
      The second `end` does not need to be specified, because the comparison
      stops once the first end is reached.

      Notice that in this example, the second begin is `rbegin`.
      This means the second iterator starts at the **reverse beginning**,
      which is the *end* of the string and each iteration moves one
      step closer to the begining.

   .. tb-tab:: Run It

      .. include:: is_palindrome.txt

While this solution does require more familiarity with the standard library,
it avoids copying the string into the container, 
removing elements from the container, and is generally simpler.


-----

.. admonition:: More to Explore

   - :cpp:`STL containers library <container>`
   - STL :container:`deque` class

