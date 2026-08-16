..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

 
.. index:: comments
   single: commenting anti-patterns
   single: commenting best practices


Code comments
=============

You should have learned different formats for code :cpp:`comments`

.. code-block:: cpp

   // a one line comment
   std::cout << "Hello C++!" << std::endl;  // this is a comment
   puts("Hello C!");
   /*
   a block comment
   printf("Hello Alice!\n");
   printf("Hello %s!\n", "Bob");
   */

What you may not have have learned is **when** to use comments.
This is partly a stylistic discussion, and some people have very strong feelings
about the use of comments in software.
These opinions range from "never use them, ever", to enormous comment blocks
at the top of every source file and before each function.
Others expect a line of code at the end of nearly every line of source.

I am not any of these people.

The primary focus of this course is on **clarity**.

- The goal of any program in any language is to express ideas in code
  as *clearly as possible*.
- If you can do that without writing any comments, great.
- If you need to explain some piece of code, add a comment.

  Although, a better solution is usually to rewrite the confusing code
  so that it doesn't need clarification with a comment.

Comments should always and only state things that cannot be captured well
in regular code.  For example:

- What are the boundary conditions or limitations of the code.
- What preconditions must exist before using the code?
- What postconditions are guaranteed to exist?  Is there a "minimum guarantee"?
- For an algorithm, why was this or that method chosen?

One notable exception to the 'keep comments to a minimum' rule is
if you are commenting a public :term:`API` for a library 
and most readers will only see generated documentation and not the
source code.

In that case, you are generally adding comments to be read by a
documentation parser/generator such as
`Doxygen <https://www.doxygen.nl/index.html>`__.
For example:

.. code-block:: cpp

   /**
    * <A short one line description>
    *
    * <Longer description>
    * <May span multiple lines or paragraphs as needed>
    *
    * @param  Description of method's or function's input parameter
    * @param  ...
    * @return Description of the return value
    */

Comments in assignments
-----------------------

In this course, I also need everyone to assert that their work is their own.
For that reason, the top of every source file should contain your name and student ID:

.. code-block:: cpp

   // file.cpp
   // Dave Parillo, 123456789


Commenting "anti-patterns"
--------------------------

An :term:`anti-pattern` is a common response to a recurring problem 
that is ineffective.
Anti-patterns represent examples that you **should not** copy!
As bad as they are, they can still be instructive.

.. tb-reveal::
   :name: reveal-1
   :showlabel: Show Comment Anti-Patterns
   :hidelabel: Hide Comment Anti-Patterns

   In case you are wondering,
   these anti-patterns are all actual code examples I have received in the past.

   One of my pet peeves is writing comments that say **exactly** what the code
   already says.

   .. code-block:: cpp

       help(argv[0]);   //passing the 1st arg. to func. help.

       for (int i=0; i<10; ++i)       // loop from 0 to 9
       {
         printf("counter: %d\n", i);  // print counter
       }

   Perhaps this is not obvious, but what is wrong here:

   .. code-block:: cpp

       int main( int argc, char* argv[] )  //or alternately char**arg[]

   .. tb-reveal::
      :name: reveal-1-1
      :showlabel: What is Wrong?
      :hidelabel: Hide

      The comment is actually telling a lie: the alternative will not compile!

   .. code-block:: cpp

       // from a file named "average.cpp"

       int number;          // number of values in the set
       double value;        // value entered at keyboard
       double average;      // average value
       double total;        // sum of all values
       char again = 'y';    // repeat running the program
       char validElement;   // consider sentinel value -1 is valid

       // what is wrong with this code block??
       if (total != 0)
         average = total / number;  // calculate the average value

       fflush(stdin); // empty input buffer
       cin.get();     // read in a character


   The following series of code blocks are a combination of several commonly provided anti-patterns
   that have been combined into a single example.

   This first code block is composed of comments that add no value.
   There is only 'noise'.
   Every comment merely says basically the same thing as the code, just not as well.

   Also, we know we are in trouble in this program as the variable names provide little
   hint about anything this program might actually do.

   .. code-block:: cpp

      // The FooCalculator class calculates a Foo.
      // @author Dave Parillo
      struct FooCalculator {
        // The Integer maxFoo defines the maximum foo
        int maxFoo = 100;
        // The Integer foo defines the current foo.
        int foo = 0;
        // The member thing is an array of strings.
        std::string thing[100];
      };

      FooCalculator f;

   In this second block, which ``isFooSmallEnough`` appears to describe
   what this function is doing, the comments again, add nothing.

   The comments for ``rammer`` and ``rammerstat`` add no value and are actually misleading,
   since neither function appears to actually compute anything.

   .. code-block:: cpp

      // The isFooSmallEnough method determines if the foo is small enough
      // @return boolean {@code true} if foo is smaller than max
      // @return boolean {@code false} if foo is larger than max
      bool isFooSmallEnough() {
        return f.foo < f.maxFoo;
      }

      // Compute a rammer
      void rammer(std::string stat) {
        if (isFooSmallEnough()) {
          f.thing[f.foo++] = stat;
        }
        std::cout << stat << '\n';
      }

      // Calculate the ramerstat function.
      // @param rammer  A String that stores the rammer value
      void rammerstat(std::string x) {
          std::ifstream ram(x);   
          std::string stat;
          while (getline(ram,stat)) {
            rammer(stat);
          }
          ram.close();
      }

   The only comment here tells us what we already know.
   It would be nice to know what is expected of ``args`` that are passed into our
   nasty little program, but perhaps the author thought that was obvious?

   ::

      // Main is a global function.
      int main(int argc, char** argv) {
        if (argc > 1) {
          for (int i = 1;i < argc; ++i) {
            rammerstat(argv[i]);
          }
        } else {
          puts ("Usage: foo-comments args");
        }
      }

   What *does* this program do if compiled and run?

The preceding advice may conflict with what you have been told in the past 
about commenting your code.
Don't worry too much about that for now.
Remember the focus is on **clarity**, not how many comments you write.
Eventually some future employer will require you to (hopefully) adhere to 
some coding standard and you should follow that guidance when you encounter it.

Commenting Dos and Don'ts
-------------------------
I spent a lot of time saying how not to write comments.
How *should* you?

First, avoid the four common excuses related to comments.
In other words, I don't need to write comments because:

- Good code is self-documenting.

  There are many things that can't be expressed in code.
  
  - *Why* a particular feature was implemented.
  - What information callers need beyond what is available in the function signature.

  If you never write comments, then you can never explain these important details.

- I don't have time to write comments.

  Writing good comments takes far less time then writing good code.
  Writing comments first can help make your designs better and prevent rework.
  With that in mind, comments are a net time-saver.
- Comments get out of date and become misleading

  This often happens when people write documentation 'far' away from the code being documented.
  If the comments go stale it is because the code changed, but the comments did not.
  Keeping code and comments close minimizes this problem.

- Comments are worthless, why bother?

  Arguably, the most valid excuse.
  However, just because other comments are bad does not mean you should not write comments yourself.



The overall idea behind comments is to capture information that was in the mind of the designer
but couldn't be captured or expressed in code.

- Comments should describe things that aren't obvious from code.
- Pick a commenting convention and use it consistently.
  In this course, I generally use the conventions from the tool Doxygen.
- Don't repeat what code says in comments.

  - Use different words in the comments from the name of the things being described.

- Focus on *what* and *why*, not *how*

  The code says *how* an entity is defined or performed.
  Comments help readers understand *what* the code is doing.

- Write comments before writing code.
  Use comments as part of the design process when writing code.
- Avoid duplicate comments in the same way we strive to avoid duplicate code.
  


-----

.. admonition:: More to Explore

   - :cpp:`comments`
   - Jeff Atwood's blog: `Code tells you how, Comments tell you why <https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why>`_
   - Eric Lippert's Blog: `One more thing about comments <https://learn.microsoft.com/en-us/archive/blogs/ericlippert/aaargh-part-six-one-more-thing-about-comments>`_
   - `A Philosphy of Software Design <https://web.stanford.edu/~ouster/cgi-bin/book.php>`__,
     John Ousterhout. Chapters 15 and 16 focus on comments.

   - `Doxygen <https://www.doxygen.nl/index.html>`__

