..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: compile-time evaluation
   pair: classes; constexpr

``constexpr`` classes
=====================
Previously, we used ``constexpr`` with variables and functions.  We can also
define a class whose constructors and member functions can participate in
constant expressions.  Such a class lets the compiler evaluate operations on
its objects while compiling the program.

Let's examine a value class for a distance in meters.

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

The data member does not need to be declared ``constexpr``.  The
``constexpr`` constructor makes it possible to create a ``distance`` object
in a constant expression.  Member functions that should be evaluated at
compile time must also be declared ``constexpr``.

In C++14, the rules for ``constexpr`` functions became less restrictive.
They may contain multiple statements and may modify an object whose lifetime
began during constant evaluation.  This lets a compile-time calculation use
the same update operations as a run-time calculation.

After we define our constructor, we can add other functions as appropriate.
In our case we want to perform basic math operations on distances.
We will use the standard pattern for arithmetic overloads.  A compound
assignment operator is a member function that updates its left-hand operand
and returns ``*this``:

.. code-block:: cpp

   constexpr distance& operator+=(const distance& other);

The corresponding ``operator+`` is a non-friend, non-member function.  It
takes its left-hand operand by value, applies ``operator+=``, and returns the
new value:

.. code-block:: cpp

   constexpr distance operator+(distance lhs, const distance& rhs) {
     lhs += rhs;
     return lhs;
   }

The copy passed as ``lhs`` is modified, while the caller's object is
unchanged.  The same pattern applies to subtraction, multiplication, and
division.


Adding the overloads for addition, subtraction, multiplication, and division
yields the following:

.. code-block:: cpp
   :name: constexpr-distance

   namespace length{
     class distance{
       public:
         explicit
         constexpr distance(double i)
           :m{i}
         {}

         constexpr distance& operator+=(const distance& other) {
           m += other.m;
           return *this;
         }
         constexpr distance& operator-=(const distance& other) {
           m -= other.m;
           return *this;
         }
         constexpr distance& operator*=(double scalar) {
           m *= scalar;
           return *this;
         }
         constexpr distance& operator/=(std::size_t scalar) {
           m /= scalar;
           return *this;
         }
         explicit constexpr operator int() const {
           return static_cast<int>(m);
         }
       private:
         double m; // meters
     };

     constexpr distance operator+(distance lhs, const distance& rhs){
       lhs += rhs;
       return lhs;
     }
     constexpr distance operator-(distance lhs, const distance& rhs){
       lhs -= rhs;
       return lhs;
     }
     constexpr distance operator*(distance lhs, double scalar){
       lhs *= scalar;
       return lhs;
     }
     constexpr distance operator*(double scalar, distance rhs){
       rhs *= scalar;
       return rhs;
     }
     constexpr distance operator/(distance lhs, std::size_t denominator){
       lhs /= denominator;
       return lhs;
     }
   } // end namespace length

We might choose to add more, but these operations demonstrate the basic idea.

Working exclusively in meters is not always convenient, so we can also add
distance literals so that we can easily work with numbers that are either
meters or kilometers:

.. code-block:: cpp
   :name: constexpr-unit

   namespace length{
     namespace unit{
       constexpr distance operator""_km(long double d){
         return distance(1000*d);
       }
       constexpr distance operator""_m(long double m){
         return distance(m);
       }
     } // end namespace unit
   } // end namespace length

Notice that these overloads are non-friend non-member functions.
Each simply constructs a new distance based on the units implied by the literal used.

.. tb-group::
   :name: constexpr_distance_tabbed

   .. tb-tab:: Using distance

      Finally we can write some functions that use our constexpr class.

      Here we add a free function that takes a list of distances and
      accumulates an average.  We could have used
      :algorithm:`std::accumulate <accumulate>`,
      or in C++17 and later, we could use :algorithm:`std::reduce <reduce>`
      to achieve the same outcome.

      Once we have that, we can define some distances,
      generate a few weeks' worth of values, and compute the final result.

      .. code-block:: cpp
         :name: constexpr-main

         constexpr length::distance average_distance(std::initializer_list<length::distance> distances){
           auto sum = length::distance{0.0};
           for (auto d: distances) sum = sum + d;
           return sum/distances.size();
         }

         int main(){
           using namespace length::unit;

           constexpr auto work = 63.0_km;
           constexpr auto commute = 2 * work;
           constexpr auto gym = 2 * 1600.0_m;
           constexpr auto shopping = 2 * 1200.0_m;

           constexpr auto week1 = 4*commute + gym + shopping;
           constexpr auto week2 = 4*commute + 2*gym;
           constexpr auto week3 = 4*gym     + 2*shopping;
           constexpr auto week4 = 5*gym     + shopping;

           constexpr auto avg_travel = average_distance({week1,week2,week3,week4});

           static_assert(static_cast<int>(avg_travel) == 264000);
           return static_cast<int>(avg_travel); // 264000m
         }

   .. tb-tab:: Run It

      This example does not print a value, but merely returns the final value
      from main.
      If you're curious as to why, copy this code into
      the online `Compiler explorer <https://godbolt.org>`__


      .. tb-code:: cpp
         :name: memory_constexpr_class
         :include:
            DISTANCE: constexpr-distance
            UNIT: constexpr-unit
            MAIN: constexpr-main

         #include <cstdlib>
         #include <cstddef>
         #include <initializer_list>

         {{DISTANCE}}
         {{UNIT}}
         {{MAIN}}

The ``constexpr`` declarations require the initializations of these distance
objects and the call to ``average_distance`` to be valid constant expressions.
The ``static_assert`` makes that requirement visible: the compiler must
evaluate the average at compile time or reject the program.

This does not mean that the entire program runs at compile time.  ``main``
still runs when the program is launched, and non-``constexpr`` objects and
expressions can be evaluated at run time.  The compiler may perform other
evaluations or optimizations as well, but ``constexpr`` does not require that.

.. admonition:: Try This!

   Copy this code into the online `Compiler explorer <https://godbolt.org>`__
   and see what the generated code looks like.

   Try setting the compiler optimization in the explorer "compiler options" text box:
   `-O2` - does anything change? It should!

   Is the final symbol code what you expected?

   What do you think is going on here?



-----

.. admonition:: More to Explore

   - From cppreference.com

     - :lang:`constexpr`

   - C++ Core Guidelines

     - :guidelines:`Con.5: Use constexpr for values that can be computed at compile time <con5-use-constexpr-for-values-that-can-be-computed-at-compile-time>`
