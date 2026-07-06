..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: associative containers; hashing concepts 

Hashing concepts
================

:doc:`Previously <../trees/map>`, 
we asserted that a :term:`map` refers to any data structure that 'maps' :term:`keys <key>` to values.
They have an advantage over sequential containers 
in that the cost of searches grows more slowly: 
:math:`log_2 {N}` for maps versus :math:`N \over 2` for the sequential containers.

Is there a way to access elements in a tree that does not become more costly
as the number of elements grows?
We need to:

- Store data in some kind of *indexable data structure*:
  something we can access using an index, such as a ``vector``.
- Compute a value that will result in the index where are data is stored.

This is exactly what the unordered containers do.

The unordered containers all depend on :term:`hashing` to find elements.
:term:`Hashing <hashing>` is a search method that uses a 
:term:`hash function` to convert a *value* into a *position* within a
:term:`hash table`. 


Hash tables trade off space for speed, sometimes achieving an average case of 
:math:`O(1)` for both search and insert times.

Often the :term:`backing storage` for a hash table is an array.
Each indexed location within the array is called a :term:`bucket`.

Generally we want a function that generates values that avoid this kind of clumping
and **then** take the modulus to insert the value into whatever hash table
size we happen to be working with.
So hashing is a two step process:

.. code-block:: cpp

   size_t hash  = function(value);
   size_t index = hash % array_size;


A simple hash function for integers could simply to take the
value ``% 10``. The results are shown below:

.. graphviz::
   :align: center
   :alt: Simple hash table

   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Simple hash table modulo 10"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{0\n60|1\n11|2\n312|3\n23|4\n14|5\n35|6\n26|7\n17|8\n268|9\n799}"
     ]

   }

The data stored in a hash table does not need to be a numeric value.
Any function capable of calculating an index position from the data in
a data type satisfies the requirements for a hash function.

Suppose, for example, that we were writing an application to work with 
calendar dates and wanted to quickly be able to translate the 
names of days of the work week (excluding the weekend) into numbers 
indicating how far into the week the day is:

========= =========
**Key**   **Value**
Monday    1
Tuesday   2
Wednesday 3
Thursday  4
Friday    5
========= =========

If we don't care about the unused space,
then we could implement our hash function like so:

.. code-block:: cpp

   unsigned hash(const std::string& dayName)
   {
       return unsigned(dayName[1] - 'a');
   }

because each of those seven strings has a distinct second character.

So we can set up the table:

.. code-block:: cpp

   std::array<string, 5> days = {"Monday", "Tuesday",
                                 "Wednesday", "Thursday", "Friday"};
   int table[96];
   for (int i = 0; i < 5; ++i) {
     table[hash(days[i])] = i+1;
   }

.. admonition:: Something to Consider

   Why is the days table size 96?

and then afterwards, we can look up those day names in 
:math:`O(1)` time:

.. code-block:: cpp

   int dayOfWeek (const string& dayName)
   {
     return table[hash(dayName)];
   }

When we are done we have created a *perfact hash table*.
A perfect hash table:

1. Computes values quickly
2. Returns values in the range of the hash table size
3. Returns a unique value for each key.

Perfect hash functions are usually only possible if we know all the keys in advance, 
which rules out their use in most practical circumstances.

There are some applications where perfect hash functions are possible.
For example, most programming languages have a number of reserved words such as
"if" or "while", but for any given language the set of reserved words is fixed.
Programmers who are writing a compiler for that language may use a 
perfect hash function over the language keywords to quickly recognize when
a word read from the source code file is a reserved word.

Generally we do not expect to have perfect hash functions.
This means that some keys will hash to the same table location.

Two keys :term:`collide <collision>` if they have the same hash function value.

For example, if we were to expand our days of the week code to include the weekend, 
then Sunday and Tuesday would collide under our current hash function because 
both have the same second letter. 
We could compensate with a more complicated hash function,
perhaps one involving a pair of letters, 
but this could also increase the number of unused/wasted slots in the table.

Collisions are frequently unavoidable simply because we do not know in advance
what all of the keys will be.

Consequently, we say that a good hash function will:

1. Computes values quickly
2. Minimizes the number of collisions

Note we also dropped the 'return values in the range of the hash table size',
because this requirement is typically enforced 
inside the hash table code by the simple technique of taking the
returned hash value modulo of the hash table size.

-----

.. admonition:: More to Explore

 - `General purpose hash function algorithms <http://www.partow.net/programming/hashfunctions/>`_

