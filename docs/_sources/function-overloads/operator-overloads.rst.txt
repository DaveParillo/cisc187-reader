..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: functions; operator overloads

Operator overloads
==================
Very few languages allow overloading basic operators.
In this section, we won't discuss all possible overloading,
but we are introducing some of the more common overloads that
generally are implemented as ordinary 'free' functions.

In C++, operators are overloaded in the form of functions with special names. 
For example, ``a+b`` and ``operator+(a,b)`` both call
the same function.

Most C++ operators can be overloaded.
You cannot change the meaning of operators for built-in types in C++. 
Operators can only be overloaded when at least 1 operand is a user-defined type. 
Other rules of overloads still apply:
overloads for a specific function signature can only be used once.

Some of the most commonly overloaded operators are ``<<`` and the
relational operators: ``==``, ``!=``, ``<``, ``<=``, ``>``, and ``>=``.

It doesn't always make sense to overload all of the relational operators.
For example, a complex number does not have a :term:`natural order`,
so you may only want to overload ``==`` and ``!=`` for a complex number.

If you overload ``==`` you should always overload ``!=``.
If you overload ``==`` and ``<``, then you should overload all 6 relational operators.


Relational operators
--------------------
Standard algorithms such as std::sort and containers such as 
:container:`set` expect ``operator <`` to be defined, by default, 
for the user-provided types, and expect it to implement strict 
:compare:`weak_ordering <weak ordering>`.
Strict weak ordering defines members of a set as *comparable* to each other.
The general signature for these non-member functions is:

.. code-block:: cpp

   // In this example, T is a placeholder for your type.
   // Note that this is not a function template.
   inline bool operator<(const T& lhs, const T& rhs)
   {
      // compare the data in left-hand side and right-hand side objects
      // for less than
   }
   
   inline bool operator==(const T& lhs, const T& rhs)
   {
      // compare the data in left-hand side and right-hand side objects
      // for equality
   }


An idiomatic way to implement strict weak ordering for a structure is to use 
lexicographical comparison provided by :utility:`std::tie <tuple/tie>`:

.. code-block:: cpp

   struct Record
   {
       std::string name;
       unsigned int floor;
       double weight;
   };

   inline bool operator<(const Record& lhs, const Record& rhs)
   {
      // parameters passed to each tie must be in the same order
      // or this will always return false
      return std::tie(lhs.name, lhs.floor, lhs.weight)
           < std::tie(rhs.name, rhs.floor, rhs.weight);
   }

If some of the data required for the comparison is private
and has no function to access the data members,
then you may need to make your relational operators friends.

Once you have defined ``operator<`` and ``operator==``,
there is no need to rewrite the comparison logic again.
It is much better to implement the remaining comparison functions
in terms of ``<`` and ``==``.

.. code-block:: cpp

   // note the operands swapped inside the function body
   inline bool operator> (const T& lhs, const T& rhs){ return   rhs < lhs; }

   inline bool operator<=(const T& lhs, const T& rhs){ return !(lhs > rhs); }
   inline bool operator>=(const T& lhs, const T& rhs){ return !(lhs < rhs); }

   inline bool operator!=(const T& lhs, const T& rhs){ return !(lhs == rhs); }

.. note::

   It is a common programming anti-pattern to reimplement all the logic for
   each relational overload.

   This is a common source of error and can lead to bugs that are very difficult
   to track down.


Insertion and extraction overloads
----------------------------------

The bitshift operators ``<<`` and ``>>``, 
although still used in hardware interfacing for the bit-manipulation functions 
they inherit from C, 
have become more prevalent as formatted stream operators in C++.

The overloads of ``operator >>`` and ``operator <<`` that take a 
:io:`std::istream <basic_istream>` reference or 
:io:`std::ostream <basic_ostream>` reference as the left hand argument
are known as insertion and extraction operators. 

The canonical forms are:

.. code-block:: cpp

   std::ostream& operator<<(std::ostream& os, const T& rhs)
   {
     // write rhs to stream
     return os;
   }

   std::istream& operator>>(std::istream& is, T& rhs)
   {
     // read rhs from stream
     if( /* could not construct T from stream */ ) {
       is.setstate(std::ios::failbit);
     }
     return is;
   }


When we use classes such as :io:`cout`, the ``<<`` operator looks at the
type on the right-hand side to determine which overload to call.

These two lines of code call the exact same function:

.. code-block:: cpp

   std::cout << "howdy!";

   operator<< (std::cout, "howdy!");


-----

.. admonition:: More to Explore

   - `Operator overloading in C++ <https://stackoverflow.com/questions/4421706/what-are-the-basic-rules-and-idioms-for-operator-overloading>`__ from stackoverflow.  
     Much of the content in this section was taken from there.
   - :lang:`Comparison operators <operator_comparison>` from cppreference.com.
 
