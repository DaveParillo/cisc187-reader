..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: const class functions

``const`` member functions
==========================
We have :doc:`previously mentioned <../function-intro/constants>` uses for ``const``,
and classes add another situation where the const keyword can be used.

An object can be created with the ``const`` *cv qualifier*, 
just like any other type:

.. code-block:: cpp

   const int x = 3;

   const fibonacci foo = {5, 8, 13};


When created ``const``, then no changes are allowed to the object.
It is OK to call a *non-modifying member function*.

How does the compiler know that a function is a non-modifying member function?
When the function is declared as ``const``.

Create a const member function by inserting the const keyword after the
parameter list and before the function body:

.. code-block:: cpp

   bool verbose() const {
     return true;
   }

Here ``const`` tells the compiler this function **will not change** the object state.

It is a *promise*.
If a ``const`` function attempts to change **any** class member, 
then a compile error results.

.. note::

   Only class member functions can be marked ``const``.

   Attempting to mark a free function as ``const`` is a compile error.

Because ``const`` changes which objects can call a member function,
it is part of the member function signature.
This means a class can provide both a ``const`` and non-``const`` version
of the same function.

.. admonition:: Why is this important?

   A ``const`` object can only call ``const`` member functions.
   Any attempt to call a non-``const`` member function is a
   compile error.

.. tb-code:: cpp
   :name: const-overload-example
   :caption: Const and non-const member function overloads

   #include <iostream>
   #include <string>
   #include <utility>

   class dog {
     std::string name_;

   public:
     explicit dog(std::string name)
       : name_{std::move(name)}
     {
     }

     std::string& name() {
       return name_;
     }

     const std::string& name() const {
       return name_;
     }
   };

   int main() {
     dog rover{"Rover"};
     const dog fido{"Fido"};

     rover.name() = "Spot";

     std::cout << "non-const dog: " << rover.name() << '\n';
     std::cout << "const dog: " << fido.name() << '\n';
   }

The two ``name`` functions have the same name and the same parameter list.
The trailing ``const`` makes them different member function signatures.
When the object is not ``const``, overload resolution chooses the
non-``const`` version, which returns a modifiable reference.
When the object is ``const``, overload resolution chooses the ``const`` version,
which returns a reference that cannot be used to modify the object.

.. tb-choice::
   :name: mc-ex-4

   Given the following:

   .. code-block:: cpp

      #include <iostream>

      class counter {
        int value_ = 0;

      public:
        counter() = default;

        void set_value(int value) {
          value_ = value;
        }

        int value() const {
          return value_;
        }
      };

      int main() {
        const counter count;
        count.set_value(13);
        std::cout << count.value() << '\n';
      }

   What is the output? Choose the **one** correct answer.

   - Program prints ``13``

     - It cannot print 13 because ``set_value`` cannot be called on a ``const`` object.

   - Does not compile

     + Calling a non-const function of an object declared ``const`` is a compile error.

   - Program runs, but does not reach the end of main

     - The program cannot run

   - Program behavior is undefined 

     - The program doesn't get this far. We know exactly what will happen.




-----

.. admonition:: More to Explore

   - From cppreference.com

     - :lang:`Const and volatile type qualifiers <cv>`.
     - :lang:`Const member functions <member_functions>`.
