..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: vector

.. _vector-intro:

The vector class
================
A :container:`vector` is intended to behave like a dynamically sized array.
It is a :term:`template`, so unlike a string, 
which is a container for characters only,
a vector can serve as a container for any type.
More on templates later, for now,
we just need to know enough to know how declare a vector.

As with strings, in standard C, 
the typical way to work with a collection of data is with a 'raw' array:

.. code-block:: c

   int a[] = {3, 1, 4, 1, 5, 9};


Some downsides to raw arrays are that they:

- Do not know their own size
- Need to have their size specified when declared
- Decay into pointers easily
- Provide no convenience functions 

The ``vector`` class solves these problems for us and a few others besides.
Declaring a ``vector`` is quite similar to the ``string`` declarations
from the previous section.
In order to access the STL vector capabilities,
use ``#include <vector>``.

.. tabbed:: tab_vector_declare

   .. tab:: Declare

      To properly declare a vector,
      the *type* of data stored in the vector
      must be declared as a type parameter.

      The ``<int>`` and ``<std::string>`` represent the *template parameters*
      passed to the ``vector``.
      It is these template parameters that allow the vector class to serve
      as a container for (almost) any type.
      There are some limits we will cover later,
      but for now, know that any normal type you already have learned about
      can be stored in a vector.

      .. code-block:: cpp

         // an empty vector of int
         vector<int> x;

         // initialize and store: "x", "x"
         vector<std::string> dos_equis (2, "x");

         // C++11 initialization list syntax
         vector<int> pi_digits = {3,1,4,1,5,9};

      Unlike a fundamental type,
      the declaration ``vector<int> x;`` does **not** create 
      an uninitialized variable.
      It creates a fully formed vector with no elements stored in it yet.
      This is perfectly OK and normal.


      However, a common error is to forget to include the template parameter:

      .. code-block:: cpp

         vector x;        // compile error

   .. tab:: Run It

      .. activecode:: vector_declare_simple_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <string>
         #include <vector>
         
         using std::vector;       // alias type std::vector

         int main() {
           vector<int> x;                          // empty vector of int

           for (const auto& value: x)
           {
             std::cout << value << ',';
           }
           std::cout << '\n';

           vector<std::string> dos_equis (2, "x");  // "x", "x"

           vector<int> pi_digits = {3,1,4,1,5,9};  // C++11 
           for (const auto& value: pi_digits)
           {
             std::cout << value << ',';
           }
           std::cout << '\n';

           return 0;
         }

.. index:: 
   pair: graph; vector

Given a vector declared as:

.. code-block:: cpp

   std::vector<int> v(4);

A container capable of storing 4 integers is created:

.. graphviz:: 

   digraph {
   node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     names [ 
        color = white;
        fillcolor=white;
        label = "{size: | <f0> data: }";
     ]
     struct [
        label = "{4 | <f0> }";
     ]
     node [shape=record, color=black, fontcolor=black, fillcolor=white, width=3.75, fixedsize=true];
     labels [label="<f0> | <f4> size", color=white];
     values [label="<f0> v[0] | <f1> v[1] | <f2> v[2] | <f3> v[3]", 
             color=black, fillcolor=lightblue, style=filled];
     edge [color=black];
     struct:f0:s -> values:f0;
     labels:f4 -> values:f3;
     {rank=same; struct,labels};
   }

Although the ``vector`` object is initialized, its contents are not.
Many compiler implementations will initialize the contents to zero,
but don't rely on this behavior.
Explicitly initialize with a default value, if that is what you want:

.. code-block:: cpp

   std::vector<int> v(4, -1);


.. index:: 
   pair: vector functions; operator=
   pair: vector functions; operator[]
   pair: vector functions; at
   pair: vector functions; operator+=
   pair: vector functions; operator==

A vector comes with a rich assortment of convenience functions.
Like an array, the :vector:`operator[] <operator_at>` can be used to access elements
without bounds checking.
Like a string, the :vector:`at <operator_at>` function provides bounds checking
and will throw a :error:`std::out_of_range exception <out_of_range>` if an out of bounds index is used on the ``vector``.

.. tabbed:: tab_vector_simple_access

   .. tab:: Access operations

      Like arrays, indexes are zero-based.

      .. code-block:: cpp

         // read vector elements
         std::cout << "First element: " << numbers[0];
         std::cout << "First element: " << numbers.at(0);

         // write vector elements
         numbers[0] = 5;
         numbers.at(0) = 5;

      A common source of error occurs when printing
      a vector.
      A vector feels like a built-in type and
      this seems like it should work:

      .. code-block:: cpp

         // compile error
         std::cout << "all numbers: " << numbers;

      The vector type does not 'know' how to send it's
      values to an output stream by default.

      .. admonition:: Something to consider

         Why do you think this feature is not built into
         the standard library?


   .. tab:: Run It

         This example demonstrates an out of range error.

         How can we fix this while changing the least amount of code possible?

      .. activecode:: vector_access_operator_ac1
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:


         #include <iostream>
         #include <vector>
           
         int main() {
           std::vector<int> numbers {2, 4, 6, 8};
           std::cout << "Size: " << numbers.size() << '\n';
           std::cout << "Second element: " << numbers[1] << '\n';
           
           numbers.at(0) = 5;
           numbers.at(4) = numbers[3] + 2;  // out of range error. 
                                            // index 4 is out of bounds

           std::cout << "All numbers:";
           for (const auto& num : numbers) {
             std::cout << ' ' << num;
           }
           std::cout << '\n';
           return 0;
         }

   .. tab:: Fill and print vector

      A vector 'hello world':
      
      1. Fill a vector in one simple way, using push_back
      2. iterate through the vector and print

      .. activecode:: vector_fill_and_print_example_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <string>
         #include <vector>

         using std::cout;
         using std::string;
         using std::vector;


         int main() {
           vector<string> words = {
              "reach", "clear", "fall", "set", "yard",
              "liquid", "wise", "badge", "four", "coherent"
           };

           cout << "Word list: \n";
           for (string s: words) {
             cout << s << ", \thas " << s.size() << " letters\n";
           }
         }


The vector class also provides:

:vector:`front` and :vector:`back`
   return a reference to the first and last elements

:vector:`size` 
   return the number of elements

:vector:`empty` 
   return ``true`` if the container is empty

Although there are more functions, these are the ones we need to worry about for now.
We will be looking more at memory management in vectors in :ref:`vector-memory`.

.. admonition:: Something to consider

   What is the difference between a ``std::string`` and 
   ``std::vector<char>``?

   Why did the developers of the STL decide it was important to include both?

Comparisons between vectors are also automatically handled by the class.
In the case of a vector, 
:vector:`operator== <operator_cmp>`,
or an equality comparison between two vectors ``a`` and ``b``,
means the two vectors are equal if ``a.size() == b.size()``
and each element in ``a`` compares equal with each element in ``b``
in the same position in the vector.

.. tabbed:: tab_vector_compare_and_assign

   .. tab:: Compare operations

      Vectors support the same syntax as the built in types.

      .. code-block:: cpp

         // declare 2 vectors, one empty and one not

         std::vector<int> x {2, 4, 6, 8};
         std::vector<int> y;

         bool test = (x == y);   // test is false

         y = x;


   .. tab:: Run It

      .. activecode:: vector_operator_equal_assign_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:


         #include <vector>
         #include <iostream>
           
         int main() {
           std::vector<int> x {2, 4, 6, 8};
           std::vector<int> y;
           
           if (x == y) {
             std::cout << "x and y are equal\n";
           } else {
             std::cout << "x and y differ\n";
           }

           y = x;          // copy all data from x into y
           if (x == y) {
             std::cout << "x and y are equal\n";
           } else {
             std::cout << "x and y differ\n";
           }

           return 0;
         }


.. admonition:: Try This!

   Create two vectors of strings containing 
   the same values and check them for equality.

   .. activecode:: vector_operation_string_compare_try_this_ac
      :language: cpp
      :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
      :nocodelens:

      #include <iostream>

      int main() {
      }



Adding data to a vector
-----------------------
How do we solve the :error:`out_of_range` exception from a few examples ago?
How do we dynamically add data to a ``vector``?

A simple way is to use the :vector:`push_back` function.

Given an vector of 3 int's:

.. graphviz:: 

   digraph {
   node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     names [ 
        color = white;
        fillcolor=white;
        label = "{size: | <f0> data: }";
     ]
     struct [
        label = "{3 | <f0> }";
     ]
     node [shape=record, color=black, fontcolor=black, fillcolor=white, width=3.75, fixedsize=true];
     labels [label="<f0> | <f2> size", color=white];
     values [label="<f0> v[0]\n= 10 | <f1> v[1]\n= 20 | <f2> v[2]\n= 30", 
             color=black, fillcolor=lightblue, style=filled];
     edge [color=black];
     struct:f0:s -> values:f0;
     labels:f2 -> values:f2;
     {rank=same; struct,labels};
   }

.. code-block:: cpp

   values.push_back(40);

Appends the value 40 to the end of the vector.

.. graphviz:: 

   digraph {
   node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     names [ 
        color = white;
        fillcolor=white;
        label = "{size: | <f0> data: }";
     ]
     struct [
        label = "{4 | <f0> }";
     ]
     node [shape=record, color=black, fontcolor=black, fillcolor=white, width=3.75, fixedsize=true];
     labels [label="<f0> | <f4> size", color=white];
     values [label="<f0> v[0]\n= 10 | <f1> v[1]\n= 20 | <f2> v[2]\n= 30 | <f3> v[3]\n= 40", 
             color=black, fillcolor=lightblue, style=filled];
     edge [color=black];
     struct:f0:s -> values:f0;
     labels:f4 -> values:f3;
     {rank=same; struct,labels};
   }


.. tabbed:: tab_vector_push_back

   .. tab:: push_back and pop_back

      :vector:`push_back` appends an element to the end
      and increases the capacity of the vector, if needed.

      :vector:`pop_back` reduces the size of the vector by one.
      The last element is no longer available.

      Note that ``pop_back`` does not return a value.

      If you need that last element, remember to save it first.

      .. code-block:: cpp

         std::vector<char> letters {'a', 'b', 'c'};

         letters.push_back('d');  // add 'd' to the end of the vector
         letters.pop_back();      // pop_back is the opposite:

   .. tab:: Run It

      .. activecode:: vector_push_back_example_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <vector>
         #include <iostream>
           
         int main() {
           std::vector<char> letters {'a', 'b', 'c'};
           
           letters.at(0) = 'z';
           letters.push_back('d');  // add 'd' to the end of the vector
           char ch = 'e';
           letters.push_back(ch);  // add 'e' to the end
           letters.pop_back();     // pop_back is the opposite:
                                   //  - removes the end element from the vector

           std::cout << "All letters:";
           for (const auto& c : letters) {
             std::cout << ' ' << c;
           }
           std::cout << '\n';
           letters.clear();         // clear all contents from vector
           return 0;
         }

.. index:: 
   pair: vector functions; capacity

Vector capacity
---------------
A vector exposes an interface that 'feels like' an array,
but the underlying storage grows to accommodate new data
as required.
With an array, you either have to allocate as much memory
as you *might* need in the worst case,
even if only a small fraction is used most of the time
or you allocate 'just enough' and when more memory
is required, copy all the data into a new array.
A vector does do this also, but the implementation is
hidden and you don't have to worry about it.

Something to be aware of - 
when ``pop_back`` is called,
no actual storage is deleted.
The memory is still available in the vector
and available for reassignment with ``pop_back``.

This extra memory after the current size is referred to
as the *total capacity* of the vector,
or just *capacity*.

.. graphviz:: 

   digraph {
   node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     names [ 
        color = white;
        fillcolor=white;
        label = "{size: | <f0> data: }";
     ]
     struct [
        label = "{4 | <f0> }";
     ]
     node [shape=record, color=black, fontcolor=black, fillcolor=white, width=3.75, fixedsize=true];
     labels [label="<f0> | <f4> size | <f5> spare\ncapacity ", color=white];
     values [label="<f0> v[0]\n= 1 | <f1> v[1]\n= 1 | <f2> v[2]\n= 1 | <f3> v[3]\n= 1 |     | <f5>   ", 
             color=black, fillcolor=lightblue, style=filled];
     edge [color=black];
     struct:f0:s -> values:f0;
     labels:f4 -> values:f3;
     labels:f5 -> values:f5;
     {rank=same; struct,labels};
   }

Managing the storage capacity in addition to the 
vector data is one of the things that make vectors efficient.

.. tabbed:: tab_phrase_o_matic_example

   .. tab:: Phrase O'matic

      The 'phrase-o-matic' is
      a port of a fun little java program from
      Head First Java, 2nd ed. ISBN-13: 978-0596009205

      .. activecode:: vector_phrase_o_matic_example_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <random>
         #include <string>
         #include <vector>

         int main() {
           // initialize a random number generator
           std::random_device r;
           std::default_random_engine eng(r());
           using rand = std::uniform_int_distribution<std::uint64_t>;

           const char* list_one[] = {
             "24/7", "multi-tier", "30,000 foot", "B-to-B", "win-win",
             "front-end", "web-based", "pervasive", "smart", "six-sigma",
             "critical-path", "dynamic", "extreme", "three-tier", "agile"
           };

           // we prefer vector over arrays
           const std::vector<std::string> list_two = {
             "empowered", "sticky", "value-added", "oriented", "centric",
             "distributed", "clustered", "branded", "outside-the-box",
             "positioned", "networked", "focused", "leveraged", "aligned",
             "targeted", "shared", "cooperative", "accelerated"
           };

           const std::vector<std::string> list_three = {
             "process", "tipping-point", "solution", "architecture",
             "core competency", "strategy", "mind-share", "portal",
             "space", "vision", "paradigm", "mission"
           };

           const std::size_t one_size = 14;  // arrays don't know their size
           auto r1 = rand {0, one_size} (eng);
           auto r2 = rand {0, list_two.size()-1} (eng);   // vectors know their size
           auto r3 = rand {0, list_three.size()-1} (eng);

           std::string phrase = {list_one[r1]};
           phrase += " " + list_two[r2] + " " + list_three[r3];

           std::cout << "What we need is a " << phrase << '\n';

           // or could have omitted temporary phrase and simply:
           // std::cout << "What we need is a " << list_one[r1] << ' '
           //                                   << list_two[r2] << ' '
           //                                   << list_three[r3] << '\n';
           return 0;
         }


.. tabbed:: tab_vector_test_cases_example

   .. tab:: vector test

      .. activecode:: vector_test_cases_example_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-Werror' '-std=c++20']
         :nocodelens:

         A short test program to demonstrate the parts of the vector interface.

         What other tests can you make?

         ~~~~
         #include <iomanip>
         #include <iostream>
         #include <string>
         #include <vector>

         using std::string;
         using std::vector;

         vector<string> make_vector() {
           return {
              "reach", "clear", "fall", "set", "yard",
              "liquid", "wise", "badge", "four", "coherent"
            };
         }

         void check (const string& name, const string& actual, const string& expected)
         {
           std::cout << std::left << std::setfill('.') 
                     << std::setw(50) << name 
                     << std::setw(7) <<  std::left;
           if(actual == expected) {
             std::cout << " OK      \n";
             return;
           }
           std::cout << " FAILED\n";
           std::cout << "\treceived [" << actual
                     << "], but expected [" << expected << "]\n";
           exit(1);
         }

         // write test cases 
         void test_simple_access(vector<string> words) {
            check("test at()", words.at(0), "reach");
            check("test operator[]", words[0], "reach");
            check("test at() end", words.at(9), "coherent");
            check("test operator[]", words[9], "coherent");

            // foo.at(i) and foo.[i] refer to the same thing
            for (auto i=0U; i< 3; ++i) {
            // for (auto i=0U; i< words.size(); ++i) {
               check("at and operator[] are the same", words.at(i), words[i]);
            }

            const string empty;
            // Try uncommenting these lines to see what happens
            //check("test at out of bounds", words.at(-1), empty);
            //check("test at out of bounds", words.at(11), empty);
            //check("test [] out of bounds", words[-1], empty);
            //check("test [] out of bounds", words[11], empty);
         }

         void test_other_access(vector<string> words) {
            check("test front()", words.front(), words.at(0));
            check("test back()", words.back(), words.at(words.size()-1));
         }

         void test_assignment(vector<string> words) {
            check("test original value", words[2], "fall");
            words[2] = "falldown";
            check("test new value", words[2], "falldown");
         }

         // call test cases 
         int main() {
           auto words = make_vector();

           test_simple_access(words);
           test_other_access(words);
           test_assignment(words);
         }

-----

.. admonition:: More to Explore

   - cppreference.com `std::vector <http://en.cppreference.com/w/cpp/container/vector>`_
   - WikiBooks.org C++ Programming `STL Containers <https://en.wikibooks.org/wiki/C%2B%2B_Programming/STL#Containers>`_


