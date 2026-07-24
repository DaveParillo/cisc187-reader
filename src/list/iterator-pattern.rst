..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| replace:: --

.. index:: 
   single: iterator pattern

Iterator pattern
================
The :lang:`range-for` statement works because C++ defines a standard
iterator interface that the compiler can use to establish basic facts
about the range of elements in the sequence:

- Where does the sequence start?
- Where is the next element?
- When does the sequence end?

  This last question can alternatively be asked as
  *"Is there a next element?"*

 
Many object-oriented languages solve this problem using a form of the
iterator design pattern. A typical object-oriented design might look like
this:

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
C++ is no different, but it does not normally use this inheritance-based
design for standard-library iterators.

C++ iterators have pointer-like syntax, and an
*Iterator* base class is generally avoided. Instead, an iterator type
supports the operations required by its iterator category. Since classes
can overload pointer-like operators, an iterator can expose a familiar
interface without using virtual functions.

The key advantage to this solution is that functions can be
written more generically.
Generic algorithms interact with a simple, consistent and well-known
interface that works both for user defined types,
plain pointers, and arrays.
For classic container iterators, this solution uses a matching ``end``
iterator to test for the end of the sequence. Modern C++20 ranges can also
use a separate sentinel type for the end position.

Each C++ standard library container provides an :term:`iterator` type
that clients can use to identify a position in the :term:`container`
and access its :term:`elements <element>`.

The following notional diagram shows the kind of concrete class that can
implement a legacy bidirectional iterator. It is not an inheritance
hierarchy: the iterator meets its requirements by providing the required
operations. A real ``std::list<T>::iterator`` may have a different internal
layout.

.. mermaid::
   :alt: A notional C++ bidirectional iterator class diagram
   :align: center

   classDiagram
      class list~T~ {
         +iterator begin()
         +iterator end()
      }

      class list_iterator~T~ {
         -node* current
         +T& operator*()
         +bool operator==(iterator)
         +bool operator!=(iterator)
         +iterator& operator++()
         +iterator operator++(int)
         +iterator& operator--()
         +iterator operator--(int)
      }

      class node~T~ {
         +T value
         +node* next
         +node* previous
      }

      list~T~ ..> list_iterator~T~ : returns
      list_iterator~T~ --> node~T~ : traverses

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
   
The iterator returned by ``begin()`` points to the first element when the
sequence is not empty. For an empty sequence, ``begin() == end()``.

The iterator returned by ``end()`` is a past-the-end position, not an element,
and must never be dereferenced. For classic container iterators, it represents
the position one past the final element. Forgetting this is a common source
of error.

-----

.. admonition:: More to Explore

  - :cpp:`Iterator Library <iterator>` at cppreference.com
  - :cpp:`C++20 Concepts Library <concepts>`
  - :cpp:`C++20 Ranges Library <ranges>`
