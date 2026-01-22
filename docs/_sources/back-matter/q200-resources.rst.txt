..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. index::
   pair: FAQ; more C++ resources

What other good C++ resources are out there?
============================================
Congratulations!
You made to the end of the semester and this book, now what?

First, take a well-earned rest.  
When you are ready to think about programming again,
consider the following for further exploration.

First, just for fun there is the
`Map of the C++17 Lands <http://fearlesscoder.blogspot.com/2017/02/the-c17-lands.html>`__.
Now that you have finished this material, 
you now know enough to see the humor in the map.

Coding challenges and puzzles
-----------------------------
If you haven't figured it out by now, I think the best way to learn to program 
in any language is by writing code.

- `exercism <https://exercism.org>`__ 
  Code practice and mentorship for everyone.
  Level up your programming skills with 2,545 exercises across 67 languages.
- `edabit <https://edabit.com>`__ - coding challenges for beginners
  in 8 different languages
- `Advent of Code <https://adventofcode.com>`__ - Help elves, learn to code.
  25 Puzzles per year since 2015.
  Technically 50 per year since each puzzle has 2 parts, each of which involves writing code.

  Puzzles can be solved using any programming language.
- `Codewars <https://www.codewars.com>`__ - coding challenges on medium level
- `LeetCode <https://leetcode.com>`__ - medium to difficult algorithm challenges
- `Project Euler <https://projecteuler.net>`__
  a series of challenging mathematical/computer programming problems that 
  require more than just mathematical insights to solve.

  Puzzles can be solved using any programming language.

  Although mathematics will help you arrive at elegant and efficient methods,
  the use of a computer and programming skills will be required to solve most problems.
- `C++ Quiz <http://cppquiz.org/>`__
  a simple online quiz you can use to test your knowledge of C++.
- `Code Chef <https://www.codechef.com>`__ 
  Code Chef is a not-for-profit educational initiative.
  They provide this platform as a way to practice and compete in friendly competition.
- `UVa Online Judge <https://uva.onlinejudge.org>`__
  online problems sets - some with published solutions.

Suggested reading
-----------------
Some of these books and articles have been around a long time,
but they are all classics that have retained considerable value.

First, a good, short blog post about
`how to teach yourself programming <http://norvig.com/21-days.html>`__.
Good advice.

- `A Philosphy of Software Design <https://web.stanford.edu/~ouster/cgi-bin/book.php>`__,
  John Ousterhout.
  A great and short book that does not require any special programming skill -
  targeted at students, but generally useful.

- `Code Complete <https://stevemcconnell.com>`__ A true compendium.
  Which may be a 'pro' or a 'con' for you.

  Originally written in 1993 and redone in 2004,
  it is a collection of software best practices with essentially no competition.
  Years later, there remains little to disagree with

- `The Pragmatic Programmer <https://pragprog.com/book/tpp/the-pragmatic-programmer>`__.
  I really like the style of this book.

  It’s thin & you can read it in any order.
  You can skip around or read it straight through.

  It’s primary focus is on honing the behaviors that turn OK programmers into great ones.
  If you read this, you see may similarities between sections in Code Complete.
  This is just less comprehensive - it’s ‘agile’!

- Chapter 16 of the 
  :wiki:`Mythical Man-Month <The_Mythical_Man-Month>`: *No silver bullets*.

  This book gets a lot of endorsements, but honestly,
  I think most of it is not too relevant to modern computing problems,
  with a few exceptions.
  The "No silver bullets” chapter complements the ‘religion’
  section at the end of Code Complete.

- *The Design of Everyday Things*, Don Norman and 
  *The Inmates are running the Asylum*, Alan Cooper.

  These two books are focused on how people interact with
  things in general (Norman),
  and software in particular (Cooper).
  Cooper’s main point is that knowing how to design
  a user interface is a distinct skill and
  you can’t just expect any old programmer
  to be a great designer - which is a point made by
  Fred Brooks in No Silver bullets,
  just in less space.
- Effective Java - yes Java.
- Effective C++
  (but it's a bit dated - along with parts of Effective C++,
  More Effective C++ and Effective Modern C++)

  You’ll find a lot of the material in Code Complete also mentioned these books as well.
  I prefer Effective Java over Effective C++, even though Josh Bloch was inspired to write
  Effective Java *by* Effective C++.
  His version is less specific -
  that has allowed it to stay relevant even though Java has changed a lot.
  I also like that Josh is not shy about calling out specifics where
  the design of the Java libraries was just wrong.
  He uses the design of 
  ``Object.clone()``, ``Object.notify()`` & ``wait()``, ``java.util.Date``,
  ``java.util.Stack`` and others as ways to point out how not to make 
  the same mistakes the creators of Java did.
  And he should know - he is one of them.

  One of the interesting things about the Effective C++ series is that you can see how the
  design of the language has evolved over the last 15 or 20 years.
  For example:

  - Effective C++ says to prefer new & delete over malloc & free
  - More Effective C++ says to prefer smart pointers over new & delete

- http://www.open-std.org is a bare bones site with a huge amount of detailed information
  related to open standards: C, C++, Python, Vulnerability information, and more.

- `Working Well with Legacy Code <https://www.cloudbees.com/blog/working-well-with-legacy-code>`__

  A clear, approachable article providing insights and strategies for dealing
  with legacy codebases.
  Thanks to Tracy Cavanaugh and the young ladies of
  `Mrs. C’s High School Club <https://www.mrscshighschoolclub.org>`__
  for this recommendation.

  Their suggestion is timely because legacy code has been on my mind lately.

  Working with legacy code matters because it represents the accumulated
  knowledge, decisions, and solutions of the past. Mastering it allows
  programmers to preserve functionality, reduce technical debt, and
  build a foundation for future innovation. By understanding and improving
  existing systems, developers gain insight into software design, architecture,
  and maintainability which are valuable skills on the journey from apprentice
  to mastery.


