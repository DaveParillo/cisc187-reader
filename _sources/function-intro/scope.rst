..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. include:: <isonum.txt>

.. index:: scope

.. _variable-scope:

Scope
=====
Each name that appears in a C++ program is only valid in some *possibly discontiguous*
portion of the source code called its :term:`scope`.

Within a scope, 
unqualified name lookup can be used to associate the name with its declaration.

.. code-block:: cpp

   #include <cassert>

   int n = 3;                  // global variable

   int main() {
     int n = 42;               // local variable 
     assert (n == 42);         // local scope definition replaces the global
   }

   void func () {
     assert (n == 3);          // only name 'n' in scope is the global one
   }

It is important to remember that global variables are exactly that -- global.
They are visible everywhere in every scope.
Once created, there is no way to make a global variable go away.
And since there is only 1 "global scope" it is easy to accidentally create name
conflicts with variables in local scopes.
This is one of (but not only) reason why global variables are considered
something to avoid on most programming projects.

.. admonition:: Macro assert

   The ``assert`` macro from C is a simple way to validate
   something in your program that **must** be true before you
   proceed.
   To use the assert macro, ``#include <cassert>``,
   then call the function ``assert``.
   The assert function takes a boolean variable or
   an expression that evaluates to a ``bool``.

   Use the assert macro in your own code to validate function
   parameters or any other important checks.


In the following example, 
all of the assertions about ``n`` are ``true``:

.. activecode:: function_scope_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
   :nocodelens:

   #include <cassert>

   int n = 3;

   int main() {
     assert (n == 3);
     int n = 42;          // local n shadows global version
     assert (n == 42);

     // a new block scope can be created anywhere
     {
       double n = -3.14159;          // inner scope shadows both outer scopes
       assert (n - -3.1415 < 0.01);
     
     } // double n is no longer in scope 

     assert (n == 42);
   }

.. admonition:: Try This!

   Remove the braces that form the block scope around ``double n``.

   What do you expect to happen?

The global variable ``n`` is created before main is ever called and exists after main exists.
Global variables always exist for the entire lifetime of a program.
They are one of the few things in a program that outlive the ``main()`` function.

Global variables are created in the order they are encountered in a program.
Because global variables are stored in special memory locations.
If they are constants, they are stored in the ``code`` program segment.
If they are variable, they are stored in the ``data`` program segment.
Because these memory segments function like stacks, they are created and destroyed like stacks.
In the case of global variables, the first variable created will be the last variable destroyed.


One last mention about global variables: globals of primitive types are initialized by default.
This is not the same behavior as local variables, which are uninitialized by default.
The confusion about when variables are initialized is a common source of error.

.. index:: local variables

Local variables
---------------

You may read somewhere that global variables are evil, harmful, or whatever.
There are no *harmful* language features.

There *are* some language features that can get you into trouble if you have not
carefully weighed the pros and cons of their use.
That is why in this book, 
we generally like to avoid absolutes and to use *prefer*.

We *prefer* keeping scope to the absolute minimum to get something done.
Because we prefer keeping scope to a minimum, we *prefer*: 

- Local variables over global variables.
- Declaring variables in the block where they are used.

There is no reason in modern languages to declare all your variables at the start of a function.
This is actually a requirement of older languages like FORTRAN and the original K&R dialect of C.
In modern languages, it's an old habit some people have carried forward for no good reason.

Errors related to scope are common,
especially for beginning programmers who tend to rely more on 
global variables, or variables with more scope than needed.
For example, what is the output of the following?

.. code-block:: cpp

   #include <iostream>

   int main() {
     int i1;
     for (i1 = 0; i1 < 10; i1++) {
       std::cout << i1 << ' ';
     }
    std::cout << '\n';
     int i2;
     for (i2 = 0; i1 < 10; i2++) {
       std::cout << i2 << ' ';
     }
   }

.. reveal:: reveal-scope-1
   :showtitle: Show Answer
   :hidetitle: Hide

   If you guessed ``0 1 2 3 4 5 6 7 8 9`` , then you got it!

   Can you explain *why*?

   Hint:  What is the value of ``i2`` when the end of main is reached?

   What should be done to fix this program?

   .. admonition:: Try This!

      Change the preceeding program and put the declarations for 
      ``i1`` and ``i2`` in their respective ``for`` loops.  
      Don't make any other changes.

      What happens?

      Why is this better than the unmodified program?

      .. activecode:: function_scope_try_this_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++11']
         :nocodelens:

         #include <iostream>

         int main() {
           int i1;
           for (i1 = 0; i1 < 10; i1++) {
             std::cout << i1 << ' ';
           }
           std::cout << '\n';
           int i2;
           for (i2 = 0; i1 < 10; i2++) {
             std::cout << i2 << ' ';
           }
         }

Even a local variable can have too much scope, as in the preceding example.

One of the simplest things you can do as a programmer to improve the clarity and
maintainability of your code and reduce errors is to minimize the scope of local variables.
The most powerful technique for minimizing the scope of local variables
is to declare them where they are first used.

The more distance between the top of a function and the place
where a variable is actually used, the more important this advice is.
If a variable is initialized far from it's first use, the reader has
probably forgotten the initial value,
or even if the variable is local or global.

Long methods with dozens of local variable are part of the reason special
variable naming schemes became popular in some programming circles
in the 70's - 90's.
Some are still popular even today (Hungarian notation).
Generally, all of these systems attempt to compensate for confusion created by
poor design choices.

Declaring a variable too early creates the problems described earlier,
but also creates the problem of causing the scope to extend later than needed.
When a variable is declared before the block in which it is used,
it also exists after the block scope ends.

This is the problem with our two ``for`` loops in the previous example.

This is a classic :term:`semantic error`. 
The code compiles and runs, 
but does not produce the expected result.

One of the reasons we prefer ``for`` loops to ``while`` loops is that 
for loops allow us to initialize the loop variables within the for block.
While loops, in contrast, nearly always define a variable controlling the exit condition
outside the scope of the while block.

**Prefer initialized local variables to unitialized ones**.
Uninitialized variables are a common source of error.
If you code contains conditional logic or loops and the variable
is accessed in its uninitialized state only occasionally, 
the result can be bugs that are difficult to identify and fix.


-----

.. admonition:: More to Explore

  - From: cppreference.com: 
    :lang:`scope` and
    :lang:`initialization`

  - CPP Core guidelines:

    - :guidelines:`Keep scopes small <Res-scope>`
    - :guidelines:`Don’t introduce a variable (or constant) before you need to use it <Res-introduce>`
    - :guidelines:`Avoid non-const global variables <i2-avoid-non-const-global-variables>`
    - :guidelines:`Keep functions short and simple <f3-keep-functions-short-and-simple>`
    - :guidelines:`Express intent <p3-express-intent>`


