..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| replace:: --

.. index:: 
   single: iterator operations
   pair: iterator; operations

Basic iterator operations
=========================
Iterators in C++ provide pointer-like operations, but their capabilities
depend on the iterator category. For example, a list iterator can move
forward and backward, while it cannot jump directly to an element by index.
The operations in the table are common examples; no iterator is required to
support every operation shown.

.. list-table:: Common iterator operations
   :header-rows: 1
   :widths: 25 75

   * - Operation
     - Result
   * - ``p == q``
     - True when ``p`` and ``q`` refer to the same position.
   * - ``p != q``
     - The negation of ``p == q``.
   * - ``*p``
     - Refers to the element at the dereferenceable position ``p``.
   * - ``*p = val``
     - Writes ``val`` when ``p`` is writable.
   * - ``val = *p``
     - Reads from the element at ``p`` and writes the result to ``val``.
   * - ``++p``
     - Increments ``p`` to the next position.

An iterator must be dereferenceable before ``*p`` is used; a past-the-end
iterator such as ``end()`` is not dereferenceable. Incrementing a past-the-end
iterator is invalid. Comparing iterators from different sequences is also
generally invalid, so compare iterators that belong to the same sequence.

.. index::
   single: iterator categories
   single: mutable iterator

Legacy iterator categories and C++20 concepts
----------------------------------------------
Different containers need different capabilities from their iterators.

The older C++ standard describes iterator capabilities using named
requirements. C++20 also provides concepts with corresponding names, such as
``std::forward_iterator`` and ``std::contiguous_iterator``. In both models,
the required operations determine what an iterator can do; the iterator does
not need to inherit from a base class.

The traversal capabilities form a hierarchy:

``input`` -> ``forward`` -> ``bidirectional`` -> ``random access`` -> ``contiguous``

Each category on the right supports the operations of the categories on its
left. Output capability is separate. An iterator can support both traversal
and output, such as a mutable vector iterator, but an output iterator does not
have to support reading or multipass traversal.

In the diagram, solid arrows show the traversal hierarchy. Dotted lines show
that output capability can be combined with any traversal capability.

.. digraph:: iter_categories
   :alt: Iterator categories

    graph [
        splines= ortho
        fontname = "Bitstream Vera Sans"
        fontsize = 14
        labelloc = b
        label = "Iterator categories"
        nodesep = 1.0
        ranksep = 0.3
    ];

    node [
        fontname = "Bitstream Vera Sans"
        style=filled, fillcolor=lightblue
        fontsize = 14,
        shape = "box",  width=0.5, height=.25
    ];
    edge [dir=back, arrowsize=0.5];

    input [label="Input Iterator",
           tooltip="Link to input_iterator concept on cppreference",
           URL="https://en.cppreference.com/w/cpp/iterator/input_iterator"];
    fwd [label="Forward Iterator",
         tooltip="Link to forward_iterator concept on cppreference",
         URL="https://en.cppreference.com/w/cpp/iterator/forward_iterator"];
    bi [label="Bidirectional Iterator",
        tooltip="Link to bidirectional_iterator concept on cppreference",
        URL="https://en.cppreference.com/w/cpp/iterator/bidirectional_iterator"];
    random [label="RandomAccess Iterator",
            tooltip="Link to random_access_iterator concept on cppreference",
            URL="https://en.cppreference.com/w/cpp/iterator/random_access_iterator"];
    contiguous [label="Contiguous Iterator",
                tooltip="Link to contiguous_iterator concept on cppreference",
                URL="https://en.cppreference.com/w/cpp/iterator/contiguous_iterator"];

    output [label="Output Iterator",
            tooltip="Link to output_iterator concept on cppreference",
            URL="https://en.cppreference.com/w/cpp/iterator/output_iterator"];

    input -> fwd -> bi -> random -> contiguous [weight=100];
    edge [style=dotted, dir=none];
    input, fwd, bi, random, contiguous -> output;
    {rank=same; output bi};


:req:`Input Iterator <InputIterator>`
   Reads elements and advances using ``operator++``. It supports only
   single-pass traversal, so an iterator copy is not expected to remain
   independently usable after one copy advances. ``std::istream_iterator``
   is an example.


:req:`Forward Iterator <ForwardIterator>`
   :req:`InputIterator`, plus default construction, equality comparison, and
   multipass traversal. Copies of a forward iterator can be advanced
   independently. The :container:`forward_list` container provides this
   iterator.

:req:`Bidirectional Iterator <BidirectionalIterator>`
   :req:`ForwardIterator`, plus pre-increment and post-increment using
   ``operator++`` and pre-decrement and post-decrement using ``operator--``.
   Containers like :container:`list`, :container:`map`, and :container:`set`
   provide this iterator.


:req:`Random Access Iterator <RandomAccessIterator>`
   :req:`BidirectionalIterator`, plus constant-time jumps using ``operator+=``,
   ``operator-=``, ``operator+``, ``operator-``, and ``operator[]``.
   Containers like :container:`vector`, :container:`deque`, :container:`array`,
   and :cpp:`string <string/basic_string>` provide random-access iterators.
   Unordered associative containers do not.


:req:`Contiguous Iterator <ContiguousIterator>`
   :req:`RandomAccessIterator`, plus a guarantee that the elements occupy one
   contiguous range of storage. The category was added to standard terminology
   in C++17, and C++20 provides the ``std::contiguous_iterator`` concept. It
   formalizes the guarantee already provided by containers such as
   :container:`vector`, :container:`array`, and
   :cpp:`string <string/basic_string>`.

:req:`Output Iterator <OutputIterator>`
   A separate capability that allows writing through dereference. An output
   iterator does not have to support reading, equality comparison, or
   multipass traversal. In modern C++, this capability is described by the
   ``std::output_iterator`` concept.

   The following example uses a back-inserting output iterator. Dereferencing
   it is valid on the left-hand side of an assignment, but it is not used to
   read a value:

   .. tb-code:: cpp
      :name: iterator_output_ac

      #include <iostream>
      #include <iterator>
      #include <vector>

      int main() {
        std::vector<int> values;
        auto output = std::back_inserter(values);

        *output = 10;
        ++output;
        *output = 20;

        for (const auto value : values) {
          std::cout << value << ' ';
        }
        std::cout << '\n';
      }

-----

.. admonition:: More to Explore

  - :cpp:`Iterator Library <iterator>` at cppreference.com
  - :cpp:`C++20 Concepts Library <concepts>`
  - :cpp:`C++20 Ranges Library <ranges>`
  - C++ Named Requirements: :req:`Iterator <Iterator>`
