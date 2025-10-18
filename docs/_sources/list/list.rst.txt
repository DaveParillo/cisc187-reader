..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; list
   pair: graph; std::list

The list class
==============
The :container:`std::list <list>` is a sequence container 
that stores data in :term:`nodes <node>`.
Each :term:`node` in a :term:`list` points to the next 
(and previous) node in the list.
Each node is a separate object that exists to encapsulate a piece of data
and to allow navigation to adjacent nodes.

.. graphviz::
   :alt: Linked list nodes

    digraph list {
       graph [
          rankdir=LR;
          //splines=ortho;
          compound=true;
          labelloc=b;
          label="Linked list nodes";
          ranksep = 1;
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
                 style=filled, fillcolor=lightblue,
                 shape=record, width=0.5, height=.25, label=""];

      
      subgraph cluster_h {
        labelloc=t
        label="head"
        head [label=" |next()| "]
      }

      subgraph cluster_a {
        labelloc=t
        label="Node A" 
        a [label="data|next()|prev()"]
      }

        subgraph cluster_b {
        labelloc=t
        label="Node B" 
         b [label="data|next()|prev()"]
      }

      subgraph cluster_t {
        labelloc=t
        label="tail"
         tail [label=" | | prev()"]
      }

      head:m-> a [lhead=cluster_a];

      a -> b [lhead=cluster_b];
      a:s -> head:s [lhead=cluster_h];

      b -> tail [lhead=cluster_t];
      b:s -> a:s [lhead=cluster_a];

      tail:s -> b:s [lhead=cluster_b];
    }

.. index:: 
   pair: graph; compact list

A more compact way to graphically represent our :term:`doubly linked list` is like this:

.. graphviz::
   :alt: A compact linked list diagram

   // doubly linked list
   digraph g {
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25];


       head [style=dotted, fillcolor=white];
       tail [style=dotted, fillcolor=white];

       head -> a -> b -> tail [ arrowhead=vee, arrowsize=0.5];
       tail -> b -> a -> head [ arrowhead=vee, arrowsize=0.5];

      {rank=same; head a b tail}
   }
   
A :term:`linked list` that stores a sequence of ``int``\s can be trivially implemented using a ``struct``:

.. code-block:: cpp

   struct node {
      int value;
      node* next;
      node* prev;
   };

The ``struct node`` contains a single value it 'owns',
plus pointers to adjacent nodes.


.. index:: 
   pair: graph; std::list

Creating a :term:`linked list` from such a 'home grown' ``struct`` is not complicated,
but it isn't pretty either:

.. sidebar:: An empty list

    .. digraph:: empty
       
       graph [
          nodesep=1,
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=dotted, 
             shape=box, width=0.5, height=.25];

       head -> tail [constraint=false];
       tail-> head [constraint=false];

.. code-block:: cpp

   // create an empty list
   node* head = new node;
   node* tail = new node;
   head->next = tail;
   tail->prev = head;


.. sidebar:: Insert node 'a' to our list

    .. digraph:: node_a

        graph [
           rankdir=LR,
           nodesep=1
        ];
        node [fontname = "Bitstream Vera Sans", fontsize=14,
              style=filled, fillcolor=lightblue, 
              shape=box, width=0.5, height=.25];

        head,tail [style=dotted, fillcolor=white];

        head,tail-> a
        a -> head, tail

.. code-block:: cpp

   // insert node a into the list
   node* a = new node;
   a->value = 61;
   a->next = tail;
   a->prev = head;
   head->next = a;
   tail->prev = a;

.. sidebar:: Insert node 'b' after a

    .. digraph:: node_b

       graph [
           rankdir=LR,
           nodesep=1
        ];
        node [fontname = "Bitstream Vera Sans", fontsize=14,
              style=filled, fillcolor=lightblue, 
              shape=box, width=0.5, height=.25];

        head,tail [style=dotted, fillcolor=white];

        head -> a -> b -> tail;
        tail -> b -> a -> head;

.. code-block:: cpp

   // insert node b after node a
   node* b = new node;
   b->value = 62;
   b->next = tail;
   b->prev = a;
   a->next = b;
   tail->prev = b;

At this point, we have created the basic structure shown in the first list diagram.
Once we have such a list, we can access all of the elements,
if we have a pointer to any one of them.
For example, to print all of the elements, we could:

.. code-block:: cpp

   node* p = head->next;
   while (p->next != nullptr) {
     std::cout << p->value << ' ';
     p = p->next;
   }


Which, given the list we created, will print ``61 62\0``.

Obviously, no one would want to use such a list.
Every trivial detail needs to be managed, and any program using it
would be more likely to leak memory or fail suddenly due to some programming error.

The :container:`std::list <list>` class hides all the implementation details and
provides a list with many convenient features:

.. code-block:: cpp

   #include <iostream>
   #include <list>
   using std::cout;

   void print_list(const list<int>&);

   int main () {
     std::list<int> list = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
     cout << "size: "  << list.size();
     cout << "\nfront: " << list.front();
     cout << "\nback: "  << list.back();

     cout << "\n\npush_back 13: ";
     list.push_back(13);
     cout << "\nsize: "  << list.size();
     cout << "\nback() " << list.back();

     print_list(list);

     return 0;
   }

   void print_list(const std::list<int>& list) {
     if (list.empty()) {
       cout << "list is empty.\n";
     } else {
       cout << "list contains:\n";
     }
     for(const int i: list) {
       cout << i << " ";
     }
     cout << "\n\n";
   }

The defining operations of a :container:`list` are:

push_back
   Add a new element to the end of the list.

pop_back
   Remove an element from the end of the list.

back
   Get the value of the element at the end of the list.

push_front
   Add a new element to the beginning of the list.

pop_front
   Remove an element from the beginning of the list.

front
   Get the value of the element at the beginning of the list.


.. note:: empty() vs. size() == 0

   In most containers, calling ``size()`` is constant time.

   That is it takes the same amount of time regardless of
   the number items in the container.

   Not so for lists.

   There are situations where a list cannot determine the size
   without traversing the range and counting them.

   In general, never assume ``size()`` is as efficient as ``empty()``.

   If you **really** want to know if a container is empty (or not),
   then call ``empty()``.

   If you **really** want to know the number of elements in a container,
   then call ``size()``.

   See *Effective STL*, for more details\ [1]_\ .

Underneath, the standard library ``list`` is not very different from the ``struct node`` above.
The primary characteristics are:

- All data is stored on the heap
- Node traversal is accomplished by following pointers from one node to the next
- Access based on an index is not allowed.
  This kind of access, called *random  access* describes
  the ability to compute a location in memory using a starting address and an offset.
  Arrays and vectors support random access.
  Linked lists do not.


-----

.. admonition:: More to Explore

   - `STL containers library <http://en.cppreference.com/w/cpp/container>`_
   - `STL iterator library <http://en.cppreference.com/w/cpp/iterator>`_
   - `Visualgo: lists <https://visualgo.net/en/list?slide=1>`_

.. topic:: Footnotes

   .. [1] Effective STL (Item #4) by Scott Meyers (Addison-Wesley Professional).  Copyright 2001 Scott Meyers, 978-0-201-74962-5.

