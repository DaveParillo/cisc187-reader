..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: function pointers; pointers to functions

Pointers to functions
=====================

In C++ you can point to anything with an address:

- Global variables
- Stack and free store variables
- Functions

When a function is called, 
an :term:`activation record` for the function is pushed onto the :term:`runtime stack`.
This means every function has an address.

Consider the following code:

.. code-block:: cpp

   #include <iostream>
   int foo() {
     return 5;
   }
   int main() {
     std::cout << foo;
   }


What does this program print?

Hint: It doesn't call the function foo

.. reveal:: reveal-fp1

   It prints the *address* of the function named ``foo``

When a function is called using ``operator()`` (the function call operator),
execution jumps to the *address* of the function being called.
We can make use of this to store the address of the function.

To declare a pointer to a function that returns an ``int`` and takes no parameters:

.. code-block:: cpp

   int (*pf)();

The pointer variable is named ``pf``.
The parentheses around ``(*pf)`` are required due to operator precedence.
Without the parentheses:

.. code-block:: cpp

   int *pf();     // not a pointer to a function

   // same as above
   int* pf();

Instead, this declares a function that returns an ``int*`` and takes no parameters.

To declare a pointer named ``func`` 
pointing to a function that returns a ``double`` and takes two parameters:

.. code-block:: cpp

   double (*func)(int x, int y);


.. tabbed:: tabbed_fp1

   .. tab:: Example

      Once you have a valid function pointer definition, 
      you can assign functions to it.

      Given the following functions:

      .. code-block:: cpp

         double add     (int x, int y) { return x+y;}
         double multiply(int x, int y) { return x*y;}
         double pi      ()             { return 3.14159265;}

      We can define a pointer to our functions

      This is legal, but not preferred, since our pointer is undefined.
      
      .. code-block:: cpp

         double (*func)(int, int);

      When you can, initialize variables with a value.

      .. code-block:: cpp

         double (*func)(int, int) = add;

   .. Tab:: Run It

      .. activecode:: ac_fp_intro1
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         double add     (int x, int y) { return x+y;}
         double multiply(int x, int y) { return x*y;}
         double pi      ()             { return 3.14159265;}

         int main () {
           // declare func and assign add to it
           double (*func)(int, int) = add;

           cout << (*func)(2,3); // prints 4

           func = multiply;
           cout << (*func)(2,3); // prints 6

           func = pi;            // error: pointer to function with
                                 // wrong number of arguments

           func = add();         // error: can't assign
                                 // function return value to function pointer
         }

A downside to traditional function pointer initialization is 
that this doesn't look like the initialization syntax we are used to.
This is a legacy of the C language C++ was originally based on.

The C++11 :lang:`type alias` allows defining a name that refers to a previously defined type:

.. code-block:: cpp

   double (*func)(int, int);          // old syntax

   using func = double(*)(int, int);  // since C++11


.. admonition:: Try This!

   Refactor the previous example to replace the traditional C syntax
   with the C++11 ``using`` type alias.

.. index::
   pair: video; function pointers

.. youtube:: p4sDgQ-jao4
   :http: https


Example: Caesar ciphers
-----------------------

A simple substitution cipher, called :wiki:`ROT13`, short for 'rotate 13 places'
can be used to obfuscate text by replacing each letter with the letter 13 letters after it in the alphabet.
It is a special case of the :wiki:`Caesar cipher <Caesar_cipher>`, 
used in ancient Rome to obscure communication between Julius Caesar and his generals.
A related variation called ROT47 extends the idea of ROT13 to include numbers and common symbols.

Suppose we want to create a program that allows users to run either ROT13 or ROT47?
There are many ways to implement such a program.
This example demonstrates how to use function pointers to dynamically 
control at which function is called within a loop at runtime.

Often, when writing a program, it is useful to start at 'the top'.
Suppose we want a simple command line program that takes
4 basic inputs:

`-h`
   A command line switch to show help.

`-l`
   A command line switch to transform only letters in the Latin alphabet.
   This switch will enable the ROT13 function.

`-f`
   A command line switch to transform the full set of printable letters ASCII character set.
   This switch will enable the ROT47 function.

standard input
   This is where the program will get the text to work on.

.. tabbed:: tabbed_fp_ceasar_example

   .. tab:: help.h

      Once we have decided on this as our basic framework, 
      we can create a file like ``help.h``:

      .. literalinclude:: caesar/help.h
         :language: cpp
         

   .. tab:: ceasar.h

      The 'fundamental unit' of any text input is a ``char``,
      so it makes sense to write our transforming functions to work with a single
      character at a time.

      We will write three functions for this program, one for ROT13 and one for ROT47.
      The third function takes a ``std::string``  and a function pointer as input,
      and transforms the string using the provided function,
      one character at a time.

      First we declare our interfaces:

      .. literalinclude:: caesar/caesar.h
         :language: cpp

      The `using declaration <http://en.cppreference.com/w/cpp/language/type_alias>`_
      exists only to simplify our use of our function pointer.
      Any place you see the word ``transform``,
      you can literally replace it with 
      ``char (*)(const unsigned char c)``
      and not change how the program behaves.

   .. tab:: ceasar.cpp

      We implemented our functions to take type ``unsigned char`` because
      they depend on the library functions ``std::isdigit`` and ``std::isalpha``.
      These function have undefined behavior if the character provided
      is not an ``unsigned char``.
         
      With these definitions in place, we can implement them:

      .. literalinclude:: caesar/caesar.cpp
         :language: cpp
         

   .. tab:: main.cpp

      And now we can put it all together from a small main program.

      One thing to note in this main is that it uses **both**
      :c:`standard input <io/std_streams>` and 
      :c:`command-line arguments <language/main_function>`.

      The difference is a common source of confusion.

      .. literalinclude:: caesar/main.cpp
         :language: cpp
         
      Note, we did not use the function call operator, ``operator()`` when 
      assigning values to ``handler``.  
      The name ``rot13`` points to the address where the function ``rot13`` 
      is stored.

.. admonition:: Try This!

   Consider compiling these files in your own environment and experimenting
   with variations.

   Why are *13* and *47* common rotations?

   Try to think of other rotations and implement them as additional program options.


-----

.. admonition:: More to Explore

   - `MyCodeSchool <http://www.mycodeschool.com>`__ video: 
     `Pointers in C/C++: function pointers <https://www.youtube.com/watch?v=ynYtgGUNelE&list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_&index=15>`__ 
   - :wiki:`Caesar cipher <Caesar_cipher>` from Wikipedia.
   - From: cppreference.com: 

     - :lang:`pointers <pointer>`
     - :cstring:`isalpha` and 
       :cstring:`islower`. 
     - :cstring:`strcmp`
     - :string:`getline`


