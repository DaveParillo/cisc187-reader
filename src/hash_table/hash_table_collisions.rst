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
Since perfect hash functions are only practical when the complete set of keys
is known in advance, a general-purpose hash table must be prepared for
collisions.

Two different keys collide when they map to the same bucket index. The keys
may have the same hash value, or they may have different hash values that are
reduced to the same bucket by the table's bucket-count calculation. After a
bucket has been selected, the table still uses an equality predicate to decide
whether a stored key is the key being searched for.

For example, in our simple hash table example,
``93 % 10 == 3``, so inserting ``93`` selects bucket ``3``. That bucket
already contains ``23``. How can the table store both values?

.. graphviz::
   :align: center
   :alt: A hash table with a collision at bucket 3

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

     value [shape=box, label="93\n93 % 10 = 3"]
     value -> arr:p1 [label="collision"]
   }

There are two general approaches. The terminology varies across textbooks,
so both names are shown here:

.. list-table:: Collision-resolution strategies
   :header-rows: 1

   * - Common name
     - Storage and collision handling
   * - :doc:`Separate chaining (open hashing) <open_hashing>`
     - Each bucket refers to a collection that can hold all keys mapped to
       that bucket. A linked list is a traditional choice, but other
       containers are possible.
   * - :doc:`Open addressing (closed hashing) <closed_hashing>`
     - Entries are stored directly in the table. When the home bucket is
       occupied, the table probes other slots according to a probe sequence.

Separate chaining can grow a bucket's collection as needed, while open
addressing must find an available slot in the table and therefore has a
capacity limit. Both strategies select candidate locations using the hash
value and then compare keys for equality.

Historically, one of the most common approaches to dealing with collisions
has been to use fixed-capacity buckets, for example an array that can hold up
to ``k`` elements at each location. This is a limited form of separate
chaining, not a complete solution by itself: if more than ``k`` keys map to
the same bucket, the table must resize the bucket or fall back to another
technique.

The following pages examine these strategies in detail.

-----

.. admonition:: More to Explore

 - :doc:`Separate chaining (open hashing) <open_hashing>`
 - :doc:`Open addressing (closed hashing) <closed_hashing>`
 - :cpp:`std::unordered_map <container/unordered_map>`
 - :cpp:`std::unordered_set <container/unordered_set>`
