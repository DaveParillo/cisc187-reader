..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: immutability
   pair: classes; constexpr

``constexpr`` classes
=====================
The :guidelines:`C++ Core guidelines generally <Rconst-immutable>`
prefers constant data and objects over mutable objects and data when possible.
Previously, when we have used ``const`` and ``constexpr`` it has generally been
limited to variables and functions.
But what about an entire class?
Can we design a class that can only store a single value?
Even if we can, should we?

Let's answer that last question first.

Immutable object provide several important benefits:

- Objects that are immutable are easier to reason about.
  They don't surprise you with unexpected behaviors.
- It can prevent errors when an object changes its state unexpectedly.
- Interfaces that accept constant objects are easier to work with and debug.
- Although we don't discuss multi-threaded programming in this course,
  constant objects are inherently thread safe - that is they can safely be
  accessed simultaneously by concurrent independent execution threads.
- Gives the compiler more tools to:

  - Report errors in usage
  - Make optimizations (more on this in a moment)


Awesome. So how can we make an immutable class?

Simply by declaring all of the class functions as ``constexpr``!

Let's examine a value class for a distance in meters.

.. code-block:: cpp

   namespace length{

     class distance{
       public:
         explicit constexpr distance(double value = 0)
           :m{value}
         {}

       private:
         double m;	 // meters 
     };

   } // end namespace length

All member functions, including any constructors must be ``const`` or ``constexpr``.
The private data is not constant.
That's OK, because we won't allow any function to change it.

Recall that ``constexpr`` member functions are implicitly ``const`` member functions -
that is, they cannot change the state of the object.

After we define our constructor, we can add other functions as appropriate.
In our case we want to perform basic math operations on distances.
And in keeping our use of the 'standard pattern' for arithmetic overloads,
we want to create member functions like this:

.. code-block:: cpp

   constexpr distance operator+=(const distance& other);

Normally when we implement these functions we modify the current object
and return ``*this``.
But we can't do that if our objects are immutable.
What we do instead is construct a new distance object by combining the 
two objects on either side of the operand:

.. code-block:: cpp

   constexpr distance operator+=(const distance& other) {
     return distance(m + other.m);
   }

The current object is still involved - it is the object on the left-hand side
of the expression, but we do not modify it.

An important implication of this implementation is that every change in state
creates a new object to store it.


Adding the overloads for addition, subtraction, multiplication, and division
yields the following:

.. code-block:: cpp

   namespace length{

     class distance{
       public:
         constexpr distance(double i)
           :m{i}
         {}

         constexpr distance operator+=(const distance& other) {
           return distance(m + other.m);
         }
         constexpr distance operator-=(const distance& other) {
           return distance(m - other.m);
         }
         constexpr distance operator*=(double scalar) {
           return distance(m*scalar);
         }
         constexpr distance operator/=(int scalar) {
           return distance(m/scalar);
         }

       private:
         double m;	 // meters 
     };

     constexpr distance operator+(distance lhs, const distance& rhs){
       return distance(lhs+= rhs);
     }
     constexpr distance operator-(distance lhs,const distance& rhs){
       return distance(lhs-= rhs);
     }
     constexpr distance operator*(int scalar, distance a){
       return distance(a*=scalar);
     }
     constexpr distance operator/(distance a, size_t denominator){
       return distance(a/=denominator);
     }

   } // end namespace length

We might choose to add more, but these 4 demonstrate the basic idea.

We should also implement the complete set of relational overloads,
since there is no reason to treat distances as anything other than
completely regular types.

Working exclusively in meters is not always convenient, so we can also add
distance literals so that we can easily work with numbers that are either
meters or kilometers:

.. code-block:: cpp

   namespace length{
     namespace unit{
       constexpr distance operator "" _km(long double d){
         return distance(1000*d);
       }
       constexpr distance operator "" _m(long double m){
         return distance(m);
       }
     } // end namespace unit
   } // end namespace length
     
Notice that these overloads are non-friend non-member functions.
Each simply constructs a new distance based on the units implied by the literal used.

.. tabbed:: constexpr_distance_tabbed

   .. tab:: Using distance

      Finally we can write some functions that use our constexpr class.

      Here we add a free function tthat takes a list of distances and
      accumulates an average.
      We could have used :numeric:`std::accumulate <accumulate>`,
      or in C++17 and later, we could use :numeric:`std::reduce <reduce>`
      to achive the same outcome.
      
      Once we have that, we can define some distances,
      generate a few weeks works of values and compute the final result.

      .. code-block:: cpp

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
           
           return int(avg_travel); // 264000m
         }

   .. tab:: Run It

      This example does not print a value, but merely returns the final value
      from main.
      If you're curious as to why, copy this code into
      the online `Compiler explorer <https://godbolt.org>`__
 

      .. activecode:: ac_memory_constexpr_classes
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <cstdlib>
         #include <initializer_list>

         namespace length{

           class distance{
             public:
               explicit constexpr distance(double i)
                 :m{i}
               {}

               constexpr distance operator+=(const distance& other) {
                 return distance(m + other.m);
               }
               constexpr distance operator-=(const distance& other) {
                 return distance(m - other.m);
               }
               constexpr distance operator*=(double scalar) {
                 return distance(m*scalar);
               }
               constexpr distance operator/=(int scalar) {
                 return distance(m/scalar);
               }

               constexpr operator int() const { return static_cast<int>(m);}

             private:
               double m;	 // meters 
           };

           constexpr distance operator+(distance lhs, const distance& rhs){
             return distance(lhs+= rhs);
           }
           constexpr distance operator-(distance lhs,const distance& rhs){
             return distance(lhs-= rhs);
           }
           constexpr distance operator*(int scalar, distance a){
             return distance(a*=scalar);
           }
           constexpr distance operator/(distance a, size_t denominator){
             return distance(a/=denominator);
           }

           namespace unit{
             constexpr distance operator "" _km(long double d){
               return distance(1000*d);
             }
             constexpr distance operator "" _m(long double m){
               return distance(m);
             }
           }
           
         } // end namespace length
           
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
           
           return int(avg_travel); // 264000m
         }

Declaring all variables as ``constexpr`` means all instances of distance and all functions are constant expressions.
The compiler performs all of these operations at compile time.
That means the *entire program will be executed at compile time* and
all the program variables and instances are immutable. 

.. admonition:: Try This!

   Copy this code into the online `Compiler explorer <https://godbolt.org>`__
   and see what the generated code looks like.

   Try setting the compiler optimiztion in the explorer "compiler options" text box:
   `-O2` - does anything change? It should!

   Is the final symbol code what you expected?

   What do you think is going on here?



-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     Rainer Grimm's blog *MODERNES C++*: `Immutable data <https://www.modernescpp.com/index.php/immutable-data>`__

   - From cppreference.com

     - :lang:`constexpr`

   - C++ Core Guidelines

     - :guidelines:`Con: Constants and immutability <Rconst-immutable>`
     - :guidelines:`Con.5: Use constexpr for values that can be computed at compile time <con5-use-constexpr-for-values-that-can-be-computed-at-compile-time>`

