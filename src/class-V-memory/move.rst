..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: moving memory
   single: std::move
   single: move semantics
   single: std::swap

Moving memory
=============
In the section on 
:doc:`../class-II-functions/overloads` we briefly covered the 
:algorithm:`std::swap <swap>` algorithm.
The implementation of swap for built in types is trivially
implemented:

.. code-block:: cpp

   void swap(int& a, int& b)
   {
      auto temp = a;
      a = b;
      b = temp;
   }

However, even though ``a`` and ``b`` are both passed by
non-const reference, this is still an expensive function to call
for any type that is large or expensive to copy.

C++11 adds facilities that give programmers tools to replace expensive copies
with moves.
In C++11, if the right hand side of an expression is an :term:`rvalue` and
if the object supports moving, then moving memory is performed instead of
copying memory.
Given a potentially large type, such as :container:`vector`, we can re-write
the swap algorithm in terms of moves

.. code-block:: cpp

   void swap(vector<string>& a, vector<string>& b)
   {
      auto temp = static_cast<vector<string>&&>(a); // cast to rvalue reference
      a = static_cast<vector<string>&&>(b);
      b = static_cast<vector<string>&&>(temp);
   }

Casting manually to a rvalue reference is ugly and awkward.
Simplifying this expression is the motivation behind :utility:`move`:

.. code-block:: cpp

   void swap(vector<string>& a, vector<string>& b)
   {
      auto temp = std::move(a); // cast to rvalue reference
      a = std::move(b);
      b = std::move(temp);
   }

The ``move`` function simply converts it's parameter into rvalue reference,
and marks the object as being ready for a 'move'.
Using ``std::move`` is exactly the same as using a static cast to
an rvalue reference.

Just a moment ago, we mentioned a big 'if' regarding moves.
We said 

   ... if the object supports moving ... 

How do we create objects that support moving?

With a move constructor.

.. index:: move constructor
   single: move assignment

Move constructors and move assignment
-------------------------------------
A move constructor is a constructor of the form:

.. code-block:: cpp

   class_name (class_name&&);

Note that the parameter to the constructor is not a constant.
This is done for the same reasons swap functions take non-const references.
We pass non-constant rvalue references to our move constructors
so that we can exchange our current (empty) object for the one provided.


.. code-block:: cpp

   X::X (X&& other)
   {
     // exchange content between other and this
   }


The move assignment operator is similar to copy assignment,
but with the now familiar rvalue reference parameter:

.. code-block:: cpp

   X& X::operator=(X&& rhs)
   {
     // exchange content between other and this
     return *this;
   }

   // Given 2 objects
   X a,b;
   // do something to b

   // We can copy them
   a = b;


   // Or force a move
   a = std::move(b);


As always we need to be concerned with what to do if our object 
manages its own resources.
If class ``X`` has, for example, data on the free store,
then we need to ensure any resources that might create side effects
are addressed when we use move assignment.

If move semantics are implemented as a simple swap, 
then the effect of this is that the objects held by ``a`` and ``b`` are 
being exchanged between ``a`` and ``b``.
Nothing is being destructed yet.
The object formerly held by ``b`` will of course be destructed eventually -
when ``b`` goes out of scope.
But if ``a`` also becomes the target of a move,
then the object formerly held by ``a`` gets passed on again.
As far as the implementer of the assignment operator is concerned,
it is not known when the object will be destructed.

So we have a small problem that needs to be fixed.
A variable has been assigned to,
but the object formerly held by that variable is still out there somewhere.
Any part of an object's destruction that has side effects should be performed
explicitly in the rvalue reference overload of the assignment operator:

.. code-block:: cpp

   X& X::operator=(X&& rhs)
   {
     // Perform a cleanup that takes care of at least those parts of the
     // destructor that have side effects. Be sure to leave the object
     // in a destructible and assignable state.

     // exchange content between other and this
   }


-----

.. admonition:: More to Explore

   - :lang:`Move constructors <move_constructor>`
   - The :algorithm:`std::swap <swap>` algorithm
   - `C++ Rvalue references explained <https://web.archive.org/web/20240325000934/http://thbecker.net/articles/rvalue_references/section_01.html>`__
     The content in this section was adapted from *Rvalue References Explained*, by Thomas Becker.
   - `Copy and Swap, 20 years later <https://mropert.github.io/2019/01/07/copy_swap_20_years/>`__
     a deeper dive into some of the tradeoffs of different implementations of copy and move
     assignment.


