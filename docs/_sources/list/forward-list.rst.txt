..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; forward_list
   pair: graph; std::forward_list

std::forward_list
.................
Like :container:`list`, 
the :container:`forward_list` is a container that stores elements in :term:`nodes <node>`
A :term:`forward list <singly linked list>` only defines pointers to the next node in the list.
This means that a forward list can only be traversed in the direction of the tail.

.. digraph:: list

   rankdir=LR;
   node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=record];

   head [shape=box];
   a [label="{ <data> 8 | <ref>  }", width=1.2]
   b [label="{ <data> 13 | <ref>  }"];
   c [label="{ <data> 21 | <ref>  }"];
   tail [shape=box];
   head:e -> a:w     [arrowhead=vee];
   a:ref:c -> b:data [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false, arrowsize=1.2];
   b:ref:c -> c:data [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false];
   c:ref:c -> tail:w [arrowhead=vee, arrowtail=dot, dir=both, tailclip=false];


The defining operations of a :container:`forward_list` are:

push_front
   Add a new element to the beginning of the list.

pop_front
   Remove an element from the beginning of the list.

front
   Get the value of the element at the beginning of the list.

Compared to :container:`list` this container provides more space efficient storage 
when bidirectional iteration is not needed.
A very light-weight container, 
it does not have any overhead compared to its implementation in C. 

-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - `STL iterator library <http://en.cppreference.com/w/cpp/iterator>`_
   - `Visualgo: lists <https://visualgo.net/en/list?slide=1>`_


