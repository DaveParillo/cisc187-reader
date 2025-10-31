..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; vector
   pair: vector; size
   pair: vector; capacity

.. _vector-memory:

The ``std::vector`` class
=========================
The :container:`std::vector <vector>` is a sequence container 
that simulates a dynamically sized array.
If you have taken a class in linear algebra, 
the vector ADT has nothing to do with mathematics,
but is simply sequential data structure.

It is a flexible and frequently used container.
Refer to :ref:`vector-intro` for an introduction to the basic functions available.

Like an array, elements are stored in adjacent memory slots.
This means that elements can be accessed not only through iterators, 
but also using offsets to regular pointers to elements.
The benefit of this is that a pointer to an element of a vector may be passed 
to any function that expects a pointer to an element of an array.

Unlike an array,
vector storage is handled automatically, being expanded and contracted as needed. 
Vectors usually occupy more space than static arrays, 
because more memory is allocated to handle future growth. 
This way a vector does not need to reallocate each time an element is inserted,
but only when the additional memory is exhausted. 
The total amount of allocated memory can be queried using the :vector:`capacity` function. 
Starting in C++11, extra memory can be returned to the system with a call to
:vector:`shrink_to_fit`.


.. index:: 
   pair: graph; std::vector

.. tabbed:: tab_vector_sz_cap

   .. tab:: Size vs Capacity

      A vector declared as:

      .. code-block:: cpp

         std::vector<int> v(6);

      Creates a vector of type ``int``,
      with size 6 and all values initialized to 0.
      At this point, the size and capacity of the vector are the same.

      If we assign new values to the vector:

      .. code-block:: cpp

         v = {2, 7, 1, 8};

      The new values replace the old.
      Although the **size** of the vector lowers from 6 to 4,
      the **capacity** of the vector is not changed.

      .. graphviz:: 
         :alt: A vector of type int

         digraph {
           graph [fontname = "Bitstream Vera Sans", 
                  labelloc=b,
                  label="A vector of type int"
           ];
           node [fontname = "Bitstream Vera Sans", fontsize=14, shape=plaintext];
           "Indices:" -> "Values:" [color=white];
           "unused storage";

           node [shape=record, width=4.75, fixedsize=true];
           indices [label="v[0] | v[1] | v[2] | v[3]| v[4] | v[5]", color=white];
           values [label="<f0> 2 | <f1> 7 | <f2> 1 | <f3> 8 | <f4> 0 | <f5> 0 ", 
                   color=black, fillcolor=lightblue, style=filled];

           values:f4,values:f5 -> "unused storage" [dir=back];
           { rank=same; "Values:"; values }
           { rank=same; "Indices:"; indices }
         }

      The data at ``v[4]`` and ``v[5]`` were originally default constructed
      and accessible when the vector was initially created with the explicit
      size = ``6``.
      Once the new data is assigned and the size of the vector is reduced,
      the ``end()`` also shrinks.
      A loop over the elements in the vector will not include
      the data at ``v[4]`` and ``v[5]``.

   .. tab:: Run It

      .. activecode:: ac_copy_vector_sz_capacity
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:
         :language: cpp

         #include <iostream>
         #include <vector>

         using std::cout;
         using std::vector;

         void print(const vector<int>& container)
         {
           cout << "size: " << container.size()
                << ", capacity: " << container.capacity() 
                << ", values: ";
           for (const auto& v: container) {
               cout << v << ' ';
           }
           cout << '\n';
         }
                 

         int main()
         {
           vector<int> v(6);
           print (v);
           v = {2, 7, 1, 8};
           print (v);
           v.pop_back();
           print (v);
           v.clear();
           print (v);
           v = {5,13};
           v.shrink_to_fit();
           print(v);
         }

.. admonition:: Try This!

   Change the previous example using different ways of initializing and
   modifying the vector.
   Try to predict the ``print`` output *before* running the program.

   Some things to try:

   - Default constructed vector
   - Push back 1 value onto an empty vector. 
   - Write a loop to push back 10 values onto a vector 1 at a time.
   - Replace clear with empty
   - Calling :container:`vector::reserve <vector/reserve>` with
     values larger and smaller than the current capacity.

This is a new and important distinction.

size
   Refers to the number of elements in the container.

capacity
   Refers to the total size of the underlying storage.

The vector ADT makes the distinction primarily for performance reasons.
The backing store of a vector is an array and an array cannot be resized.
Adding even one element to a completely full array involves several steps:

- making a new array with a larger capacity
- copying the old array into the new array
- destroying the old array storage

That is a lot of work and a potentially expensive operation.
For this reason, vectors normally never reduce the capacity of 
and array unless explicitly instructed to do so.

It also explains why tools like ``clang-tidy`` will 
`complain <https://clang.llvm.org/extra/clang-tidy/checks/performance-inefficient-vector-operation.html>`__
if it finds calls to :container:`vector::push_back <vector/push_back>`
in a loop after a default constructed vector is declared.

.. index:: 
   pair: vector; as C function parameters

Passing vectors to C functions
------------------------------

The data layout of a vector makes it easy to pass a vector to a legacy C
function that expects a raw array.
This is something that comes up more often than you might expect.
The book *Effective STL* has a good discussion of 
passing string and vector objects to legacy C functions\ [1]_\ .

Given a legacy C function that expects a raw array:

.. code-block:: cpp

  void print_sum (const int* values, size_t array_size) {
    int sum = 0;
    for (size_t i = 0; i < array_size; ++i) {
      sum += values[i];
    }
    printf("Sum of ints in the array is %d\n", sum);
  }

We expect to be able to pass in an array and print the sum:

.. code-block:: cpp

   int main() {

     int data[] = { -30, 102, 55, -19, 0, 222, -3000, 4000, 8, -2 };
     const int numValues = sizeof data / sizeof(int);

     print_sum (data, num_values);

     return 0;
   }

We can pass a ``vector`` to this same legacy function:

.. code-block:: cpp

   int main() {
     int data[] = { -30, 102, 55, -19, 0, 222, -3000, 4000, 8, -2 };
     const int num_values = sizeof data / sizeof(int);

     print_sum (data, num_values);

     std::vector<int> v;
     v.insert (v.begin(), data, data + num_values);	// insert the ints in data
                                                    // into v at the front

     print_sum (&v[0], v.size());   // ok, unless v is empty

     if (!v.empty()) {              // safer
       print_sum (&v[0], v.size()); //&v[0] is better than v.begin()
     }

     return 0;
   }


-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - `Clang-tidy vector performance checks <https://clang.llvm.org/extra/clang-tidy/checks/performance-inefficient-vector-operation.html>`__

.. topic:: Footnotes

   .. [1] Effective STL (Item #16) by Scott Meyers (Addison-Wesley Professional).  Copyright 2001 Scott Meyers, 978-0-201-74962-5.

