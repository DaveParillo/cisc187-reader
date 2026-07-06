..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| unicode:: U+2014 

.. index:: 
   single: iterator pattern

Iterator pattern
================
The :lang:`range-for` loop works because the function
expects a standard interface the loop can use to establish
basic facts about the range of elements in the sequence:

- Where does the sequence start?
- Where is the next element?
- When does the sequence end?

  This last question can alternatively be asked as
  *"Is there a next element?"*

 
Most OO languages solve this problem using a form of the
iterator design pattern.

.. mermaid::
   :alt: A notional iterator pattern UML diagram
   :align: center

   classDiagram
      client --> map : uses
      map *-- map_iterator
      iterator <|-- map_iterator
      iterator <|-- list_iterator
      client --> list : uses
      list *-- list_iterator

      class iterator {
         +first() virtual
         +has_next() virtual
         +next() virtual
      }

      class list_iterator {
         +first()
         +has_next()
         +next()
      }

      class map_iterator {
         +first()
         +has_next()
         +next()
      }


Because design patterns represent general ideas about solving
classes of problems, they are language independent.
In the case of :term:`iterators <iterator>`,
the idea has solutions in most modern languages, including C++.
Each language generally provides iterators using a design
appropriate for the language. 
C++ is no different.

C++ implements iterators using pointer semantics and an
*Iterator* base class is generally avoided in C++ iterators.
Since classes can overload all of the pointer operations,
an iterator can be implemented that exposes a pointer interface.

The key advantage to this solution is that functions can be
written more generically.
Functions interact with a simple, consistent and well-known
interface that works both for user defined types,
built-in pointer types, and arrays.
However, this solution does require an "end" iterator to test for equality.

Each STL container class provides an :term:`iterator` class
that clients can use to retrieve the correct 
:term:`element` from the :term:`container`.

.. digraph:: iterator
   :align: center
   :alt: Container iterators

   graph [
        fontname = "Bitstream Vera Sans"
        fontsize = 14
        labelloc = b
        label = "Begin and end iterators"
        nodesep = 0.5
   ];

   node [
        fontname = "Bitstream Vera Sans"
        style=filled, fillcolor=lightblue
        fontsize = 14, label=""
        shape = "box",  width=0.5, height=.25
   ];

   a -> b -> c -> d -> e -> f [constraint=false, arrowhead=vee, arrowsize=0.5];
   c [label=". . .", fillcolor=none, color=white];
   f [style=dotted];
    
   node [shape=none]
   begin [label="begin()", fillcolor=none]
   end [label="end()", fillcolor=none]
    
   begin -> a;
   begin -> b [weight=2, style=invis];
   end -> f;
   end -> e [weight=2, style=invis];

   {rank=same; a b c d e f};
   
The element defined by ``begin()`` is part of the sequence.

The element defined by ``end()`` is **not part** of the sequence.
In C++, the ``end`` iterator is always one past the end of the sequence.
Forgetting this is a common source of error.

-----

.. admonition:: More to Explore

  - :cpp:`Iterator Library <iterator>` at cppreference.com
  - :cpp:`C++ Concepts: Iterator <named_req/Iterator>`
