..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: allocators
   pair: memory; new
   pair: memory; delete
   pair: vector; reserve

Allocators
==========
Those of you who have been paying attention may have noticed most
containers in the standard library have declarations like:

.. code-block:: cpp

   template< class T, 
             class Allocator = std::allocator<T>>
   class vector;

What is the second template type parameter for?

An :memory:`allocator` manages the memory of each element stored in
the container. The job of an allocator is similar to what the operators
:memory:`new` and :memory:`delete <new>` do, but in a more generic an extensible way.
An allocator can allocate and deallocate memory for its elements and
initialize and destroy element memory.
And it can perform each of these actions as separate steps.

Why bother?

Allocators were originally conceived during the initial development of
the standard library when library developers realized that some classes
that took a template parameter of type ``T`` could break if ``T`` did
not have a default constructor.
An allocator can create default values for types that don't have their own
default values.
Similarly, an allocator can ensure memory is destroyed when we are
finished with it.
In short, the original ``new`` and ``delete`` operators did not handle
all the cases required for advanced memory management.

- Designers realized the container should be independent of the underlying memory model.
  For example, the  Intel Memory Model on x86 architectures use six different variants:
  
  tiny, small, medium, compact, large, and huge.

  Allocators allow container users to define exactly the memory allocation scheme
  appropriate for their runtime environment.
  
- Containers separate the memory allocation and deallocation from the 
  initialization and destruction of their elements.

  A call to :container:`vector::reserve(n) <vector/reserve>` 
  allocates memory for at least n elements.
  The constructor for each element will **not** be called.

We can handle types without a default value by giving users the option
to specify the value to be used when we need a default:

.. code-block:: cpp

     void resize(size_t new_capacity, T default_value = T())
     {
       reserve(new_capacity);
       std::fill(begin()+size_, begin()+capacity_, default_value);
       size_ = new_capacity;
     }

This form of resize() will use ``T()``, unless the user provides an alternative.
For example:

.. code-block:: cpp

   bag<double> stuff;
   stuff.resize(100);        // add 100 doubles all == 0.0
   stuff.resize(200, 3.14);  // add 200 copies of 3.14
   stuff.resize(300, 0.0);   // add 200 copies of 0.0 (redundant)


The destructor problem is harder to address.
We need to deal with a data structure that may contain a mix of some
initialized data and some uninitialized data.
Typically, we are very careful to avoid uninitialized data and
the associated programming errors.
Now as the developers of generic containers we have to handle this problem
so that users of these containers don't have to.

First we need a way to get an manipulate uninitialized storage.
**This** is where :memory:`allocator` comes in.
A simplified allocator looks like this:

.. code-block:: cpp

   template<class T>
     class allocator {

       using value_type    = T;
       // other types and constructors omitted

       T*   allocate  (size_t n);        // allocate space to n objects of T
       void deallocate(T* p, size_t n);  // deallocate n objects of T
                                              // starting at location p

       void construct(T* p, const T& value);  // construct a value of T in p
       void destroy  (T* p);                  // destroy the T in p

     };

These 4 functions provide the core capabilities of an allocator:

- Allocate memory of a size suitable to hold an object of type ``T``
  *without initializing it*.
- Construct an object of type ``T`` in uninitialized space.
- Destroy an object of type ``T`` - returning the memory space
  to the uninitialized state.
- Deallocate uninitialized memory of size suitable for an object of type ``T``.

.. index:: allocator_traits
   pair: allocator_trits; allocate
   pair: allocator_trits; construct
   pair: allocator_trits; deallocate
   pair: allocator_trits; destroy

Using std::allocator_traits
---------------------------
An allocator is exactly what a container to separate 
memory allocation from object construction and
memory deallocation from object destruction.

How does a container use an allocator?
First, as in the standard library, we need a allocator type parameter
and a local variable to store an instance of the allocator.
Although you can use an allocator directly,
the allocator interfaces are deprecated, and we are going to use
the :memory:`allocator_traits` interface.
The allocator_traits class template provides the standardized way
to access various properties of Allocators.
The standard containers and other standard library components access
allocators through this template, which makes it possible to use any
class type as an allocator.

.. code-block:: cpp

   template<class T, class Allocator = std::allocator<T>>
    class bag {

      Allocator allocator_;

      // . . .
    };

The :memory:`allocator_traits` interface consists entirely of static
members - no object instance exists and it is completely stateless,
however the syntax is a bit verbose, which is why I frequently alias it
in a class:

.. code-block:: cpp

   template<class T, class Allocator = std::allocator<T>>
    class bag {

      Allocator allocator_;
      using memory = std::allocator_traits<Allocator>;

      // . . .
    };

Now except for using our allocator object, the class is unchanged.
Container users can ignore the allocator unless they need a ``bag``
that manages memory for its elements in some unusual way.

The only class functions that require modification are those that deal
directly with memory:

- object construction and destruction
- memory allocation and deallocation


.. code-block:: cpp

   void reserve(size_t new_capacity)
   {
     // never decrease allocation
     if (new_capacity <= capacity_) {
       return;
     }
     // allocate new space
     T* new_data = new T[new_capacity];

     // copy into new space
     std::copy(begin(), end(), new_data);

     // delete old memory
     delete[] data_;

     // point to the new data
     data_ = new_data;
     capacity_ = new_capacity;
   }

Refactoring the original version of ``reserve`` to use an allocator
involves several steps.



.. code-block:: cpp

   void reserve(size_t new_capacity)
   {
     // never decrease allocation
     if (new_capacity <= capacity_) {
       return;
     }

     // allocate new space
     T* new_data = memory::allocate(allocator_, new_capacity);

     // copy into new space
     for (size_t i = 0; i < new_capacity; ++i) {
       memory::construct(allocator_, &new_data[i], data_[i]);
     }

     // delete old memory
     for (size_t i = 0; i < capacity_; ++i) {
       memory::destroy(allocator_, &data_[i]);
     }

     // deallocate old space
     memory::deallocate(allocator_, data_, capacity_);
     data_ = new_data;
     capacity_ = new_capacity;
   }



-----

.. admonition:: More to Explore

   - From cppreference.com

     - Named requirement :cpp:`Allocator <named_req/Allocator>`
     - :memory:`allocator_traits`
     - :memory:`new`

   - Writing allocators

     - `Memory Management with std::allocator <https://www.modernescpp.com/index.php/memory-management-with-std-allocator>`__
     - `Allocator Boilerplate <https://howardhinnant.github.io/allocator_boilerplate.html>`__

