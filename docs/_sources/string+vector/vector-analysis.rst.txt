..  Copyright (C)  Brad Miller, David Ranum, and Jan Pearce

    This work is licensed under the Creative Commons
    Attribution-NonCommercial-ShareAlike 4.0 International License. To view a
    copy of this license, visit
    http://creativecommons.org/licenses/by-nc-sa/4.0/.


.. index::
   pair: analysis; vector

Analysis of Vector Operators
============================
Accessing data using an index and assigning to an index position
that already exists both take the same amount of time no matter how
large the vector is. When an operation like this is independent of
the size then it is :math:`O(1)`.

As we have seen, one
way to create a longer vector is to use the ``push_back()`` method.
The ``push_back()`` method is typically :math:`O(1)`, provided
there is adequate capacity in the underlying array.

First we’ll use ``push_back()`` method.
:ref:`The following code <lst_mkvectcpp>` shows the code for
making our vector.

.. _lst_mkvectcpp:

::

   #include <vector>
   using std::vector;

   void test_push_back(int size){
       vector<int> vect;
       for (int i = 0; i < size; ++i){
           vect.push_back(i);
       }
   }

And we can time how long it takes to push 10,000 values into a vector.

.. activecode:: vactor_analysis_push_back_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:


   #include <chrono>
   #include <iostream>
   #include <vector>
   using std::vector;

   void test_push_back(int size){
       vector<int> vect;
       for (int i = 0; i < size; i++){
           vect.push_back(i);
       }
   }

   int main(){
       using msec_t = std::chrono::duration<double, std::milli>;

       auto begin = std::chrono::steady_clock::now();
       test_push_back(10'000);
       auto end = std::chrono::steady_clock::now();
       msec_t elapsed_time = end - begin;

       std::cout << "push_back (msec): " << elapsed_time.count() << '\n';

       return 0;
   }

In the experiment above the statement that we are timing is the function
call to ``test_push_back``. 
From the experiment, we see the amount of time taken by the push_back operation. 
Not only is the ``push_back()`` function call duration being measured, but the time to allocate space is being measured.

We can improve the runtime a bit further by setting an adequate reserve for the vector
in advance. Doing this will keep us from having to move the entire vector to an
adequately sized space in memory as the vector grows.

.. activecode:: vector_analysis_compare_cppac_3
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <vector>
   using std::vector;

   void test_push_back(int size){
       vector<int> vect;
       for (int i = 0; i < size; ++i){
           vect.push_back(i);
       }
   }

   void test_reserve(int size){
       vector<int> v(size);
       for (int i = 0; i < size; ++i){
           v[i] = i;
       }
   }

   int main(){
       using std::cout;
       using std::chrono::steady_clock;
       using msec_t = std::chrono::duration<double, std::milli>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "push_back\t"
            << std::setw(8) << "pre-allocated vector (all times in msec)\n";

       for(int size = 1'000; size < 1'000'000; size += 50'000) {

         auto begin = steady_clock::now();
         test_push_back(size);
         auto end = steady_clock::now();
         msec_t elapsed_1 = end - begin;

         auto begin2 = steady_clock::now();
         test_reserve(size);
         auto end2 = steady_clock::now();
         msec_t elapsed_2 = end2 - begin2;

         cout << std::setprecision(6) << std::fixed
              << size << '\t'
              << std::setw(8) << elapsed_1.count() << '\t'
              << std::setw(8) << elapsed_2.count() << '\n';
       }
       return 0;
   }

A graph of the loops in the preceding code should look something like this:

.. plot::
   :alt: Comparison of vector::push_back times

   import matplotlib.pyplot as plt

   size = [1000, 51000, 101000, 151000, 201000, 251000, 301000, 351000,
           401000, 451000, 501000, 551000, 601000, 651000, 701000, 751000,
           801000, 851000, 901000, 951000]
   push_back_times = [0.095743, 3.755487, 6.140636, 8.298554, 9.219730,
            11.246443, 15.596590, 18.093017, 18.821956, 20.606710, 23.227368,
            27.039730, 29.823470, 30.539703, 32.493372, 34.575437,
            35.588323, 37.498568, 38.398027, 40.377150]
   pre_allocated_times = [0.032560, 1.304584, 2.185269, 2.741993, 4.140298,
            4.769269, 5.732273, 6.211213, 7.903502, 8.875864, 8.971830,
            10.871387, 10.237928, 11.157351, 12.564938, 12.729338,
            13.665438, 14.635036, 15.659069, 16.639636]


   plt.figure(figsize=(8, 6))
   plt.plot(size, push_back_times, marker='o', label='push_back')
   plt.plot(size, pre_allocated_times, marker='^', label='preallocated vector')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (msec)', fontsize=12)
   plt.title('Comparison of vector::push_back() times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()




Now that we have seen how performance can be measured concretely you can
look at :ref:`the table below <tbl_vectbigocpp>` to see the complexity of some
basic vector operations. When ``pop_back()`` is called, the vector size
is reduced by 1 and it takes constant time: :math:`O(1)`.
However, when ``erase()`` is called the time is :math:`O(n)`.
The reason for this lies in how C++ chooses to implement vectors.
When an item is taken from the front of the vector,
in C++ implementation, all the other elements in
the vector are shifted one position closer to the beginning.
This implementation also allows the index operation to be :math:`O(1)`.
This is a trade-off that the C++ implementers thought was a good one.

.. _tbl_vectbigocpp:

.. table:: **Complexity of C++ vector operations**

    ===================== ==================
                Operation         Complexity
    ===================== ==================
                 index []               O(1)
       index assignment =               O(1)
              push_back()     amortized O(1)
               pop_back()               O(1)
                 erase(i)               O(n)
          insert(i, item)               O(n)
         find(b, e, item)               O(n)
                reserve()               O(n)
                  begin()               O(1)
                    end()               O(1)
                   size()               O(1)
    ===================== ==================

The ``push_back()`` operation is :math:`O(1)` unless there is inadequate capacity,
in which case the entire
vector is moved to a larger contiguous underlying array, which
is :math:`O(n)`.
However, since over the long term, as :math:`n` grows large, then number of
vector copies is small.
So on average, even though there are some :math:`O(n)` operations, it turns out
that ``push_back()`` is constant time.

As a way of demonstrating the difference in performance between ``pop_back()``
and ``erase()``, let’s do another timing experiment.
Our goal is to be able
to verify the performance of the ``pop_back()`` operation on a vector of a known
size when the program pops from the end of the vector using ``pop_back()``, and again when the
program pops from the beginning of the vector using ``erase()``. We will also want to
measure this time for vectors of different sizes. What we would expect to
see is that the time required to pop from the end of the vector will stay
constant even as the vector grows in size, while the time to pop from the
beginning of the vector will continue to increase as the vector grows.

:ref:`The following code <lst_popmeascpp>` shows one way to measure the difference
between the ``pop_back()`` and ``erase()``.

.. _lst_popmeascpp:

.. activecode:: vector_analysis_popbackvserase_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   #include <chrono>
   #include <iostream>
   #include <iomanip>
   #include <numeric>
   #include <vector>
   using std::vector;

   int main(){
       using std::cout;
       using std::chrono::steady_clock;
       using msec_t = std::chrono::duration<double, std::micro>;

       cout << std::setw(6) << "size\t"
            << std::setw(8) << "pop_back\t"
            << std::setw(8) << "erase\t\t"
            << std::setw(8) << "how much faster is pop_back?\n";
       cout << std::setw(19) << "(microsec)\t"
            << std::setw(10) << "(microsec)\n";

       for(int size = 10'000; size < 100'000; size += 10'000) {
           // Create 2 identical vectors with values 0..N
           vector<int> data1(size);
           std::iota(data1.begin(), data1.end(), 0);
           vector<int> data2(data1);

           
         auto begin1 = steady_clock::now();
         for (int i = 0; i < size; i++){
           data1.pop_back();
         }
         auto end1 = steady_clock::now();
         msec_t elapsed_1 = end1 - begin1;
         
         auto begin2 = steady_clock::now();
         for (int i = 0; i < size; i++){
           data2.erase(data2.begin());
         }
         auto end2 = steady_clock::now();
         msec_t elapsed_2 = end2 - begin2;
           
         cout << std::setprecision(6) << std::fixed
              << size << '\t'
              << std::setw(8) << elapsed_1.count() << '\t'
              << std::setw(8) << elapsed_2.count() << "\t"
              << std::setprecision(0)
              << std::setw(8) << elapsed_2.count() / elapsed_1.count() << " times\n";
       }
       return 0;
   }


Although erase is :math:`O(n)`, a graph showing how much faster ``pop_back()``
can be as the size of a vector grows can still be surprising.


.. plot::
   :alt: 

   import matplotlib.pyplot as plt

   pre_allocated_times = [0.032560, 1.304584, 2.185269, 2.741993, 4.140298,
            4.769269, 5.732273, 6.211213, 7.903502, 8.875864, 8.971830,
            10.871387, 10.237928, 11.157351, 12.564938, 12.729338,
            13.665438, 14.635036, 15.659069, 16.639636]

   size = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
   pop_back_times = [77.484000, 207.863000, 260.518000, 337.395000,
          415.250000, 491.310000, 534.726000, 638.469000, 690.822000]
   erase_times = [3958.742000, 17091.076000, 38126.306000, 66376.176000,
          103593.720000, 144023.923000, 198196.516000, 259339.321000, 326903.495000]

   plt.figure(figsize=(8, 6))
   plt.plot(size, pop_back_times, marker='o', label='pop_back')
   plt.plot(size, erase_times, marker='^', label='erase')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (microsec)', fontsize=12)
   plt.title('Comparison of pop_back() and erase() times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()


**Self Check**

.. tabbed:: tab_check

   .. tab:: Q1


      .. dragndrop:: matching_VectorBO
         :feedback: Review operations and their complexity
         :match_1: begin(), end(), size(), index [], index assignment = ,push_back(), pop_back()||| O(1) 
         :match_2: reserve(), erase(i), insert(i, item),find(srt, stp, item)|||O(n)
         :match_3: find(srt, stp, item)|||O(log n)
         
         Drag the operation(s) on the left to their corresponding complexity


-----

.. admonition:: More to Explore

   - :ref:`analysis_big_o`
   - cppreference.com `std::vector <http://en.cppreference.com/w/cpp/container/vector>`__ overview
   - `Average time complexity <https://yourbasic.org/algorithms/amortized-time-complexity-analysis/>`__




