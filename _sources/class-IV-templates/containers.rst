..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: class; container

Container classes
=================
Container classes are simply user defined types that provide easy access to
a collection of data that is the same type.
You are already familiar with several container classes:

- ``std::string``
- ``std::vector``
- ``std::bitset``
- ``std::array``

There are more in the STL, but they all have one thing in common.
They store a collection of data of **a single type**.

Containers are like arrays in that regard, however,
container classes have many features that raw arrays lack.

C++11 adds a *list initialization* as a feature.
List initialization provides 2 key benefits:

#. No implicit narrowing conversions
#. No floating point to integral type conversions
#. Ability to initialize a container using a list syntax

Consider the following examples.

.. code-block:: cpp

   double d = 3.14;
   int pi = d;      // compiles, but probably a bug

   int  i  {d};     // compile error
   char c1 {i};     // compile error
   char c2 {128};   // ok - 128 fits in type char
   int  x  {c2};    // ok - widening conversion

   double z {x};    // compile error
                    // yes, a widening conversion, but 
                    // no floating point to int conversions allowed
                    // in either direction

What about 'initializer list' syntax?

An initializer list is a type constructed when using list initialization
**followed by an assignment operator**.

.. code-block:: cpp

   auto a = 1;       // a is an int
   auto b {2};       // b is an int
   auto c = {3};     // c is an initializer_list<int>

The type of ``c`` can be unexpected when the type is
not a container type.
It is important to note the initializer_list constructor
is preferred above all others if it exists in a class.

.. index:: initializer_list

Initializer list constructors
-----------------------------
The :utility:`initializer_list` was introduced in C++11 to simplify
container initialization and make it more uniform.
Prior to C++11, you could initialize an array with a value list:

.. code-block:: cpp

   int fib[] = {1, 1, 2, 3, 5, 8, 13};

However, trying the same style for other standard library containers
would result in a compile error:

.. code-block:: cpp

   // compile error in C++03 and prior
   std::vector<int> fib = {1, 1, 2, 3, 5, 8, 13};

Prior to C++11, if you wanted to add a known set of values to a vector
you would have to push them back one at a time using ``push_back``,
either one line at a time, in a loop, or using an algorithm from the STL.

An **initializer_list<T>** is a lightweight wrapper that that creates
a temporary array of type **T**.

.. code-block:: cpp

   std::initializer_list<int> fib = {1, 1, 2, 3, 5, 8, 13};

Any class can define a constructor that takes a 
:utility:`initializer_list` type as a parameter.
Obviously, it makes sense to define an ``initializer_list``
constructor only for a type that can be correctly constructed
from a list of values.
Containers are the most obvious example and are the motivation
behind initializer lists.


.. tabbed:: initializer_tab1

   .. tab:: Example

      The following example defines the absolute minimum
      you would need to define a simple class that can
      be initialized like :container:`std::array <array>`.

      It defines a stack array of specified size using the non-type
      parameter ``N`` and allows a new **array** to be constructed
      using (only) an initializer list. No other constructors
      are included in this example.

      .. code-block:: cpp

         template <class T, size_t N>
         struct array {
             T data_[N];
             array(const std::initializer_list<T>& list) {
               std::copy(list.begin(), list.end(), data_);
             }
         };


      An array instance can now be created from an initializer list
      using standard C++ syntax.

      .. code-block:: cpp

         array<int,7> fib = {1,1,2,3,5,8,13};

      The assignment from the temporary list to the array object does
      require an implicit conversion between the two types.

   .. tab:: Run It

      This example converts the ``struct`` into a ``class``
      and makes the one argument constructor ``explicit``.

      Notice how the declaration of variable ``fib``
      changes in main when the initializer_list constructor
      is marked as ``explicit``.

      .. activecode:: ac_template_container_initializer_list
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <algorithm>
         #include <cstddef>
         #include <initializer_list>
         #include <iostream>

         template <class T, size_t N>
           class array {
             private:
               T data_[N];
             public:
               explicit
               array(const std::initializer_list<T>& list) {
                 std::copy(list.begin(), list.end(), data_);
               }
               constexpr
                 const T& operator[](const size_t& index) const 
                 { return data_[index]; }
               T& operator[](const size_t& index)
                 { return data_[index]; }
           };

         int main()
         {
           auto fib = array<int, 7>{1,1,2,3,5,8,13};
             
           for (size_t i = 0; i<7; ++i) {
             std::cout << fib[i] << ' ';
           }
           std::cout << '\n';
         }

**Note:** Initializer lists will always favor a matching initializer_list 
constructor over other potentially matching constructors. 
So, if our array had a one argument constructor that took a single value of
type ``T``:

.. code-block:: cpp

   array<int,1> fib = {3};

Then this declaration would invoke 
``array(const std::initializer_list<T>&)`` and not 
``array(int)``.
If you want to match to ``int`` constructor once a list constructor has been defined, 
you’ll need to use copy initialization or direct initialization. 
The rule applies to ``std::vector`` and other standard library container classes
that define both a list constructor and another one argument conversion constructor.

.. code-block:: cpp

   // Calls std::vector::vector(std::size_type)
   // creates 3 value-initialized elements: 0 0 0
   std::vector<int> data( 3 );

   // Calls std::vector::vector(std::initializer_list<int>)
   // creates 1 element with value = 3
   std::vector<int> data{ 3 };



-----

.. admonition:: More to Explore

   - :lang:`C++11 list initialization <list_initialization>`
   - :utility:`Initializer list constructors <initializer_list>`
 
