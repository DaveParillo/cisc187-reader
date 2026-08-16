..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   pair: algorithm analysis; std::list

Analysis of list operators
==========================
Lists can be faster than vectors when inserting or erasing at a position
that is already represented by an iterator.
They are not generally faster for every operation, however.
We know ``push_back()`` is amortized :math:`O(1)` for a vector,
and we know that a vector does not have a ``push_front()`` operation.
Inserting at the beginning of a vector requires shifting all of its
existing elements to make room.


:ref:`The table below <tbl_listbigo>` shows the asymptotic complexity
of some common list operations.
Note that many are constant time when the required iterator is already available.
Note that many list operations such as ``insert`` and ``erase`` take an iterator
as a parameter.
Once you have the iterator, these operations take constant time,
however, getting the correct iterator can often take :math:`O(n)`,
if you have not saved the iterator from a previous operation.

.. _tbl_listbigo:

.. table:: **Complexity of C++ List Operators**

    ================================ ================================
                Operation                     Complexity
    ================================ ================================
    assignment =                     O(n + m), where n and m
                                     are the two list sizes
    push_front()                     O(1)
    pop_front()                      O(1)
    push_back()                      O(1)
    pop_back()                       O(1)
    erase(i)                         O(1)
    insert(i, item)                  O(1)
    insert(i, b, e)                  O(n) in the inserted range
    splice(whole list)               O(1)
    begin()                          O(1)
    end()                            O(1)
    size()                           O(n) before C++11;
                                     O(1) since C++11
    ================================ ================================

Here ``i`` is an iterator identifying the position. The constant-time
``erase`` and ``insert`` entries describe operations after that iterator
has been found. The whole-list ``splice`` overload transfers existing nodes
without copying their values.

Both ``vector`` and ``list`` support an ``insert()`` method.
There are multiple overloads for each and both support inserting
a range of elements at an arbitrary location in the container.
The :ref:`following code <lst_test_insert>` shows the code for
inserting a range into a container.

.. _lst_test_insert:

::

   template<class Container>
   void test_insert(Container& data, const Container& new_data){
       data.insert(data.begin(), new_data.begin(), new_data.end());
   }


The :ref:`test_insert code <lst_test_insert>` inserts the range at the
beginning of the current data set.
This situation should benefit the linked list and handicap the vector.
This is one of the classic situations where linked lists are said to
outperform vectors.
Let's insert chunks of data onto the front of both a list and a vector.
:ref:`The following code <lst_insert_vs_vector>` shows what happens when an ``int``
is stored in the containers.

.. _lst_insert_vs_vector:

In this example, we take increasingly large containers
and insert increasingly large containers to their fronts.

Each iteration creates containers with an initial size.
The test function then inserts a second container of equal size
at position 0.

.. tb-code:: cpp
   :name: list_analysis_insert_ints_ac

   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <list>
   #include <vector>

   using std::list;
   using std::vector;

   template<class Container>
   void test_insert(Container& data, const Container& other){
       data.insert(data.begin(), other.begin(), other.end());
   }


   int main(){
       using std::cout;
       using clock = std::chrono::steady_clock;
       using msec_t = std::chrono::duration<double, std::milli>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "vector::insert\t"
            << std::setw(8) << "list::insert\n";

       for(int size = 10'000; size < 100'001; size += 10'000) {
         vector<int> vector_data (size);
         vector<int> new_vector_data (size);
         vector_data.reserve(size * 2);
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


Both list and vector have linear complexity for this form of insert.
The list must create nodes for the inserted range.
The vector must also move its existing elements after the insertion point.
This example reserves enough vector capacity to avoid measuring a possible
reallocation, so the comparison focuses on moving elements versus allocating
list nodes.

But it's not even close.
The embedded example intentionally stops at ``100,000`` so it can run within
the textbook compiler time and memory limits.
The graph below was generated separately, offline, with a longer version of
this benchmark and a loop starting at ``10,000`` and increasing by ``50,000``
until it reached ``1,000,000``.
Therefore, its final measured point is ``960,000``.

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


It may not look like it, but both of these insertions are :math:`O(n)` in
the size of the range inserted.
In this particular run, for small types like ``int``, the vector was about
150 times faster than the linked list. The exact ratio depends on the compiler,
library, hardware, allocator, and system load.

How can this be?

In short: memory.

Recall that a vector stores its elements contiguously.
A linked list typically allocates each node separately.

Computers have a feature called cache memory and it turns out the vector is
able to exploit this resource better than a list.

.. admonition:: What is Cache Memory?

   Modern processors use a hierarchy of storage, including registers, cache,
   and main memory. Cache is smaller and faster than main memory, and the
   processor automatically moves data between these levels in cache lines.
   When nearby data is reused, contiguous storage gives the processor a better
   chance of finding it in cache instead of waiting for main memory.

   Cache is relatively small and is managed by hardware. Its replacement policy
   is not necessarily simply "least frequently used."

Although both commonly use dynamically allocated storage, because the vector is a single chunk,
the CPU has a better chance of keeping more of the data in cache memory.

In addition, it turns out that modern CPUs are just very good at creating, copying,
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

.. tb-code:: cpp
   :name: list_analysis_compare_largeac

   #include <array>
   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <list>
   #include <vector>

   using std::list;
   using std::vector;

   template<class Container>
   void test_insert(Container& data, const Container& other){
       data.insert(data.begin(), other.begin(), other.end());
   }

   // a bloated class to make insert work harder
   template<int N>
   struct junk {
       std::array<unsigned char, N> data;
   };


   int main(){
       using std::cout;
       using clock = std::chrono::steady_clock;
       using msec_t = std::chrono::duration<double, std::milli>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "vector::insert\t"
            << std::setw(8) << "list::insert\n";

       constexpr int JUNK_SIZE = 2048;

       for(int size = 1'000; size < 10'001; size += 1'000) {
         vector<junk<JUNK_SIZE>> vector_data (size);
         vector<junk<JUNK_SIZE>> new_vector_data (size);
         vector_data.reserve(size * 2);
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
The ``JUNK_SIZE`` value is measured in bytes, so ``2048`` is 2 KiB per element.
That value was roughly the break-even point on the compiler used for the JOBE example.
The graph below was generated separately, offline, with ``JUNK_SIZE`` set to
8192, or 8 KiB per element.

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

   - `C++ benchmark - std::vector VS std::list VS std::deque <https://baptiste-wicht.com/posts/2012/12/cpp-benchmark-vector-list-deque.html>`__
