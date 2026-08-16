..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation, with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   single: hash functions
   pair: hash tables; hash functions

Hash functions
==============
Unless we have special knowledge about the keys, the best we can do to
minimize collisions is choose a hash function that distributes likely keys
uniformly. In other words, if keys are selected at random, each bucket should
be about as likely to receive the next key as any other bucket.

This is sometimes harder to achieve in practice than we might expect.

A good hash function:

- Is fast and easy to compute.
- Distributes likely keys uniformly across the available hash values.
- Returns the same hash value whenever two keys compare equal.

The hash function returns a hash value, normally a ``std::size_t``. The hash
table maps that value to a bucket using its current bucket count. A hash
function therefore does not need to know the table size or return a value in
the range ``0`` through ``bucket_count - 1``.

.. note::

   Do not get hung up on trying to find hash functions that "mean something".
   Most hash functions do not compute anything useful or natural. They are
   chosen to be fast and to distribute the expected keys well.

Integer hashes
--------------
If an integer is already a suitable non-negative bucket index, no additional
mixing is needed. In a real hash table, however, the table still converts the
hash value into an index after the hash function returns it:

.. tb-code:: cpp
   :name: integer_hash_ac

   #include <cstddef>
   #include <iostream>

   std::size_t integer_hash(int value) noexcept {
     return static_cast<std::size_t>(value);
   }

   std::size_t bucket_index(int value, std::size_t bucket_count) noexcept {
     return integer_hash(value) % bucket_count;
   }

   int main() {
     std::cout << bucket_index(42, 10) << '\n';
   }

So integer keys are easy, but you cannot always take their values for granted.
A company once assigned an integer ID number to every employee. When the
computerized payroll system was created, the IDs were assigned like this:

- Start with a list of all current employees, in alphabetical order by name.
- Assign the first person the ID ``00005``, the next person ``00010``, then
  ``00015``, and so on.

This left gaps in the ID sequence that could be used later for new employees.
When a new person was hired, someone compared the new person's name with the
alphabetical list and assigned a number in the appropriate gap.

Because of this scheme, most generated IDs were divisible by 5. Suppose a
hash table with ``bucket_count == 100`` reduces these IDs with ``% 100``:

.. code-block:: cpp
   :caption: Pseudocode

   hash_value <- integer_hash(id)
   bucket_index <- hash_value % 100

There are 20 multiples of 5 in the range from 0 through 99. Thus, if the IDs
are multiples of 5, they use only 20 percent of the buckets rather than being
distributed uniformly.

Changing the bucket count to ``101`` changes the remainders:

.. list-table:: Example remainders with 101 buckets
   :header-rows: 1

   * - Keys
     - Bucket indices
   * - ``00005, 00010, ..., 00100``
     - ``5, 10, ..., 100``
   * - ``00105, 00110, ..., 00200``
     - ``4, 9, ..., 99``
   * - ``00205, 00210, ..., 00300``
     - ``3, 8, ..., 98``
   * - ``00305, 00310, ..., 00400``
     - ``2, 7, ..., 97``

The lesson is that the distribution of the original key values matters. A
prime bucket count can help a simple modulo-based scheme avoid patterns such
as this one, but it is not a guarantee of uniform distribution. Real hash
tables choose their bucket counts and hash policies together; a good hash
function still needs to distribute the expected keys well.

String hashes
-------------
String hash functions often combine information from every character. A
simple sum is fast, but it loses character position. Words that differ only by
transposing two characters produce the same result:

.. tb-code:: cpp
   :name: string_sum_hash_ac

   #include <cstddef>
   #include <iostream>
   #include <string>

   std::size_t sum_hash(const std::string& word) noexcept {
     std::size_t value = 0;
     for (unsigned char character : word) {
       value += character;
     }
     return value;
   }

   int main() {
     std::cout << std::boolalpha;
     std::cout << (sum_hash("stop") == sum_hash("pots"));
   }

An improved approach accounts for the position of each character. This
polynomial-style hash is still only an example; its quality depends on the
expected input distribution and the way the table reduces the result:

.. tb-code:: cpp
   :name: string_polynomial_hash_ac

   #include <cstddef>
   #include <iostream>
   #include <string>

   std::size_t polynomial_hash(const std::string& word) noexcept {
     constexpr std::size_t factor = 31;
     std::size_t value = 0;
     for (unsigned char character : word) {
       value = value * factor + character;
     }
     return value;
   }

   int main() {
     std::cout << std::boolalpha;
     std::cout << (polynomial_hash("stop") == polynomial_hash("pots"));
   }

The unsigned arithmetic can overflow, and that is well-defined modulo
``std::numeric_limits<std::size_t>::max() + 1``. Overflow is not itself a
problem for a hash function; the important question is whether the resulting
values are distributed well for the keys being used.

For built-in and standard-library types, manually writing a hash function is
usually unnecessary. The standard library provides the class template
:cpp:`std::hash <utility/hash>` and specializations for its standard types.

Hashing user-defined types
--------------------------
If you use a user-defined type as a key, the unordered container needs both a
hash function and an equality predicate. Equivalent keys must compare equal
and must produce the same hash value. There are two common ways to provide the
hash function:

1. Define a full specialization of ``std::hash`` for the user-defined type.
2. Define a separate hash functor and pass it to the unordered container.

The first approach is shown below. This is a complete example: ``point``
defines equality, the specialization combines both fields, and the unordered
set uses the resulting hash function.

.. tb-code:: cpp
   :name: point_hash_ac

   #include <cstddef>
   #include <functional>
   #include <iostream>
   #include <unordered_set>

   struct point {
     int x;
     int y;
   };

   bool operator==(const point& left, const point& right) noexcept {
     return left.x == right.x && left.y == right.y;
   }

   namespace std {
     template <>
     struct hash<point> {
       std::size_t operator()(const point& value) const noexcept {
         const auto x_hash = std::hash<int>{}(value.x);
         const auto y_hash = std::hash<int>{}(value.y);
         return x_hash * 73u + y_hash * 557u;
       }
     };
   }

   int main() {
     std::unordered_set<point> points;
     points.insert({1, 2});
     points.insert({2, 1});
     points.insert({1, 2});
     std::cout << points.size() << '\n';
   }

The ``template <>`` syntax marks a full specialization of the existing
``std::hash`` class template. It is valid to add this specialization to
``namespace std`` because ``point`` is a user-defined type. The specialization
must be declared before code instantiates ``std::hash<point>``.

The multipliers in this example are only a simple field-combination heuristic;
prime numbers do not guarantee that collisions are minimized. For a different
design, define a hash functor outside ``namespace std`` and pass it as the
third template argument to ``std::unordered_set`` or the fourth template
argument to ``std::unordered_map``.

-----

.. admonition:: More to Explore

 - :cpp:`std::hash <utility/hash>`
 - :cpp:`Hash requirements <unord.req>`
 - :cpp:`std::unordered_set <container/unordered_set>`
 - :cpp:`std::unordered_map <container/unordered_map>`
