..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. index::
   single: permutations
   single: random uniform_int_distribution
   single: random shuffle
   single: shuffle

Permutations
============
A permutation of a sequence :math:`\mathbf{S}`
is simply the members of :math:`\mathbf{S}` arranged in some order.
For example, a permutation of the integers 1 through :math:`n` would
be those values arranged in some order.
If the sequence contains :math:`n` distinct members, then there are
:math:`n!` different permutations for the sequence.
This is because there are :math:`n` choices for the first member in
the permutation; for each choice of first member there are :math:`n-1`
choices for the second member, and so on.

.. tabbed:: permute

   .. tab:: permute

      Sometimes one would like to obtain a random permutation for a
      sequence, that is, one of the :math:`n!` possible permutations is
      selected in such a way that each permutation has equal probability of
      being selected.
      A simple function for generating a random permutation is as
      follows.

      .. code-block:: cpp

         //Randomly permute the values in array
         void permute(int data[], int n) {
           for (int i = n; i > 0; --i) {
             int j = std::uniform_int_distribution<int> {0, i-1} (eng);
             std::swap(data[i-1], data[j]);  // swap data[i-1] with a random
           }                                 // position in the range 0 to i-1.
         }

      Here, the :math:`n` values of the sequence are stored in
      positions 0 through :math:`n-1` of array ``data``.
      Function :utility:`swap`
      exchanges elements in array ``data``,
      and :numeric:`uniform_int_distribution <random/uniform_int_distribution>`
      returns an integer value uniformly distributed 
      in the range 0 to :math:`i-1`.

   .. tab:: Run It

      .. activecode:: math_permute_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <random>
         #include <utility>

         namespace {
           // make a random number generator
           std::random_device r;
           std::default_random_engine eng(r());
         }

         //Randomly permute the values in array
         void permute(int data[], int n) {
           for (int i = n; i > 0; --i) {
             int j = std::uniform_int_distribution<int> {0, i-1} (eng);
             std::swap(data[i-1], data[j]);  // swap data[i-1] with a random
           }                                 // position in the range 0 to i-1.
         }
         void print(int data[], int n) {
           for (int i = 0; i<n; ++i) {
             std::cout << data[i] << '\t';
           }
           std::cout << std::endl;
         }
         int main() {
           int data[] = {1,1,2,3,5,8,13,21,34};

           for (int i = 0; i<5; ++i) {
             permute(data, 9);
             print(data, 9);
           }
           std::cout << '\n';
         }


   .. tab:: shuffle

      Randomly shuffling a range of data is a common enough activity
      that it is implemented in the standard library.
      The :algorithm:`shuffle <random_shuffle>` function
      does what our permute function does, but a bit more generically.

      .. code-block:: cpp
         
         std::shuffle(std::begin(data), std::end(data), eng);

      Instead of an entire array it takes a range of data and
      a random number generator.

   .. tab:: Run shuffle

      .. activecode:: math_permute_shuffle_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <algorithm>
         #include <iostream>
         #include <iterator>
         #include <random>

         namespace {
           std::random_device r;
           std::default_random_engine eng(r());  // make a random number generator
         }

         void print(int data[], int n) {
           for (int i = 0; i<n; ++i) {
             std::cout << data[i] << '\t';
           }
           std::cout << std::endl;
         }
         int main() {
           int data[] = {1,1,2,3,5,8,13,21,34};

           for (int i = 0; i<5; ++i) {
             std::shuffle(std::begin(data), std::end(data), eng);
             print(data, 9);
           }
           std::cout << std::endl;
         }


.. admonition:: More to Explore

   - From cppreference.com

     - :numeric:`Random number generation <random>` and
       :algorithm:`random_shuffle`
     - :numeric:`Common math functions <math>`
     - :algorithm:`is_permuation` and :algorithm:`next_permuation` 

.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.

