..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Hello, world!
=============
Welcome to CISC187 and welcome to this book.

This book is intended for students taking CISC187 at SD Mesa.
You should already have a solid understanding of the
material presented in the vast majority of first semester C and C++ courses.

This entire course focuses on writing code.
Even this book provides opportunities for you to write,
compile, and evaluate code on may pages.
Often the interactive code is on a separate tab,
for example:

.. tabbed:: hello_world

   .. tab:: Example

      A C++ construct that may be new to you is the
      :lang:`range-based for <range-for>` loop.
      When your goal is to iterate over all the elements
      in a container or array, a range-for loop
      is easier to write and understand.

      .. code-block:: cpp

         for (auto value: data)           // for each value in data
         {
           std::cout << "value is " << value << '\n';
         }

      Introduced in C++11, a range-for loop extracts values
      from containers one at a time and assigns them to a variable.

   .. tab:: Run It

      A complete example program using the code explained
      on the *Example* tab.

      .. activecode:: hello_world_rangefor_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         // compiled with: -std=c++11
 
         #include <iostream>

         int main () {
           int data[] = { 1, 2, 3, 5, 8 };
           for (auto value: data)           // for each value in data
           {
             std::cout << "value is " << value << '\n';
           }
           return 0;
         }

      Feel free to modify this code and re-run it to see what
      happens when you change it.

The remaining section on this page list some things I expect
everyone to know on the first day of class.
Review this material and if anything looks unfamiliar
then read the linked content and ask questions.

.. index:: #pragma once
   pair: introductory topics; header files
   single: header guard

**Source files and header files**

One of the primary goals of this course is to begin creating programs more
complex than those written previously.
One of the core skills required when writing large programs is to split 
different parts of the program source into separate files.

You may have only had to do this a few times previously, 
but you should know by now:

* What are the differences between source and header files?

  * Why do they exist?
  * What are :term:`header guards <header guard>`?
  * What is ``#pragma once``?

  See :cpp:`preprocessor/include` for more information.

.. index:: 
   pair: introductory topics; compilation vs. linking

**Compilation vs. linking**

* What happens during compilation?  Linking?
* How to use function *main()*, *argc*, and *argv*
* :io:`cout` and the meaning of statements like:

.. code-block:: cpp

   #include <iostream>
   #include <stdio.h>

   int main() {
     std::cout << "Hello C++!" << std::endl;
     puts("Hello C!");
     printf("Hello Alice!\n");
     printf("Hello %s!\n", "Bob");
   }
   
You may not have seen :cstdio:`printf <fprintf>` and :cstdio:`puts` before.
They are output functions C++ inherits from C.
Normally, in C++ we use stream I/O functions and classes,
but the old C functions are still there if you need them.

Built-in types, variables and operations
----------------------------------------
You should already be familiar with declaring fundamental :cpp:`types`
(``int``, ``char``, ``double``, ``unsigned``, etc.).
You should also know that other :types:`fixed width integer types <integer>`
exist (``int16_t``, ``uint64_t``, etc.) 
even if you haven't used them very much.
You should also be familiar with the basic math operations and operators
(``+``, ``-``, ``=``, ``==``, etc.).
Including the shortcut operators (``++``, ``+=``, etc.).
We will be expanding our knowledge of operators and operations
extensively during this course.

.. index:: 
   single: type conversion
   single: widening conversion
   single: narrowing conversion

You should know the difference between *declaring*, *initializing*, and
*assigning a value* to a variable.
It is (sometimes) valid to assign variables of one type to those of a different
type, for example, `double x = 12;` assigns the integer `12` to the `double x`.
This is a **widening conversion** and is always safe.
The opposite of a widening conversion is a **narrowing conversion**.
A narrowing conversion frequently involves the loss of information.
Most compilers will warn about narrowing conversions even in cases where
they are allowed.

Keep in mind that a common source of error in programs is unintentional
narrowing conversions that occur during math operations.
For example:

.. tabbed:: hello_world_narrowing

   .. tab:: Example

      What is the output, given the following?

      .. code-block:: cpp

         double value = 3 / 2;

   .. tab:: Run It

      .. activecode:: hello_world_narrowing_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>

         int main() {
           double value = 3 / 2;
           std::cout << "The value is: " << value << ".\n";
         }

      Fix this program so that the correct value is displayed.


You should know how to explicitly cast fundamental types from one
type to another.
Most people should be familiar with the ``static_cast`` form:

::
    
   auto almost_pi = static_cast<int>(3.14159);

Some people may have also learned the C-style cast:

::
    
   auto almost_pi = (int)3.14159;

These two casts are roughly equivalent, but the first is preferred.
We discuss why later in the book.
We will be learning other ways to explicitly cast that are a bit more consistent
with C++11's more uniform initialization syntax.

Finally, you should know the basic keywords of the language,
at least those common to both C and C++, and legal identifier names
for functions and variables.

User-defined types
------------------
Although you may not have done any object oriented programming yourself,
you probably have used objects, even if you weren't aware of it.
The C++ standard provides many classes.
Two of the oldest classes handle stream formatted input and output:
:io:`cin` and :io:`cout`.

You should have already encountered code like:

.. code-block:: cpp

   std::string  name;
   std::cout << "Enter your name: ";
   std::cin  >> name;
   std::cout << "Hello," << name << "!\n";

You may have been taught the basics of :cpp:`string` and :container:`vector`.
It is hard to do much (non-embedded) C++ programming without ever using either.
A bit like writing a paragraph in English without using the letter 'e'.
Try that sometime!

We will be working with ``std::string`` and ``std::vector``
often in this course, so if you haven't used them yet,
don't worry - you will.

File input and output
---------------------

I expect you to know how to use some form of file input and output,
whether it is the C-style :cstdio:`printf` and :cstdio:`scanf`, or the
C++-style input and output file streams: :io:`ofstream` and :io:`ifstream <basic_ifstream>`.
Both are serviceable, have their own advantages and disadvantages.
This course emphasizes *contemporary* C++ and encourages the use of
C++ generally, but sometimes ``printf`` is a perfectly acceptable
alternative to ``cout``. 

Don't panic.

While file I/O is not a primary focus of this course,
you will be expected to employ basic I/O in labs and projects.

.. tabbed:: tab_io_examples

   .. tab:: C style IO

      This example uses ``printf`` and ``scanf`` to interact with
      the standard console input and output.

      .. activecode:: hello_world_scanf_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:
         :stdin: Alice

         #include <cstdio>

         int main () {
           char name[20];
           scanf("%s", name);
           printf("Hello, %s!\n", name);
         }

      .. admonition:: Try This!

         Feel free to change the input to something else to see what happens.

         What happens if we enter a name longer tahn our buffer size?

   .. tab:: C++ style IO

      This example uses ``std::cout`` and ``std::cin`` to interact with
      the standard console input and output.


      .. activecode:: hello_world_cin_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:
         :stdin: Alice

         #include <iostream>
         #include <string>

         int main () {
           std::string name;
           std::cin >> name;
           std::cout << "Hello, " << name << "!\n";
         }

      Feel free to change the input to something else to see what happens.


   .. tab:: C file IO

      Reading from a file to access external data:

      .. activecode:: df_ac_poem_c_file_io
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :datafile: poem
         :nocodelens:

         #include <cstdio>

         int main() {
            // assuming the file 'poem' exists in the current directory
            FILE* ptr = fopen("poem","r");
            if (ptr == NULL) {
              printf("Unable to open poem.");
              return 1;
            }
            char c;
            // read the text file one byte (char) at a time
            while (fscanf(ptr,"%c",&c) == 1) {
              putchar(c);
            }
            return 0;
         }

   .. tab:: C++ file IO

      Reading from a file to access external data:

      .. activecode:: df_ac_poem_stream_io
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :datafile: poem
         :nocodelens:

         #include <fstream>
         #include <iostream>

         int main () {
           // assuming the file 'poem' exists in the current directory
           std::ifstream is("poem");
           char c;
           // read the text file one byte (char) at a time
           while (is.get(c)) {
             std::cout << c;
           }
           is.close();
           return 0;
         }

      .. admonition:: Try This!

         Change this program to read from the poem file
         one **line** at a time instead of reading single
         characters at a time.

         Hint: change ``char`` to ``std::string`` and use :string:`getline`
         instead of ``get``.

   .. tab:: poem

      .. datafile:: poem
         :edit:

                   Jabberwocky

         "Beware the Jabberwock, my son!
           The jaws that bite, the claws that catch!
         Beware the Jubjub bird, and shun
           The frumious Bandersnatch!"

         He took his vorpal sword in hand:
           Long time the manxome foe he sought --
         So rested he by the Tumtum tree,
           And stood awhile in thought.

         And, as in uffish thought he stood,
           The Jabberwock, with eyes of flame,
         Came whiffling through the tulgey wood,
           And burbled as it came!

         One, two! One, two! And through and through
           The vorpal blade went snicker-snack!
         He left it dead, and with its head
           He went galumphing back.

         And, has thou slain the Jabberwock?
           Come to my arms, my beamish boy!
         O frabjous day! 'Callooh! Callay!'
           He chortled in his joy.

                       -- Lewis Carroll, 1871

Keep in mind that each of the I/O examples presented are just
one way to solve these problems.
Each of them could have been written differently and
achieved exactly the same goals.
For example, reading files one byte at a time is not generally
the most efficient file read solution, but it is extremely simple.
At this point, we are not concerned with a thorough treatment
of input and output, rather we are just reviewing major concepts
and showing the differences between C standard I/O and C++ I/O.

Statements and branching
------------------------

Writing basic statements and conditionally executing code,
or executing blocks of code repeatedly, are fundamental skills
common to all programming languages.

Everyone should be **extremely familiar** with writing
``if``, ``switch``, ``for``, and ``while`` blocks.

You should have used combinations of statements and branching 
to perform tasks perhaps as complex as:

* Computing an amortization table
* Computing population growth
* Parsing text


For example, loops and conditionals make it easy to 
print all the odd numbers between 1 and 100, inclusive.

.. activecode:: ac_print_odds_hello_world
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
   :nocodelens:

   #include <iostream>
   using std::cout;

   int main() {
     cout << "Odd numbers:\n";
     for (int num = 1; num <= 100; ++num) {
       if (num % 2 != 0) {
         cout << '\t' << num << '\n';
       }
     }
   }


Fixing errors in code
---------------------

You should know the difference between basic types of errors:

* :term:`Compile-time errors <compile-time error>`
* Link-time (linker) errors 
* :term:`Runtime errors <runtime error>`
* :term:`Semantic errors <semantic error>`

I expect some basic experience using a debugger in whatever 
programming environment you may have used previously.

If not, refer to the section :doc:`../build-tools/debugging`.

.. note::

   If **any** of the material in the preceding sections sounds unfamiliar, then

   * Consider working through the `week 1 example source code <https://github.com/DaveParillo/cisc187/tree/master/examples/week01>`_

   * Review the material from your first semester text

-----

.. admonition:: More to Explore

   - :lang:`range-based for <range-for>` loop, :lang:`for` loops,
     and :lang:`while` loops
   - :lang:`if`
   - :doc:`../build-tools/debugging`
   - Jeff Atwood's blog: `Code smells <https://blog.codinghorror.com/code-smells/>`_


