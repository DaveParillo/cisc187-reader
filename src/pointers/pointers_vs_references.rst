..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: pointers; references

Comparison with references
==========================

Recall from our earlier discussions of pass by reference
that the ``address of`` operator ``&`` allows us to pass by reference:

.. code-block:: cpp
   :linenos:

   #include <iostream>

   void by_value(int x) {
     x = 99;
     std::cout << "in by_value the address of x is " 
               << &x << '\n';
   }

   void by_reference (int& x) {
     std::cout << "in by_ref the address of x is   " 
               << &x << '\n';
     x = -1;
   } 

In function ``by_value`` the statement ``x = 99;`` changes the copy provided.
The value of ``x`` is printed, but is destroyed when ``x`` goes out of scope on line 6.

No special character is needed if you want to use a function that takes a reference:

.. code-block:: cpp

   #include <iostream>

   int main () {
     int beta = 11;
     std::cout << "the address of beta is " 
               << &beta << '\n';
 
     by_value(beta);

     std::cout << "beta = " << beta << '\n';

     by_reference(beta);

     std::cout << "beta is now " 
               << beta << '\n';
   }

References do have some definite advantages:

- A reference must always be initialized using an existing object.
  In other words, a reference can **never** be ``null``.
- A reference can't be reassigned to a different object
- A ``const`` reference means you can't modify the thing the reference refers to
- References are simpler, more limited, and inherently safer than pointers

However, there are important things you can't do with references:

- You can't assign an address to a reference

  - This would have the effect of having a reference refer to a different object
  - The technical term for this is that references are not **assignable**

- You can't operate on a reference

  - In other words, you can't increment the referred to memory address,
    which, by definition, would involve having the reference refer to a different object

- You can't use a single reference to refer to more than one object
- You can't use references in containers such as ``vector``

  - Containers can only hold *assignable* entities

We still need to be able to do all these kinds of memory manipulations.
In C++, we achieve these goals using *pointers*.

Function passing semantics
--------------------------
We can pass pointers to a function that expects a reference: 

.. code-block:: cpp

   #include <cassert>

   void by_reference (int& x) {
     x = -1;
   }

   int main() {
     int  i = 5;
     int* p = &i;
     by_reference(p);
     assert (i == -1);
     return 0;
   }


If we pass in only ``p``, what happens?

.. tb-reveal::
   :name: reveal-skill-check
   :showlabel: Show Answer

   The program fails to compile.

   We can't pass an ``int*`` to a function expecting an ``int&``.


.. admonition:: Non-const references vs. pointers

   Some programmers consider passing by non-const reference bad style,
   because the call syntax is the same as pass by value.
   When a variable is passed into a function by non-const reference
   there is no visual indication to the programmer of what to expect.
   Without reading additional documentation or
   reading the source code, 
   there is no way to know if the function will change its parameter or not.

   .. code-block:: cpp

      void func (int& x);

      int main() {
        int x = 5;
        func(x);       // will x change?
      }


   For this reason, a function that takes a *non-owning pointer* is preferred:

   .. code-block:: cpp

      void func (int* x);
    
      int main() {
        int x = 5;
        func(&x);       // Caller expects x to change
      }

   A function signature is a *contract* between the function author and
   the function caller.
   A function that takes non-const references represents a poorly written contract.
   Callers don't know what to expect when the function is called.
   Even if the parameter isn't changed today, it might tomorrow.
   A non-owning pointer makes the intent clear.
   There is still no *requirement* to change the parameter,
   but since the caller is explicitly passing in an address, 
   they can expect it to change.


-----

.. admonition:: More to Explore

   - `MyCodeSchool <http://www.mycodeschool.com>`__ video: 
     `Pointers in C/C++ playlist <https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_>`__ 


