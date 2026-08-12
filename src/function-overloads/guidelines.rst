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

   .. tb-group::
      :name: side_effects

      .. tb-tab:: Side effects

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

      .. tb-tab:: Run It

         .. tb-code:: cpp
            :name: functions_guidelines_side_effects_ac

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

.. tb-video:: https://www.youtube.com/watch?v=9mWWNYRHAIQ
   :name: youtube-9mWWNYRHAIQ

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
If you can't describe what a function is doing in a single, simple sentence, 
this is a sign that maybe you need to restructure your code. 
Having a function that does more than one thing (or does different things depending on its arguments) 
is likely to lead to confusion.

So, for example, this is not a good function definition:

.. code-block:: cpp

   // This code is an anti-pattern.
   // It's an example of how NOT to write a function.

   /** 
    * If get_max is true, return maximum of x and y,
    * else return minimum.
    */
   int compute_min_or_max(int x, int y, bool get_max) {
     if(x > y) {
       if(get_max) { 
         return x;
       } else {
         return y; 
       }
     } else { 
       if(get_max) { 
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
   constexpr int maximum (int x, int y) {
     return (x < y) ? y : x;
   }

   // return the minimum of x and y
   // if x == y, return y
   constexpr int minimum (int x, int y) {
     return (y < x) ? y : x;
   }

   constexpr int compute_min_or_max(int x, int y, bool get_max) {
       if(get_max) {
         return maximum(x, y);
       }
       return minimum(x, y);
   }

   // or more compactly:
   constexpr int compute_min_or_max(int x, int y, bool get_max) {
     return get_max ? maximum(x,y) : minimum(x,y);
   }

   
Is this *slightly* more typing? Yes.
At the end of the day, you will be far happier testing and debugging the three simpler functions
than the first version.
Your future co-workers will thank you.

.. note::

   Also be aware the C++ standard library provides functions
   :algorithm:`std::min <min>` and
   :algorithm:`std::max <max>`,
   which eliminate the need for our ``minimum`` and ``maximum`` entirely
   and have the advantage of working on any :term:`comparable` type.

   This would transform the previous example to:

   .. code-block:: cpp

      #include <algorithm>

      constexpr int compute_min_or_max(int x, int y, bool get_max) {
        return get_max ? std::max(x,y) : std::min(x,y);
      }

.. index::
   pair: repl.it; number guessing
   pair: repl.it; command line argument parsing
   pair: repl.it; parsing command line arguments

Example: number guessing
------------------------
A more realistic example might help.

.. tb-group::
   :name: function_guidelines_guessing_example_tab

   .. tb-tab:: Original

      While randomly surfing the internet I stumbled on a small program
      intended to help people understand C++.

      Unfortunately, it is full of issues and this is the kind of program structure
      that will **not** help you when trying to create your own complicated projects.

      As an interactive program it does not run in the textbook.
      Copy this program to your development environment and compile it locally.

      .. code-block:: cpp

         #include <iostream>
         #include <cstdlib>
         #include <ctime>

         int main(void) {
            srand(time(NULL)); // To not have the same numbers over and over again.

            while(true) { // Main loop.
               // Initialize and allocate.
               int number = rand() % 99 + 2; // System number is stored in here.
               int guess; // User guess is stored in here.
               int tries = 0; // Number of tries is stored here.
               char answer; // User answer to question is stored here.

               while(true) { // Get user number loop.
                  // Get number.
                  std::cout << "Enter a number between 1 and 100 ("
                            << 20 - tries << " tries left): ";
                  std::cin >> guess;
                  std::cin.ignore();

                  // Check is tries are taken up.
                  if(tries >= 20) {
                     break;
                  }

                  // Check number.
                  if(guess > number) {
                     std::cout << "Too high! Try again.\n";
                  } else if(guess < number) {
                     std::cout << "Too low! Try again.\n";
                  } else {
                     break;
                  }

                  // If not number, increment tries.
                  tries++;
               }

               // Check for tries.
               if(tries >= 20) {
                  std::cout << "You ran out of tries!\n\n";
               } else {
                  // Or, user won.
                  std::cout << "Congratulations!! " << std::endl;
                  std::cout << "You got the right number in " << tries << " tries!\n";
               }

               while(true) { // Loop to ask user is he/she would like to play again.
                  // Get user response.
                  std::cout << "Would you like to play again (Y/N)? ";
                  std::cin >> answer;
                  std::cin.ignore();

                  // Check if proper response.
                  if(answer == 'n' || answer == 'N' || answer == 'y' || answer == 'Y') {
                     break;
                  } else {
                     std::cout << "Please enter 'Y' or 'N'...\n";
                  }
               }

               // Check user's input and run again or exit;
               if(answer == 'n' || answer == 'N') {
                  std::cout << "Thank you for playing!";
                  break;
               } else {
                  std::cout << "\n\n\n";
               }
            }

            // Safely exit.
            std::cout << "\n\nEnter anything to exit. . . ";
            std::cin.ignore();
            return 0;
         }

      .. admonition:: Try This!

         How many bugs or other issues can you find in this program without looking at the 'Bugs' tab?


   .. tb-tab:: Bugs

      This program has several bugs.

      Code like:

      .. code-block:: cpp

         if(tries >= 20)

      seems to imply the loop stops cleanly after 20 tries.
      But the check happens after the program prompts for another guess,
      so the user can be asked for a 21st input when there are ``0`` tries left.
      That input is ignored because the loop breaks before checking it.
      Off-by-one errors like this are common.

      There is also a range bug in the random number expression:

      .. code-block:: cpp

         int number = rand() % 99 + 2;

      The prompt says the number is between 1 and 100, but this expression
      only produces values from 2 through 100. The program can never choose 1.


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

      Another input bug is repeated in several places:

      .. code-block:: cpp

         std::cin.ignore();

      This ignores only one character. If the user types extra characters,
      such as ``42abc`` or ``yes``, the leftover characters remain in the input
      stream and can break the next input operation.


   .. tb-tab:: Issues

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

      Another issue is the way the random numbers are created:

      .. code-block:: cpp

         int number = rand() % 99 + 2;

      Quick!

      Can we be **certain** that this correctly creates a number from
      1 to 100, inclusive?

      The code is just not that easy to reason about.

      - We have to know how rand works
      - We have to remember what modulus does.

      Yes, not big hurdles, but this is where bugs hide.
      The range bug described in the previous tab is an example of that.

      The standard library has a superior alternative to ``rand``:

      .. tb-code:: cpp
         :name: function_random_ac

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


      Because there are no functions, it is necessary to repeat blocks of code like this:

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
      Even though the following works, I just prefer alternatives.

      .. code-block:: cpp

         if(answer == 'n' || answer == 'N' || answer == 'y' || answer == 'Y') {

      Consider a function:

      .. code-block:: cpp

         char play_again() {
           return std::tolower(
               get_entry("Would you like to play another game? [y/n] ").front());
         }

         // and use it like this
         while ('y' == play_again());

      Useless comment. Are these comments helping?

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

   .. tb-tab:: Final

      ..  tb-group::

          .. tb-tab:: prompt

             Input is a separate concern from the game rules.
             Moving prompt handling into its own file gives the rest of the
             program one place to ask for validated text or numbers.
             That makes input errors easier to fix because the validation code
             is no longer scattered through ``main``.

             .. code-block:: cpp
                :name: prompt.h

                #ifndef MESA_CISC187_PROMPT_H
                #define MESA_CISC187_PROMPT_H

                #include <string>
                #include <string_view>

                // Get text input from the user
                // The only validation needed is for them to not enter nothing
                std::string get_entry (std::string_view prompt);

                // get integer input from the user, within the range (min .. max)
                int get_value (std::string_view prompt, int min=0, int max=100);

                #endif

             .. code-block:: cpp
                :name: prompt.cpp

                #include <iostream>
                #include <limits>
                #include <string>
                #include <string_view>

                #include "prompt.h"

                using std::cin;
                using std::cout;

                std::string get_entry (std::string_view prompt)
                {
                  cout << prompt;
                  std::string line;
                  while (getline(cin, line)) {
                    if (!line.empty())
                      break;
                    line.clear();
                  }
                  return line;
                }

                // attempt to read a single int from the user.
                int get_value (std::string_view prompt, int min, int max)
                {
                  std::cout << prompt;
                  std::string line;
                  int val = std::numeric_limits<int>::max();
                  while (getline(std::cin, line)) {
                    try {
                      val = std::stoi(line);
                      if (val < min || val > max) {
                        std::cerr << "Value out of range. Try again the range (" << min << ',' << max << "): ";
                      } else {
                        break;
                      }
                    } catch ( ... ) {
                      std::cerr << "Bad input, try again: ";
                    }
                    line.clear();
                  }
                  return val;
                }

          .. tb-tab:: guess

             The game logic is also separate from ``main``.
             The ``guess`` function owns one round of play: ask for guesses,
             compare them to the target number, count attempts, and report the
             result. This makes the game easier to read and gives the program a
             natural place to test or change the rules without touching startup
             code.

             .. code-block:: cpp
                :name: guess.h

                #ifndef MESA_CISC187_GUESS_H
                #define MESA_CISC187_GUESS_H

                // return true if the guessed number matches the goal value
                // and print a hint towards the goal
                bool guess_matches (int guess, int goal);

                // play the number guessing game
                // @param number is the number the user needs to guess
                void guess(int number);

                #endif


             .. code-block:: cpp
                :name: guess.cpp
  
                #include <iostream>
  
                #include "guess.h"
                #include "prompt.h"
 
                using std::cout;
 
                bool guess_matches (int guess, int goal) {
                  if(guess > goal) {
                        cout << "Too high! ";
                    return false;
                  }
                  if(guess < goal) {
                        cout << "Too low! ";
                        return false;
                  }
                    return true;
                }
 
                void guess(int number) {
                  constexpr int maximum_tries = 10;
                  int tries_remaining = maximum_tries;
                  while (tries_remaining > 0) {
                    if (guess_matches(get_value("Enter a number between 1 and 100: ", 1, 100), number)) {
                     break;
                    } else {
                      --tries_remaining;
                      cout << "Try again. (" << tries_remaining << " tries left)\n";
                    }
                  }

                  if (tries_remaining == 0) {
                    cout << "You ran out of tries!\n\n";
                  } else {
                    cout << "Congratulations!! \n"
                             << "You got the right number in "
                             << (maximum_tries - tries_remaining + 1) << " tries!\n";
                  }
                }

             .. admonition:: Something to consider

                Why did we choose to change the max number of tries
                from 20 to 10?

          .. tb-tab:: main

             The job of ``main`` is now small: create the random number
             generator, start each round, and ask whether to play again.
             That is an advantage of splitting out ``prompt`` and ``guess``:
             ``main`` describes the program at a high level instead of hiding
             that structure inside input loops and special cases.

             .. code-block:: cpp
                :name: main.cpp

                #include <iostream>
                #include <locale>
                #include <random>
 
                #include "guess.h"
                #include "prompt.h"

                // Helper to simplify the prompt in main.
                char play_again();
 
                int main() {
                  std::random_device r;
                  std::default_random_engine eng(r()); // make a random number generator
                  do {
                    int number = std::uniform_int_distribution<int>{1, 100}(eng);
                    guess(number);
                  } while ('y' == play_again());
                  std::cout << "Thanks for playing!\n";
                }
 
                char play_again() {
                  return std::tolower(
                     get_entry("Would you like to play another game? [y/n] ").front(),
                     std::locale());
                }



      This is **NOT** the only way to improve the original program.
      It's merely one way.

Notice the finished program isn't shorter than the original.
That was not our goal.
It rarely is.
We made the program *clearer* and easier to reason about.
While we were at it, we fixed some bugs and made it a bit more reusable and maintainable.

-----

.. admonition:: More to Explore

   - C++ Core Guidelines for :guidelines:`functions <s-functions>`
   - :cpp:`Unit testing library list <links/libs#Testing>`
   - A very brief description of 
     "`extract method <https://refactoring.com/catalog/extractFunction.html>`_" from Martin Fowler's Refactoring site.
   - `ExtractMethod <http://wiki.c2.com/?ExtractMethod>`_ discussion from the 
     `PortlandPatternRepository <http://wiki.c2.com/?PortlandPatternRepository>`_ - the very first wiki

   .. tb-video:: https://www.youtube.com/watch?v=9mWWNYRHAIQ&list=PLs3KjaCtOwSY34fFKyhOFovFlB7LikDwe&index=41

