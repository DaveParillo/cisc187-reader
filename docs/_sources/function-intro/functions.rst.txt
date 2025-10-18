..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
..  Some of the content in this section is adapted from
    http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
   
.. index:: functions

Introduction to functions
=========================

A *function* is a group of statements that work together to perform a task.
A function is composed of:

- A *name*
- Zero or more *parameters*
- A return value

  - A function that returns no value must still declare that fact by
    specifying a return type ``void``.

.. code-block:: cpp

   return_type function_name (argument list)
   {
      // zero or more statements
   }

The part outside the braces is called the **function declaration**.
The braces and their contents is called the **function body**.
Once defined, a function may be called and
the task it defines can be executed as often as needed.

.. tabbed:: function_simple_intro

   .. tab:: Example

      Some simple, specific examples:

      .. code-block:: cpp

         int area (int height, int width) {
           return height*width;
         }

         void say_hello() {
           std::cout << "hello";
         }

   .. tab:: Run It

      .. activecode:: functions_simple_intro_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <iostream>

         int area (int height, int width) {
           return height*width;
         }

         void say_hello() {
           std::cout << "hello";
         }

         int main () {
           say_hello();
           std::cout << "\narea = " << area(4,3) << '\n';
           return 0;
         }

.. codelens:: functions_simple_intro_cl
   :caption: Simple functions
   :language: cpp

   #include <iostream>

   int area (int height, int width) {
     return height*width;
   }

   void say_hello() {
     std::cout << "hello";
   }

   int main () {
     say_hello();
     std::cout << "\narea = " << area(4,3) << '\n';
     return 0;
   }



Function declarations and compilation units
-------------------------------------------

By default, functions have global :term:`scope`: 
they can be used anywhere in your program, even in other files. 
If a file doesn't contain a :term:`declaration` for a function  before it is used, 
then the compiler will complain.

The solution is to either:

(a) Move the function definition before any functions that use it; or 
(b) Put in a declaration without a body before any functions that use it, 
    in addition to the declaration that appears in the function definition. 

Option (b) is generally preferred, 
and is the only option when the function is used in a different file.

To make sure that all declarations of a function are consistent, 
the usual practice is to put them in an
:cpp:`include <preprocessor/include>` file. 
For example, if the ``area`` function is used in a lot of places, 
we might put it in its own file ``area.cpp``:

.. code-block:: cpp

   #include "area.h"

   int area (int height, int width) {
     return height*width;
   }

.. index:: 
   pair: #include search path; make

The file ``area.cpp`` above uses an  ``#include`` directive to include a copy 
of the following header file area.h:

.. code-block:: cpp

   #ifndef AREA_H
   #define AREA_H

   /* Returns the area of a rectangle */
   int area (int height, int width);

   #endif /* AREA_H */

Note that the declaration in ``area.h`` doesn't have a body. 
Instead, it's terminated by a semicolon, like a variable declaration. 
A *function declaration* serves the same purpose as a *variable declaration*:
they both introduce a new name and its type into a :term:`scope`.

The ``#ifndef``, ``#define``, and ``#endif`` together form a pattern called a
:term:`header guard` or *include guard*.
They ensure the functions in include files are defined only once.

By convention, the documentation for functions is primarily in the include file.
The idea is that ``area.h`` is the public interface of this module, 
and so the explanation of how to use the function should be there.
The reason ``area.cpp`` includes ``area.h`` is to get the compiler to 
verify that the declarations in the two files match.

- ``area.h`` contains the function declaration
- ``area.cpp`` contains the function definition (which includes a declaration)

.. admonition:: Best Practice

   Keep your declarations and definitions separate.

   The source file that *defines* a function should include the file that *declares*
   a function.

Every other file that needs to use the ``area`` function uses an include directive
``#include "area.h"`` at the top of the file that uses it:

.. code-block:: cpp
   :linenos:

   #include "area.h"

   bool too_small (int x, int y) {
     const int min_size = 10;
     return area(x, y) < min_size; 
   }

The ``#include`` on line 1 uses double quotes instead of angle brackets; 
this tells the compiler to look for ``area.h`` in the current directory 
instead of the system include directory (typically /usr/include).
Using ``make``, you can add directories to the include search path using ``-I``.

.. seealso:: 

   :doc:`scope`

.. index:: call stack
   pair: functions; call stack
   pair: pointer; stack pointer
   pair: graph; call stack

The call stack
--------------
Functions are routinely called from many places
and more than one function can be 'active' at any one time.
The CPU needs a mechanism to keep track of every function call,
all function parameters, and local variables,
so that the CPU can execute each instruction in its proper order.

Some of this information will be stored in **registers**, 
memory locations built into the CPU itself, 
but most will go on the :term:`stack`, 
a region of memory that on typical machines grows downward, 
even though the most recent additions to the stack are called the “top” of the stack. 

.. graphviz::
   :align: center
   :alt: Typical program memory layout

   digraph memory {
     fontname = "Bitstream Vera Sans"
     label="Typical program memory layout"
     node [
        fontname = "Bitstream Vera Sans"
        fontsize = 11
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     mem [
        label = "{stack\n (grows down)|\n\n\nunused memory\n\n|\nfree store\n(grows up)|\nstatic data\n|\ncode\n(text area)}"
     ]

   }

Typically, each called function and any local variables, return values, or
parameters passed in, is stored in a special data structure called a **stack frame**
or an **activation record**.
Each function call pushes another activation record onto the stack.

The location of the top of the stack is stored in the CPU in a special register called the **stack pointer**.
So a typical function call looks like this internally:

#. The current instruction pointer or program counter value, 
   which gives the address of the next line of machine code to be executed, 
   is pushed onto the stack.
#. Any arguments to the function are copied either into specially designated 
   registers or onto new locations on the stack. 
   The exact rules for how to do this vary from one CPU architecture to the next, 
   but a typical convention might be that the first few arguments are copied 
   into registers and the rest (if any) go on the stack.
#. The instruction pointer is set to the first instruction in the code for the function.
#. The code for the function allocates additional space on the stack to hold its 
   local variables (if any) and to save copies of the values of any registers 
   it wants to use (so that it can restore their contents before returning to its caller).
#. The function body is executed until it hits a return statement.
#. Returning from the function is the reverse of invoking it: 
   
   - Any saved registers are popped back from the stack, 
   - The return value is copied to a standard register, 
   - The values of the instruction pointer and stack pointer are restored 
     to what they were before the function call.

From the programmer’s perspective, 
the important point is that both the arguments and the local variables inside a 
function are stored in freshly allocated locations that are thrown away after the function exits. 
After a function call the state of the CPU is restored to its previous state, 
except for the return value. 
Any arguments passed to a function are passed as copies by default,
so changing the values of the function arguments inside the function has no effect on the caller. 
Any information stored in local variables is lost.

.. admonition:: Try This!

   Read the code below and predict what the output should be **before** stepping through it.

   .. codelens:: functions_dig_deeper_cl
      :language: cpp

      #include <iostream>

      // forward function declarations
      void dig();
      void deeper();

      int main() {
        std::cout << "Programs always start in function main.\n";

        dig();

        std::cout << "Returned to main.\nexiting.";
        return 0;
      }

      void dig() {
        std::cout << "Digging...\n";
        deeper();
        std::cout << "Still digging...\n";
      }

      void deeper() {
        std::cout << "now even deeper....\n";
      }



-----

.. admonition:: More to Explore

  - `Basic intro to functions <https://www.youtube.com/watch?v=-87KQS-rZCA>`__
    from Buckys C++ Programming Tutorials.
  - From: cppreference.com: 
    `function declarations <http://en.cppreference.com/w/cpp/language/function>`_. 
  - cppplusplus.com tutorial on `functions <http://www.cplusplus.com/doc/tutorial/functions/>`_

