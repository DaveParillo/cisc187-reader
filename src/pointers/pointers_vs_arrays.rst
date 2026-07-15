..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: pointers; arrays

Pointers and arrays
===================

Pointers are not arrays and arrays are not pointers.
However, much confusion arises between them because
*arrays in expressions* often behave like pointers.
The term you'll often see is that *arrays decay into pointers*.

Things don't really "decay" in C or C++, but the name of an array
resolves to an address.
Given the following array:

.. code-block:: cpp

   int data[5] = {3, 5, 8, 13, 21};

The variable ``data[0]`` stores the value ``3``.
The variable ``data`` stores the address of element 0.

Pointers store addresses, so the same of an array and a pointer
both store the same kinds of data.

Any array type will implicitly convert to a pointer of the type stored in the array.
The pointer is constructed to point to the first element of the array.
This conversion happens whenever arrays are used in an expression where
arrays are not expected, but pointers are:

.. tb-code::
   :show-tutor:

   #include <iostream>
     
   int main() {
     int a[3] = {13, 21, 35};
     int* p = a;
 
     std::cout << sizeof a << '\n'  // prints size of array
               << sizeof p << '\n'; // prints size of a pointer

    for(int n: a) {          // okay: arrays can be used in range-for loops
      std::cout << n << ' '; // prints elements of the array
    }
    // for(int n: p) {       // error: no range for looping on a pointer


    // arrays and pointers share the same semantics
    std::cout << '\n'
              << *a << '\n' // prints the first element
              << *p << '\n' // same
              << *(a + 1) << ' ' << a[1] << '\n'  // prints the second element twice
              << *(p + 1) << ' ' << p[1] << '\n'; // same
   }

This behavior applies to function calling as well:

.. tb-code::
   :show-tutor:


   #include <iostream>
     
   // print first element of array using pointer dereference
   void g(int (&a)[3]) {
     std::cout << *a << '\n'; 
   }
     
   // print first element of array using array semantics through pointer
   void f(int* p) {
     std::cout << p[0] << '\n';
   }

   int main() {
     int a[3] = {13, 21, 35};
     int* p = a;
 
    // where arrays are acceptable, but pointers aren't, only arrays may be used
    g(a); // okay: function takes an array by reference
    // g(p); // error: pointers do not implicitly convert to arrays

    // where pointers are acceptable, but arrays aren't, both may be used:
    f(a); // okay: function takes a pointer
    f(p); // okay: function takes a pointer
   }


.. tb-group::
   :name: array-pointer-tabbed

   .. tb-tab:: Run It

      This example shows many of the concepts we have discussed so far in one spot.

      .. tb-code:: cpp
         :name: ac-array-pointer-cpp-larger-example-with-addresses

         #include <iostream>

         int main()
         {
             using std::cout;
             int data[5] = {8, 13, 21, 34, 55};

             int* p1 = data;
             int* p2 = data + 1;
             int  i1 = * data + 1;
             int  i2 = * (data + 1);
             int  i3 = * p2 + 1;

             cout << "The address of data is: " << data << ", " << &data  << ", " << p1 << '\n';
             cout << "The 1st val in data is: " << * data << ", " << * p1 << '\n';
             cout << "The address of p1 is: " << &p1 << '\n';

             cout << "The address of data[1] is: " << (data+1) << ", " << p2 << '\n';
             cout << "The 2nd val in data is: " << * (data+1) << ", " << * p2 << ", " << i2 << '\n';

             cout << "8+1 equals: " << (* data +1) << ", " << i1  << ", " << * p1 + 1 << '\n';
             cout << "13+1 equals: " << * (data +1)+1 << ", " << i3  << ", " << * p2 + 1 << '\n';

             cout << "(*data + 1): \t" << (* data) << "\t\t" << (* data + 1) << '\n';
             cout << "*(data + 1): \t" << (* data) << "\t\t" << * (data + 1) << '\n';
             cout << "(&data + 1): \t" << (* (&data)) << " " << (&data + 1) << '\n';

             cout << "Print dataay address locations:\n";
             for (int i=0; i<5; ++i) {
               cout << (data+i) << ", "; // each location is 4 bytes larger
             }
             cout << std::endl;

             int array_bytes = sizeof data;
             int int_bytes = sizeof (int);
             int array_size = array_bytes / int_bytes;

             cout << "size: " << array_size
                  << "\n# bytes in array: " << array_bytes
                  << "\n# bytes in 1 int: " << int_bytes << '\n';

             return 0;
         }


Array indexing pitfalls
.......................

**Pitfall #1**

Arrays perform absolutely no bounds checking.

Read that again.

Good.

Now consider that no compiler will complain about this code:

.. code-block:: cpp
   :linenos:

   int* p = int[3];
   p[0]  = 3;  // OK
   p[2]  = 5;  // OK
   p[99] = 8;  // oops!  where did we write this?
   p[-7] = 8;  // or this!

No compiler will inform you that on line 4 we just wrote an ``8``
at a location 96 positions past the end of the array.
Nor will it inform you that on line 5, we just wrote to a location
7 positions before the beginning of the array.

Most pointer examples you see will never attempt to use ``operator[]``
to index a pointer that is not an array.
This is a good thing, but as you might expect, if you make a mistake,
the compiler has nothing to offer:

.. code-block:: cpp

   int  n = 5;
   int* p = &n;

   int x = p[99] + 2;

Even with all compiler warnings enabled, most compilers will emit nothing at all.
No compiler will inform you that
we just accessed a piece of memory 98 ``ints`` past the one you own.
Whatever is stored there, we then added 2 to it
and assigned that value to ``y``.
The compiler doesn't even know ``p`` is a pointer to just one ``int``.

Most programmers know better than to make errors this large.
We're just demonstrating here that even big mistakes can be completely
ignored by the compiler.
What is for more common is an 
`off by one error <https://cwe.mitre.org/data/definitions/193.html>`__
where your array index or pointer address is wrong only by 1.
Accessing even a single byte outside your valid memory bounds is
still an error and one of the most common errors in C and C++ programs.

**Pitfall #2**

From the standard:

  The definition of the subscript ``operator[]`` is that ``E1[E2]`` is identical to ``(*((E1)+(E2)))``. 
  Because of the conversion rules that apply to the binary ``operator+``, 
  if ``E1`` is an array object (equivalently, a pointer to the initial element of an array object) 
  and ``E2`` is an integer, ``E1[E2]`` designates the ``E2``\-th element of ``E1`` (counting from zero).

.. note::

   What the standard doesn't repeat here is that addition commutes, that is 
   :math:`a+b = b+a`.
   A side-effect of this fact is that for any array and index pair ``a[i]``,
   then  ``a[i]`` must be equivalent to ``i[a]``.

   .. tb-code:: cpp
      :name: ac-array-index-1
      :show-tutor:



      #include <iostream>
      using std::cout;

      int main() {
        int a[4] = {3, 5, 8, 13};
        cout << "Print each array element 4 times:\n";
        for (int i=0; i<4; ++i) {
          cout << a[i]   << ' ' 
               << *(a+i) << ' ' 
               << *(i+a) << ' ' 
               << i[a]   << '\n';
        }
      }

   Although the standard does not strictly *prohibit* this syntax,
   doesn't mean you should use it.

This pitfall is only a problem when using arrays of type ``int`` with easily confused variable names. 
The lesson: use variables appropriate for the scope.
In this case, perhaps a single letter (a) for the array was too short.


.. index:: character arrays

Arrays of type ``char``
.......................

In the C language, 
the abstract idea of a string is implemented with an array of characters.
Arrays of ``char`` that are null terminated are commonly called *C strings*.

In older C and C++ code using C strings,
it's common to see code that uses the null terminator in 
the C string as a loop exit condition:

.. tb-code:: c
   :name: ac-array-c-copy-idiom
   :show-tutor:

   #include <stdio.h>

   // an old C idiom to copy a 'string'
   int main (int argc, char** argv) {
     char a[] = "Hello World!";
     char b[13];

     // print one char at a time
     int i;
     for (i=0; i<12;++i) putchar(a[i]);
     printf("\n");


     char* p1 = a; 
     char* p2 = b;
     for (int i=0; a[i]; ++i) p2[i] = p1[i];

     printf("copy:\n");
     printf("%s\n", p2);  // print chars until '\0' detected
     return 0;
   }

Code like this can fail if the source string contains any embedded null characters.
The risk is that this code works fine 99% of the time, but fails
when working with character data from an uncontrolled source 
(a network or socket interface, for example).

.. admonition:: Try This!

   Run the previous example, but modify it,
   replacing the 'Hello World' with 'Hello\\0World'.
   What happens?

   What warnings does the compiler display?

-----

.. admonition:: More to Explore

   - Array declarations in :c:`C <language/array>` and :lang:`C++ <array>`
   - MITRE Common Weakness Enumerations
     `Off by one error <https://cwe.mitre.org/data/definitions/193.html>`__
   - :wiki:`Wikipedia Off-by-one errors <Off-by-one_error>`
  


