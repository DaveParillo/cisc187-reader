..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: analysis; list

Analysis of list operators
==========================
Conventional wisdom states that a list is faster than a vector
when operating on elements other than the back.
We know ``push_back()`` is :math:`O(1)` for vector and we know
that vector doesn't have a 'push_front', because it's something
we intuitively feel we should discourage in a vector.
Every push front would involve shifting all the elements in the vector
down one position.


:ref:`The table below <tbl_listbigo>` shows the Big-O efficiency of some
basic list operations. 
Note that many are constant time.
Note that many list operations such as ``insert`` and ``erase`` take an iterator
as a parameter.
Once you have the iterator, these operations take constant time,
however, getting the correct iterator can often take :math:`O(n)`,
if you have not saved the iterator from a previous operation.

.. _tbl_listbigo:

.. table:: **Big-O Efficiency of C++ List Operators**

    ===================== ==================
                Operation   Big-O Efficiency
    ===================== ==================
             assignment =               O(n)
              push_back()               O(1)
               pop_back()               O(1)
                 erase(i)               O(1)
          insert(i, item)               O(1)
          insert(i, b, e) O(n) in the range
                          from ``b``, ``e``
                 splice()               O(1)
                  begin()               O(1)
                    end()               O(1)
                   size() O(1) or O(n) C++11
                   size()   O(1) after C++11
    ===================== ==================

Both ``vector`` and ``list`` support an ``insert()`` method.
There are multiple overloads for each and both support inserting
a range of elements at an arbitrary location in the container.
The :ref:`following code <lst_test_insert>` shows the code for
inserting a range into a container.

.. _lst_test_insert:

::

   template<class Container>
   void test_insert(Container data, Container new_data){
       data.insert(data.begin(), new_data.begin(), new_data.end());
   }


The ref:`test_insert code <lst_test_insert>` inserts the range at the
beginning of the current data set.
This situation should benefit the linked list and handicap the vector.
This is one of the classic situations where linked lists are said to
outperform vectors.
Let's insert chunks of data onto the front of both a list and a vector.
:ref:`The following code <lst_insert_vs_vector>` shows what happens when an ``int``
is stored in the containers.

.. _lst_insert_vs_vector:

.. activecode:: list_analysis_insert_ints_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   In this example, we take increasingly large containers
   and insert increasingly large containers to their fronts.

   Each insert operation creates a new vector with an initial size.
   The test function then inserts a second vector of equal size
   at position 0.
   ~~~~
   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <list>
   #include <vector>

   using std::list;
   using std::vector;

   template<class Container>
   void test_insert(Container data, Container other){
       data.insert(data.begin(), other.begin(), other.end());
   }


   int main(){
       using std::cout;
       using clock = std::chrono::high_resolution_clock;
       using msec_t = std::chrono::duration<double, std::milli>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "vector::insert\t"
            << std::setw(8) << "list::insert\n";

       for(int size = 10'000; size < 100'001; size += 10'000) {
         vector<int> vector_data (size);
         vector<int> new_vector_data (size);
         auto begin = clock::now();
         test_insert(vector_data, new_vector_data);
         auto end = clock::now();
         msec_t elapsed_1 = end - begin;

         list<int> list_data (size);
         list<int> new_list_data (size);
         auto begin2 = clock::now();
         test_insert(list_data, new_list_data);
         auto end2 = clock::now();
         msec_t elapsed_2 = end2 - begin2;

         cout << std::setprecision(6) << std::fixed
              << size << '\t'
              << std::setw(8) << elapsed_1.count() << '\t'
              << std::setw(8) << elapsed_2.count() << '\n';
       }
       return 0;
   }  


Both list and vector have similar complexity for this form of insert.
Both are linear in ``std::distance(first, last)`` - and vector has an additional
linear term in the distance between the insert position and end of the container.
(Vector has all those moves to perform).
Since we chose to insert at the first element location and force the destination
vector to resize on every insert, we really expect lists to outperform vector.

But it's not even close.
Running the previous code on values up to 1,000,000 should produce results similar to this:

.. plot::
   :alt: Comparison of vector and list insert times

   import matplotlib.pyplot as plt

   size = [10, 60, 110, 160, 210, 260, 310, 360, 
           410, 460, 510, 560, 610, 660, 710, 760,
           810, 860, 910, 960]

   vector_times = [0.149666, 0.358037, 0.355287, 0.487078, 0.703649, 0.948806,
                   1.151017, 1.331725, 1.348218, 1.528021, 1.753822, 2.150972,
                   1.939195, 2.031408, 2.507573, 2.688096, 2.445838, 2.709392,
                   3.025199, 3.031434]

   list_times = [5.941721, 39.379121, 67.065143, 94.302894, 130.4518, 152.329729,
                 174.837027, 201.646729, 248.44119, 329.826644, 363.771584, 331.078847,
                 361.184401, 400.703482, 458.117769, 429.139843, 459.218392, 479.405774,
                 511.681739, 543.634678]

   plt.figure(figsize=(8, 6))
   plt.plot(size, vector_times, marker='o', label='vector')
   plt.plot(size, list_times, marker='^', label='list')

   plt.xlabel('Size (thousands)', fontsize=12)
   plt.ylabel('Time (msec)', fontsize=12)
   plt.title('Comparison of vector and list insert() times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()


.. admonition:: Try This!

   The online compiler is limited in both memory and time allowed.

   Run this example on your own computer with larger values and compare.


.. index:: cache memory
   pair: memory; cache miss


It may not look like it, but both of these lines are both :math:`O(n)` on the distance
over the size of the range inserted.
It's just that for small types like ``int``, the vector is on average 150 times
faster than the linked list.

How can this be?

In short: memory.

Recall that for a vector all the data resides in a single chunk of data.
For a linked list, each new  member lives in a separate location.

Computers have a feature called cache memory and it turns out the vector is
able to exploit this resource better than a list.

.. admonition:: What is Cache Memory?

   Cache memory is a small amount of computer memory that provides high-speed data access
   to a processor and stores frequently used computer programs, applications and data.
   Cache memory is the fastest memory available and acts as a buffer between RAM and the CPU.
   When a processor requests data that already has an instance in cache memory,
   it does not need to go to the main memory or the hard disk to fetch the data.
   The processor checks whether a corresponding entry is available in the cache every time
   it needs to read or write a location which reduces the time required to access information.

   Cache memory is relatively small - it is intended to speed access to frequently used data,
   not serve as a replacement for RAM.
   When the cache is full and something needs to be written, the least frequently used data
   is overwritten.

Although both keep their data on the free store, because the vector is a single chunk,
the CPU has a better chance of keeping more of the data in cache memory.

In addition, it turns out that modern CPU's are just very good at creating, copying,
and moving chunks of memory.

There are situations where a list does outperform vector, we just have to work harder to see it.

To force our test containers to work harder, instead of a vector of ``int``,
we create a type that is a simple array wrapper:

::

   // a bloated class to make insert work harder
   template<int N>
   struct junk {
       std::array<unsigned char, N> data;
   };

Other than the change in type stored in the vector, nothing is different from the ``int``
timing example.

::

   vector<junk<2048>> vector_data (size);

.. activecode:: list_analysis_compare_largeac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:
   
   #include <array>
   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <list>
   #include <vector>

   using std::list;
   using std::vector;

   template<class Container>
   void test_insert(Container data, Container other){
       data.insert(data.begin(), other.begin(), other.end());
   }

   // a bloated class to make insert work harder
   template<int N>
   struct junk {
       std::array<unsigned char, N> data;
   };


   int main(){
       using std::cout;
       using clock = std::chrono::high_resolution_clock;
       using msec_t = std::chrono::duration<double, std::milli>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "vector::insert\t"
            << std::setw(8) << "list::insert\n";

       constexpr int JUNK_SIZE = 2048;

       for(int size = 1'000; size < 10'001; size += 1'000) {
         vector<junk<JUNK_SIZE>> vector_data (size);
         vector<junk<JUNK_SIZE>> new_vector_data (size);
         auto begin = clock::now();
         test_insert(vector_data, new_vector_data);
         auto end = clock::now();
         msec_t elapsed_1 = end - begin;

         list<junk<JUNK_SIZE>> list_data (size);
         list<junk<JUNK_SIZE>> new_list_data (size);
         auto begin2 = clock::now();
         test_insert(list_data, new_list_data);
         auto end2 = clock::now();
         msec_t elapsed_2 = end2 - begin2;

         cout << std::setprecision(6) << std::fixed
              << size << '\t'
              << std::setw(8) << elapsed_1.count() << '\t'
              << std::setw(8) << elapsed_2.count() << '\n';
       }
       return 0;
   } 


A change in data type stored in the vector produces different results.

The online compiler is limited in both memory and time allowed.
The 2MB value for ``JUNK_SIZE`` is roughly the 'break even' point on this compiler.
The graph below shows what running with and 8MB size looks like.

Run this example on your own computer with larger values and compare.

.. plot::
   :alt: Comparison of vector and list insert times

   import matplotlib.pyplot as plt

   size = [ 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
   vector_times = [31.075628, 61.593806, 97.173366, 122.9618,
                   176.697422, 190.916136, 211.435129, 249.227746, 270.062249, 280.568809]

   list_times = [22.655183, 46.228086, 77.28783, 99.212702, 125.413728, 146.850171,
                 150.138818, 180.029761, 196.170772, 205.610067]
   
   plt.figure(figsize=(8, 6))
   plt.plot(size, vector_times, marker='o', label='vector')
   plt.plot(size, list_times, marker='^', label='list')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (msec)', fontsize=12)
   plt.title('Comparison of vector and list insert() times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()


The sheer size of the data in each vector element increases the likelihood of a *cache miss*.
In this case, the data is too large to fit much, if anything, in cache memory.
The CPU fails to find it in cache, so it must retrieve it from RAM every time.

Both the vector and list are clearly :math:`O(n)` and the list is outperforming the vector.

.. admonition:: Try This!

   What other situations might a list outperform a vector.
   Try some of the following with data types of different sizes:

   - Reversing data
   - Sorting data
   - Filling or constructing data
   - Removing data

-----

.. admonition:: More to Explore

   - `C++ benchmark – std::vector VS std::list VS std::deque <https://baptiste-wicht.com/posts/2012/12/cpp-benchmark-vector-list-deque.html>`__




