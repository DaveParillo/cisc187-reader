..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: pointers

Pointers
========

People make a big deal out of pointers.
They really aren't that hard to understand.
We already know that a variable stores some value:

.. code-block:: cpp
   
   double euler = 2.718281828459;

We use the name ``euler`` to retrieve the value.

A pointer is simply a variable that stores an *address*:

.. code-block:: cpp
   
   double* e_pointer = &euler;

The value assigned to ``e_pointer`` is the *address of* the variable ``euler``.

.. index:: 
   pair: graph; call stack

While some of the memory in a running program is stored in
a small number of **registers**, 
these live on the CPU chip and perform specialized functions like keeping track of the 
location of the next machine code instruction to execute.
Most of the memory of interest to programmers is **main memory**, 
which (mostly) lives outside the CPU chip and which stores the code and data of a running program. 
Main memory is partitioned within a program into the following areas, 
which we have seen in the section :doc:`../function-intro/functions`.

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

Each part of a program: functions, variables, and objects are stored in main memory and
each is assigned a unique address.
When the CPU wants to fetch a value from a particular location in main memory, 
it must supply the address.
Frequently, we don't need to concern ourselves with the address of a value.
Instead, we use a variable or function name and the 
CPU resolves the address for us.
Sometimes we need more control, and then we use **pointers** to store memory addresses
and manipulate them like any other variable.
In C++, 
they are defined as a family of types that can be passed as arguments, 
stored in variables, returned from functions, etc.

Declaring pointers
------------------

A pointer is defined by the operator ``*`` *and* a **type**.
Both are required because a pointer can be thought of as a compound type.
The ``*`` declares that the system should store an initial memory address, not a value.
The type instructs the system how many bytes after the initial location
need to be allocated for storage of the value pointed to.
``int* int_pointer;`` defines a new, uninitialized pointer to an ``int``.

Both 
``int * int_pointer;`` and ``int *int_pointer;`` 
declare the exact same variable.
White space does not matter and the last variation is common.
Personally, I prefer ``int* p``, 
because it emphasizes (for me) that the *type*
is *integer pointer*.
Declarations of pointers to other fundamental types follow a similar pattern:

``double* dbl_pointer;`` is an uninitialized pointer to a ``double``.
 
``char* char_ptr;`` is an uninitialized pointer to a ``char``.

Each of these declarations creates a variable of either 4 or 8 bytes, depending on the architecture.
On any given CPU all pointers are the same size, regardless of what they point to - 
because the **only** thing a pointer ever stores is an address.
The pointer variable stores a specific memory location (the address) and the *value*
associated with the pointer is stored in one or more bytes starting at the pointer
address.

Like any other variable in C++, 
an uninitialized pointer will initially contain garbage --- in this case, 
the address of a location that might or might not contain something important. 
To initialize a pointer, 
you assign it the address of something that already exists.
If you already have an object, you can use the **address of operator** ``&``:

.. code-block:: cpp

   int main() {
     int n = 5; // a stack int
     int* p;    // a pointer to an int
     p = &n;    // p now points to n
   }

As you might expect, you do not need to declare pointers uninitialized.
You can declare and initialize in a single step.
Once you have an initialized pointer, use the **dereference operator** ``*``
to get the value stored in the pointer, or to assign a new value.


.. code-block:: cpp

   int main() {
      int x  = 10;
      int* p = &x;    // assign the address of x to p
      *p     = 7;     // x is now 7, p is unchanged

      int x2  = *p;   // assign the value of x to new int x2
      int* p2 = &x2;  // get a pointer to another int

      p2 = p;         // p2 and p both point to x
      p  = &x2;       // make p point to another object
   }


The equivalent example for references is:

.. code-block:: cpp

   int main() {
      int y  = 10;
      int& r = y;    // the & is in the type, not in the initializer
      r      = 7;    // assign to y through reference r

      int  y2 = r;   // read y through r (no * needed)
      int& r2 = y2;  // get a reference to another int

      r2  = r;       // the value of y is assigned to y2 
      //r = &y2;     // error: you can't change the value of a reference
                     //   (no assignment from int* to an int&)
   }

-----

.. admonition:: More to Explore

   - `MyCodeSchool <http://www.mycodeschool.com>`__ video: 
     `Pointers in C/C++ playlist <https://www.youtube.com/playlist?list=PL2_aWCzGMAwLZp6LMUKI3cc7pgGsasm2_>`__ 


