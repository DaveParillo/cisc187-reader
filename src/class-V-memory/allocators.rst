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
:memory:`new` and :memory:`delete <new>` do, but in a more generic and extensible way.
An allocator can allocate and deallocate memory for its elements and
containers can separately initialize and destroy objects in that memory.
The important point is that allocation and construction are separate steps,
and destruction and deallocation are also separate steps.

Why bother?

Allocators were originally conceived during the initial development of
the standard library to allow containers to be independent of a single
hard-coded memory allocation strategy.
They also support the way containers work internally:
a container may allocate storage now, but construct objects in that
storage later.
In short, a container needs more control than a simple use of
``new[]`` and ``delete[]`` provides.

- Designers realized a container should not be tied to exactly one allocation strategy.
  Allocators allow specialized code to choose a memory allocation scheme
  appropriate for its runtime environment.
  
- Containers separate the memory allocation and deallocation from the 
  initialization and destruction of their elements.

  A call to :container:`vector::reserve(n) <vector/reserve>` 
  allocates memory for at least n elements.
  The constructor for each element will **not** be called.

For example, a container can reserve space without constructing any values.
When it later needs to create new elements,
it can require the caller to provide the values to construct.
This avoids requiring ``T`` to be default-constructible:

.. code-block:: cpp

     void resize(std::size_t new_size, const T& value)
     {
       reserve(new_size);
       while (size_ < new_size) {
         push_back(value);
       }
     }

This form of ``resize`` does not need to use ``T()``.
The caller supplies the value used to initialize new elements.
For example:

.. code-block:: cpp

   bag<double> stuff;
   stuff.resize(200, 3.14);  // add copies of 3.14 until size is 200
   stuff.resize(300, 0.0);   // add copies of 0.0 until size is 300


The destruction problem is harder to address.
We need to deal with a data structure that may contain a mix of some
initialized data and some uninitialized data.
Typically, we are very careful to avoid uninitialized data and
the associated programming errors.
Now as the developers of generic containers we have to handle this problem
so that users of these containers don't have to.

First we need a way to get and manipulate uninitialized storage.
**This** is where :memory:`allocator` comes in.
A simplified modern allocator interface looks like this:

.. code-block:: cpp

   template<class T>
   class allocator {
   public:
     using value_type = T;

     // other types and constructors omitted

     T* allocate(std::size_t n);
     void deallocate(T* p, std::size_t n);
   };

The allocator itself allocates and deallocates raw storage.
Containers should use :memory:`allocator_traits` to construct and destroy
objects in that storage.

.. cpp:: 20

   Older allocator examples often show direct allocator member functions
   named ``construct`` and ``destroy``.
   Those direct members of :memory:`allocator` were deprecated in C++17
   and removed in C++20.
   Use :memory:`allocator_traits` instead.

These operations provide the core capabilities containers need:

- Allocate memory of a size suitable to hold an object of type ``T``
  *without initializing it*.
- Construct an object of type ``T`` in uninitialized space using
  :memory:`allocator_traits`.
- Destroy an object of type ``T`` using :memory:`allocator_traits`,
  returning the memory space
  to the uninitialized state.
- Deallocate uninitialized memory of size suitable for an object of type ``T``.

.. index:: allocator_traits
   pair: allocator_traits; allocate
   pair: allocator_traits; construct
   pair: allocator_traits; deallocate
   pair: allocator_traits; destroy

Using std::allocator_traits
---------------------------
An allocator is what a container uses to separate memory allocation
from object construction, and memory deallocation from object destruction.

How does a container use an allocator?
First, as in the standard library, we need an allocator type parameter
and a local variable to store an instance of the allocator.
Although you can use an allocator directly,
some old direct allocator member functions are no longer part of C++20.
We are going to use the :memory:`allocator_traits` interface.
The ``allocator_traits`` class template provides the standardized way
to access various properties of allocators.
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

   void reserve(std::size_t new_capacity)
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
This sketch shows the main idea, but it omits the exception-safety details
required in a production container.

.. code-block:: cpp

   void reserve(std::size_t new_capacity)
   {
     // never decrease allocation
     if (new_capacity <= capacity_) {
       return;
     }

     // allocate new space
     T* new_data = memory::allocate(allocator_, new_capacity);

     // copy into new space
     for (std::size_t i = 0; i < size_; ++i) {
       memory::construct(allocator_, &new_data[i], data_[i]);
     }

     // destroy old elements
     for (std::size_t i = 0; i < size_; ++i) {
       memory::destroy(allocator_, &data_[i]);
     }

     // deallocate old space
     if (capacity_ != 0) {
       memory::deallocate(allocator_, data_, capacity_);
     }
     data_ = new_data;
     capacity_ = new_capacity;
   }

For real container code, if construction of one of the new elements throws,
the already-constructed new elements must be destroyed and the newly allocated
memory must be deallocated before the exception continues.
That is one reason writing standard-library-quality containers is difficult.

For most programs, do not write your own allocator or container.
Use the standard containers and RAII types first.
If a program needs to choose a memory allocation strategy at runtime,
the C++17 :memory:`pmr` library provides polymorphic allocators and
memory resources designed for that purpose.



-----

.. admonition:: More to Explore

   - From cppreference.com

     - Named requirement :cpp:`Allocator <named_req/Allocator>`
     - :memory:`allocator_traits`
     - :memory:`new`

   - Writing allocators

     - `Memory Management with std::allocator <https://www.modernescpp.com/index.php/memory-management-with-std-allocator>`__
     - `Allocator Boilerplate <https://howardhinnant.github.io/allocator_boilerplate.html>`__
