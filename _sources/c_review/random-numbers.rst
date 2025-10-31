.. _random:

Random numbers
--------------

.. index::
   single: deterministic

Most computer programs do the same thing every time they are executed,
so they are said to be **deterministic**. Usually, determinism is a good
thing, since we expect the same calculation to yield the same result.
For some applications, though, we would like the computer to be
unpredictable. Games are an obvious example.

.. index::
   single: nondeterministic

Making a program truly **nondeterministic** turns out to be not so easy,
but there are ways to make it at least seem that way. One of
them is to generate "pseudorandom" numbers and use them to determine the
outcome of the program. Pseudorandom numbers are not truly random in the
mathematical sense, but for our purposes, they will do.

C++ provides a function called 
:numeric:`uniform_int_distribution <random/uniform_int_distribution>`
that returns a pseudorandomly generated integer value uniformly distributed 
within the range you specify.
It is declared in the header file ``random``, which is another part
of the standard library.

To see a sample, run this loop:

.. activecode:: random_numbers_AC_1
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
   :nocodelens:

   Take a look at the active code below, which generates 4 random numbers.
   ~~~~
   #include <iostream>
   #include <random>

   int main () {
      // make a random number generator
      std::random_device device;
      std::default_random_engine gen(device());

       for (int i = 0; i < 4; i++) {
           int upper_bound = 10000;
           int x = std::uniform_int_distribution<int> {0, upper_bound} (gen);
           std::cout << x << '\n';
       }
       return 0;
   }


Notice there is a lot going on in this small program.

1. Before we create a random number, we have to create
   a random number generator *engine*.

   The engine is the object that actually does all the hard work.

   The C++ standard library provides many options and variations
   for pseudorandom engines, since it is such an important topic.

   But for most simple purposes, the default way is good enough.

2. The ``uniform_int_distribution`` object needs 3 pieces of information:

   - ``<int>`` - the type of the random value to return
   - ``{0, 10000}`` - the range of values (inclusive) to select from
   - ``(gen)`` - the engine to use


.. tabbed:: self_check

   .. tab:: Q1

      .. fillintheblank:: random_numbers_1

          Pseudorandom numbers are said to be __________, because different numbers are generated every time the program is executed.

          - :([Nn]ondeterministic|NONDETERMINISTIC): Correct!
            :([Dd]eterministic|DETERMINISTIC): Incorrect! Deterministic programs do the same thing every time they are executed.
            :.*: Incorrect!

   .. tab:: Q2

      .. mchoice:: random_numbers_2
         :answer_a: cstdlib
         :answer_b: random
         :answer_c: cmath
         :answer_d: iostream
         :correct: a
         :feedback_a: Correct!
         :feedback_b: Incorrect!
         :feedback_c: Incorrect!
         :feedback_d: Incorrect!

         What header file do we need to declare in order to use 
         ``std::uniform_int_distribution``?


   .. tab:: Q3

      .. mchoice:: random_numbers_3

          If we wanted to generate a random number between 0 and 12, 
          and we have previously declared
          
          .. code-block::

             std::random_device dev;
             std::default_random_engine engine(dev());


          what should be our next line of code?

          -   ``int x = std::uniform_int_distribution<int> {0, 12} (gen);``

              -   Does not compile. No variable ``gen`` in this program.

          -   ``std::uniform_int_distribution<int> {0, 12} (engine);``

              -   Any random value created is lost.
                  The return value is not stored.

          -   ``int x = std::uniform_int_distribution<int> {0, 13} (engine);``

              -   This returns some random number between 0 and 13, which is out of range.

          -   ``int x = std::uniform_int_distribution<int> {0, 12} (engine);``

              +   Correct!

