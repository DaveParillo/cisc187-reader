..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
..  Some of the content in this section is adapted from
    http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
   
.. index:: static functions

Static functions and variables
==============================
By default, all functions are global; 
they can be used in any file of your program whether or not a declaration appears in a header file. 
To limit access to the
current file, declare a function or variable ``static``, like this:

.. code-block:: cpp

   // assume all these definitions are in a single file "foo.cpp"

   // static variable used by non-static functions
   static bool verbose = false;

   bool is_verbose() {
     return verbose;
   }

   // vprint could reside in another file
   void vprint (std::string message) {
     if (is_verbose()) {
       std::cout << message << '\n';
     }
   }
   // this function only works if it is the same file
   // as the one where verbose is defined
   void verbose_print (std::string message) {
     if (verbose) {
       std::cout << message << '\n';
     }
   }

   // local static function can only be called in this compilation unit
   static void helloHelper(void) {
     puts("hi!");
   }

   // anyone can call `hello`
   void hello(int repetitions) {
     for(int i = 0; i < repetitions; ++i) {
       helloHelper();
     }
   }

Similar to file static functions and variables, 
the keyword ``static`` can also be used inside functions.
Static variables are initialized only the first time the function is called,
for example:

.. code-block:: cpp


   size_t counter() {
     static size_t count = 0;
     return ++count;
   }

The first time ``counter`` is called, 
the variable ``count`` is initialized to zero.
Each call thereafter, ``count`` is increased by 1 and the new value is returned.

Another appropriate use of static variable in functions:
when defining a constant that should only be initialized once.
For example, our earlier ``too_small`` function, could be:

.. code-block:: cpp

   #include "area.h"

   bool too_small (int x, int y) {
     static const int min_size = 10;
     return area(x, y) < min_size; 
   }


Under very rare circumstances,
it may be useful to have a variable local to a function that persists from one function call to the next.
You can do so by declaring the variable static.
For example, here is a function that counts how many times it has been called:

.. code-block:: cpp

   // return the number of times the function has been called
   int counter(void) {
     static count = 0;
     return ++count; 
   }

Static local variables are stored in the same memory space as global variables. 
But they are only visible inside the function that declares them. 
This makes them slightly less troublesome than global variables;
there is no fear that some unrelated code elsewhere will quietly change their value.
Static variables are rarely used in practice, however,
because they do not work well in multi-threaded applications.


.. index::
   pair: namespace; anonymous

Anonymous namespaces
--------------------
It is possible to define a namespace without a name.
Unnamed namespace members have potential scope 
from their point of declaration to the **end of the translation unit**.

In other words, they behave a bit like global variables, 
visible to all functions, but *only* within the source file
where the namespace is defined.

Unnamed (or anonymous) namespaces are considered a 'modern'
C++ alternative to declaring variables as ``static``
within a translation unit.

.. code-block:: cpp


   static int i;

   // anonymous namespace
   namespace {
     int i;
   }

At one point the C++ standards committee planned to deprecate the use
of ``static`` in this way and force the use of namespaces,
but that decision was reversed in 2009.

Unnamed namespaces are preferred over the use of the keyword static
for several reasons:

- The ``static`` keyword can have different meanings depending on context

  Namespaces only have one purpose: to define and enclose a scope.

  Namespaces provide a uniform and consistent way of controlling visibility.
  You don't have to use different tools for the same thing.

- A namespace can encapsulate anything.
  Only functions and objects can be declared static.

  User defined types, which is the focus of the second half of this course
  cannot be declared static.


   .. code-block:: cpp

      // valid statements
      static void my_function() { /* function body */ }
      static int  my_variable;

      // invalid
      static class sample_class { /* class body */ };
      static struct sample_struct { /* struct body */ };

      // valid
      namespace 
      {  
        class sample_class { /* class body */ };
        struct sample_struct { /* struct body */ };
      }


- When using an anonymous namespace, 
  the function/object name is mangled properly, 
  which allows you to see something like "(unique namespace)::xyz" 
  in the symbol table after de-mangling, 
  and not just "xyz" with static linkage.




.. tb-group::
   :name: anon_namespace_tab

   .. tb-tab:: Example

      At compile time,
      This definition is treated as a definition of a namespace with a
      unique name and a using-directive in the current scope.


      .. code-block:: cpp

         namespace {
           int i;       // defines ::(unique)::i
         }

      The unique name of the namespace is hidden.
      Since it is not known, no code outside the current
      translation unit can access it.

      It is technically possible to have more than one unnamed
      namespace in the same translation unit.

      .. code-block:: cpp

         namespace {
           int i;       // defines ::(unique)::i
         }

         namespace A {
             namespace {
                 // reusing the name 'i' in this scope is a bad idea . . .
                 int i; // A::(unique)::i
                 int j; // A::(unique)::j
             }
             void g() { i++; } // A::unique::i++
         }

      As a best practice, you should keep unnamed namespaces to a minumum
      and declare them near the top of your translation unit
      so that they stand out.


   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: ac_anon_namespace_1

         #include <iostream>

         namespace {
           int i = 0;       // defines ::(unique)::i
         }

         void f() {
           ++i;         // increments ::(unique)::i
         }

         namespace A {
           namespace {
             // reusing the name 'i' in this scope is a bad idea . . .
             int i = 3;          // A::(unique)::i
             int j = 5;          // A::(unique)::j
           }
           void g() { ++i; } // A::unique::i++
         }

         using namespace A;  // introduces all names from A into global namespace

         void h() {
           // error: ::(unique)::i and ::A::(unique)::i are both in scope
           // i++;

           A::i++; // ok, increments ::A::(unique)::i
           j++;    // ok, increments ::A::(unique)::j
           f();
         }

         int main() {
         }




-----

.. admonition:: More to Explore

  - From: cppreference.com: 

    - :lang:`Function declarations <function>`
    - :lang:`Storage class specifiers <storage_duration>`
    - :lang:`Namespace declarations <namespace>` and 
      :lang:`Namespace aliases <namespace_alias>`

