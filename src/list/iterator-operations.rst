..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. |---| unicode:: U+2014 

.. index:: 
   single: iterator operations
   pair: iterator; operations

Basic iterator operations
=========================
By design, iterators in C++ feel as if you are using pointers.
Most iterators support the same operations as pointers.

+--------------+--------------------------------------------------------+
| Operation    |  Result                                                |
+==============+========================================================+
| ``p == q``   | ``true`` if and only if ``p`` and ``q``                |
|              | point to the same element or both point to ``end``     |
+--------------+--------------------------------------------------------+
| ``p != q``   | negation of above                                      |
+--------------+--------------------------------------------------------+
| ``*p``       | refers to the element pointed to by ``p``              |
+--------------+--------------------------------------------------------+
| ``*p = val`` | writes ``val`` to the element pointed to by ``p``      |
+--------------+--------------------------------------------------------+
| ``val = *p`` | reads from the element pointed to by ``p`` and         |
|              | writes to ``val``                                      |
+--------------+--------------------------------------------------------+
| ``++p``      | increment the iterator, making it point to the next    |
|              | element in the container or to ``end``                 |
+--------------+--------------------------------------------------------+

.. index:: 
   single: iterator categories
   single: mutable iterator

Iterator categories
-------------------
Different containers need different capabilities from their iterators.

Instead of being defined by specific types, 
each category of iterator is defined by the operations that can be performed on it. 
This definition means that any type that supports the necessary operations 
can be used as an iterator |---| for example, 
a pointer supports all of the operations required by 
:req:`Random Access Iterator <RandomAccessIterator>`,
so a pointer can be used anywhere a :req:`Random Access Iterator <RandomAccessIterator>` is expected.

All of the iterator categories (except :req:`Output Iterator <OutputIterator>`) can be organized into a hierarchy, 
where more powerful iterator categories Random Access Iterator) 
support the operations of less powerful categories (e.g. :req:`Input Iterator <InputIterator>`). 
If an iterator falls into one of these categories and also satisfies the 
requirements of :req:`Output Iterator <OutputIterator>`, 
then it is called a *mutable iterator* and supports both input and output. 
Non-mutable iterators are called *constant iterators*.

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

    input [label="Input Iterator", URL="https://en.cppreference.com/cpp/named_req/InputIterator"];
    fwd [label="Forward Iterator", URL="https://en.cppreference.com/cpp/named_req/ForwardIterator"];
    bi [label="Bidirectional Iterator", URL="https://en.cppreference.com/cpp/named_req/BidirectionalIterator"];
    random [label="RandomAccess Iterator", URL="https://en.cppreference.com/cpp/named_req/RandomAccessIterator"];
    contiguous [label="Contiguous Iterator", URL="https://en.cppreference.com/cpp/named_req/ContiguousIterator"];
 
    output [label="Output Iterator", URL="https://en.cppreference.com/cpp/named_req/OutputIterator"];

    input -> fwd -> bi -> random -> contiguous [weight=100];
    edge [style=dotted, dir=none];
    input, fwd, bi, random, contiguous -> output;
    {rank=same; output bi};


:req:`Input Iterator <InputIterator>`
   Read elements and increments using ``operator++``, without multiple passes.
   Classes like :io:`basic_istream <basic_istream>` provide this iterator.


:req:`Forward Iterator <ForwardIterator>`
   :req:`InputIterator`, plus increment using ``operator++``, with multiple passes.  
   The :container:`forward_list` container provides this iterator.

:req:`Bidirectional Iterator <BidirectionalIterator>`
   :req:`ForwardIterator`, plus decrement using ``operator--``
   Containers like :container:`list`, :container:`map`, and :container:`set`
   provide this iterator.


:req:`Random Access Iterator <RandomAccessIterator>`
   :req:`BidirectionalIterator`, plus access using ``operator[]``
   Before C++17, containers like :container:`vector`, :container:`array`, 
   and :cpp:`string <string/basic_string>` provided this iterator.
   It is still used for unordered collections like 
   :container:`unordered_map` and :container:`unordered_set`


:req:`Contiguous Iterator <ContiguousIterator>`
   :req:`RandomAccessIterator`, plus the container makes a continuous storage guarantee.
   This category was added in C++17.
   Before C++17, iterators of containers like :container:`vector` and :container:`array`
   were often treated as a separate category.
   This category simply formalizes what was happening in practice.

:req:`Output Iterator <OutputIterator>`
   More of a 'sub category' of all of the others.
   If the iterator allows writing to the element, it is also an :req:`OutputIterator`
   An output iterator can **only** be dereferenced on the left-hand side of an expression:

   .. code-block:: cpp

      vector<int> v = {1,2,3};
      auto it = v.begin();
      *it = 0;

-----

.. admonition:: More to Explore

  - :cpp:`Iterator Library <iterator>` at cppreference.com
  - C++ Named Requirements: :req:`Iterator <Iterator>`
