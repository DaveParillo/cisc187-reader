..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: object pointers
   pair: pointers; class members

Pointers to objects
===================

As we have previously discussed, pointers can point to anything.
We create pointers to objects much like any other type.

Raw pointers where we have to manage the memory ourselves:

.. code-block:: cpp

   int* p = new int{5};
   dog* d = new dog{"Fido"};

And smart pointers that manage the memory for us:

.. code-block:: cpp

   auto p = std::unique_ptr<int>(new int{5});
   auto d = std::unique_ptr<dog>(new dog{"Fido"});

In both cases, the initialization essentially identical.

Given a simple :term:`POD` for a dog:

.. code-block:: cpp

  struct dog {
    std::string name;
    double age;
  };

Access to members of any objects created uses the *member access operator*
``operator .``:

.. code-block:: cpp

   // create a dog with initial values
   dog buddy = {"Andy", 12.6};

   // use member access operator to get values
   std::cout << "My dog's name and age is: " 
     << buddy.name << " and "
     << buddy.age << ".\n";

When you need to access members through a pointer,
the operator precedence rules for pointer dereference
and member access are a common source of error.
When ``buddy`` is a pointer:

.. code-block:: cpp

   auto buddy = std::unique_ptr<dog>(new dog{"Andy", 12.6});

It seems that if ``buddy.name`` works when not a pointer, then
given a pointer to a ``buddy``, that ``*buddy.name``
should work, but it does not.
The member access operator has higher precedence than
the dereference operator.
The code ``*buddy.name`` is equivalent to ``*(buddy.name)``.
This is almost always a bug.
In this case, ``name`` is not a pointer type and cannot be dereferenced.

Explicit use of parentheses is one way to fix this problem:

.. code-block:: cpp

   (*buddy).name

This works, but the syntax is ugly.
For this reason, the ``operator ->`` is used to 
access members of a pointer to an object.
The code ``buddy->name`` is easier to read than ``(*buddy).name``.

Putting it all together:

.. activecode:: class_i_intro_summary_ac
   :language: cpp
   :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
   :nocodelens:

   #include <iostream>
   #include <memory>
   struct dog {
     std::string name;
     double age;
   };

   int main() {
     using std::cout;
     auto buddy = std::unique_ptr<dog>(new dog{"Andy", 12.6});

     cout << "name using dereference and member access: " << (*buddy).name
          << '\n'
          << "name using pointer to member: " << buddy->name;
   }

The last version is the most commonly used because it is less error prone
and easier to read.


-----

.. admonition:: More to Explore

   - From cppreference.com

     - :lang:`C++ Operator precedence <operator_precedence>` and
       :lang:`member access operators <operator_member_access#Built-in_member_access_operators>`.


