..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: immutability
   pair: classes; immutable

Immutable classes
=================
The :guidelines:`C++ Core Guidelines generally <rconst-immutable>`
prefer constant data and objects over mutable objects and data when possible.
Immutable objects provide several important benefits:

- Objects that are immutable are easier to reason about.
  They do not surprise you with unexpected state changes.
- Immutability can prevent errors when an object changes state unexpectedly.
- Interfaces that accept constant objects are easier to work with and debug.
- Although we do not discuss multithreaded programming in this course,
  immutable objects can safely be shared by concurrent independent threads.
- Immutability gives the compiler more information to use when reporting
  errors and making optimizations.

An immutable class does not provide a way to modify an existing object.
Its data members are private, and its member functions that inspect the object
are ``const``.  Operations that appear to change an object instead construct
and return a new object.

We will use the same distance value class from the previous section:

.. code-block:: cpp

   namespace length{
     class distance{
       public:
         explicit constexpr distance(double value = 0)
           :m{value}
         {}

       private:
         double m; // meters
     };
   } // end namespace length

The data member is not ``const``.  It does not need to be, because no public
member function can modify it.  The constructor creates the initial value,
and the ``const`` member functions below can only inspect that value.

The familiar compound-assignment operators are problematic in an immutable
class.
In a mutable class, ``operator+=`` would modify the left-hand object and return
``*this``.  An immutable class cannot do that.  These overloads are ``const``
member functions that would need return a new ``distance`` instead:

.. code-block:: cpp

   constexpr distance operator+=(const distance& other) const {
     return distance(m + other.m);
   }

The spelling gives the operation an appearance of mutability, but the
existing object is never modified.  A new value must create a new instance;
objects in this example can only be created and viewed.

Using this overload would create surprises since expressions like:
``a += b`` would not modify ``a``.

Other binary operators are non-friend, non-member functions that take the
both operands as ``const&`` and return a new object:

.. code-block:: cpp

   constexpr distance operator+(const distance& lhs, const distance& rhs){
     return distance(lhs.value() + rhs.value());
   }

The same pattern applies to subtraction, multiplication, and division.

Adding the complete set of operations gives us this immutable class:

.. code-block:: cpp
   :name: immutable-distance

   namespace length{
     class distance{
       public:
         explicit
         constexpr distance(double value)
           :m{value}
         {}

         explicit constexpr operator int() const {
           return static_cast<int>(m);
         }
         constexpr double value() const {
           return m;
         }
       private:
         double m; // meters
     };

     constexpr distance operator+(const distance& lhs, const distance& rhs){
       return distance(lhs.value() + rhs.value());
     }
     constexpr distance operator-(const distance& lhs, const distance& rhs){
       return distance(lhs.value() - rhs.value());
     }
     constexpr distance operator*(const distance& lhs, const distance& rhs){
       return distance(lhs.value() * rhs.value());
     }
     constexpr distance operator*(double scalar, const distance& rhs){
       return distance(scalar * rhs.value());
     }
     constexpr distance operator/(const distance& lhs, std::size_t denominator){
       return distance(lhs.value() / denominator);
     }
   } // end namespace length

.. important::


   The use of ``constexpr`` in this class is **not** what is providing the
   immutablilty here.
   Immutability exists because the class only defines ``const`` member
   functions.

   ``constexpr`` here allows the class to participate in ``constexpr`` compile
   time evaluation.


.. tb-code:: cpp
   :name: immutable-unit
   :hidden:

   namespace length::unit {
     constexpr distance operator""_km(long double d){
      return distance(1000 * d);
     }
     constexpr distance operator""_m(long double m){
       return distance(m);
     }
   } // end namespace length::unit

.. tb-group::
   :name: immutable_distance_tabbed

   .. tb-tab:: Using distance

      This function calculates an average using the immutable distance type.
      Each assignment to ``sum`` binds the name to a newly created value;
      no existing distance is modified.

      .. code-block:: cpp
         :name: immutable-main

         constexpr length::distance average_distance(std::initializer_list<length::distance> distances){
           auto sum = length::distance{0.0};
           for (auto d: distances) sum = sum + d;
           return sum / distances.size();
         }

         int main(){
           using namespace length::unit;

           constexpr auto work = 63.0_km;
           constexpr auto commute = 2 * work;
           constexpr auto gym = 2 * 1600.0_m;
           constexpr auto shopping = 2 * 1200.0_m;

           constexpr auto week1 = 4 * commute + gym + shopping;
           constexpr auto week2 = 4 * commute + 2 * gym;
           constexpr auto week3 = 4 * gym + 2 * shopping;
           constexpr auto week4 = 5 * gym + shopping;

           constexpr auto avg_travel = average_distance({week1, week2, week3, week4});

           static_assert(static_cast<int>(avg_travel) == 264000);
           return static_cast<int>(avg_travel); // 264000m
         }

   .. tb-tab:: Run It

      This example does not print a value, but returns the final value from
      ``main``.  To inspect the generated code, copy it into the online
      `Compiler explorer <https://godbolt.org>`__.

      .. tb-code:: cpp
         :name: memory_immutable_class
         :include:
            DISTANCE: immutable-distance
            UNIT: immutable-unit
            MAIN: immutable-main

         #include <cstddef>
         #include <initializer_list>

         {{DISTANCE}}

         {{UNIT}}

         {{MAIN}}

The operators provide familiar syntax, but they do not make the class
mutable.  ``work += work`` creates ``doubled_work`` and leaves ``work``
unchanged, as the two ``static_assert`` statements demonstrate.

Template metaprogramming approach
---------------------------------
The immutable class above stores its value in an *object*.
Another approach is to store the value in the *type itself*.
This is the technique used by template metaprograms:
a template argument supplies metadata, and template specializations or
instantiations perform work while the program is compiled.

The classic example is a factorial calculation.
The general template recursively refers to a smaller instantiation, and the
specialization ends the recursion at ``1``:

.. tb-code:: cpp

   #include <iostream>

   template <int N>
   struct factorial{
     static int const value = N * factorial<N-1>::value;
   };

   template <>
   struct factorial<1>{
     static int const value = 1;
   };

   int main() {
      std::cout << "5! = " << factorial<5>::value;
   }

For a distance, the template argument can hold the number of meters.
This requires C++20 because earlier C++ standards did not allow floating-point
values as non-type template parameters:

.. code-block:: cpp

   template <double M>
   struct distance{
     static constexpr double value = M;
   };

Now each arithmetic result can have its own type.  For example, adding two
distances creates a ``distance`` whose template argument is the sum of the
two input arguments:

.. code-block:: cpp

   template <double LHS, double RHS>
   constexpr auto operator+(distance<LHS>, distance<RHS>)
     -> distance<LHS + RHS>{
     return {};
   }

The same idea works for subtraction, multiplication, and division.  A scalar
also has to be compile-time metadata if the result type is to include the
scaled value.  An ordinary function parameter such as ``int scalar`` cannot
be used in a return type, so we represent an integer scalar with
``std::integral_constant``:

.. code-block:: cpp

   template <int N>
   inline constexpr std::integral_constant<int, N> constant{};

   template <int N, double M>
   constexpr auto operator*(std::integral_constant<int, N>, distance<M>)
     -> distance<N * M>{
     return {};
   }

This gives us the intended compile-time calculation while making the
template metadata visible in the expression:

.. code-block:: cpp

   auto work = distance<63.0>{};
   auto commute = constant<2> * work;

The braces are required because ``distance<63.0>`` names a type.  The
``constant<2>`` wrapper is also intentional.  Writing ``2 * work`` would
look simpler, but the value ``2`` would be an ordinary function argument and
could not determine the result type ``distance<126.0>``.

Here is the immutable distance class converted to use template metadata:

.. tb-code:: cpp
   :name: immutable-distance-metaprogram

   #include <type_traits>

   namespace length{
     template <double M>
     struct distance{
       static constexpr double value = M;
     };

     template <int N>
     inline constexpr std::integral_constant<int, N> constant{};

     template <double LHS, double RHS>
     constexpr auto operator+(distance<LHS>, distance<RHS>)
       -> distance<LHS + RHS>{
       return {};
     }

     template <double LHS, double RHS>
     constexpr auto operator-(distance<LHS>, distance<RHS>)
       -> distance<LHS - RHS>{
       return {};
     }

     template <int N, double M>
     constexpr auto operator*(std::integral_constant<int, N>, distance<M>)
       -> distance<N * M>{
       return {};
     }

     template <double M, int N>
     constexpr auto operator*(distance<M>, std::integral_constant<int, N>)
       -> distance<M * N>{
       return {};
     }

     template <int N, double M>
     constexpr auto operator/(distance<M>, std::integral_constant<int, N>)
       -> distance<M / N>{
       return {};
     }
   } // end namespace length

   int main(){
     using namespace length;

     constexpr auto work = distance<63.0>{};
     constexpr auto commute = constant<2> * work;
     constexpr auto total = commute + constant<2> * distance<1600.0>{};

     static_assert(decltype(work)::value == 63.0);
     static_assert(decltype(commute)::value == 126.0);
     static_assert(decltype(total)::value == 3326.0);
   }

This technique makes immutability structural: an object has no data member
that can change, and a different distance is represented by a different
type.  The trade-off is a more restrictive interface.  Every value that must
appear in a result type has to be available as template metadata, which is
why this approach is useful for demonstrating metaprogramming but is not a
general replacement for the previous immutable value class.

.. admonition:: More to Explore

   - The content on this page was adapted from Rainer Grimm's blog
     *MODERNES C++*: `Immutable data <https://www.modernescpp.com/index.php/immutable-data>`__

   - From cppreference.com

     - :lang:`constexpr`

   - C++ Core Guidelines

     - :guidelines:`Con: Constants and immutability <rconst-immutable>`
     - :guidelines:`Con.5: Use constexpr for values that can be computed at compile time <con5-use-constexpr-for-values-that-can-be-computed-at-compile-time>`
