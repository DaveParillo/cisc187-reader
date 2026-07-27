..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation, with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: analysis; separate chaining

Analysis of separate chaining
=============================
In a separate-chaining hash table, each bucket refers to a collection of keys.
Let:

- :math:`N` be the number of elements stored in the table.
- :math:`M` be the number of buckets.

We define :math:`\lambda`, the :term:`load factor`, as:

.. math::

   \lambda = \frac{N}{M}

Unlike an open-addressing table, a separate-chaining table can have more
elements than buckets, so :math:`\lambda` can be greater than ``1``. If a
table has one bucket for every stored element, then :math:`\lambda = 1` on
average. A well-behaved hash function distributes the elements across the
buckets, but the individual chain lengths will still vary.

The cost of a lookup has two parts:

1. Compute the hash value and reduce it to a bucket index.
2. Search the selected bucket using the key-equality predicate.

For fixed-size keys, the first part is usually treated as constant time. For
variable-size keys such as strings, hashing can also depend on the key length.
The analysis below focuses on the bucket-search portion.

An unsuccessful search examines the selected bucket and compares the search
key with each element in that bucket. Under a uniform-distribution assumption,
the expected number of key comparisons is the average chain length:
:math:`\lambda`.

A successful search examines the matching element and, on average, half of
the other elements in its bucket. The expected number of comparisons is
approximately :math:`1 + \frac{\lambda}{2}`.

For a finite table with uniform random placement, the more precise expression
is :math:`1 + (N - 1)/(2M)`. The simpler expression is easier to use and has
the same behavior as the table grows.

This shows why the number of buckets matters through the load factor. If the
table has far more buckets than elements, most chains have zero or one item.
If the number of elements grows while the bucket count stays fixed, the
average chain grows as :math:`\lambda = N/M`.

The graph shows the approximate successful-search cost as the load factor
increases. It models the number of key comparisons after the bucket has been
selected; it does not include the cost of computing a variable-length key's
hash value.

.. plot::

   import numpy as np
   import matplotlib.pyplot as plt

   load_factor = np.linspace(0, 10, 100)
   successful_search = 1 + (load_factor / 2)
   plt.plot(load_factor, successful_search)

   plt.ylim(0, 10)
   plt.xlim(0, 10)

   plt.title('Successful search cost vs. load factor')
   plt.xlabel(r'Load factor ($\lambda$)')
   plt.ylabel('Average key comparisons')
   plt.xticks(np.arange(0, 10.1, step=1))
   plt.yticks(np.arange(0, 10.1, step=1))

   plt.show()

Separate chaining degrades gradually as the load factor grows. There is no
single load factor at which resizing becomes mathematically required: a chain
can continue to grow as long as the program has memory. A smaller load factor
usually improves lookup time at the cost of more bucket storage.

The best threshold depends on the hash function, the bucket container, the
hardware, and the workload. Values around ``1`` to ``3`` can be useful
illustrative experiments for list-based buckets, but they are not universal
rules. A production implementation should measure its workload or use a
container policy rather than relying on this range.

When the load factor exceeds the chosen threshold, the table can rehash:

1. Allocate a new bucket array, usually with a larger bucket count.
2. Recompute each element's bucket index using the new bucket count.
3. Insert each element into its new bucket.

Changing the bucket count changes every bucket index, so rehashing must visit
all :math:`N` elements. A prime bucket count can help particular modulo-based
hash schemes, but it does not guarantee a uniform distribution. The bucket
count and hash policy should be chosen together.

The standard unordered containers expose related policy operations, including
:cpp:`max_load_factor <container/unordered_map/max_load_factor>`,
:cpp:`reserve <container/unordered_map/reserve>`, and
:cpp:`rehash <container/unordered_map/rehash>`. Their implementations choose
the actual bucket policy and manage the rehash operation for the programmer.

.. note::

   Assume that :math:`N` keys are placed independently and uniformly into
   :math:`N` buckets. This is the classic **balls-and-bins problem**. The
   expected length of the longest chain is:

   .. math::

      \Theta\left(\frac{\log N}{\log \log N}\right)

   This is an expected maximum under the stated random-placement assumptions;
   it does not mean that every lookup takes logarithmic time. A particular
   hash function can perform much worse if its keys are not distributed well.

Suppose we use a tree rather than a list for each bucket. If the selected
bucket contains :math:`L` elements, a balanced tree can reduce its search cost
to :math:`O(\log L)`. This requires the key type, or a supplied comparator, to
provide a strict weak ordering in addition to the equality predicate used by
the hash table. It does not make the hash table's worst-case lookup constant:
all :math:`N` keys could still map to one bucket, producing a cost of
:math:`O(\log N)` for a balanced tree bucket.

With list-based buckets and a uniform hash function, the expected lookup cost
is approximately :math:`O(1 + \lambda)`, in addition to hash computation.
When :math:`M` is much larger than :math:`N`, most buckets have zero or one
element and the expected cost is close to constant. When :math:`N` is much
larger than :math:`M`, the average chain length is large and the expected cost
approaches linear behavior in the number of stored elements when ``M`` is
fixed.

The bottom line is that hash tables trade bucket storage for shorter searches.
Good hash distribution and a suitable load-factor policy are both necessary
to make that trade worthwhile.

-----

.. admonition:: More to Explore

   - :doc:`Separate chaining implementation <open_hashing>`
   - :doc:`Open addressing (closed hashing) <closed_hashing>`
   - :cpp:`max_load_factor <container/unordered_map/max_load_factor>`
   - :cpp:`reserve <container/unordered_map/reserve>`
   - :cpp:`rehash <container/unordered_map/rehash>`
   - :wiki:`Balls into bins problem<Balls_into_bins_problem>` on Wikipedia.
