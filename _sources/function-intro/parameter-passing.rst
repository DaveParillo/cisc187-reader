..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
..  Some of the content in this section is adapted from
    http://www.cs.yale.edu/homes/aspnes/classes/223/notes.html
   
.. index:: 
   pair: functions; passing parameters
   single: pass by value
   pair: parameter passing; by value

Passing parameters
==================
In C and C++, parameter passing defaults to **pass by value**.
Unless you specify otherwise,
function parameters are initialized with *copies* of the actual arguments, 
and function callers get back a *copy* of the value returned by the function.
Pass by value is the simplest way to get data into and out of functions.

.. code-block:: cpp

   void printFavorite(int x) {
     // 'x' is a copy of 'favorite'
     std::cout << "my favorite number is " << x << '\n';
   }

   int main() {
     int favorite = 72;
     printFavorite(favorite);
   }


The important point is that two copies of my favorite number are stored.
The one declared in main, ``favorite``, and
the one declared in printFavorite, ``x``.
The parameter ``x`` is initialized using the value of ``favorite`` in main.

.. codelens:: function_parameter_pass_cl1
   :language: cpp

   #include <iostream>

   // define the function
   void printFavorite(int x) {
     std::cout << "my favorite number is " << x << '\n';
   }

   int main() {
     int favorite = 72;
     printFavorite(favorite);
     return 0;
   }


More than one parameter can be passed.
For example, 
a function to add two numbers makes copies of both parameters
adds them together and returns a result, which is also copied.

Step through this example and see how the copies of both local variables and
return values are managed on the stack.

.. codelens:: function_parameter_pass_cl2
   :language: cpp

   #include <iostream>

   // This function takes two parameters.
   int add_numbers(int x, int y){
     int answer = x + y;
     return answer;
   }

   int main() {
     int a = 13;
     int b = 21;
     int sum = add_numbers(a, b);
     std::cout << sum << '\n';
     return 0;
   }

One benefit of pass by value is that local changes to parameters
do not impact the caller.
That is, the caller can trust their data has not been modified.

.. activecode:: function_pass_by_value_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
   :nocodelens:

   #include <iostream>
   #include <string>

   void print_n (const std::string message, int repeat) {
     while (repeat > 0) {
       std::cout << message << '\n';
       --repeat;
     }
   }

   int main() {
     int n = 3;
     print_n ("hello, world", n);
     std::cout << "n = " << n;
   }

.. index:: 
   single: pass by reference
   pair: parameter passing; by reference

For large / complex data types, however, pass by value becomes expensive even in small programs.
An alternative to pass by value, is called **pass by reference**.
The function parameter passed into the function is still a new variable.
That does not change.
However, rather than passing a *copy* of the entire object, 
instead we *bind the address* of the original object to a new variable.
Only the object reference is passed to the function.

.. tabbed:: pointer_vs_ref_tabbed

   .. tab:: Pointers and References

      In this respect, a reference behaves much like a ``const pointer``.

      - Both require an initial value in order to compile
      - Neither can refer to (or point to) a different object

      .. code-block:: cpp

         int  n = 3;          // typical int declaration
         int  m = 5;

         int& a = n;          // a refers to n
         int* p = &n;         // p points to n, 
                              // but could point to something else

         int* const p2 = &m;  // p2 point to m and can only point there


      The following are compile errors:

      .. code-block:: cpp

         int& b;              // a reference that doesn't refer to anything
         p2 = &n;             // attempt to change what a const pointer points to

      If the pointer comparison is confusing, do not worry.
      We will delve more deeply into pointers soon,
      this is just for comparison for those people who have an introduction
      into pointers.


   .. tab:: Run It


      .. activecode:: function_intro_reference_vs_pointer_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>

         int main() {
           int  n = 3;          // typical int declaration
           int  m = 5;

           int& a = n;          // a refers to n
           int& b = m;          // b refers to m
             
           int* p = &n;         // p points to n, 
                                // but could point to something else
             
           int* const p2 = &m;  // p2 points to m and can only point there


           // any use of a is equivalent to thing the variable
           // that a refers to
           a = b;
           std::cout << "n = " << n << '\n';
             
           a = 0;
             
           p = &m;       // OK
           //p2 = &n;   // compile error

           std::cout << "n = " << n << '\n'
                     << "m = " << m << '\n'
                     << "a = " << a << '\n'
                     << "b = " << b << '\n'
                     << "p = " << * p << '\n'
                     << "p2 = " << * p2 << '\n';
         }

               


We use the *address of operator* ``&`` to declare that only the address of the 
variable is passed, rather than a copy.
The primary advantage is that since all addresses are the same size,
the cost of passing is the same, 
regardless of how large the object is.

Understanding references is critical to understanding how C++11 and
later version of the language function.
References are a major new language feature and we will be using them
often from now on.

.. admonition:: Try This!

   Modify the ``print_n`` function signature so that 
   the variable ``repeat`` is a **reference** instead of a copy.

   .. activecode:: function_pass_by_ref_ac
      :language: cpp
      :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
      :nocodelens:


      #include <cassert>
      #include <iostream>
      #include <string>

      void print_n (const std::string message, int repeat) {
        while (repeat > 0) {
          std::cout << message << '\n';
          --repeat;
        }
      }


      int main() {
        int n = 3;
        print_n ("hello, world", n);
        std::cout << "n = " << n;

        assert ( n == 0 );        // program terminates if false
      }

A common source of confusion when starting out with references is
keeping the ``operator&`` straight.

The meaning of this operator depends on how it is used.

On the left-hand side of an assignment,
or in function parameters, ``&`` **always** defines a 
reference to a type:

.. code-block:: cpp

   int& a = 3;
   const int& cr(a);     // cr refers to a, 
                         // but we can't change the value of a using cr

   void show_usage (std::string& message);

   const double& pi = 3.1415926;

On the right-hand side of an assignment,
``&`` **almost always** means address of a variable.
The only exception is when casting to a reference type:

.. code-block:: cpp

   int n = 3;
   int* p = &n;      // p points to the address of the variable n

   const int& cr(a);     // const reference

   // cast away the 'const' part of cr
   int& r2 = const_cast<int&>(cr);


In the last code block, notice that both ``cr`` and ``r2`` refer to ``a``,
however, ``r2`` can change the value of ``a`` because we cast away the ``const``
modifier that was part of ``cr``.

Although the language allows casting away ``const`` like this,
you should use this feature very sparingly.


There is a lot going on in the following program.
You should step through this code and make sure you
understand what is happening to the variables in ``main``
and the functions called from ``main``.

   .. codelens:: function_parameter_pass_by_ref_cl
      :language: cpp

      #include <iostream>
      
      // A copy of x is passed to this function.
      // Changes to x are not reflected in the caller.
      void by_value(int x) {
        std::cout << "in by_val the address of x is   " << &x << '\n';
        x = 99;
      }

      // A reference to x is passed to this function.
      // Changes to x are not reflected in the caller.
      void by_reference (int& x) {
        std::cout << "in by_ref the address of x is   " << &x << '\n';
        x = -1;
      }

      int main () {
        auto alpha = 11;
        auto beta = 11;

        std::cout << "in main the address of alpha is " << &alpha << '\n';
        std::cout << "in main the address of beta is  " << &beta << '\n';

        by_value(alpha);
        by_reference(beta);

        std::cout << "alpha is now " << alpha << '\n';
        std::cout << "beta is now " << beta << '\n';
        return 0;
      }

.. tabbed:: tabbed-skill-check-functions

   .. tab:: Q1

      Given the following program:

      .. code-block:: cpp
         :linenos:

         #include <iostream>

         int change_and_add(int &a, int &b) {
           a = 3;
           b = 4;
           return a + b;
         }

         int main() {
           int a = 1;
           int b = 2;
           int c = change_and_add(a, a);
           std::cout << a << b << c;
         }

      .. fillintheblank:: fib_param_1

         What is the output from this program?

         - :428: Correct.
           :123: The variable a is modified in this program.
           :437: The variable b is never modified in this program.
           :427: Variable a is modified <em>twice</em> before the addition is performed.
           :.*: What is passed to the function change_and_add? What changes? What doesn't?


-----

.. admonition:: More to Explore

  - :lang:`Reference initialization <reference_initialization>`
  - :lang:`const_cast conversion <const_cast>`
  - :lang:`Value categories <value_category>`

