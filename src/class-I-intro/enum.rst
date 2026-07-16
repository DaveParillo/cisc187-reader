..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: keyword; enum
   single: enumerated types

Enumerated types
================

An :lang:`enum` (enumerated type) is a distinct type whose value is restricted 
to a range of values (see below for details), 
which may include several explicitly named constants ("enumerators"). 
The values of the constants are values of an integral type known as the 
*underlying type* of the enumeration.

There are two distinct kinds of enumerations: 

unscoped enumeration
    declared with the keyword ``enum`` 
    
scoped enumeration
    declared with the enum-key ``enum class`` or ``enum struct`` 

Unscoped enumerations
---------------------

Each enumerator becomes a named constant of the enumeration's type 
(that is, name), 
visible in the enclosing scope, 
and can be used whenever constants are required.

.. code-block:: cpp

   enum color { red, green, blue };
   color r = red;
   switch(r)
   {
     case red  : std::cout << "red\n";   break;
     case green: std::cout << "green\n"; break;
     case blue : std::cout << "blue\n";  break;
   }

Each enumerator is associated with a value of the underlying type. 
When initializers are provided in the enumerator-list, 
the values of enumerators are defined by those initializers. 
If the first enumerator does not have an initializer, the associated value is zero. 
For any other enumerator whose definition does not have an initializer, 
the associated value is the value of the previous enumerator plus one.

Values of unscoped enumeration type are implicitly-convertible to integral types. 
If the underlying type is not fixed, the value is convertible to the first type 
from the following list able to hold their entire value range: 
``int``, ``unsigned int``, ``long``, ``unsigned long``, ``long long``, or ``unsigned long long``. 
If the underlying type is fixed, the values can be converted to their promoted underlying type.

.. code-block:: cpp

   enum color { red, yellow, green = 20, blue };
   color c = red; // c  implicitly converts to 0
   int n = blue;  // n == 21

Consider the following program:

.. tb-code:: cpp
   :name: unscoped-enum-problems
   :caption: Problems caused by unscoped enumerations

   #include <iostream>

   enum direction { north, south, east, west };

   void show_direction(int direction) {
     std::cout << "Direction: " << direction << '\n';
   }

   int main() {
     direction dir = west;
     show_direction(dir);
     int num = dir;
     show_direction(num);

     for (int i = north; i < 8; ++i) {
       show_direction(i);
     }
   }

.. tb-reveal::
   :name: reveal-enum-issues
   :showlabel: What problems does this program have?

   #. The unscoped enum ``direction`` is not type safe

      - Any integral type can be assigned to it

   #. The line ``int num = dir;`` assigns a direction to an int
   #. The for loop is unaware that there are only 4 directions, not 8.
   #. Function ``show_direction`` implies it takes a direction as an argument,
      but any integral type will be processed without complaint
   #. The function ``show_direction`` can't print a human readable direction.
      It can only print a number.

Scoped enums were introduced to address these specific shortcomings.

Scoped enumerations
-------------------
Like unscoped enumerations,
each enumerator becomes a named constant of the enumeration's type 
visible in the enclosing scope, 
and can be used whenever constants are required.

Unlike unscoped enums, scoped enums do **not** implicitly convert to integral types,
but can be converted with a static or explicit cast.

.. code-block:: cpp

   enum class color { red, green = 20, blue };
   color r = color::blue;
   switch(r)
   {
     case color::red  : std::cout << "red\n";   break;
     case color::green: std::cout << "green\n"; break;
     case color::blue : std::cout << "blue\n";  break;
   }
   // int n = r;                // error: no implicit int conversion
   int n = static_cast<int>(r); // OK, n = 21

.. cpp:: 23

   Starting in C++23, ``std::to_underlying`` provides a named standard-library
   function for the same conversion.
   These statements are equivalent:

   .. code-block:: cpp

      std::to_underlying(color::red)

      static_cast<int>(color::red)

All the C++ enumerated types are very simple compared to the same types in other languages.
However, it is easy to add features as needed.
Given the following scoped enum:

.. code-block:: cpp

   // If this were declared enum struct, nothing in this example changes...
   //
   enum class direction { north, south, east, west };

We can implement a stream overload to allow printing enum members with 
human readable strings:

.. code-block:: cpp

   std::ostream& operator<<(std::ostream& os, direction dir) {
     switch (dir) {
       case direction::north: return os << "north";
       case direction::east:  return os << "east";
       case direction::south: return os << "south";
       case direction::west:  return os << "west";
     }
     return os;
   }


And an array allows the enum to be used in a range for loop:

.. code-block:: cpp

   constexpr std::array directions {
     direction::north,
     direction::east,
     direction::south,
     direction::west
   };

Now the show directions program looks like this:

.. tb-code:: cpp
   :name: scoped-enum-directions
   :caption: Printing and iterating scoped enum values

   #include <array>
   #include <iostream>

   enum class direction { north, south, east, west };

   std::ostream& operator<<(std::ostream& os, direction dir) {
     switch (dir) {
       case direction::north: return os << "north";
       case direction::east:  return os << "east";
       case direction::south: return os << "south";
       case direction::west:  return os << "west";
     }
     return os;
   }

   constexpr std::array directions {
     direction::north,
     direction::east,
     direction::south,
     direction::west
   };

   void show_direction(direction dir) {
     std::cout << "Direction: " << dir << '\n';
   }
     
   int main() {
     direction dir = direction::west;
     std::cout << "Show one direction:\n";
     show_direction(dir);
     
     std::cout << "Loop through all directions:\n";
     for (const auto dir: directions) {
       show_direction(dir);
     }
   } 



Another example uses the same techniques to build a deck of cards.

.. tb-code:: cpp
   :name: class-enum-cards-ex1

   #include <array>
   #include <iostream>
   #include <vector>

   enum class rank {
     ace = 1, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
   };

   // Define an array of rank to allow range-for looping
   constexpr std::array ranks {
     rank::ace, rank::two, rank::three, rank::four, rank::five,
     rank::six, rank::seven, rank::eight, rank::nine, rank::ten,
     rank::jack, rank::queen, rank::king
   };

   enum class suit {
     clubs, diamonds, hearts, spades
   };

   // Define an array of suit to allow range-for looping
   constexpr std::array suits {
     suit::clubs, suit::diamonds, suit::hearts, suit::spades
   };

   struct card {
     rank card_rank;
     suit card_suit;

     card(rank r, suit s)
       : card_rank{r},
         card_suit{s}
     {
     }
   };

   std::ostream& operator<<(std::ostream& os, rank value);
   std::ostream& operator<<(std::ostream& os, suit value);
   std::ostream& operator<<(std::ostream& os, const card& value);

   // short, but take care . . . 
   // a change in the order of the enum could break this,
   // Assumes order: A,2,3,4,5,6,7,8,9,10,J,Q,K
   std::ostream& operator<<(std::ostream& os, rank value) {
     if (value > rank::ace && value < rank::jack) {
       os << static_cast<int>(value);
     } else if (value == rank::ace) {
       os << "Ace";
     } else if (value == rank::jack) {
       os << "Jack";
     } else if (value == rank::queen) {
       os << "Queen";
     } else {
       os << "King";
     }

     return os;
   }

   std::ostream& operator<<(std::ostream& os, suit value) {
     switch(value) {
       case suit::clubs:    os << "Clubs"; break;
       case suit::diamonds: os << "Diamonds"; break;
       case suit::hearts:   os << "Hearts"; break;
       case suit::spades:   os << "Spades"; break;
     }
     return os;
   }

   std::ostream& operator<<(std::ostream& os, const card& value) {
     return os << value.card_rank << " of " << value.card_suit;
   }

   int main() {
     std::vector<card> deck;
     for (const auto s: suits) {
       for (const auto r: ranks) {
         deck.emplace_back(r, s);
       }
     }
     for (const auto& c: deck) {
       std::cout << c << '\n';
     }
   }

-----

.. admonition:: More to Explore

   - From cppreference.com:

     - :lang:`Enumeration declaration <enum>`
     - :utility:`std::to_underlying <to_underlying>`
   - `Enumeration (Microsoft) <https://learn.microsoft.com/en-us/cpp/cpp/enumerations-cpp?view=vs-2019>`__
