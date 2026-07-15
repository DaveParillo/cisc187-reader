..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: templates; concepts

Concepts overview
=================

One of the pitfalls when using templates,
especially templates in unfamiliar libraries,
is that C++ templates can be *too generic*.
When you declare a template with either a ``class`` or ``typename``,
literally **any** ``class`` or ``typename`` could be passed in.

What if your template assumes one of the provided types has a
``push_back`` function?
C++ has a mechanism to resolve this ambiguity and enforce
additional requirements on template arguments used as parameters.

.. cpp:: 20

   The first stable release of concepts was in C++20.

   If you want to use concepts and named requirements you need to
   ensure your compiler supports C++20.


Concepts
--------

Concepts are named requirements for template arguments.
They make templates less ambiguous by stating what operations a type must
support before the template can be used.
A concept is a compile-time :term:`predicate` expression: an expression that
evaluates to ``true`` or ``false``.
When the expression is ``true``, the template argument satisfies the concept.
When the expression is ``false``, the template cannot be used with that
argument.

The standard library defines many useful concepts in the
:cpp:`concepts library <concepts>`.
For example, :cpp:`std::integral <concepts/integral>` is satisfied by integer
types such as ``int`` and ``long``, but not by ``double`` or ``std::string``.

.. tb-code:: cpp

   #include <concepts>
   #include <iostream>

   template <std::integral T, int N>
   constexpr T multiply(T val) {
     return val * N;
   }

   int main() {
     std::cout << multiply<int, 3>(7) << '\n';

     // Error: double is not an integral type.
     // std::cout << multiply<double, 3>(2.5) << '\n';
   }

This constraint is part of the template declaration.
The compiler checks it before trying to generate the function body.
If the constraint is not satisfied, the compiler can report that the template
argument does not satisfy ``std::integral`` instead of producing a long list of
unrelated overload failures.

A concept can also be written by the programmer.
The following example defines ``SmallValue`` using simple primitive
operations. The expression ``sizeof(T) <= sizeof(long)`` is a compile-time
predicate.

.. tb-code:: cpp

   #include <iostream>

   template <typename T>
   concept SmallValue = sizeof(T) <= sizeof(long);

   template <SmallValue T>
   void print_size(T value) {
     std::cout << value << " uses " << sizeof(T) << " bytes\n";
   }

   int main() {
     print_size(42);
     print_size('a');

     // Error on systems where long double is larger than long.
     // print_size(3.14L);
   }

.. index:: requires

Keyword: ``requires``
---------------------

A *requires clause* is an additional constraint on template arguments or a function.
C++20 supports requires clauses and requires expressions.

The ``requires`` keyword can be used after a template parameter list:

.. code-block:: cpp

   #include <concepts>

   template <typename T>
     requires std::floating_point<T>
   constexpr T average(T a, T b) {
     return (a + b) / 2;
   }

It can also be used with an abbreviated function template:

.. code-block:: cpp

   #include <concepts>

   constexpr auto twice(std::integral auto value) {
     return value * 2;
   }

Both examples are valid C++20.
The first form is useful when the constraint is more complex or when several
template parameters are involved.
The second form is compact when each parameter has a simple constraint.

A *requires expression* can test whether a specific expression is valid for a
type. The following concept checks whether a value of type ``T`` can be read
from an input stream:

.. code-block:: cpp

   #include <concepts>
   #include <istream>

   template <typename T>
   concept StreamExtractable = requires(std::istream& in, T& value) {
     { in >> value } -> std::same_as<std::istream&>;
   };

The body of the ``requires`` expression is not executed.
It asks whether the expression ``in >> value`` is valid and whether its result
type is ``std::istream&``.
That is exactly the operation needed by a generic input function.
This example reads one value and fails if the input cannot be read as ``T`` or
if extra non-whitespace input remains:

.. tb-code:: cpp
   :stdin: 2.7818 x

   #include <concepts>
   #include <iostream>
   #include <istream>
   #include <stdexcept>
   #include <string>

   namespace mesa {
     struct point {
       int x = 0;
       int y = 0;
     };

     template <typename T>
     concept StreamExtractable = requires(std::istream& in, T& value) {
       { in >> value } -> std::same_as<std::istream&>;
     };

     template <StreamExtractable T>
     T get(std::istream& in) {
       T result;
       if (!(in >> result)) {
         throw std::runtime_error("input could not be read as the requested type");
       }

       std::string extra;
       if (in >> extra) {
         throw std::runtime_error("unexpected input after the value: " + extra);
       }

       return result;
     }
   }

   int main() {
     auto num = mesa::get<float>(std::cin);
     std::cout << "Value: " << num << '\n';

     // Error: mesa::point does not satisfy StreamExtractable.
     // auto bad_value = mesa::get<mesa::point>();
     return 0;
   }

Attempting to ``get`` a ``mesa::point`` is a compile error because
``mesa::point`` does not define an ``operator>>`` overload.
With a concept, the compiler can diagnose the failed requirement directly.
The exact wording depends on the compiler, but the error is usually centered on
the unsatisfied concept:

.. code-block:: none

   error: no matching function for call to 'get<mesa::point>'
   note: constraints not satisfied
   note: the required expression 'in >> value' is invalid

Without the concept, the compiler would try to compile the body of ``get`` and
fail at ``buf >> result``.
That can produce a long list of unrelated ``operator>>`` overloads, because the
compiler has to explain every candidate it considered.

.. code-block:: none

   /usr/include/c++/v1/cstddef:135:3: note: candidate function template not viable: no known conversion from 'std::istringstream' (aka 'basic_istringstream<char>') to 'byte' for 1st argument
   operator>> (byte  __lhs, _Integer __shift) noexcept
   ^
   /usr/include/c++/v1/istream:625:1: note: candidate function template not viable: no known conversion from 'mesa::point' to 'unsigned char *' for 2nd argument
   operator>>(basic_istream<char, _Traits>& __is, unsigned char* __s)
   ^
   /usr/include/c++/v1/istream:633:1: note: candidate function template not viable: no known conversion from 'mesa::point' to 'signed char *' for 2nd argument
   operator>>(basic_istream<char, _Traits>& __is, signed char* __s)
   ^

   // many others omitted

The more code you have written and the more code pulled in from ``#include`` directives,
the longer the list will be.
It can run on for thousands of lines.
Concepts give the compiler a better place to stop and a better vocabulary for
the diagnostic.

.. important::

   Why did ``get`` still need the checks and ``throw`` statements?
   If ``x`` is not ``StreamExtractable``, why is any check inside ``get``
   needed?

   .. tb-reveal::

      ``StreamExtractable`` checks a **type** at compile time.
      It answers the question, "Can this type be read from a stream with
      ``operator>>``?"

      It does not check the actual characters supplied at run time.
      A ``float`` is stream-extractable, so ``get<float>`` is allowed to
      compile. But the input from ``std::cin`` might still be missing,
      malformed, or followed by unexpected text.

      The concept protects the template from being instantiated with a type
      that has no suitable input operation. The checks inside ``get`` protect
      the program from bad input values.

You will sometimes encounter *named requirements* in C++ code.

The :cpp:`named requirements listed <named_req>`
are the named requirements used in the C++ standard to define the 
expectations of the standard library.

Some named requirements are now represented by C++20 concepts.
Others remain specification terms that describe standard library behavior.
When a named requirement has a matching concept, prefer the concept in new code.
It documents intent and lets the compiler enforce the requirement.

-----

.. admonition:: More to Explore

   - `a bit of background for concepts and C++17 <https://isocpp.org/blog/2016/02/a-bit-of-background-for-concepts-and-cpp17-bjarne-stroustrup>`_ Bjarne Stroustrup
   - :wiki:`Concepts C++ <Concepts_(C%2B%2B)>` from Wikipedia
   - From cppreference.com

     - :cpp:`Concepts Library <concepts>`
     - :lang:`Constraints and concepts <constraints>`
     - :cpp:`Named requirements <named_req>`
