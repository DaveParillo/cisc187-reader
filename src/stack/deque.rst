..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; std::deque

The deque class
===============
The :container:`deque` (double-ended queue) is an indexed sequence container that 
allows fast insertion and deletion at both its beginning and its end. 
In addition, 
insertion and deletion at either end of a ``deque`` never invalidates pointers 
or references to the rest of the elements.

It's primary role in the standard library is to function as
the default container underlying ``std::stack`` and ``std::queue``.

.. tb-code:: cpp
   :name: container-deque-example
   :caption: Basic std::deque usage

   #include <iostream>
   #include <deque>
   #include <string>

   using std::cout;
   using std::deque;
   using std::string;

   void print (const deque<string>& container)
   {
     cout << "\n\nItems in the Deque: \n";
     for (const auto& value: container) {
       cout << value << ' ';
     }
     cout << '\n';

   }

   int main() {
     deque<string> d;
     cout << "Deque Empty? " << d.empty() << '\n';
     d.push_back("Zebra");
     cout << "Deque Empty? " << d.empty() << '\n';

     d.push_front("Turtle");
     d.push_front("Panda");
     d.push_back("Catfish");
     d.push_back("Giraffe");

     cout << "Deque Size: " << d.size() << '\n';
     cout << "Item at the front: " << d.front() << '\n';
     cout << "Item at the back: " << d.back() << '\n';

     print (d);

     d.pop_back();
     d.pop_front();

     cout << "\n\nItem at the front: " << d.front();
     cout << "\nItem at the back: " << d.back();
     cout << "\nDeque Size: " << d.size();

     print (d);
   }

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

.. tb-code:: cpp
   :name: ac-container-deque-palindrome
   :caption: Palindrome checker using std::deque

   #include <iostream>
   #include <deque>
   #include <iostream>
   #include <string>

   using std::deque;
   using std::string;

   bool check_palindrome(const string& value) {
     if (value.size() < 2) return true;
     deque<char> letters (value.begin(), value.end());

     while (letters.size() > 1) {
       char first = letters.front();  // could omit these temporaries
       char last = letters.back();
       if (first != last) {
          return false;
       }
       letters.pop_front();
       letters.pop_back();
     }
     return true;
   }

   int main() {
     std::cout << std::boolalpha 
               << check_palindrome("not a palindrome") << '\n';
     std::cout << check_palindrome("radar") << '\n';
   }

.. index:: std::equal

A moment of full disclosure:
even though it is possible to use a deque to determine if a string is a
palindrome or not, it's far from the simplest or most efficient
solution to the problem.
Simply checking the string characters directly is better.

.. tb-group::

   .. tb-tab:: Is Palindrome

      The standard library provides the :algorithm:`equal` template which
      allows comparing the values in a pair ranges.

      .. code-block:: cpp
         :name: is-palindrome

         bool is_palindrome(const std::string& value) {
            return equal(value.begin(), 
                         value.begin() + value.size()/2, 
                         value.rbegin());
         }

      The first `begin` and `end` define a range of values to be compared.
      The second `begin` defines the start of the second range of values.
      The second `end` does not need to be specified, because the comparison
      stops once the first end is reached.

      Notice that in this example, the second begin is `rbegin`.
      This means the second iterator starts at the **reverse beginning**,
      which is the *end* of the string and each iteration moves one
      step closer to the begining.

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: container-equal-palindrome
         :caption: Palindrome checker using std::equal
         :include:
            IS_PALINDROME: is-palindrome

         #include <algorithm>
         #include <iostream>
         #include <string>

         {{IS_PALINDROME}}

         int main() {
           std::cout << std::boolalpha 
                     << is_palindrome("not a palindrome") << '\n';
           std::cout << is_palindrome("radar") << '\n';
         }

While this solution does require more familiarity with the standard library,
it avoids copying the string into the container, 
removing elements from the container, and is generally simpler.


-----

.. admonition:: More to Explore

   - :cpp:`Containers library <container>`
   - The :container:`deque` class
