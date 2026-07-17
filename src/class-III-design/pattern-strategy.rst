..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: design pattern; strategy

Strategy pattern
================
.. graphviz::
   :alt: Fly strategy
   :align: right
   :caption: Fly strategy

   digraph "strategy"
   {
     node [
       fontname="BitstreamVeraSans",
       fontsize="12",
       color="black",
       fillcolor="lightblue",
       shape=record,
       style="filled"
     ];
     fly [
       label="{fly_behavior|-strategy: std::function\<void\>\l|+fly(): void\l}"
     ];
   }

We can think of flying as a *strategy* different birds employ to move around.
Birds don't *inherit* a fly behavior, they *have it*.
The centerpiece of the solution is to isolate many different
types of flying behavior behind a single class that stores
a pointer to a function implementing the behavior.
Each implementation defines a different **strategy** for the interface.

Any callable entity (function, function object, or lambda) is
a potential strategy that derived classes of a bird can now use.

.. code-block:: cpp
   :name: fly-strategy-core
   :caption: Fly strategy support code

   #include <concepts>
   #include <functional>
   #include <iostream>
   #include <utility>

   // an alias to avoid copying std::function<void()> everywhere
   using fly_strategy = std::function<void()>;

   template <typename S>
   concept fly_strategy_source =
     std::constructible_from<fly_strategy, S>;

   class fly_behavior {
   public:
     template <fly_strategy_source S>
     explicit fly_behavior(S&& new_strategy)
       : strategy_{std::forward<S>(new_strategy)}
     {
     }

     void fly() const {
       strategy_();
     }

     template <fly_strategy_source S>
     void strategy(S&& new_strategy) {
       strategy_ = std::forward<S>(new_strategy);
     }

   private:
     fly_strategy strategy_;
   };

   // a function object that implements a strategy
   struct soar
   {
     void operator()() const {
       std::cout << "fly by soaring.\n";
     }
   };

   // a free function can also implement a strategy
   void no_flying_allowed() {
     std::cout << "I don't fly.\n";
   }


The concept ``fly_strategy_source`` is a real template requirement:
any strategy must be a callable object that can be stored in a
``std::function<void()>``.
The ``fly_behavior`` class owns that callable and provides one place
to execute or replace the current strategy.

The base class now *delegates* the fly behavior to the strategy
instead of either defining a single fixed behavior or forcing every
derived class to create one.
In languages without lambda expressions, each implemented strategy
is usually implemented as a separate class, each inheriting from the base
strategy class.
In C++, an inheritance based solution is possible, but not required.
There is no 'best' solution - your needs must drive the final
design decision.
In general, if the strategy also needs to store state information,
then implement as a class or function object.
If the strategy is stateless, then implement a functional solution.

.. code-block:: cpp
   :name: bird-base
   :caption: Bird base class using the fly strategy

   class bird {
   public:
     bird()
       : flight_{soar{}}
     {
     }

     template <fly_strategy_source S>
     explicit bird(S&& new_strategy)
       : flight_{std::forward<S>(new_strategy)}
     {
     }

     virtual ~bird() = default;

     template <fly_strategy_source S>
     void set_fly_behavior(S&& new_strategy) {
       flight_.strategy(std::forward<S>(new_strategy));
     }

     void fly() const {
       flight_.fly();
     }

   private:
     fly_behavior flight_;
   };

In this example, a bird may

- default construct the default soaring strategy, or
- set a strategy when constructed, or
- change the strategy at some point after construction.

An example of birds using the strategy:

.. code-block:: cpp
   :name: strategy-birds
   :caption: Birds with different fly strategies

   // a hawk can use the default soar behavior
   class hawk : public bird {
   public:
     hawk() = default;
   };

   // this penguin defines its fly behavior using a free function
   class penguin : public bird {
   public:
     penguin()
       : bird{no_flying_allowed}
     {
     }
   };

And now the reusable pieces can be combined into a complete program.

.. tb-code:: cpp
   :name: strategy-hawk-penguin
   :caption: Hawk and penguin fly strategies
   :run-before: fly-strategy-core, bird-base, strategy-birds

   int main() {
     hawk h;
     h.fly();

     penguin p;
     p.fly();

     // change the behavior for just this penguin
     p.set_fly_behavior(
       []() {
         std::cout << "With a rocket pack, now I can fly!\n";
       }
     );
     p.fly();
   }

Notice that we fixed our inheritance problem by using :term:`composition`.
Not only did composition allow us to encapsulate a family of behaviors,
it also allowed a simple hook to enable changing the behavior at runtime.

-----

.. admonition:: More to Explore

   - `Strategy Design Pattern <https://www.oodesign.com/strategy-pattern/>`__ on oodesign.com
     and on :wiki:`Wikipedia <Strategy_pattern>`.
   - `Design Patterns Are Missing Language Features <http://wiki.c2.com/?DesignPatternsAreMissingLanguageFeatures>`__ from the PortlandPatternRepository.
