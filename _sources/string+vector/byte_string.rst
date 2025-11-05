..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: byte string; C string

String abstractions in C
========================

In the C language, 
the abstract idea of a string is implemented with an array of characters.

.. code-block:: c

   // the char array must be null terminated
   char a[] = {'h', 'e', 'l', 'l', 'o', '\0'};  // null == '\0'

   char b[] = {'h', 'e', 'l', 'l', 'o', 0};     // null == 0 also

   // a quoted literal is just a special case of a char array
   char* c = "hello";

Arrays of ``char`` that are null terminated are commonly called 
:string:`byte strings </byte>` or
:string:`C strings <c_str>`.
Given the byte string:

.. code-block:: c

   const char* howdy = "hi there!";

   
.. index:: 
   pair: graph; char array

In memory, ``howdy`` is automatically transformed into:

.. graphviz::

   digraph char_array {
     fontname = "Bitstream Vera Sans"
     label="Character array in memory"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{'h'|'i'|' '|'t'|'h'|'e'|'r'|'e'|'!'|'\\0'}";
     ]
     idx [ 
        color = white;
        fillcolor=white;
        label = "{howdy[0]|howdy[1]|howdy[2]|howdy[3]|howdy[4]|howdy[5]|howdy[6]|howdy[7]|howdy[8]|howdy[9]}";
     ]


   }

The last character in the array, ``'\0'`` is the *null character*,
and is used to indicate the end of the string.
The null character is a  ``char`` equal to 0.

.. activecode:: byte_string_null_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   #include <iostream>

   int main () {
      if (const char null1 = '\0', null2 = 0;             // C++17
          null1 == null2) {
           std::cout << "these values are the same\n";
       } else {
           std::cout << "not the same\n";
       }
   }

      
.. note::

    Care must be taken to ensure that the array is large enough to hold 
    all of the characters AND the null terminator.
    Forgetting to account for null, 
    or having a 'off by one error' is one of the most 
    common mistakes when working with C strings.

    
.. index:: 
   pair: array; character
   pair: graph; byte string

A character array may allocate more memory that the characters currently stored in it.
An array declaration like this:

.. code-block:: c

   char hi[10] = "Hello";

results in an in-memory representation like this:

.. graphviz::

   digraph c {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="Character array with reserve memory"
     node [
        fontname = "Courier"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr [
        label = "{H|e|l|l|o|\\0| | | | }"
     ]

   }

The array elements after the null are unused, but could be.
So, an array of size 10 has space for 4 more characters, 9 total.

C strings have an advantage of being extremely lightweight and simple.
Their main disadvantage is that they are too simple for many applications.
Their simplicity makes them a pain to work with,
which is why the Standard Template Library (STL) contains the :cpp:`string` class.

Working with C strings
======================
The C programming language has a set of functions implementing operations
on strings (character strings and byte strings) in the standard library.
Various operations, such as copying, concatenation, tokenization, and searching are supported.

The complete list of :string:`byte string functions </byte>` is available from
cppreference.com.

It's important to know how to work with byte strings in C++
because the C string functions that C++ inherits from C continue to
provide a few capabilities not implemented elsewhere in the STL.

In addition, when the type you have is a byte string,
it's just easier and more efficient to manipulate the byte string
directly, rather than create a temporary ``std::string`` merely to 
perform an operation and then convert back.
In general, you want to try to avoid these kinds of unnecessary type conversions.

.. activecode:: c_string_array_example_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   #include <cstdio>   // printf
   #include <cstring>  // for strcpy function

   // In C, a string is literally an array of char
   //
   // This is not the same as the string class from the STL.

   int main()
   {
     char a[] = {'h', 'e', 'l', 'l', 'o', '\0'};  // the char array must be null terminated
     char b[] = {'h', 'e', 'l', 'l', 'o', 0};     // null == 0
     const char* c = "hello";                     // a string is just a special case of a char array

     for (int i = 0; a[i]; ++i) {                 // explain why this loop terminates
       printf ("%c %c %c\n", a[i], b[i], c[i]);
     }

     // copying strings 
     char* d = 0;
     d = a;      // we only copied a pointer here!
     if (a == d) {
       d[0] = 'H';
     }
     printf ("\na and d strings:\n  %s %s\n", a, d);

     char e[sizeof(b)];
     strcpy(e, b); 
     e[0] = 'H';
     printf ("\nb and e strings:\n  %s %s\n", b, e);

     // a = e;    // compile error.  C strings are not assignable

     return 0;
   }


.. index::
   single: toupper
   single: locale

Change character case
---------------------
Many languages provide utilities to change character case as part of the
string class.

Not C++.

C++ uses the legacy :string:`null-terminated byte strings library </byte>` 
to provide these features.

Changing character case is a common task and unless you choose
to write your own version of these functions,
these functions from the STL are the ones you should use.

Many string conversion functions are defined in the ``cctype`` header.
These functions which C++ inherited from C are often perfectly acceptable,
however, there are some notable exceptions, 
such as the :cpp:`toupper<locale/toupper>` function.

.. tabbed:: cctype_toupper

   .. tab:: toupper(std::locale())

      This version of ``std::toupper`` function takes a single ``char``,
      which can be **any** character type, 
      is not modified, and returns a character of the *same type*
      as the character type provided.

      Because of this, the C++ version that uses ``std::locale``
      is preferred.

      .. activecode:: string_toupper_locale_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <cctype>    // C toupper
         #include <locale>    // C++ toupper

         int main() {
           using std::cout;
           char eng[14] = "hello, world!";

           // Use C version
           for (const auto& c: eng) {
             cout << std::toupper(c) << ' ';
           }
           cout << '\n';
           // Use locale aware version - no conversion
           for (const auto& c: eng) {
             cout << "'" << std::toupper(c, std::locale())  << "' ";
           }

           return 0;
         }
  
   .. tab:: toupper()

      The ``std::toupper`` function takes a single ``char``,
      which is not modified, and returns an ``int``.
      The return value can be used as the upper case
      version of the input character.

      .. note:: **Use the right toupper!**

         The C version of toupper returns **int** values, *not*
         character values.
         This can cause unexpected behavior or conversions.

         For these resaons, the ``std::locale()`` version of
         toupper is preferred.

         See the previous tab for details.

      ``toupper`` is defined in header ``cctypes``.

      This function uses the default **C** locale to replace the
      lowercase letters ``abcdefghijklmnopqrstuvwxyz``
      with respective uppercase letters 
      ``ABCDEFGHIJKLMNOPQRSTUVWXYZ``.
      Non-ASCII characters are not handled.

      Recall that ``char`` implicitly convert to ``int``.

      .. activecode:: string_toupper_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <cctype>
         #include <iostream>

         int main() {
           char value[15] = "hello, world!";
           char& first = value[0];
           // failure to assign the return value of toupper
           // to a variable is a common source of error.
           first =  std::toupper(first);
           std::cout << value << '\n';
           return 0;
         }

.. index::
   single: strcpy
   single: strncpy
   single: strcmp
   single: strncmp

Copying and comparing C strings
-------------------------------
Unlike most of the types we work with in C++,
byte strings are simple arrays.
Arrays cannot be assigned to each other using ``operator=``.
Values in array must be copied one elements at a time,
for example using a loop.

Similarly, if you compare two arrays for equivalence,
``operator==`` will only return ``true``
if both arrays share the same memory address.

This is not what we usually want.

Like copying, in order to check a pair of arrays for equivalence
a loop is used to compare each element one at a time
until a difference is found.

The copy and compare functions are defined in the ``cstring`` header.

.. tabbed:: cstdlib_byte_string_copy_compare

   .. tab:: strcpy()
      
      The :cstring:`strcpy` function
      takes two byte strings as parameters and
      copies the source character array including the null terminator,
      to the destination character array.

      .. activecode:: byte_string_strcpy_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:
         
         #include <cstring>
         #include <iostream>
 
         int main()
         {
             const char* src = "Take the test.";

             // src[0] = 'M';        // can't modify string literal
             char dest[16];          // mutable destination
             std::strcpy(dest, src);
             dest[0] = 'M';
             std::cout << src << '\n' << dest << '\n';
         }

      Note the order of the arguments.

      A common source of error is to swap the order of the arguments.
                   
   .. tab:: strncpy()
      
      The :cstring:`strncpy` function
      copies byte strings, but will copy at most a provided ``count``
      number of characters.


      .. activecode:: byte_string_strncpy_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:
         
         #include <cstring>
         #include <iostream>

         int main() {
             const char* src = "hi";
             char dest[6] = {'a', 'b', 'c', 'd', 'e', 'f'};
             std::strncpy(dest, src, 5);
          
             std::cout << "The contents of dest are: ";
             for (char c : dest) {
                 if (c) {
                     std::cout << c << ' ';
                 } else {
                     std::cout << "nul" << ' ';
                 }
             }
             std::cout << '\n';
         }

   .. tab:: strcmp()
      
      The :cstring:`strcmp` function
      takes two byte strings as parameters and
      returns a ``0`` if every element in both arrays is equal.

      If the first operand is greater than the second, then a positive value is returned.
      If the first operand is less than the second, then a negative value is returned.

      .. activecode:: byte_string_strcmp_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <cstdlib>
         #include <cstring>
         #include <iostream>
 
         int main() {
           const int count = 3;
           const char* argv[count] = {"test_prog", "--value", "42"};
           int value = 0;
             
           for (int i=1; i < 3; ++i) {
             if (strcmp(argv[i], "--value") == 0) {
               ++i;
               if (i < count) {
                 value = atoi(argv[i]);
               } else {
                 std::cerr << 
                   "Error using '--value' argument: no value specified\n";
                 break;
               }
             } else {
               std::cerr << "Unknown command received!";
               break;
             }
           }
           std::cout << "value: " << value << '\n';
         }

      .. note::

         These functions are not locale-aware.

         If you need to make locale aware comparisons,
         then use :cstring:`strcoll`.

               
   .. tab:: strncmp()
      
      The :cstring:`strncmp` function
      takes two byte strings as parameters and
      returns a ``0`` if every element in both arrays is equal.

      However, this function only compares the at most
      a specified number of characters.


      .. activecode:: byte_string_strncmp_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         #include <cstring>
         #include <iostream>

         void demo(const char* lhs, const char* rhs, int sz) {
             int compare = std::strncmp(lhs, rhs, sz);

             if(compare == 0) {
                 std::cout << "First " << sz << " chars of ["
                           << lhs << "] equal [" << rhs << "]\n";
             } else if(compare < 0) {
                 std::cout << "First " << sz << " chars of ["
                           << lhs << "] precede [" << rhs << "]\n";
             } else if(compare > 0) {
                 std::cout << "First " << sz << " chars of ["
                           << lhs << "] follow [" << rhs << "]\n";
            }
         }

         int main() {
             demo("Hello, world!", "Hello, everybody!", 13);
             demo("Hello, everybody!", "Hello, world!", 13);
             demo("Hello, everybody!", "Hello, world!", 7);
             demo("Hello, everybody!" + 12, "Hello, somebody!" + 11, 5);
         }

      .. note::

         These functions are not locale-aware.

         If you need to make locale aware comparisons,
         then use :cstring:`strcoll`.


**Self Check**

.. tabbed:: tab_check

   .. tab:: Q1

      .. fillintheblank:: byte_string_fitb2

         Given the following:

         .. code-block:: c

            char text[32];
            strcpy(text, "hello");
            int len = strlen(text);

         What is the value of ``len``?

         - :5: Correct.
           :6: String length does not include the null character.
           :4: Sizes are not indexes.
           :x: Try again.

   .. tab:: Q2

      .. activecode:: byte_string_sc_ac1
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-std=c++20']
         :nocodelens:

         Fix the errors in the ``printf`` line below:

         ~~~~
         #include <cstdio>
         #include <string>

         int main() {
           std::string yazoo = "ritish alternative band";
           char c = 'B';
             
           printf ("%c%s\n",c, yazoo);
         }

   .. tab:: Q3

      .. fillintheblank:: byte_string_fitb3

         Which ``#include`` is required to use functions such as
         ``std::atoi`` and ``std::atof``?

         - :cstdlib: Correct.
           :cstring: These are C library functions
           :string: These are C library functions
           :x: Try again.


   .. tab:: Q4

      .. fillintheblank:: byte_string_fitb4

         Which ``#include`` is required to use functions such as
         ``std::stoi`` and ``std::stol``?

         - :string: Correct.
           :cstring: These are not C functions
           :cstdlib: These are string functions added in C++11
           :x: Try again.

-----

.. admonition:: More to Explore

   - cppreference.com :cpp:`byte strings <string/byte>`
   - Bjarne Stroustrup's C++11 FAQ: `Raw String literals <http://www.stroustrup.com/C++11FAQ.html#raw-strings>`_
   - Locales:

     - `Thinking in C++: Locales <https://www.linuxtopia.org/online_books/programming_books/c++_practical_programming/c++_practical_programming_101.html>`__
     - `Differences between the C Locale and the C++ Locales <https://stdcxx.apache.org/doc/stdlibug/24-3.html>`__

