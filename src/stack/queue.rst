..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: sequence containers; queue
   pair: graph; std::queue

The queue class
===============
A :container:`queue` is another special purpose container adapter
that limits random element access to all parts of the storage.
A *queue* is just another word for a line.
Like a stack, a queue restricts element access to the ends.
*Unlike* a stack, a queue allows access to both ends:

- New elements can only be added to the "back" of the line
- Elements can only be retrieved from the "front" of the line.

Imagine a line at the bank or a store.
An orderly queue means that the people who get in line first
are the first customers called.
This is the guarantee :container:`queue` enforces.
A queue is a FIFO (first-in, first-out) data structure.

The :container:`std::queue <queue>` is a container adapter that gives the programmer the 
functionality of a queue.

The class template acts as a wrapper to the underlying container - only 
a specific set of functions is provided. 
The queue pushes elements on the back of the underlying container, 
and pops them from the front.

.. graphviz::
   :align: center
   :alt: std::queue elements

   digraph g {
       graph [
          labelloc=b;
          label="std::queue elements";
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25, label=""];

       a,b,d,e;
       node [style=none];
       c [label=". . .", color=white];

       back [shape=none, label="back()"];
       front [shape=none, label="front()"];

       a -> b -> c -> d -> e [ arrowhead=vee];
       back -> a:w [dir=back];
       e:e -> front;

       node [style=invis] x,y;
       x -> a [style=invis];
       y -> e [style=invis];
       {rank=sink; a b c d e}
   }


   
.. index:: 
   pair: graph; queue operations

The defining operations of a :container:`queue` are:

push 
   Add a new element to the back (end) of the queue.

pop
   Remove an element from the front (beginning) of the queue.

front
   Get the value of the element at the beginning of the queue.

back
   Get the value of the element at the end of the queue.

.. graphviz::
   :align: center
   :alt: std::queue operations

   // shows push and pop, enqueue / dequeue
   digraph g {
       graph [
          labelloc=b;
          label="std::queue operations";
       ];
       node [fontname = "Bitstream Vera Sans", fontsize=14,
             style=filled, fillcolor=lightblue,
             shape=box, width=0.5, height=.25, label=""];


       o,z [style=dotted];
       a,b,d,e;
       node [style=none];
       c [label=". . .", color=white];

       back [shape=none, label="push()"];
       front [shape=none, label="pop()"];

       o -> a -> b -> c -> d -> e [ arrowhead=vee];
       e -> z [ arrowhead=none];
       back -> o [style=dotted];
       front -> z [style=dotted, dir=back];

       {rank=sink; o a b c d e z}
   }


Minor modifications change ``pop_all()`` from a function
performing ``stack`` operations into one
performing ``queue`` operations:

.. code-block:: cpp

   #include <iostream>
   #include <queue>

   #define QueueContainer typename

   template <QueueContainer C>
   void pop_all(C& q) {
     while(!q.empty()) {
       std::cout << q.front() << " ";
       q.pop();
     }
     std::cout << "\npopped all from queue\n";
   }

The STL containers ``std::list`` and ``std::deque`` can be adapted to create a queue.

Circular queues
---------------
A :index:`circular queue`, :index:`cyclic buffer`, or :index:`ring buffer` 
is a data structure that uses a single, 
fixed-size buffer as if it were connected end-to-end.
A ring buffer is a good choice when you need the
behavior of a queue and the buffer size can be fixed.

There are many ways to implement this data structure and the following
is just an example of one.

.. tb-group::
   :name: ring_concept_tab

   .. tb-tab:: Empty

      Conceptually, a circular buffer is a closed ring of data.

      - One element needs to be chosen as the start of the data.
        The terms ``start``, ``begin``, or ``head`` are all reasonable.
      - One element needs to be chosen as the end of the data.
        The terms ``last``, ``end``, or ``tail`` are all reasonable.

      The start locations of ``head`` and ``tail`` are arbitrary.

      A ring buffer is initially empty and of some predefined length.
      For example, this is an 8-element buffer conceptually:

      .. graphviz::
         :graphviz_dot: circo
         :align: center
         :alt: empty buffer

         digraph { 
            mindist=0.5;
            node [fontname = "Bitstream Vera Sans", fontsize=14,
              style=filled, fillcolor=lightblue
            ];

            0->1
            1->2
            2->3
            3->4
            4->5
            5->6
            6->7
            7->0
            node [shape=plain, style=""];
            head -> 0
            tail -> 0
         }

      The ``tail`` node always refers to the element just past the end
      of our data (as always).
      So when the head and tail are equal, the buffer is empty.

      The ``capacity`` is the maximum number of elements that can be
      stored in the buffer.
      In this example, the capcacity is ``8``.

      The ``size`` is the current number of elements used in the buffer.
      In our initially empty buffer, the size is ``0``.

      Since there are no true circular sections of memory, it is normal to
      represent a circular buffer in a normal contiguous linear memory block.
      An array is a good choice.

      .. graphviz:: 
         :align: center
         :alt: empty buffer - linear representation

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 | <f7>7 "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f0 -> head [dir=back]
           ring:f3 -> tail [style=invis]
           ring:f0:se -> tail [dir=back]
         }

   .. tb-tab:: Add

      Adding one element to the buffer involves storing a new value 
      at the tail location and moving the tail.

      .. graphviz::
         :graphviz_dot: circo
         :align: center
         :alt: add one to buffer

         digraph { 
            mindist=0.5;
            node [fontname = "Bitstream Vera Sans", fontsize=14,
              style=filled, fillcolor=lightblue, label=""
            ];
            0->1
            1->2
            2->3
            3->4
            4->5
            5->6
            6->7
            7->0
            0 [label="A"]
            node [shape=plain, style=""];
            head [label="head"];
            tail [label="tail"];
            head -> 0
            tail -> 1
         }

      And in the array:

      .. graphviz:: 
         :align: center
         :alt: add one - linear representation

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>A| <f1> | <f2> | <f3> | <f4> | <f5> | <f6> | <f7> "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f0 -> head [dir=back]
           ring:f3 -> tail [style=invis]
           ring:f1 -> tail [dir=back]
         }

      The buffer size is now ``1``.

      If two more items are added, the tail moves accordingly.
      The head does not move as items are added.

      .. graphviz::
         :align: center
         :alt: add two more to buffer

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>A | <f1>B | <f2>C | <f3> | <f4> | <f5> | <f6> | <f7> "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f0 -> head [dir=back]
           ring:f3 -> tail [style=invis]
           ring:f3 -> tail [dir=back]
         }

      The buffer size is now ``3``.

   .. tb-tab:: Remove

      Removing an element from the buffer involves 

      - returning the oldest element from the buffer
      - moving the head
      - decrease buffer size

      As with earlier containers, there is no need to erase the oldest
      element, since after the head has moved, we can no longer access it.

      .. graphviz::
         :align: center
         :alt: remove 1 element

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>A | <f1>B | <f2>C | <f3> | <f4> | <f5> | <f6> | <f7> "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f1 -> head [dir=back]
           ring:f3 -> tail [style=invis]
           ring:f3 -> tail [dir=back]
         }

      The buffer size is now ``2``.

   .. tb-tab:: Full Buffer

      Starting with our buffer containing [B,C], we can add elements until it
      is completely full.

      Recall we popped ``A`` from this buffer earlier.

      Adding a few elements moves the tail and increases the size.

      .. graphviz::
         :align: center
         :alt: adding more to buffer

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>A | <f1>B | <f2>C | <f3>D | <f4>E | <f5>F | <f6> | <f7> "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f1 -> head [dir=back]
           ring:f6 -> tail [style=invis]
           ring:f6 -> tail [dir=back]
         }

      At this point the buffer is almost full.
      The tail now refers to the first element in the array.
      It needed to wrap around to avoid potentially allowing a write outside
      the array bounds.
      The slot containing 'A' is available for writing, since it was removed earlier.

      .. graphviz::
         :align: center
         :alt: almost full buffer

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>A | <f1>B | <f2>C | <f3>D | <f4>E | <f5>F | <f6>G | <f7>H "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f1 -> head [dir=back]
           ring:f0 -> tail [style=invis]
           ring:f0 -> tail [dir=back]
         }

      One more write to the element at position 0 and
      now the buffer is completely full.

      .. graphviz::
         :align: center
         :alt: full buffer

         digraph {
           node [fontname = "Bitstream Vera Sans", 
                  fontsize=14,
                  shape=record, 
                  style=filled, 
                  fillcolor=lightblue
           ];
           ring [label="<f0>I | <f1>B | <f2>C | <f3>D | <f4>E | <f5>F | <f6>G | <f7>H "] 
           ring:f7:e -> ring:f0:w
           node [shape=plain, style=""];
           ring:f1 -> head [dir=back]
           ring:f0 -> tail [style=invis]
           ring:f1 -> tail [dir=back]
         }

      The buffer size is now ``8``.
      It is important to note that in this implementation
      ``head == tail`` does not represent the idea of an empty buffer.
      In this implementation the ``head == tail`` state can mean either
      a completely empty or a full queue.

      An extra variable ``size`` is used to distinguish empty from full,
      since we know the array size
      ahead of time.
      If we chose to not keep track of size and use only the head and tail
      then the maximum size of the would be :math:`capacity - 1`.

      Different designs could result in different outcomes, there are no
      hard and fast rules here.
      I chose this implementation because it is easy to reason about and
      does not waste a storage slot, at the cost of an additional variable.

      What do we do when our buffer is full?
      At this point, we have choices:

      - Allow no writes to the buffer until elements are removed.

        This is common when it is important to never lose any information,
        such as when processing keystrokes from the user, or managing a
        print queue.

      - Allow writes to overwrite the oldest elements.
        The oldest values are lost in favor of new values.

        This implementation is used when the oldest information may 
        no longer be important enough by the time the buffer is full.


-----

.. admonition:: More to Explore

   - :cpp:`STL containers library <container>`
   - STL :container:`queue` class
   - MyCodeSchool video: 
     `Data structures: introduction to queue <https://www.youtube.com/watch?v=XuCbpw6Bj1U&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=22>`__ 
   - :wiki:`Circular buffer <Circular_buffer>` on wikipedia

