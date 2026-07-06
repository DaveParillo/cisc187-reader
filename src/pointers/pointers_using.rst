..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: pointer operations
   pair: pointers; using

Using pointers
==============
The simplest way to use a pointer is to get their value as with any other variable. 
This value will be an address, 
which can be stored in another pointer variable of the same type.

.. code-block:: cpp

   int n = 2;
   int* p = &n;  // points to n
   int* q = p;   // points to n also


Once a pointer has been dereferenced, it is treated exactly like any other variable of that type.

.. code-block:: cpp

   *p = *p + *q; // n = 4

Pointers support many of the same operations as other arithmetic types.

+--------------+--------------------------------------------------------+
| Operation    |  Result                                                |
+==============+========================================================+
| ``p == q``   | ``true`` if and only if ``p`` and ``q``                |
|              | both store the same address or the ``nullptr`` type    |
+--------------+--------------------------------------------------------+
| ``p != q``   | negation of above                                      |
+--------------+--------------------------------------------------------+
| ``*p``       | refers to the value pointed to by ``p``                |
+--------------+--------------------------------------------------------+
| ``*p = val`` | writes ``val`` to the storage location                 |
|              | pointed to by ``p``                                    |
+--------------+--------------------------------------------------------+
| ``val = *p`` | reads from the location pointed to by ``p`` and        |
|              | writes to ``val``                                      |
+--------------+--------------------------------------------------------+
| ``++p``      | increment the pointer, making it point to the next     |
| ``p++``      | memory address after ``p``                             |
+--------------+--------------------------------------------------------+
| ``p = p+x``  | add the integral value ``x`` to the pointer making it  |
|              | point to ``x`` memory addresses after ``p``            |
+--------------+--------------------------------------------------------+
| ``--p``      | decrement the pointer, making it point to the previous |
| ``p--``      | memory address before ``p``                            |
+--------------+--------------------------------------------------------+
| ``p = p-x``  | subtract ``x`` from ``p`` making it                    |
|              | point to ``x`` memory addresses before ``p``           |
+--------------+--------------------------------------------------------+

The ``*`` operator binds very tightly, in other words,
is it has high *precedence*.
You can usually use ``*p`` anywhere you could use the variable it points to 
without worrying about parentheses. 
However, a few operators, 
such as the unary decrement and increment (``--`` and ``++``) operators, 
and the member of (``.``) operator used to unpack structs and classes, 
all have higher precedence. 
These require parentheses if you want the ``*`` to take precedence.

.. tb-code:: cpp
   :name: pointers_using_intro_cl
   :show-tutor:
   :caption: Using pointers

   #include <iostream>
   int main() {
     int n = 2;
     int* p = &n;  // points to n
     int* q = p;   // points to n also
     *p = *p + *q; // n = 4
     std::cout << "n = " << n << '\n';

     int* p2n = &n;  // another pointer to n
     (*p)++; // increments n
     std::cout << "n = " << n << '\n';
     std::cout << "* p = " << * p << '\n';
     *p++;   // increments p
             // p now points to next address in memory
             // Almost always an error
     std::cout << "* p = " << * p << '\n';

     return 0;
   }

Unlike the fundamental types in C++,
pointer types do not implicitly convert to other types.
While we expect to be able to assign an int to a double,
it is a compile error to assign an int pointer to a double pointer:

.. code-block:: cpp
   
   int    i = 5;
   double d = i;     // OK.  implicit widening conversion

   int*    pi = &i;
   double* di = pi;  // compile error

-----

.. admonition:: More to Explore

   - :lang:`Operator Precedence<operator_precedence>`
   - From the ISO C++ FAQ: `Does "Const Fred* p" mean that *p can't change? <https://isocpp.org/wiki/faq/const-correctness#ptr-to-const-aliasing>`_


