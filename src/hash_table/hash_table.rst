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

:doc:`Previously <../trees/map>`, we described a :term:`map` as a data
structure that maps :term:`keys <key>` to values. An ordered map takes
:math:`O(\log N)` time for lookup, while a successful linear search examines
:math:`N / 2` elements on average.

Hashing provides a different tradeoff: lookup, insertion, and erasure can take
average :math:`O(1)` time, but a poor hash distribution can make an operation
take :math:`O(N)` time.
We need to:

- Store data in some kind of *indexable data structure*, such as a ``vector``.
- Compute a hash value from the key.
- Reduce that hash value to a valid bucket index.

This is the basic idea behind the unordered containers.

The unordered containers all depend on :term:`hashing` to find elements.
:term:`Hashing <hashing>` is a search method that uses a
:term:`hash function` to convert a *key* into a hash value. The hash table
then maps that hash value to a bucket.


Hash tables trade space for speed, often achieving average :math:`O(1)` lookup,
insertion, and erasure times when the hash distribution is good.

Often the :term:`backing storage` for a hash table is an array.
Each indexed location within the array is called a :term:`bucket`.

Generally we want a function that distributes keys evenly across its possible
hash values. The table then reduces the hash value to the current number of
buckets. So lookup is a two-step process:

.. code-block:: bash
   :caption: Pseudocode

   hash_value <- hash_function(key)
   bucket_index <- hash_value % bucket_count


A simple hash function for non-negative integers could take the value
``% 10``. The results are shown below:

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

The data stored in a hash table does not need to be numeric. A hash function
can accept a key of any type and return a ``std::size_t`` hash value. The hash
table, rather than the hash function, is responsible for converting that value
into a current bucket index.

Suppose, for example, that we were writing an application to work with 
calendar dates and wanted to quickly be able to translate the 
names of days of the work week (excluding the weekend) into numbers 
indicating how far into the week the day is:

.. list-table:: Weekday keys and values
   :header-rows: 1

   * - Key
     - Value
   * - Monday
     - 1
   * - Tuesday
     - 2
   * - Wednesday
     - 3
   * - Thursday
     - 4
   * - Friday
     - 5

For these five keys, the second character is unique. We can use that
observation for a small perfect hash function. The largest index is
``'u' - 'a' == 20``, so a 21-element zero-based table is sufficient.

The following example builds the table and performs a lookup:

.. tb-code:: cpp
   :name: weekday_perfect_hash_ac

   #include <array>
   #include <cstddef>
   #include <iostream>
   #include <string_view>

   std::size_t day_index(std::string_view day_name) {
     return static_cast<std::size_t>(day_name[1] - 'a');
   }

   int day_of_week(const std::array<int, 21>& table,
                  std::string_view day_name) {
     return table[day_index(day_name)];
   }

   int main() {
     constexpr std::array<std::string_view, 5> days{
       "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"
     };
     std::array<int, 21> table{};

     for (std::size_t i = 0; i < days.size(); ++i) {
       table[day_index(days[i])] = static_cast<int>(i + 1);
     }

     std::cout << day_of_week(table, "Thursday") << '\n';
   }

When we are done we have created a *perfect hash table* for this fixed set of
weekday keys.
A perfect hash table:

1. Computes hash values quickly.
2. Produces a unique bucket index for each known key.
3. Allows each known key to be looked up directly in the table.

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

Two keys :term:`collide <collision>` if they map to the same bucket index.
Different hash values can collide after the table reduces them with the
modulus operation. A hash table still needs an equality comparison to confirm
that a key in the bucket is the key being searched for.

For example, if we were to expand our days of the week code to include the weekend, 
then Sunday and Tuesday would collide under our current hash function because
both have the same second letter.
We could compensate with a more complicated hash function,
perhaps one involving a pair of letters, 
but this could also increase the number of unused/wasted slots in the table.

Collisions are frequently unavoidable simply because we do not know in advance
what all of the keys will be.
The following pages examine specific strategies for hashing and resolving
collisions, including separate chaining and open and closed hashing.

Consequently, we say that a good hash function will:

1. Compute hash values quickly.
2. Distribute likely keys evenly across the available hash values.
3. Return the same hash value whenever two keys compare equal.

The hash function does not need to return a value in the range of the table.
That requirement is enforced inside the hash table by reducing the returned
hash value modulo the bucket count.

The standard library supplies :container:`std::unordered_map <unordered_map>`
and :container:`std::unordered_set <unordered_set>`. These containers combine
a hash function with an equality predicate and manage buckets, rehashing, and
load factor for us. The following pages study the collision strategies that
an implementation can use internally.

-----

.. admonition:: More to Explore

 - :cpp:`std::hash <utility/hash>`
 - :container:`std::unordered_map <unordered_map>`
 - :container:`std::unordered_set <unordered_set>`
