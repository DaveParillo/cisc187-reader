..  Copyright (C)  Brad Miller, David Ranum, and Jan Pearce

    This work is licensed under the Creative Commons
    Attribution-NonCommercial-ShareAlike 4.0 International License. To view a
    copy of this license, visit
    http://creativecommons.org/licenses/by-nc-sa/4.0/.

.. index::
   pair: analysis; string

Analysis of String Operators
============================
Prior to C++11 the string class was not required to store its
character elements contiguously. Now string acts much like the vector class, except
for some string optimizations and other minor differences.

C++11 strings use contiguous storage locations
in an underlying (typically larger) array just like :container:`vector`.
Due to this, the character elements in strings can be accessed and
traversed with the help of iterators, and they
can also be accessed randomly using indexes.

Like vectors, strings have a dynamic size meaning that whenever
a new character is inserted or deleted,
their size changes automatically.
Just like vectors, new elements can be inserted into or deleted from any part of a string,
and automatic reallocation for other existing items in the string is applied.

Indexing and assigning a new character to an index position
that already exists both take :math:`O(1)`, in other words,
the same amount of time no matter how large the string is.

Now that we have seen how performance can be measured concretely you can
look at the :ref:`string operations table <tbl_strbigocpp>`
to see the Big-O efficiency of all the basic string operations and you
will see a striking resemblance to vectors because
the implementations are so similar.

.. _tbl_strbigocpp:

.. table:: **Big-O Efficiency of C++ String Operations**

    ===================== ==================
                Operation   Big-O Efficiency
    ===================== ==================
                 index []               O(1)
       index assignment =               O(1)
              push_back()     amortized O(1)
               pop_back()               O(1)
                 erase(i)               O(n)
          insert(i, item)               O(n)
         find(b, e, item)   O(log n) or O(n)
                reserve()               O(n)
                  begin()               O(1)
                    end()               O(1)
                   size()               O(1)
    ===================== ==================


`push_back()` is :math:`O(1)` unless there is inadequate capacity.
Then the entire string is moved to a larger contiguous underlying array.
Copying all the old string data to a new location is :math:`O(n)`.

.. index::
   single: std::chrono
   pair: analysis; string

The previous table says that ``find`` could be :math:`O(n)` or :math:`O(\log(n))`.
One might ask why not just write a little for loop instead?
Searching for a value seems like such a simple thing.
Why go through the effort to figure out how to use all these string functions?
Let's find out.

In the program below, the time to perform operations is measured using the
:cpp:`std::chrono<chrono>` library.
It provides a flexible collection of types that track time with varying degrees of precision.
:chrono:`steady_clock::now<steady_clock/now>` returns the current time.
The elapsed time between two time points is stored in a :chrono:`duration` object.
Duration objects make it obvious what the time units are and also makes it easy to convert.
The is one of the major advantages over the C time functions.

To use the ``steady_clock`` to time an algorithm or function, create two time points.
To get the total runtime, subtract the begin time from the end time.

.. activecode:: string_analysis_explore_find_ac1
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-std=c++20']
   :nocodelens:

   This example creates a series of increasingly long strings.

   Every character except for one is the same.

   The program prints how long it takes to find it when placed
   at the midpoint of the string.

   ~~~~
   #include <chrono>
   #include <iomanip>
   #include <iostream>
   #include <string>

   int main() {
       using std::cout;
       using std::chrono::steady_clock;
       using msec_t = std::chrono::duration<double, std::milli>;
       
       cout << std::setw(6) << "size\t\t"
            << std::setw(8) << "string::find\t"
            << std::setw(8) << "for loop (all times in msec)\n";
       for(int size = 1e6; size < 1e8; size += 5e6) {
           // create a big string
           std::string haystack (size, 'h');

           // insert a unique character
           auto needle = 'n';
           haystack[size/2] = needle;

           // search for needle in haystack using string find function
           auto begin = steady_clock::now();
           if (haystack.find(needle) == std::string::npos) {return -1;}  // error
           auto end = steady_clock::now();
           msec_t elapsed_msecs = end - begin;

           // search for needle in haystack using a for loop
           auto begin_for = steady_clock::now();
           for (auto k = 0; k < size; ++k) {
               if (haystack[k] == needle) { break; }
               if (k > size/2)            { return -2; }  // error
           }
           auto end_for = steady_clock::now();
           msec_t for_msecs = end_for - begin_for;
           
           cout << std::setw(6) << size << '\t';
           if (size < 9e6) { cout << '\t'; }
           cout << std::setprecision(6) << std::fixed
                << std::setw(8) << elapsed_msecs.count() << '\t'
                << std::setw(8) << for_msecs.count() << '\n';
       }
       return 0;
   }


A graph of the loops in the preceding code should look something like this:

.. plot::
   :alt: Comparison of string::find and for loop times

   import matplotlib.pyplot as plt

   size = [1000000, 6000000, 11000000, 16000000, 
           21000000, 26000000, 31000000, 36000000,
           41000000, 46000000, 51000000, 56000000, 
           61000000, 66000000, 71000000, 76000000, 
           81000000, 86000000, 91000000, 96000000]
   string_find_time = [0.024468, 0.218486, 0.359959, 0.602038, 0.814801, 
                       1.074333, 1.189831, 1.373441, 1.563834, 1.719521,
                       1.945079, 2.099539, 2.190302, 2.439188, 2.716300,
                       2.764016, 3.105540, 3.266905, 3.254770, 3.504598]
   for_loop_time = [1.522594, 9.030538, 16.719590, 25.310635, 35.890875,
                    40.771007, 46.808778, 55.002455, 61.804416, 69.015913,
                    76.374849, 85.228255, 99.184631, 100.451749, 110.015415,
                    114.440083, 121.729622, 127.503536, 135.736084, 147.112380]
   plt.figure(figsize=(8, 6))
   plt.plot(size, string_find_time, marker='o', label='std::string::find')
   plt.plot(size, for_loop_time, marker='^', label='for loop')

   plt.xlabel('Size', fontsize=12)
   plt.ylabel('Time (msec)', fontsize=12)
   plt.title('Comparison of string::find and for loop times', fontsize=14)
   plt.legend(fontsize=12)
   plt.xticks(fontsize=12)
   plt.yticks(fontsize=12)

   plt.show()


.. admonition:: Try This!

   What is the Big-O of :string:`find`? :math:`O(n)` or :math:`O(\log(n))`?

   What happens if the needle value is in a location other than the midpoint?
   Try the beginning and end to see what happens.

   Challenge: Try putting the needle in a random location to see what happens.



-----

.. admonition:: More to Explore

   - :ref:`analysis_big_o`
   - cppreference.com `Strings library <http://en.cppreference.com/w/cpp/string>`_ overview
   - Mike Shahar post: `Exploring std::string <https://shaharmike.com/cpp/std-string/>`_
   - `Average time complexity <https://yourbasic.org/algorithms/amortized-time-complexity-analysis/>`__




