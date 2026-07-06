..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: std::string vs byte strings
   pair: byte string; C string
   single: string
   single: string abstractions

The string class
================
Like a byte string, a ``std::string`` is storage for a character sequence:

.. code-block:: cpp

   #include <string>        // access std::string functions
   
   using std::string;       // alias type std::string to 'string'

   int main() {
     string x;                          // empty string
     string greet =  "Hello, World!";   // create from C string
     string hello   ("Hello, World!");  // as above, constructor style syntax
     string howdy = {"Hello, World!"};  // C++11 only
     string howdy   {"Hello, World!"};  // as above, = is optional
     return 0;
   }

What is different is that a ``std::string`` is a full-fledged *object*.
It knows it's own size, and comes with many convenience functions.

Notice that unlike a built-in variable declaration such as ``int x;``,
the declaration ``string x`` is **not** incomplete.
The variable ``x`` is a complete and valid ``string`` object
that stores no characters.

.. index:: 
   pair: string functions; operator[]
   pair: string functions; operator+=
   pair: string functions; operator==

.. tb-group::
   :name: tab_string_simple

   .. tb-tab:: Simple operations

      .. tb-code:: cpp
         :name: string_simple_operator_ac1

         #include <iostream>
         #include <string>

         using std::string;

         int main() {
           string a = "hello";
           a += ", world!";        // joining strings is pretty easy

           // Copying or creating one string from another feels as natural
           // as a fundamental type.
           string b = a;

           if (a == b)             // Same goes for comparisons
           {
             // modify values
             b[0] = 'H';           // and a string feels like an 'array of char' 
             b[7] = 'W';
           }

           std::cout << a << '\n'; // and has stream support
           std::cout << b << '\n';

           return 0;
         }


   .. tb-tab:: front() and back()

      This tab shows alternate functions for accessing the first and last
      characters in a string.

      .. tb-code:: cpp
         :name: string_front_back_ac

         #include <iostream>
         #include <string>

         int main() {
           std::string value = "hello, world!";

           std::cout << "first: " << value.front() << '\n';
           std::cout << "last: " << value.back() << '\n';
           return 0;
         }

   .. tb-tab:: append()

      The ``append`` function allows you to append *N* copies of a character or
      an array of characters to the end of a string.

      .. tb-code:: cpp
         :name: string_append_ac

         #include <iostream>
         #include <string>

         int main() {
          using std::cout;
           std::string hi = "hello";
           std::string howdy = hi;

           cout << "original: " << hi   << '\n';

           hi.append(5, 'o');   // append 5 o's
           hi.append(", world!");
           cout << hi << '\n';

           cout << "original: " << howdy   << '\n';

           // append returns a new string value, so
           // calls to append can be chained together
           howdy.append(5, 'o').append(", world!");
           cout << howdy << '\n';

           return 0;
         }

   .. tb-tab:: insert()

      The ``insert`` function allows you to insert 1 character or
      an array of characters at a position in a string.

      .. tb-code:: cpp
         :name: string_insert_ac

         #include <iostream>
         #include <string>

         int main() {
           std::string value = "hello, world!";

           std::cout << "original: " << value << '\n';

           value.insert(0,3,'*');       // insert "***" at position 0
           std::cout << value << '\n';

           // insert a char array before the '!'
           value.insert(value.size()-1," (this means you)");
           std::cout << value << '\n';

           return 0;
         }

Using the :string:`operator[]<operator_at>` to access select characters in a string is,
like an array,
not range checked.
This means that if you use an index referring to an invalid position,
then your program might have undefined behavior, or fail unexpectedly.
You can use the function :string:`at` anywhere ``operator[]`` is allowed.
The ``at`` function is range checked.
While there is a cost associated with this check, 
if the index provided is out of range, 
then an :error:`std::out_of_range exception <out_of_range>` is thrown,
which must be caught,
otherwise the program will terminate.

.. code-block:: cpp

   if (a == b)
   {
     b.at(0)  = 'H';   // might be OK
     b.at(-1) = 'W';   // never OK.  throws exception
   }


Remember that a ``std::string`` is **not** a byte string.
``std::string`` is a class.
A decision was made long ago that in order to remain more compatible with
C, double quited strings should evaluate to byte strings.
Declarations like this are a common source of confusion for new programmers:

.. code-block:: cpp

   auto my_string = "Howdy!";


What type is ``my_string``?

.. tb-reveal::
   :name: reveal_my_string

   ``my_string`` is **not** a std::string.

   The default type for characters enclosed in double quotes is ``const char*``.

This is one of those situations where :lang:`auto` may not be deducing the type
you actually want.
There are several simple ways to use auto *and* get the type
deduced to be a ``std::string``.

.. tb-group::
   :name: string_auto_deduction

   .. tb-tab:: Example

      .. cpp:: 14

         Adds the concept of a *std::string literal* to the language.

         You can simply append an ``s`` to the end of the quoted string.
         This identifies the literal as type std::string instead of
         ``const char*``.

         .. code-block:: cpp

            auto my_string = "Howdy!"s;    // preferred

      Alternatively, you can call the string constructor explicitly, which
      works for C++ versions older than C++14.

      .. code-block:: cpp

         auto my_string = string("Howdy!");

         auto your_str  = string{"Howdy!"};  // C++11 initialization syntax

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: string_auto_deduction_ac

         #include <string>
         #include <iostream>
         #include <iomanip>  // std::quoted

         int main()
         {
             using namespace std::string_literals;
             using std::string;

             auto my_string = "Howdy!"s; 
             auto howdy2 = string("Howdy!");
             auto your_str  = string{"Howdy!"};  // C++11 initialization syntax

             string s1 = "abc\0\0def";
             string s2 = "abc\0\0def"s;

             std::cout << "s1: " << s1.size() << ' ' << std::quoted(s1) << '\n';
             std::cout << "s2: " << s2.size() << ' ' << std::quoted(s2) << '\n';
         }

      .. note::

         Look carefully at the size values printed for ``s1`` and ``s2``.

         Are those sizes expected? Why or why not?

.. index::
   pair: string functions; empty
   pair: string functions; find
   pair: string functions; find_first_of
   pair: string functions; rfind
   pair: string functions; size


Getting information out of a string
-----------------------------------

A ``string`` knows its own size and can provide other useful information.

.. code-block:: cpp
   
   #include <cassert>
   #include <string>
   using std::string;
   int main() {
     string my_string = "Hello";

     assert( my_string.size() == 5 );  // .length() is available also
     if (!my_string.empty()) {
       my_string += ", there.";       // my_string == "Hello, there."
     }
     return 0;
   }

And the string class provides many functions dedicated to finding substrings
within a string.

.. tb-group::
   :name: tab_find_string

   .. tb-tab:: Example: find

      The simplest example is the :string:`find` function.

      Given any string object, for example, this string:

      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 12
         :dedent: 3

      defined using the string literal syntax,
      creates a new object ``us``.

      Once we have a ``string``, calling the string member function 
      find always returns a position:

      - Either a position within the string, or
      - The special value :string:`std::string::npos<npos>` 
        which means the value was not found in the string.

      We can use this to check if we found what we were looking for:

      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 13-16
         :dedent: 3

      The position returned by find is a zero-based index
      into the string.

      Find can also take a sequence of characters.
      In that case, it returns the position to the first ``char``
      where the entire sequence is matched.

      **Reverse find**

      Similar to ``find``, :string:`rfind` performs the same
      task as find, but iterates through the string in reverse order:
      starting at the end and moving towards the first character.
      Keep in mind that the position returned is still based
      on the same index positions as regular ``find``.

      **Find first of**

      The :string:`find_first_of` function takes a ``char`` sequence,
      but unlike find where the entire sequence is used to find a match,
      ``find_first_of`` examines each character in the sequence,
      on at a time, and returns the *minimum position* of **any**
      of the characters listed as function arguments in the string.
      For example:

      .. literalinclude:: find-string.txt
         :language: cpp
         :lines: 17, 23
         :dedent: 3

      The function returns the position of 'e' in 'Hello world',
      even though 'e' and 'o' are both present,
      because 'e' is first.

      The order of the character arguments do not matter.
      The results would be exactly the same if the arguments were
      'uoiea'.
      Don't take my word for it, try it yourself.

   .. tb-tab:: Run It

      .. include:: find-string.txt

.. index::
   single: std::string::npos 

The special value :string:`std::string::npos<npos>` is used both as an end of string indicator
by functions that expect a string and
as an indicator of *not found* by functions that return an index (like find).

.. tb-video:: https://www.youtube.com/watch?v=nkKeA74p3RY
   :name: youtube-nkKeA74p3RY

.. index::
   single: stoi
   single: stod

Convert a byte string to a number
---------------------------------
Another common string task is parse a C string
and extract a numeric value.

The number conversion functions are part of the ``string`` header.
There are number conversion functions that C++ inherits from C.
They are all in the ``cstdlib`` header.
Of these C functions, the ``atoi`` and ``atof`` functions should not be used.
They fail silently.
That is if something bad happens, there is no way to check and even detect
whether the function completed its task.

Use :string:`stoi <stol>` and :string:`stod <stof>` instead.

.. tb-group::
   :name: std_string_numeric_conversion

   .. tb-tab:: stoi()

      :string:`stoi <stol>` extracts an integer value from a string.

      ``stoi`` discards any whitespace characters until the first non-whitespace
      character is found, 
      then takes as many characters as possible to form a valid integer
      number representation and converts them to an integer value.

      The valid integer value consists of the following parts:

      - an optional plus or minus sign
      - the digits 0-9

      .. tb-code:: cpp
         :name: byte_string_stoi_ac

         #include <string>
         #include <iostream>

         int main() {
             std::cout << std::stoi("42") << '\n';

             const char* str_pi = "3.14159";
             std::cout << std::stoi(str_pi) << '\n';
         }



   .. tb-tab:: stod()

      :string:`stod <stof>` extracts an floating point value from a byte string.

      Other than return value, it functions similarly to ``stoi``.

      .. tb-code:: cpp
         :name: byte_string_stod_ac

         #include <string>
         #include <iostream>

         int main()
         {
             std::cout << std::stod("42") << '\n';

             std::cout << std::stod("0.0000000123") << "\n"
                       << std::stod("0.012") << "\n"
                       << std::stod("15e16") << "\n"
                       << std::stod("-0x1afp-2") << "\n"
                       << std::stod("inf") << "\n"
                       << std::stod("Nan") << "\n";
         }




All of these functions allow for error handling, which we will cover in a future chapter.
For now, know that these function will generate errors if given bad or unexpected input.


.. index::
   pair: string functions; c_str

Converting a std::string to a C string 
--------------------------------------

You cannot use ``std::string`` in a function 
that expects ``const char*`` - you must convert it
to a null terminated character array.

.. code-block:: cpp

   auto my_name = "Alice"s;


   printf ("Hello again, %s\n", my_name);       // compile error!

   // the c_str() function converts a string into a c string
   printf ("Hello again, %s\n", my_name.c_str());


**Self Check**

.. tb-group::
   :name: tab-skill-check-string

   .. tb-tab:: Q1

      .. tb-blank::
         :name: string_fitb1

         Given the following:

         .. code-block:: cpp

            std::string x = "The rain in Spain. . . ";
            size_t pos = x.find("in");

         What is the value of ``pos``?

         {{blank}}

         .. tb-answer::
            :match: 6
            :feedback: Correct.
            :hint: 9; No. There is another substring 'in'
            :hint: 7; String positions are zero-based
            :hint: x; Try again.

   .. tb-tab:: Q2

      .. tb-parsons::
         :name: string_pp1
         :no-indent:

         .. code-block:: c

            {{group}}
            int main() {
            {{endgroup}}
            {{group}}
              std::string  us = "Team USA";
            {{endgroup}}
            {{group}}
              auto snowflake = us.find_first_of("Korea");
            {{endgroup}}
            {{group}}
              if (snowflake == std::string::npos) {
            {{endgroup}}
            {{group}}
                std::cout << "Did not find anything\n";
            {{endgroup}}
            {{group}}
              } else {
            {{endgroup}}
            {{group}}
                std::cout << "Found it!\n";
            {{endgroup}}
            {{group}}
              }
              return snowflake;
            {{endgroup}}
            {{group}}
            }
            {{endgroup}}

   .. tb-tab:: Q3

      .. tb-blank::
         :name: string_fitb5

         Given the following:

         .. code-block:: cpp

            #include <string>

            int main (){
              std::string s = "Donald Duck";
              int value = 0;
              if (s.find_first_of(' ') == s.find_last_of(' ')) {
                value = 3;
              } else {
                value = 5;
              }
              return value;
            }

         What value is returned from main?

         {{blank}}

         .. tb-answer::
            :match: 3
            :feedback: Correct.
            :hint: 0; In an if/else block one of the blocks must always be entered.
            :hint: 5; What positions are returned from both find statements?
            :hint: x; Try again.

-----

.. admonition:: More to Explore

   - cppreference.com :cpp:`Strings library <string>` overview
   - YoLinux `String class tutorial <http://www.yolinux.com/TUTORIALS/LinuxTutorialC++StringClass.html>`_
   - Bjarne Stroustrup's C++11 FAQ: `Raw String literals <https://www.stroustrup.com/C++11FAQ.html#raw-strings>`_
