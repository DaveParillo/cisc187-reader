..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| replace:: --

.. index::
   pair: iterator; using

Using iterators
===============

An iterator is an object that identifies a position in a container.
It can be dereferenced like a pointer to access the element at that position.
When a range-based ``for`` loop is not the right tool, an explicit iterator
allows a program to control traversal more precisely.

Declaring and dereferencing an iterator
---------------------------------------
The iterator type is associated with the container and its element type.
For example, ``std::vector<int>::iterator`` and
``std::vector<std::string>::iterator`` are different types.

In modern C++, ``auto`` is usually the clearest way to declare an iterator:

.. tb-code:: cpp
   :name: using_iterator_declaration_ac

   #include <iostream>
   #include <vector>

   int main() {
     std::vector<int> nums = {1, 2, 3, 4, 5};
     auto it = nums.begin();

     std::cout << *it << '\n';
   }

The expression ``*it`` accesses the element. The iterator itself represents
a position; it is not the element value. The iterator must be dereferenceable,
so ``nums.end()`` cannot be dereferenced.

Traditional iterator loops
---------------------------
An explicit iterator can be used in a traditional ``for`` loop:

.. tb-code:: cpp
   :name: using_iterator_for_ac

   #include <iostream>
   #include <vector>

   int main() {
     const std::vector<int> nums = {1, 2, 3, 4, 5};
     std::cout << "nums contains:";

     for (auto it = nums.begin(); it != nums.end(); ++it) {
       std::cout << ' ' << *it;
     }
     std::cout << '\n';
   }

The same traversal can be written with a ``while`` loop. Braces are required
when the loop body contains both the output operation and the increment:

.. tb-code:: cpp
   :name: using_iterator_while_ac

   #include <iostream>
   #include <vector>

   int main() {
     const std::vector<int> nums = {1, 2, 3, 4, 5};
     std::cout << "nums contains:";

     auto it = nums.begin();
     while (it != nums.end()) {
       std::cout << ' ' << *it;
       ++it;
     }
     std::cout << '\n';
   }

When the loop body does not need to modify the container, a range-based
``for`` loop is usually shorter and clearer:

.. tb-code:: cpp
   :name: using_iterator_range_for_ac

   #include <iostream>
   #include <vector>

   int main() {
     const std::vector<int> nums = {1, 2, 3, 4, 5};
     std::cout << "nums contains:";

     for (const auto& num : nums) {
       std::cout << ' ' << num;
     }
     std::cout << '\n';
   }

The range declaration initializes a loop variable from each element.
With ``const auto&``, it binds a read-only reference and avoids copying the
element. Use ``auto&`` when the loop should modify elements, or ``auto`` when
an independent copy is useful. Unlike ``*it``, the range variable is already
the element value or reference; it is not an iterator and must not be
dereferenced.

Limits of range-based ``for``
------------------------------
Range-based ``for`` is designed to visit every element in order.
It is not the best fit when a loop needs a custom stopping condition or must
coordinate traversal through multiple containers. An explicit loop can stop
where the program needs:

.. tb-code:: cpp
   :name: using_iterator_partial_ac

   #include <iostream>

   int main() {
     for (int value = 32; value > 0; value /= 2) {
       std::cout << value << ' ';
     }
     std::cout << '\n';
   }

When two containers must be traversed together, keep one iterator for each
container and stop when either reaches its end:

.. tb-code:: cpp
   :name: using_iterator_multiple_ac

   #include <iostream>
   #include <list>
   #include <vector>

   int main() {
     const std::vector<int> left = {1, 2, 3, 4};
     const std::list<int> right = {10, 20, 30};

     auto left_it = left.begin();
     auto right_it = right.begin();
     while (left_it != left.end() && right_it != right.end()) {
       std::cout << *left_it + *right_it << ' ';
       ++left_it;
       ++right_it;
     }
     std::cout << '\n';
   }

C++20 also provides ranges and views for composing some partial traversals.
Explicit iterators remain useful when a loop needs stateful control that is
clearer as an imperative loop.

Container functions that require iterators
------------------------------------------
Container functions that use position information generally accept iterators
rather than an integral position or an index like ``operator[]``.

``insert``
   Inserts elements before the position identified by an iterator.

The following example inserts one value, repeated values, a range from another
container, and a raw array range. The iterator returned by ``insert`` points
to the first inserted element. Vector insertion can invalidate existing
iterators, so the example obtains a fresh iterator before each later operation.

.. tb-code:: cpp
   :name: using_iterator_insert_ac

   #include <iostream>
   #include <iterator>
   #include <vector>

   void print(const std::vector<int>& values) {
     for (const auto value : values) {
       std::cout << ' ' << value;
     }
     std::cout << '\n';
   }

   int main() {
     std::vector<int> nums(3, 100);
     print(nums);

     auto it = nums.insert(nums.begin(), 200);
     print(nums);

     it = nums.insert(nums.begin(), 2, 300);
     print(nums);

     std::vector<int> fib = {1, 1, 2, 3, 5, 8, 13, 21};
     it = nums.begin() + 2;
     nums.insert(it, fib.begin(), fib.end());
     print(nums);

     int values[] = {501, 502, 503};
     nums.insert(nums.begin(), std::begin(values), std::end(values));
     print(nums);
   }

``erase``
   Removes one element or a contiguous range of elements.

The following example erases the first element, erases a range, and then
removes every even value. ``vector::erase`` returns an iterator to the element
that follows the erased range. Erasing from a vector invalidates iterators and
references at or after the erase position, so the returned iterator must be
used for continued traversal.

.. tb-code:: cpp
   :name: using_iterator_erase_ac

   #include <iostream>
   #include <vector>

   void print(const std::vector<int>& values) {
     for (const auto value : values) {
       std::cout << ' ' << value;
     }
     std::cout << '\n';
   }

   int main() {
     std::vector<int> nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
     print(nums);

     nums.erase(nums.begin());
     print(nums);

     nums.erase(nums.begin() + 2, nums.begin() + 5);
     print(nums);

     nums = {2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4, 5, 9};
     for (auto it = nums.begin(); it != nums.end();) {
       if (*it % 2 == 0) {
         it = nums.erase(it);
       } else {
         ++it;
       }
     }
     print(nums);
   }

.. cpp:: 20

   ``std::erase_if(nums, predicate)`` is a concise alternative
   when the goal is simply to remove elements matching a condition. The
   following example removes all odd values from the first ten Fibonacci
   numbers:

   .. tb-code:: cpp
      :name: using_iterator_erase_if_ac
      :compileargs: ['-std=c++20', '-Wall', '-Wextra', '-pedantic']

      #include <algorithm>
      #include <iostream>
      #include <vector>

      void print(const std::vector<int>& values) {
        for (const auto value : values) {
          std::cout << ' ' << value;
        }
        std::cout << '\n';
      }

      int main() {
        std::vector<int> fibonacci = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34};
        print(fibonacci);

        std::erase_if(fibonacci, [](int value) {
          return value % 2 != 0;
        });
        print(fibonacci);
      }

   The explicit loop above shows why an iterator must advance differently
   after ``erase`` than after an element is retained.

-----

.. admonition:: More to Explore

   - :cpp:`Iterator Library <iterator>`
   - :cpp:`C++20 Concepts Library <concepts>`
   - :cpp:`C++20 Ranges Library <ranges>`
   - :container:`std::vector::erase <vector/erase>`
   - :container:`std::vector::insert <vector/insert>`
