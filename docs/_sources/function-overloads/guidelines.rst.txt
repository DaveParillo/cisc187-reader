..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
   
.. index:: function writing guidelines

General function writing guidelines
===================================
#. Write for clarity and correctness **first**
#. Avoid *premature optimization*
#. Avoid *premature "pessimization"*
   That is, prefer faster when **equally** clear
#. Minimize side-effects

   A function that modifies its parameters is said to have *side-effects*.
   Programs with too many side-effects are hard to predict and debug.

   Returning to our call-stack example.
   What if the function signatures were changed to accept a pass-by-reference parameter?

   .. tabbed:: side_effects

      .. tab:: Side effects

         .. code-block:: cpp

            void dig(double& x);
            void deeper(double& x);

         Given that the names of these functions provide no insight to their purpose,
         there is no way to know without inspecting the source if
         the variable x is modified when passed to these functions.

         .. code-block:: cpp

            void dig(double& val) {
              std::cout << "Digging...\n";
              val /= 2;
              deeper(val);
              std::cout << "Done digging...\n";
            }

         Unless it's obvious from the name of the function,
         side effects are almost always unexpected.

      .. tab:: Run It

         .. activecode:: functions_guidelines_side_effects_ac
            :language: cpp
            :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
            :nocodelens: 

            #include <iostream>

            void dig(double& val);
            void deeper(double& val);

            int main() {
              double pi = 3.14159;
              std::cout << "in main.\npi = " << pi << '\n';
              dig(pi);

              std::cout << "Returned to main.\npi = " << pi << '\n';
              return 0;
            }

            void dig(double& val) {
              std::cout << "Digging...\n";
              val = val * 2;
              deeper(val);
              std::cout << "Done digging...\n";
            }

            void deeper(double& val) {
              val -= 1;
              std::cout << "now even deeper....\n";
            }

   This is one of the reasons why some programmers **only** use pass-by-reference
   when the parameter is ``const``.
   Some programmers prefer passing pointers over non-``const`` parameters.
   This requires the caller to explicitly pass in an address and 
   clearly states that the function may modify the parameter.

#. Keep functions short

   - A function should do *one* thing well

     If you see a function doing more than one thing
     consider breaking it up into multiple functions

   - Is this (slightly) more work?

     In the short run, perhaps.

     In the long run, your total time spent
     debugging, testing, maintaining, and modifying
     will be far, far less than if you packed everything into one monster function


   - Note that :term:`unit testing <unit test>` is practically impossible 
     once functions reach a certain size.

#. Strive to write a function *once* and never modify it again.
#. Check function parameters for validity.
   Unless you *completely* trust the caller (and their caller...)

   - It should be obvious: do not trust ``argv[]``


.. index::
   pair: video; function returns

.. youtube:: 9mWWNYRHAIQ
   :http: https
   :divid: return_9mWWNYRHAIQ

When to write a function
------------------------

As with any kind of abstraction, there are two goals to making a function:

- **Encapsulation**: 
  If you have some task to carry out that is simple to describe from the outside, 
  but messy to understand from the inside, 
  then wrapping it in a function lets the caller carry out this task without having to know the details. 

  This is also useful if you want to change the implementation later.
- **Code re-use**: 
  If you find yourself writing the same lines of code in several places 
  (or worse, are tempted to copy a block of code to several places), 
  you should probably put this code in a function 
  (or perhaps more than one function, 
  if there is no succinct way to describe what this block of code is doing).

Both of these goals may be trumped by the goal of making your code **clear**. 
If you can’t describe what a function is doing in a single, simple sentence, 
this is a sign that maybe you need to restructure your code. 
Having a function that does more than one thing (or does different things depending on its arguments) 
is likely to lead to confusion.

So, for example, this is not a good function definition:

.. code-block:: cpp

   // This code is an anti-pattern.
   // It's an example of how NOT to write a function.

   /** 
    * If getMax is true, return maximum of x and y,
    * else return minimum.
    */
   int computeMinOrMax(int x, int y, bool getMax) {
     if(x > y) {
       if(getMax) { 
         return x;
       } else {
         return y; 
       }
     } else { 
       if(getMax) { 
         return y;
       } else {
          return x; 
       }
     } 
   }

This function is clearly trying to do two things and not doing either one very well.
Two functions would be far simpler:

.. code-block:: cpp

   // return the maximum of x and y
   // if x == y, return y
   int maximum (int x, int y) {
     return (x < y) ? y : x;
   }

   // return the minimum of x and y
   // if x == y, return y
   int minimum (int x, int y) {
     return (y < x) ? y : x;
   }

   int computeMinOrMax(int x, int y, bool getMax) {
       if(getMax) {
         return maximum(x, y);
       }
       return minimum(x, y);
   }

   // or more compactly:
   int computeMinOrMax(int x, int y, bool getMax) {
     return getMax ? maximum(x,y) : minimum(x,y);
   }

   
Is this *slightly* more typing? Yes.
At the end of the day, you will be far happier testing and debugging the three simpler functions
than the first version.
Your future co-workers will thank you.

.. note::

   Also be aware the STL provides functions
   `std::min <http://en.cppreference.com/w/cpp/algorithm/min>`_ and
   `std::max <http://en.cppreference.com/w/cpp/algorithm/max>`_,
   which eliminate the need for our ``minimum`` and ``maximum`` entirely
   and have the advantage of working on any :term:`comparable` type.

   This would transform the previous example to:

   .. code-block:: cpp

      #include <algorithm>

      int computeMinOrMax(int x, int y, bool getMax) {
        return getMax ? std::max(x,y) : std::min(x,y);
      }

.. index::
   pair: repl.it; number guessing
   pair: repl.it; command line argument parsing
   pair: repl.it; parsing command line arguments

Example: number guessing
------------------------
A more realistic example might help.

.. tabbed:: function_guidelines_guessing_example_tab

   .. tab:: Original

      While randomly surfing the internet I stumbled on a small program
      intended to help people understand C++.

      Unfortunately, it is full of issues and this is the kind of program structure
      that will **not** help you when trying to create your own complicated projects.

      Open this in Replit and run ``./main`` in the console tab.
      You may need to type ``make main`` first.

      .. raw:: html

         <iframe height="400px" width="100%" 
          src="https://repl.it/@DaveParillo/NumberGuessingFunctionRefactorOriginal?lite=true" 
          scrolling="no" 
          frameborder="no" 
          allowtransparency="true" 
          allowfullscreen="true" 
          sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>


      .. admonition:: Try This!

         How many bugs or other issues can you find in this program without looking at the 'Bugs' tab?


   .. tab:: Bugs

      This program has a few bugs.

      Code like:

      .. code-block:: cpp

         if(tries >= 20)

      seems to imply you have 20 tries.
      The program actually gives you 21.
      Off-by-one errors like this are common.


      This code looks ok, but isn't.

      .. code-block:: cpp

         std::cout << "Enter a number between 1 and 100 (" << 20 - tries << " tries left): ";
         std::cin >> guess;
         std::cin.ignore();

      There is no error checking on guess before it is used.
      Non-integer input causes the program to enter an infinite loop.

      Related to this, there is this code:

      .. code-block:: cpp

         int guess; 

         // try to get guess

         if(guess > number)

      Since guess is uninitialized, if ``cin`` fails to fill ``guess``,
      then ``guess`` will not have any value when the if statement is evaluated,
      which is undefined behavior.


   .. tab:: Issues

      This is fundamentally a C program on a C++ forum.

      Yes, it uses ``cin`` and ``cout``.

      That doesn't make it a C++ program.

      A clue it was copied from C:

      .. code-block:: cpp

         int main (void) . . .

      Explicitly using ``void`` to declare a function take no parameters
      is a best practice in C.
      Otherwise the compiler assumes the function can take **any number**
      of parameters.
 
      In C++, ``main()`` or any other function that takes no parameters
      is implicitly void.


      .. index:: rand
      .. index:: random
      .. index:: random_device
      .. index:: uniform_int_distribution

      Next problem is the way the random numbers are created:

      .. code-block:: cpp

         int number = rand() % 99 + 2;

      Quick!

      Can we be **certain** that this correctly creates a number from
      1 to 100, inclusive?

      The code is just not that easy to reason about.

      - We have to know how rand works
      - We have to remember what modulus does.

      Yes, not big hurdles, but this is where bugs hide.
      And for the record, the program asks the user to pick a number
      from 1 to 100, but this algorithm will never choose 1.

      The standard library has a superior alternative to ``rand``:

      .. activecode:: function_random_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens: 

         #include <iostream>
         #include <random>

         int main() {
           std::cout << "Random numbers: \n";
           // Seed with a real random value, if available
           std::random_device r;
           std::default_random_engine eng(r());  // make a random number generator

           for (int i = 0; i < 10; ++i) {
             // generate the next uniformly distributed integer between 0 and 999
             // using the random default engine
             std::cout << std::uniform_int_distribution<int> {0, 999} (eng) << '\n';
           }
         }
        

      Because there are no functions, it is necessary to repeat block of code like this:

      .. code-block:: cpp

         std::cout << "Enter a number between 1 and 100 (" << 20 - tries << " tries left): ";
         std::cin >> guess;
         std::cin.ignore();


      In general, the pattern

      - Prompt
      - Assign
      - Validate
      - Repeat (if needed) or exit

      Is common.
      Because it's tedious to copy over and over,
      this program omits the error handling and the repeat.

      A function is the obvious choice here.

      .. admonition:: Try This!

         Run the program on the original tab, but enter a letter or
         other nonsense input instead of a number.

         How would you fix this?  Try it!
         

      More repetition.
      How many times is the number ``20`` used in this program?

      If you wanted to change the max number of guesses to 10,
      how many places do you need to remember?
      And this is just one file.
      These kinds of duplications can become painful to
      maintain as programs grow.
      They can quickly get out of control.

      Finally, pet peeves of mine:

      This code is mostly redundant.
      I just prefer not to see code that looks like this, even though it works.

      .. code-block:: cpp

         if(answer == 'n' || answer == 'N' || answer == 'y' || answer == 'Y') {

      I would rather use a function:

      .. code-block:: cpp

         char play_again() {
           return std::tolower(
               get_entry("Would you like to play another game? [y/n] ").front());
         }

         // and use it like this
         while ('y' == play_again());

      instead of:

      .. code-block:: cpp

         while(true) { // Loop to ask user is he/she would like to play again.
            // Get user response.
            std::cout << "Would you like to play again (Y/N)? ";
            std::cin >> answer;
            std::cin.ignore();
			
            // Check if proper response.
            if(answer == 'n' || answer == 'N' || answer == 'y' || answer == 'Y') {
               break;
            } else {
               std::cout << "Please enter \'Y\' or \'N\'...\n";
            }
         }



      Is this comment helping?

      .. code-block:: cpp

         // Get number.
			std::cout << "Enter a number between 1 and 100 (" << 20 - tries << " tries left): ";

      .. code-block:: cpp

         // Safely exit.
         std::cout << "\n\nEnter anything to exit. . . ";
         std::cin.ignore();

      Please don't ask me to enter an additional confirmation to exit,
      when I **just** said 'No' to the previous question.

      There is no need to do this. What is *safe* about this?
      Just exit your program.

   .. tab:: Final

      Open this in Replit and run ``./main`` in the console tab.
      You may need to type ``make main`` first.


      .. raw:: html

         <iframe height="400px" width="100%" 
          src="https://repl.it/@DaveParillo/NumberGuessingFunctionRefactor?lite=true" 
          scrolling="no" 
          frameborder="no" 
          allowtransparency="true" 
          allowfullscreen="true" 
          sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
       

      This is **NOT** the only way to improve the original program.
      It's merely one way.

Notice the finished program isn't shorter than the original.
That was not our goal.
It rarely is.
We made the program *clearer* and easier to reason about.
While we were at it, we fixed some bugs and made it a bit more reusable and maintainable.


-----

.. admonition:: More to Explore

   - C++ Core Guidelines for :guidelines:`functions <S-functions>`
   - :cpp:`Unit testing library list <links/libs#Testing>`
   - A very brief description of 
     "`extract method <http://refactoring.com/catalog/extractMethod.html>`_" from Martin Fowler's Refactoring site.
   - `ExtractMethod <http://c2.com/cgi/wiki?ExtractMethod>`_ discussion from the 
     `PortlandPatternRepository <http://c2.com/cgi/wiki?PortlandPatternRepository>`_ - the very first wiki


