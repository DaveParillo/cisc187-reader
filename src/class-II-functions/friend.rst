..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: friend functions
   pair: functions; friend
   single: friend specifier

Friend vs non-friend functions
==============================
Some operators must be implemented as member functions,
``operator=``, ``operator[]``, and member access - 
both ``operator.`` and ``operator->>``,
because the language requires it.
We have choices where we define the others.

Some are commonly implemented as non-member functions,
because their left operand cannot be modified by you. 
The most prominent of these are the stream insertion and extraction operators.
The left operands are stream classes from the standard library which you cannot change.

For operators where you have to choose to either implement them as a
member function or a non-member function, 
use the following guidelines: 

#. If it is a **unary operator**, 
   then implement it as a **member** function.
   For example, ``operator++``.

#. If a binary operator treats both operands equally
   then implement as a **non-member** function.

   Generally, neither operand is modified in this situation.
   The relational operators all fall into this category.

#. If a binary operator does not treat both of its operands equally 
   then consider making it a member function.

   If the left-hand side operator is modified in the operation,
   or the function returns the ``this`` pointer, then
   it should be a member function of the left hand operand type.

   Otherwise, it can be implemented as a non-member function.

In the previous section, the relational operators were all declared as
*non-friend non-member* functions.
This is considered best practice by many programmers.

.. epigraph::

   Prefer writing non-friend non-member functions

   -- Item 44 of *C++ Coding Standards*, by Herb Sutter and Andrei Alexandrescu


Compare to the functionally similar friend, member overload
for ``operator==``:

.. code-block:: cpp

   friend bool operator==(const item& x, const item& y) {
     return x.value == y.value;
   }

- A non-friend function does not automatically know that a function is
  part of a class template unless told.

  This is why the non-friend functions repeat the template declaration
  from the ``struct``.

- The friend functions declared in the class are implicitly *inlined*.
  The compiler *may* replace function calls to these functions with
  in-line copies of the function body.
  The compiler is not obligated to do so, but usually does.

  To get the same behavior from non-member functions, the :lang:`inline`
  keyword is used.

- The ``friend`` keyword is often used to provide private member access to
  non-member functions.
  In the case of the ``item`` struct, this wasn't needed.

  The use of friend here prevents the ``this`` pointer from being passed
  to functions declared (and in this case defined) in the data structure
  body.


-----

.. admonition:: More to Explore

   - :lang:`friend` specifier
   - Item 44 from `C++ Coding Standards, Sutter and Alexandrescu, 2004. <https://www.google.com/search?client=safari&rls=en&q=isbn+978-0321113580>`__

