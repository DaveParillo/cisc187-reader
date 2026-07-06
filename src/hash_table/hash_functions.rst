..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: hashing concepts; hash functions

Hash functions
==============
Unless we have special knowledge about the keys, 
the best we can say about "minimizing the number of collisions" 
is that we hope that our hashing function will distribute the keys uniformly, 
that is, if keys are selected at random, then the probability of the next 
key going into any particular position in the hash table should be 
the same as for any other position.

This is sometimes harder to achieve in practice than we might expect.

So to recap: a good hash function:

- Is fast and easy to compute
- Distributes keys uniformly across the table.

.. note::

   Don't get hung up on trying to find hash functions that "mean something".
   Most hash functions don't compute anything useful or "natural".
   They are simply functions chosen to satisfy our requirements 
   (fast and uniform over the range :math:`0 \to (table\_size-1)`.

Integer hashes
--------------
If your integers are already in the range :math:`0 \to (table\_size-1)`
then there is nothing to do:

.. code-block:: cpp

   int hash(int i) {return i;}

So integer keys are easy, but you can't always take them for granted. 
A company once assigned an integer ID number to every employee.
When the computerized system for the company payroll was created, 
the way the IDs were assigned when like this:

- Start with a list of all current employees, in alphabetical order by name.
- Assign the first person in the list the ID ``00005``,
  the next person ``00010``, then ``00015``, and so on.

This left "gaps" in the ID number sequence that could be used later for new employees.

When a new person was hired,
someone would compare the new person's name to the alphabetical list of 
employee names and would assign the new person a number lying somewhere 
in the gap between the people already in the list.

Because of this scheme,
more than 3/4 of the ID numbers in the company were evenly divisible by 5.

Let's suppose some hash table with ``size == 100`` simply use the hash
function described previously and use ``%`` to constrain them to the table:

.. code-block:: cpp

   int hash(int i) {return i % 100;}

There are 20 numbers divisible by 5 in the range from 0 to 99.
So 3/4 of the ID numbers would hash into only 1/5 of the table positions.
These numbers are not being distributed uniformly.

There is an easy fix:
change the hash table size to ``101``.
Making the table just 1 element larger improves the distribution considerably:

======================== ===============
keys                     hash to
00005, 00010, ..., 00100 5, 10, ..., 100
00105, 00110, ..., 00200 4, 9, ..., 99
00205, 00210, ..., 00300 3, 8, ..., 98
00305, 00310, ..., 00400 2, 7, ..., 97
======================== ===============

The lesson here: the distribution of the original key values is important.

The difference between using 100 vs using 101 is no accident.
Choosing prime numbers for hash table sizes tends to 
increase the uniformity of key distributions.

String hashes
-------------
Hash functions for strings generally work by adding up some expression applied
to each character in the string
(remember that a char is just another integer type in C++).

We need to be a little careful to get an appropriate distribution.
Although a char could be any of 255 different values, 
most strings actually contain only the 96 "printable" characters starting at 
ASCII value 32 (blank).

Also we often want to make sure that similar strings, 
likely to occur together, don’t hash to the same location. 
So a simple hash function like this:

.. code-block:: cpp

   unsigned hash (const string& words)
   {
      unsigned value = 0;
      for (const auto& ch: words) {
        value += ch;
      }
      return value;
   }

doesn't work very well.
Words that differ only by transposition of characters have the same value.

An improved approach is to account for the position of each character
in the string.

.. code-block:: cpp

   unsigned hash (const string& words)
   {
      unsigned value = 1;
      constexpr unsigned factor = 31;  // or any suitable prime
      for (const auto& ch: words) {
        value = value*factor + ch;
      }
      return value;
   }

If ``value`` becomes large, eventually this expression may overflow,
but for unsigned types this is not a problem.
Again, we are looking for a uniform distribution of values we can 
generate for our hash table.

Manually writing our own hash functions for builtin
standard library types is not needed.
The STL provides the template :utility:`std::hash<hash>`
and a set of standard overrides for types in the standard library.

Hashing user defined types
--------------------------
If you define your own ``struct`` or ``class``, you need to write your own 
hash function.
Normally this will be a ``std::hash<>`` override.
Consider a ``struct point`` and a sample hash function:

.. code-block:: cpp

   struct point {
     int x;
     int y;
   }

   namespace std {
     template <>
     struct hash<point>
     {
       std::size_t operator()(const point& p) const
       {
         return   std::hash<int>()(7919) // or any suitable prime
                + std::hash<int>()(p.x) * 73
                + std::hash<int>()(p.y) * 557;
       }
     };
   }

The ``std::hash`` override must be a function template,
although in this case, no template parameter is needed.
The template declaration ``template <>`` is perfectly valid.

.. note::

   Notice a recurring theme: prime numbers as multipliers.
   Prime numbers as multipliers help minimize collisions when the hash values
   of different parts of an object have the same value
   or are simple multiples of one another.

-----

.. admonition:: More to Explore

 - `General purpose hash function algorithms <http://www.partow.net/programming/hashfunctions/>`_

