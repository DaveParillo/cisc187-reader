..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


Other pointer characteristics
=============================
This section wraps up pointers with a discussion of some
alternative constraints and special pointer types.

.. index:: const pointers
   pair: pointers; const
   pair: keyword; const

Constant pointers
-----------------

Pointers can be declared ``const``, just like any other type.
Where ``const`` appears controls what is held constant:

.. code-block:: cpp
  
    // odd whitespace to help see where const is used
          int         x = 5;
          int*       p1 = &x;  // non-const pointer to non-const int
    const int*       p2 = &x;  // non-const pointer to const int
          int* const p3 = &x;  // const pointer to non-const int
    const int* const p4 = &x;  // const pointer to const int

You may find it helpful to read pointer declarations from right to left.

- In ``p1``, nothing is constant.  Either the pointer or the value pointed to can change.
- In ``p2``, the pointer can change,  but the value pointed to is constant.
  You can't use this pointer to change the value of x.
- In ``p3``, the pointer is constant,  but the value pointed to can change.
  You can use this pointer to change the value of x, but can't point to a different variable.
- In ``p4``, both are held constant.

.. index:: nullptr

The ``nullptr`` type
--------------------

In section `Comparison with references`, 
we mentioned that unlike a reference,
a pointer might point to 'nothing'.

What exactly is 'nothing'?

Many languages refer to this 'nothing' as ``NULL``.

Prior to C++11, there was no unambiguous definition.
Typically the value 0 was used:

.. code-block:: cpp

  #define NULL 0LL

This definition carries over from standard C.

Using the value ``long long 0`` as an indicator for a null pointer created
several problems over the years in C++ programs.

Null pointers are the same type as regular integral types.

While it is unlikely that the number 0 could ever be confused with a valid address,
it creates problems regular old C never had to handle.
Specifically, C++ introduces function overloads,
which exposes the weakness in using an integral type for both
numbers and the concept ``NULL``.
For example:

.. code-block:: cpp

   #include <cstdio>
   #define NULL 0LL

   // Three overloads of f
   void f(int)   { puts("f(int)"); }
   void f(bool)  { puts("f(bool)"); }
   void f(void*) { puts("f(void*)"); }
 
   int main() {
     f(0);     // calls f(int) overload, not f(void*)
 
     f(NULL);  // might not compile, typically calls
               // f(int) overload.  
               // Never calls f(void*)
   }
   
The overload with ``f(NULL)`` is never called,
because ``NULL`` is not a pointer type.

C++ resolves this by creating a new type just to hold the null pointer.
The type is ``nullptr_t`` and the variable of that type is ``nullptr``.

.. code-block:: cpp

   #include <cstdio>

   // Three overloads of f
   void f(int)   { puts("f(int)"); }
   void f(bool)  { puts("f(bool)"); }
   void f(void*) { puts("f(void*)"); }
 
   int main() {
     f(0);        // calls f(int) overload as before
 
     f(nullptr);  // calls f(void*) overload
   }

The variable ``nullptr`` is a distinct type.
It is not a pointer type, pointer to member, integral type, size type, reference type,
or a member of any type group.
The ``nullptr`` **does** implicitly convert to a pointer type.

In short, using ``nullptr`` improves code clarity and correctness.
Using ``nullptr`` improves code clarity, especially when auto variables are involved.
Consider the following code example, from Effective Modern C++:

.. code-block:: cpp

   // A function that returns a pointer
   int* findRecord() {
     return nullptr;
   }

   int main() {
     // If you don’t happen to know (or can’t easily find out) what findRecord returns, 
     // it may not be clear whether result is a pointer type or an integral type. 
     //
     // After all, 0 (what result is tested against) could go either way. 

     {
       auto result = findRecord();

       if (result == 0) {
       }
     }

     // If you see the following, on the other hand ...
     {
       auto result = findRecord();

       if (result == nullptr) {
       }
       // there’s no ambiguity: result must be a pointer type.
     }

   }

``void`` pointers
-----------------

A *void pointer* is a
pointer to some memory, but the compiler doesn't know the type.

It is about as close to a raw machine address as you can get in C++.

Legitimate uses are
calls between functions in different languages or
templates where the provided value could literally be *anything*,
such as the actual implementation of ``new`` in C++.

.. admonition:: Important!

   ``void*`` is not the same as ``void``

   There are no objects of type void:

   .. code-block:: cpp

      int i;           // declare an int
      void x;          // error!  void is not a type
      void print();    // function returns nothing


**Any** pointer can be assigned to ``void*``:

.. code-block:: cpp
   :linenos:

   int*    i  = new int{5}; 
   double* x  = new double[10];
   int*    j  = i;             // OK: i and j are both int*
   void*   p1 = i;             // OK: assign int* to void*
   void*   p2 = d;             // OK: assign double* to void*

   int*    i2 = p1;            // error
                               // can't assign void* to int*

The last assignment is invalid, even though ``p1`` was last assigned an ``int*``.
A human reader knows the void pointer currently holds an int pointer,
but the compiler does not.

The compiler **can't** know the size of the value pointed to.
``void`` isn't a type, so it has no size:

.. code-block:: cpp

   int*    i = new int{5}; 
   void*   p = i;             // OK
   int*    j = p;             // error


To resolve this error, 
we have to give the compiler size information.
We can use one of C++ *casts* to convert ``void*``
to another pointer type that has a size:

.. code-block:: cpp

   int*    i = new int{5}; 
   void*   p = i;                    // OK
   //int*  j = p;                    // error
   int*    j = static_cast<int*>(p); // OK


-----

.. admonition:: More to Explore

   - From the ISO C++ FAQ: `Does "Const Fred* p" mean that *p can't change? <https://isocpp.org/wiki/faq/const-correctness#ptr-to-const-aliasing>`_
   - Effective Modern C++ by Scott Meyers `Item 8: Prefer nullptr to 0 and NULL <https://www.google.com/search?q=isbn+0636920033707>`_


