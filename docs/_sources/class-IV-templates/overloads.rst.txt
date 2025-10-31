..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: class; operator[] overload
   pair: array index; operator overload

Overloading ``operator[]``
==========================
User-defined types that provide array-like access that allows both reading and writing
often overload ``operator[]``.

One of the rules of the language is that ``operator[]`` must be implemented
as a member function.
Generally ``const`` and non-const versions of the overload are implemented.

.. code-block:: cpp

   struct T
   {
             value_t& operator[](size_t index)       { return data[index]; }
       const value_t& operator[](size_t index) const { return data[index]; }
   };

In addition to the member-only rule that the C++ language requires,
there are a few best practice considerations for this operator.
They mostly center around the fact that `operator[]`` can only accept a single value.
What if you want to use this operator in a user defined type that
behaves like a multi-dimensional array?

Often people attempt to overload `operator[][]` - but it does not exist.

In general, if you have a type with single dimension access,
then it's OK to overload ``operator[]``.
If your type has data in multiple dimensions, then
prefer overloading ``operator()`` instead.
For a detailed description of the *why*, refer to the following subsection.


Multi-dimension array access
----------------------------
To provide multidimensional array access semantics, 
e.g. to implement a 3D array access ``a[i][j][k] = x;``,
the overload for ``operator[]`` must return a reference to a 2D object, 
which has to have its own ``operator[]`` which returns a reference to a 1D object,
which has to have ``operator[]`` which returns a reference to the element. 
To avoid this complexity, 
some libraries opt for overloading ``operator()`` instead.

Because ``operator()`` does not have the one parameter restriction that
``operator[]`` does, functions taking multiple parameters can be implemented
directly without any excessive complicated function call chaining.
And for users, the syntax is cleaner:

.. code-block:: cpp

   int main() {

     matrix a;
     
     // operator[] syntax
     a[i][j][k] = value;

     // operator() syntax
     a(i,j,k) = value;

   }

In the following example, notice that our matrix class uses a simple
one dimensional array as its :term:`backing store`.
So even though our class exposes a two-dimensional interface,
our data is stored differently.

.. code-block:: cpp
   
   data_ = new T[rows * cols];

An array is simple and efficient.
The class does not expose this implementation detail and if we wanted
to replace the array with something else later,
no matrix class users would be affected.

.. tabbed:: matrix_tab1

   .. tab:: operator() Example

      
      When using the ``operator()`` overload,
      only a single pair of functions is required,
      one function to return the value
      and other to return a value that can be assigned to a ``const``.

      This solution is general and scales up and down as needed,
      easily accommodating more or fewer dimensions.


      .. code-block:: cpp

         T& matrix<T>::operator() (size_t row, size_t col);

         const T& matrix<T>::operator() (size_t row, size_t col) const;


      One note about the above examples.
      If you know the type ``T`` is a primitive type,
      or you have a non-templated matrix and you define your value type
      to be a built in type (int, double, etc), then you should
      return by value instead of const reference.

      .. code-block:: cpp

         double& matrix::operator() (size_t row, size_t col);

         const double matrix::operator() (size_t row, size_t col) const;


      The non-const version should still be a reference to the value in the
      :term:`backing store`, so that it can be modified.

      If you don't want users modifying your data at all, then only provide
      a ``const`` version of the operator overload.


   .. tab:: Run It

      .. activecode:: ac_matrix_function_call_operator
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:
   
         #include <algorithm>
         #include <cstdlib>
         #include <iostream>
         #include <stdexcept>

         template <class T>
         class matrix {
         public:
           matrix(size_t rows, size_t cols);
           T& operator() (size_t row, size_t col);
           const T&  operator() (size_t row, size_t col) const;
           // ...
          ~matrix();
           explicit matrix(const matrix& m);
           // matrix& operator= (const matrix& m);
           // many other useful functions not implemented
         private:
           size_t rows_;
           size_t cols_;
           T* data_;
         };

         template <class T>
         inline
         matrix<T>::matrix(size_t rows, size_t cols)
           : rows_ (rows)
           , cols_ (cols)
         {
           if (rows == 0 || cols == 0)
             throw std::out_of_range("Matrix constructor has 0 size");
           data_ = new T[rows * cols];
           for (size_t i = 0; i < rows_*cols_; ++i) {
               data_[i] = 0;
           }
         }

         template <class T>
         inline
         matrix<T>::matrix(const matrix<T>& m)
           : rows_ (m.rows_)
           , cols_ (m.cols_)
         {
           std::copy(m.data_, m.data_+rows_*cols_, data_);
         }

         template <class T>
         inline
         matrix<T>::~matrix()
         {
           delete[] data_;
         }

         template <class T>
         inline
         T& matrix<T>::operator() (size_t row, size_t col)
         {
           if (row >= rows_ || col >= cols_)
             throw std::out_of_range("Matrix subscript out of bounds");
           return data_[cols_*row + col];
         }

         template <class T>
         inline
         const T& matrix<T>::operator() (size_t row, size_t col) const
         {
           if (row >= rows_ || col >= cols_)
             throw std::out_of_range("const Matrix subscript out of bounds");
           return data_[cols_*row + col];
         }

         int main()
         {
             matrix<double>a {3,5};
             a(0,0) = -1;
             a(1,1) = 1;
             a(1,2) = 2;
             a(1,3) = 3;
             a(2,4) = 5;
             
             for (size_t i = 0; i<3; ++i) {
               for (size_t j = 0; j<5; ++j) {
                  std::cout << a(i,j) << ' ';
               }
                 std::cout << '\n';
             }
         }

In the interest of completeness, the following example shows one way to
implement a 2D matrix class that provides an interface for ``my_matrix[i][j]``.
This example uses a vector of vectors,
although other solutions are possible.
                  
.. tabbed:: matrix_tab2

   .. tab:: operator[] Example

      What are the main differences from the preceding implementation?

      The backing store is a vector of vectors:

      .. code-block:: cpp

         std::vector<std::vector<T>> data_;

      As previously discussed, the ``operator[]`` takes at most a 
      single parameter.
      This means we must return a ``vector<T>&`` from our operator.

      .. code-block:: cpp

         std::vector<T>& operator[] (size_t row);

      How does the second dimension work?

      Recall that the vector class has its own ``operator[]`` overload.
      The final dimension with the element value is retrieved from
      the index into the column vector of the matrix.


      A destructor is no longer needed because this version of the matrix
      class does not manage its own memory.
      All the memory management is handled by the vector class.

   .. tab:: Run It

      .. activecode:: ac_matrix_index_operator
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:
   
         #include <cstdlib>
         #include <iostream>
         #include <vector>

         template <class T>
         class matrix {
           public:
             matrix(size_t rows, size_t cols);
             explicit matrix(const matrix& m);
             
             std::vector<T>& operator[] (size_t row);
             const std::vector<T>& operator[] (size_t row) const;

             size_t rows() const {return data_.size(); }
             size_t cols() const
             {
                 return rows()? data_[0].size(): 0; 
             }
           private:
             std::vector<std::vector<T>> data_;
         };

         template <class T>
         inline
         matrix<T>::matrix(size_t rows, size_t cols)
           : data_ (rows)
         {
           for (auto& row: data_) {
             row.resize(cols);
           }
         }

         template <class T>
         inline
         matrix<T>::matrix(const matrix<T>& m)
           : data_ (m.data_)
         { }

         template <class T>
         inline
         std::vector<T>& matrix<T>::operator[] (size_t row)
         {
             return data_[row];
         }

         template <class T>
         inline
         const std::vector<T>& matrix<T>::operator[] (size_t row) const
         {
           return data_[row];
         }

         int main()
         {
             matrix<double>a {3,5};
             a[0][0] = -1;
             a[1][1] = 1;
             a[1][2] = 2;
             a[1][3] = 3;
             a[2][4] = 5;
             
             for (size_t i = 0; i<3; ++i) {
               for (size_t j = 0; j<5; ++j) {
                  std::cout << a[i][j] << ' ';
               }
                 std::cout << '\n';
             }
         }

               
                                    

-----

.. admonition:: More to Explore

   - `Operator overloading in C++ <https://stackoverflow.com/questions/4421706/what-are-the-basic-rules-and-idioms-for-operator-overloading>`__ from stackoverflow.  
   - `ISO C++ FAQ: 'How do I create a subscript operator for a Matrix class?' <https://isocpp.org/wiki/faq/operator-overloading#matrix-subscript-op>`__
 
