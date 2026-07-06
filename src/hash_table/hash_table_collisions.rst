..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: hash table; collisions

Resolving collisions
====================
Since we know that perfect hash functions are not generally
possible except in limited cases,
we must assume that sometimes a hash function will generate
the same value for two different objects.

For example, in our simple hash table example,
if we need to add another value that *collides*
with an existing entry,
then how can we store it?

.. graphviz::
   :align: center
   :alt: Simple hash table

   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Where can we store 93?"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{0\n60|1\n11|2\n312|<p1>3\n23|4\n14|5\n35|6\n26|7\n17|8\n268|9\n799}"
     ]

     value [shape=box, label=93]
   }

There are two general approaches:

- :term:`Open hashing <open hashing>`: 
  The hash table stores data structures that each holds multiple items.
- :term:`Closed hashing <closed hashing>`
  The keys are stored directly in the table.
  This requires finding an open bucket in the table for each value.

Historically, one of the most common approaches to dealing with collisions
has been to use fixed size :term:`buckets<bucket>`, for example
an array that can hold up to k (some small constant) elements.
The problem with this approach is 
if we get more than :math:`k` collisions at the same location, 
then we still need to fall back to some other technique.

-----

.. admonition:: More to Explore

 - `General purpose hash function algorithms <http://www.partow.net/programming/hashfunctions/>`_

