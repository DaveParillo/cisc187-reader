..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: analysis; hash table

Analysis of hash tables
=======================
:ref:`The table below <tbl_hashbigo>` shows the average case Big-O efficiency of some
basic unordered_map operations. 
For each operation that has average case constant time efficiency,
the *worst case* complexity is :math:`O(n)`.

.. _tbl_hashbigo:

.. table:: **Big-O Efficiency of C++ unordered map Operators**

    ===================== ==================
                Operation   Big-O Efficiency
    ===================== ==================
             assignment =               O(1)
                 insert()               O(1)
                   find()               O(1)
               contains()               O(1)
                  erase()               O(1)
                  clear()               O(n)
    ===================== ==================

The reason these operations may have :math:`O(n)` complexity is because
the performance of the container is ultimately controlled by the quality
of the hash function for the key type in the container.
If the hash function performs poorly (many collisions),
then the benefits of hash tables are lost and we decay into list performance.
When the hash function quality is high, then the performance is good.

When we discussed the messy and neat closets in :ref:`trees_trees`,
we mentioned the primary motivation for non-sequential containers was search.
Unlike even a sorted vector or a tree, hash tables provide constant time
access tot he correct bucket containing our data and linear search is required
only when collisions exist.

:ref:`The following code <hash_find_vs_vector>` shows what happens when searching
in an unordered map vs a vector.

.. _hash_find_vs_vector:

.. activecode:: hash_analysis_find_vs_vector_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   #include <algorithm>
   #include <chrono>
   #include <iomanip>
   #include <iostream>
   #include <numeric>
   #include <unordered_map>
   #include <vector>

   int main() {
       using clock = std::chrono::high_resolution_clock;
       std::cout << std::setw(6) << "size"
                 << std::setw(10) << "vector"
                 << std::setw(20) << "hash table\n";
       // for(int size = 10'000; size < 100'001; size += 20'000) {
       int size = 35000;
           // fill vector
           std::vector<int> sequence (size);
           std::iota(sequence.begin(), sequence.end(), 0);
           // search vector
           auto begin = clock::now();
           for(const auto& it: sequence){
               if(std::find(sequence.begin(), sequence.end(), it) == sequence.end()) {
                   std::cerr << "Failed to find an expected value in vector! Halting.\n";
                   return -2;
               }
           }
           auto end = clock::now();
           std::chrono::duration<double> elapsed_secs = end - begin;
           // fill hash table
           std::unordered_map<int, int> table;
           for(int item = 0; item < size; ++item){
               table[item] = item;
           }
           begin = clock::now();
           // search hash table
           for(const auto& it: table){
               if(table.find(it.first) == table.end()) {
                   std::cerr << "Failed to find an expected value in map! Halting.\n";
                   return -2;
               }
           }
           end = clock::now();
           std::chrono::duration<double> elapsed_secs_ht = end - begin;

           // Printing final output
           std::cout << std::fixed   << std::setprecision(4)
                     << std::setw(6) << size << '\t'
                     << std::setw(8) << elapsed_secs.count() << '\t'
                     << std::setw(8) << elapsed_secs_ht.count() << '\n';
       // }
       return 0;
   }

        
.. admonition:: Try This!

   The online compiler is limited in both memory and time allowed.

   Run this example on your own computer with the loop enabled
   and with larger values and compare.


The vector is linear in ``std::distance(begin, end)`` and as expected,
the hash table is constant time.
Running the previous code should produce results similar to this:

.. plot::
   :alt: Comparison of vector and hash table search times

   import matplotlib.pyplot as plt

   size = [10000, 30000, 50000, 70000, 90000]

   vector_times = [ 0.4303, 3.7153, 10.7513, 21.4044, 36.1914]

   hash_times = [ 0.0009, 0.003, 0.0045, 0.0063, 0.0089]

   plt.figure(figsize=(8, 6))
   plt.plot(size, vector_times, marker='o', label='vector')
   plt.plot(size, hash_times, marker='^', label='unordered map')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (seconds)', fontsize=12)
   plt.title('Comparison of vector and hash table search times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()


So what about the tree ADT?
The `std::set` is generally implemented as a tree.
The C++ standard guarantees logarithmic complexity in the size of the container.


.. activecode:: hash_analysis_find_vs_set_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:


   How does std::set find compare to std::unordered_map find?

   ~~~~
   
   #include <algorithm>
   #include <chrono>
   #include <iomanip>
   #include <iostream>
   #include <numeric>
   #include <set>
   #include <unordered_map>

   int main() {
       using clock = std::chrono::high_resolution_clock;
       std::cout << std::setw(6) << "size"
                 << std::setw(10) << "set"
                 << std::setw(20) << "hash table\n";
       for(int size = 5'000; size < 100'001; size += 5'000) {
           // fill set
           std::set<int> tree;
           for(int item = 0; item < size; ++item){
               tree.insert(item);
           }
           // search set
           auto begin = clock::now();
           for(const auto& it: tree){
               if(tree.find(it) == tree.end()) {
                   std::cerr << "Failed to find an expected value in set! Halting.\n";
                   return -2;
               }
           }
           auto end = clock::now();
           std::chrono::duration<double> elapsed_secs = end - begin;
           // fill hash table
           std::unordered_map<int, int> table;
           for(int item = 0; item < size; ++item){
               table[item] = item;
           }
           begin = clock::now();
           // search hash table
           for(const auto& it: table){
               if(table.find(it.first) == table.end()) {
                   std::cerr << "Failed to find an expected value in map! Halting.\n";
                   return -2;
               }
           }
           end = clock::now();
           std::chrono::duration<double> elapsed_secs_ht = end - begin;

           // Printing final output
           std::cout << std::fixed   << std::setprecision(4)
                     << std::setw(6) << size << '\t'
                     << std::setw(8) << elapsed_secs.count() << '\t'
                     << std::setw(8) << elapsed_secs_ht.count() << '\n';
       }
       return 0;
   } 


Although the std::set find is logarithmic complexity, from a practical sense,
it compares favorably with the hash table.
The graph below shows example output for values up to 1,000,000.

.. plot::
   :alt: Comparison of set and hash table find times

   import matplotlib.pyplot as plt

   size = [ 50000, 100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000,
            500000, 550000, 600000, 650000, 700000, 750000, 800000, 850000, 900000,
            950000, 1000000]

   set_times = [ 0.0115, 0.0205, 0.0315, 0.0444, 0.0528, 0.0655, 0.0769, 0.0928,
                 0.1033, 0.1118, 0.125, 0.1408, 0.1495, 0.1595, 0.1825, 0.1893,
                 0.2026, 0.2136, 0.2314, 0.238]

   hash_times = [ 0.0047, 0.0089, 0.0136, 0.0183, 0.0233, 0.0274, 0.0324, 0.0374,
                  0.0407, 0.0461, 0.05, 0.0558, 0.0601, 0.0644, 0.0692, 0.0745,
                  0.0784, 0.0831, 0.0882, 0.0931]
   
   plt.figure(figsize=(8, 6))
   plt.plot(size, set_times, marker='o', label='set')
   plt.plot(size, hash_times, marker='^', label='unordered map')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (msec)', fontsize=12)
   plt.title('Comparison of set and hash table insert() times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()

.. admonition:: Try This!

   The online compiler is limited in both memory and time allowed.

   Run this example on your own computer with larger values and compare.



-----

.. admonition:: More to Explore

   - TBD




