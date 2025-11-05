..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

The ``main`` function
=====================
C++ programs are made up of functions and
every executable program must have exactly one function
named ``main`` that serves as the entry point for the program.
Libraries do not need a main, because they are intended to link
with another program that contains a main.
Several restrictions apply to the main function that 
don't apply to any other C++ functions. The main function:

- Does not need to be declared
- Cannot be overloaded
- Cannot be declared as inline or static
- Cannot have its address taken
- Cannot be called from your program

.. index:: argc, argv
   pair: coliru; command line argument parsing
   pair: coliru; parsing command line arguments


.. tabbed:: function_simple_main

   .. tab:: main

      There are only a few main signatures that are valid entry points:

      .. code-block:: cpp

         // if main takes no arguments
         int main()

         // if main takes command-line arguments
         int main(int argc, char* argv[])

      The names ``argc`` and ``argv`` are traditional.
      You could use any valid identifier, but most programs use these.

      - ``int argc``: the total number of arguments in argv, strings separated by *white space* (space or tab characters)
      - ``char *argv[]``: an array of these strings

        ``char *argv[]`` can also be specified as ``char **argv``, 
        which is the same thing, if you remember pointers from your first semester.
        If not, we'll cover it soon.

      Some compilers allow passing the current system environment variables
      as a third argument passed into main.
      The environment variables are also passed in as an array of C strings.

      .. code-block:: cpp

         int main(int argc, char** argv, char** envp)


      If the linker can't find a function that evaluates to one of the above,
      then it will fail and your program build is incomplete.

   .. tab:: Run It

      A simple :index:`command line argument` handling program.
      `Compile, link, run (coliru) <https://coliru.stacked-crooked.com/>`__ provides a c++
      compiler and a very basic command line.

      Press the "edit" button and then 'Compile, link and run" to compile and run the program.

      .. raw:: html

         <div>
         <iframe height="600px" width="100%" src="https://coliru.stacked-crooked.com/a/c4e50db1d3dea7cb" scrolling="yes" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
         </div>

      Replit provides an interactive shell.
      You can run this program manually in the shell by typing

      .. code-block:: text

         ./main


Another convention is to store the name of the program as invoked on the 
command line in ``argv[0]``.
One side effect of this is that ``argc`` is **never** equal to zero and
the array ``argv`` always contains at least 1 c string.

**Why bother with command line programs?**

Command line arguments make programs more flexible.
They allow users to run the same program in different ways,
often to provide more or less detailed output or otherwise
change the behavior at runtime.

C++ is primarily used in *systems programming* and
is a fundamental part of all *\*nix* programs.
*\*nix* is short for *Unix* (and friends), *MacOS X*, and *GNU/Linux*.
The combination of command line argument handling and
taking input from *standard input* and
writing output to *standard output*
is the core around which most *\*nix* programs are designed.

.. index:: 
   pair: graph; command line arguments

Parsing command line arguments
------------------------------
Parsing the command line is all about getting the user entered
C strings from the command line and into our program in a
useful form.

The important thing to remember is that ``argc`` and ``argv`` are 
passed automatically to main and are available for use.
If you run a program named ``foo`` invoked as::

   /home/dave/foo -n 10 www.sdmesa.edu

Then ``argc`` would be set = ``4`` and array ``argv`` would contain
4 arrays of length 15:

.. graphviz::
   :align: center
   :alt: The two dimensional array argv

   digraph argv {
     rankdir=LR
     fontname = "Bitstream Vera Sans"
     label="The two dimensional argv array"
     node [
        fontname = "Bitstream Vera Sans"
        fontsize = 14
        shape = "plain"
     ]
     argv0 [label="argv[0]"];
     argv1 [label="argv[1]"];
     argv2 [label="argv[2]"];
     argv3 [label="argv[3]"];

     edge [style = invis;]
     node [
        fontname = "Bitstream Vera Sans"
        fontsize = 14
        shape = "record"
        style=filled
        fillcolor=lightblue
     ]
     arr0 [
        label = "{/|h|o|m|e|/|d|a|v|e|/|f|o|o|\\0}"
     ]
     argv0 ->  arr0;
     arr1 [
        label = "{-|n|\\0| | | | | | | | | | | | }"
     ]
     argv1 -> arr1;
     arr2 [
        label = "{1|0|\\0| | | | | | | | | | | | }"
     ]
     argv2 -> arr2;
     arr3 [
        label = "{w|w|w|.|m|e|s|a|.|e|d|u|\\0| | }"
     ]
     argv3 -> arr3;

     argv0 -> argv1 -> argv2 -> argv3

     {rank=same; argv0 argv1 argv2 argv3}

   }

Different program ``foo`` invocations would result in different values for argc and argv.

There is nothing special about the character ``-``.
It is a convention used to distinguish command line arguments
with special meaning (the switches) from other content.

.. index::
   pair: coliru; echo
   pair: coliru; command line argument parsing
   pair: coliru; parsing command line arguments

.. tabbed:: tab_cmdline

   .. tab:: echo

      A simple :index:`echo` program can demonstrate using command line parameters
      in a program.

      `coliru <https://coliru.stacked-crooked.com>`__ is a website that provides a
      a simple C++ compiler and some command line access online.
      Press the "compile, link, and run" button to run the program on the command line.

      You can run this program with different parameters by typing additional arguments after the:

      .. code-block:: text

         && ./echo

      .. raw:: html

         <div>
         <iframe height="600px" width="100%" src="https://coliru.stacked-crooked.com/a/1d4bde960431d139" scrolling="yes" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
         </div>


      .. admonition:: Try This!

         Run ``echo`` with a variety of inputs, such as:

         .. code-block:: text

            San Diego
            "Mesa College"

         Can you explain the differences?

   .. tab:: Parsing values

      Everything that is passed to main through ``argv`` is a C string.
      If you expect to receive a number on the command line,
      you need to transform the value from a character array
      into the appropriate numeric value yourself.

      Traditional command line argument parsing proceeds as follows:

      .. code-block:: bash

         foreach argument
         do
            if the current value equals an expected value
               process the argument
            else if the current value equals a different expected value
               process the argument
            else
               let the user know we received something unexpected
            done if
         done foreach

      There are many ways to check if two character arrays are equivalent.
      In this example, we use :index:`strcmp`:

      .. code-block:: cpp

         if (std::strcmp(argv[i], "-h") == 0) {
           // display help text
           break;
         }

      The strcmp and related functions are defined in the legacy
      C string header ``<cstring>``.
      The function compares two null-terminated byte strings 
      lexicographically (the way they would sort alphabetically).
      The sign of the result is the sign of the difference between the 
      values of the first pair of characters 
      (both interpreted as unsigned char) that differ in the two strings.
      The behavior is undefined if either argument are not pointers to
      null-terminated strings.

      If the function returns ``0``, the the two arrays are considered
      equivalent.

      Sometimes a command line argument is used to communicate that a 
      value of a particular type is expected to follow.
      Let's say we want our hello world program to repeat its message
      a certain number of times.
      We need a way to communicate this information to the program.

      .. code-block:: cpp

         if (std::strcmp(argv[i], "-r") == 0) {
           // We should try to repeat, 
           // increment the loop counter based on argc
           ++i;
           if (i < argc) {              // is there really a next argument?
               repeat = std::stoi(argv[i]);
           } else {
             std::cerr << "Error using '-r' argument: no repeat value provided\n";
         }

      There are many other ways to process the command line and many
      libraries exist to aid in the task.
      The technique presented here is simple and only uses facilities from
      the standard library.

   .. tab:: Run It

      .. raw:: html

         <div>
         <iframe height="600px" width="100%" src="https://coliru.stacked-crooked.com/a/3ccefe74d19c4f22" scrolling="yes" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
         </div>

      .. admonition:: Try This!

         Run this program with a variety of inputs and see what happens.

         Try passing no arguments or switches, 
         the same switch more than once,
         and a switch with no value after it.

A common source of confusion is distinguishing between 'standard input'
and the command line.
Parameters passed to a program after the program name are only
stored in the array ``argv``.
Most operating systems allow you to use the special characters
``<``, ``>`` (:index:`redirection operators`)
and ``|`` :index:`pipe operators` to direct data into the :index:`standard input`
of a program.
Information sent to a program using redirection or pipes is immediately
available for use by any facility that can process the standard input
stream, such as :io:`cin`.

You can also use :index:`cin` to manage a 'scripted conversion'
with a user, where you prompt for input using :index:`cout`
and process the input using cin, however,
processing standard input using redirection is
far more flexible in terms of creating reusable programs that
work together.

This idea is the foundation of :index:`Unix` and its many derivatives,
including :index:`GNU/Linux` and :index:`Mac OS`.

-----

.. admonition:: More to Explore

   - `Using the getopt function <https://www.gnu.org/software/libc/manual/html_node/Using-Getopt.html>`_ - from gnu.org
   - Textbook: :doc:`../pointers/pointers`
   - From cppreference.com:

     - :io:`cin`, :io:`cout`, and :io:`cerr`
     - :cstring:`strcmp`, and :cstring:`strncmp`
     - :string:`stoi <stol>`, and :cstring:`strtol`



