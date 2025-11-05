..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: rvalues
   single: lvalues
   single: rvalue references

Lvalues, rvalues, and references
================================
In addition to the builtin types and pointers,
C++ adds a new type - the reference type.
A major addition to C++11 is the addition of the
*rvalue reference*.
It is easier to understand rvalue references if we discuss
lthe others first.

The original definition of lvalues and rvalues from C is as follows:

- An **lvalue** is an expression that may appear on the left or
  on the right side of an assignment
- An **rvalue** is an expression that can only appear on the
  right hand side of an assignment. For example,

  .. code-block:: cpp

     int a = 42;
     int b = 43;

     // a and b are both l-values:
     // these are all OK
     a = b;
     b = a;
     a = a * b;

     // a * b is an rvalue:
     int c = a * b; // ok, rvalue on right hand side of assignment
     a * b = 42;    // error, rvalue on left hand side of assignment

In C++, this is still useful as an intuitive view to lvalues and rvalues.
However, C++ with its user-defined types introduces some subtleties
regarding modifiability and assignability that cause this definition to be incorrect. 

An **lvalue** is an expression that identifies a non-temporary object.
For example:

  .. code-block:: cpp

     // These are all valid assignments
     int i = 42;
     i = 43;              // i is an lvalue
     int* p = &i;         // i is an lvalue
     int& foo();
     foo() = 42;          // foo() is an lvalue
     int* p1 = &foo();    // foo() is an lvalue


An **rvalue** is an expression that identifies a temporary object
or a literal not assigned a memory address.
For example:

  .. code-block:: cpp
  
     // valid assignments
     int bar();
     int j = 0;
     j = bar();     // bar() is an rvalue
     j = 42;        // ok, 42 is an rvalue

     // invalid
     int* p2 = &bar(); // cannot take the address of an rvalue

An **rvalue reference** is a reference to an *rvalue*.
That is, a reference to a *temporary object* or
a reference to a literal not assigned a memory address.
As we will see in the next section,
rvalue references are a key component of move operations and
forwarding data to another location without copying it.

If ``X`` is any type, then ``X&&`` is called an *rvalue reference to X*.
To distinguish from ordinary references,
the reference ``X&`` is now also called an *lvalue reference*.
An rvalue reference is a type that behaves like the ordinary reference ``X&``,
but there are several thing to look out for.
During function overload resolution,
lvalues will prefer function signatures containing lvalue references,
and rvalues prefer the new rvalue references:

.. code-block:: cpp

   void foo(X& x);  // lvalue reference overload
   void foo(X&& x); // rvalue reference overload

   X x;
   X foobar();

   foo(x); // argument is lvalue: calls foo(X&)
   foo(foobar()); // argument is rvalue: calls foo(X&&)


-----

.. admonition:: More to Explore

   - :lang:`Reference declarations <reference>`


The content in this section was adapted from *Rvalue References Explained*, by Thomas Becker.


