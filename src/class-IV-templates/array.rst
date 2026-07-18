..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; array

The ``std::array`` class
============================
The :container:`std::array <array>` is a container that encapsulates fixed size arrays.
Since it is literally a wrapper around a raw array,
the size of a ``std::array`` must be defined when declared.

.. code-block:: cpp

   std::array <int, 12> days_per_month;

The array class is very lightweight and has very little
costs over a raw array.
Additionally, ``std::array`` provides convenience functions such as:

:container:`at() <array/operator_at>` and :container:`operator[] <array/operator_at>` 
   range checked access and unchecked access

:container:`front() <array/front>` and :container:`back() <array/back>`
   access to the first and last elements

:container:`size() <array/size>` 
   return the number of elements

:container:`empty() <array/empty>` 
   check if the container is empty

Unlike a raw array, ``std::array`` cannot infer its size if
declared with an initializer list:

.. tb-code:: cpp

   #include <array>
   #include <iostream>
   using std::cout;

   int main() {
     // compile error: array template parameter missing:
     //std::array<char> letters = {{'h', 'o', 'w', 'd', 'y', '!'}};

     std::array<char, 6> letters = {{'h', 'o', 'w', 'd', 'y', '!'}};

     cout << "The first character is: " << letters.front() << '\n';
     cout << "The last character is: " << letters.back() << '\n';

     for (const auto& c: letters) {
       cout << c;
     }
   }


-----

.. admonition:: More to Explore

   - :cpp:`STL containers library <container>`

