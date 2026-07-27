..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: associative containers; map
   single: key-value pair
   single: std::pair

The map class
=============

A :term:`map` refers to any data structure that maps :term:`keys <key>` to
values. The standard-library ``map`` stores each key together with its mapped
value in a :utility:`std::pair <pair>`.

The containers discussed so far have focused on storing one thing at a time.
That is, each stores values of a single type.
Maps add a new wrinkle.
A ``map`` stores :utility:`pairs <pair>` of things.
Traditionally, the pair stored is referred to as a :term:`key-value pair`.\ [1]_

Nearly every programming language provides some kind of ``map`` implementation.
Some languages use the terms *associative array* or *dictionary*,
but structurally, they are very similar.

**Values** are retrieved from a ``map`` using the **key**.
Each :term:`key` must be unique.
In other words, keys are members of a ``set``.
Like a :container:`std::set <set>`, inserting a second node with the same key
has no effect. The mapped value can be updated through ``operator[]`` or
``insert_or_assign``.
Unlike a ``std::set``,
a :container:`std::map <map>` provides the :container:`map::operator[] <map/operator_at>`.

The examples on this page use the following shared setup:

.. code-block:: cpp
   :name: map-common

   #include <iostream>
   #include <functional>
   #include <map>
   #include <set>
   #include <string>

   std::map<std::string, int> sample_inventory() {
     return {
       {"apple", 12},
       {"kiwi", 4},
       {"lemon", 1},
       {"pear", 4},
       {"peach", 4},
       {"grape", 100},
       {"cocoa", 3}
     };
   }

The following complete example demonstrates iteration, updating an existing
mapped value, inserting through ``operator[]``, and checked access with
``at``:

.. tb-code:: cpp
   :name: map_basics_ac
   :run-before: map-common

   int main() {
     std::map<std::string, int> name_counts {
       {"Alice", 27},
       {"Bob", 3},
       {"Clara", 1}
     };

     for (const auto& kvp : name_counts) {
       std::cout << kvp.first << ": " << kvp.second << '\n';
     }

     name_counts["Bob"] = 42;       // update an existing value
     name_counts["Darla"] = 9;      // insert a missing key

     std::cout << "Bob is " << name_counts.at("Bob") << '\n';
     std::cout << "Darla is " << name_counts["Darla"] << '\n';
   }

``operator[]`` default-initializes a mapped value when the key is absent.
Use ``at`` when a missing key should be reported instead; ``at`` throws
``std::out_of_range`` for an absent key. Neither operation changes the key
ordering.

The :container:`map::insert <map/insert>` function follows the same unique-key
contract as ``set::insert``: an equivalent key is not inserted and an existing
mapped value is not overwritten. Use ``insert_or_assign`` when an update is
intended.

.. cpp:: 17

   C++17 added ``insert_or_assign`` and ``try_emplace`` for code that wants
   to state its insertion or update intent explicitly. ``insert_or_assign``
   updates an existing mapped value, while ``try_emplace`` does nothing when
   the key already exists and constructs the mapped value only when needed.

   .. tb-code:: cpp
      :name: map_insert_or_assign_ac
      :run-before: map-common

      int main() {
        auto inventory = sample_inventory();
        inventory.insert_or_assign("kiwi", 10);
        inventory.try_emplace("mango", 6);

        std::cout << inventory.at("kiwi") << ' '
                  << inventory.at("mango") << '\n';
      }

.. cpp:: 20

   C++20 added :container:`map::contains <map/contains>` for membership
   checks when the mapped value is not needed.

   .. tb-code:: cpp
      :name: map_contains_ac
      :run-before: map-common

      int main() {
        const auto inventory = sample_inventory();
        std::cout << std::boolalpha
                  << inventory.contains("kiwi") << ' '
                  << inventory.contains("mango") << '\n';
      }

.. cpp:: 20

   C++20 also provides :algorithm:`std::erase_if <erase_if>` for removing
   map entries based on their key-value pairs.

   .. tb-code:: cpp
      :name: map_erase_if_ac
      :run-before: map-common

      int main() {
        auto inventory = sample_inventory();
        std::erase_if(inventory, [](const auto& entry) {
          return entry.second < 5;
        });

        for (const auto& entry : inventory) {
          std::cout << entry.first << ": " << entry.second << '\n';
        }
      }

Selected map functions
----------------------
Access and assignment
    :container:`at and operator[] <map/operator_at>`,
    :container:`insert_or_assign <map/insert_or_assign>`
Capacity
    :container:`empty <map/empty>`, :container:`size <map/size>`, and :container:`max_size <map/max_size>`
Modifiers
    :container:`clear <map/clear>`, :container:`emplace <map/emplace>`,
    :container:`insert <map/insert>`, :container:`try_emplace <map/try_emplace>`,
    :container:`erase <map/erase>`, and :container:`swap <map/swap>`
Lookup
    :container:`count <map/count>`, :container:`find <map/find>`, :container:`equal_range <map/equal_range>`, 
    :container:`upper_bound <map/upper_bound>`,
    :container:`lower_bound <map/lower_bound>`, and
    :container:`contains <map/contains>`

For an ordered ``map``, lookup, insertion, and erasure take :math:`O(\log N)`
time and the container uses :math:`O(N)` storage. A sequential container may
be faster for small data sets or workloads that benefit from contiguous
storage, so the choice should be based on the operations the program needs.

.. note::

   There is no ``push_back()`` for a map.

   The ``map`` decides where elements go, not you.
   All access requires either knowing the key or having an iterator.

Map structure
-------------
Internally, a ``map`` is an ordered tree-like structure. Implementations often
use a self-balancing tree such as a :wiki:`Red-black tree <Red-black_tree>`;
the standard does not require a particular implementation.
Each node in the tree is a :utility:`std::pair <pair>`.


.. digraph:: larger
   :alt: An ordered tree used to illustrate map keys

   graph [
          nodesep=0.25, ranksep=0.3, splines=line;
          labelloc=b;
          label="An ordered tree of map entries";
       ];
   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=circle, fixedsize=true, width=0.3];
   edge [weight=1, arrowsize=0.5, dir=none];

   a, b, am, c, d, bm, e, f, cm, g, h, dm, i, j, em, k, l, fm, m;
   am, bm, cm, dm, em, fm [style=invis, label=""];

   a->b,c;
   b->d [weight=2]; // nudge b: trees b & c are not balanced
   b->e;
   c->f,g;
   d->h,i;
   e->j,k;
   f->l,m;

   edge [style=invis, weight=100];
   d->dm; 
   e->em;
   b->bm;
   f->fm;
   c->cm;
   a->am;

Map entries are ordered by their :term:`keys <key>`, using a comparison object
that defines a :req:`strict weak ordering <Compare>`. The default comparison
uses ``operator<``, but the map constructor can receive a custom comparator,
just as with a ``set``.

The map's ``value_type`` is a pair whose first member is ``const``. A key
cannot be changed through an iterator because that could violate the ordering
invariant, but the mapped value can be changed.

All map entries are visited in key order according to the map's comparison
object. By default, that is ascending order according to ``operator<``. The
following example extracts keys into a ``set`` and then uses ``upper_bound``
to find the first key greater than ``"kiwi"``.

.. tb-code:: cpp
   :name: map_lookup_ac
   :run-before: map-common

   int main() {
     const auto inventory = sample_inventory();
     std::set<std::string> inventory_keys;

     for (const auto& entry : inventory) {
       inventory_keys.insert(entry.first);
     }

     std::cout << "All fruit keys:\n";
     for (const auto& key : inventory_keys) {
       std::cout << key << ' ';
     }

     std::cout << "\nKeys greater than kiwi:\n";
     for (auto it = inventory.upper_bound("kiwi");
          it != inventory.end();
          ++it) {
       std::cout << it->first << ' ';
     }
     std::cout << '\n';
   }

Maps can use a custom comparator just like sets. This complete example stores
the same entries in descending key order:

.. tb-code:: cpp
   :name: map_custom_compare_ac
   :run-before: map-common

   int main() {
     const auto inventory = sample_inventory();
     const std::map<std::string, int, std::greater<std::string>> reverse_inventory {
       inventory.begin(), inventory.end()
     };

     for (const auto& entry : reverse_inventory) {
       std::cout << entry.first << ": " << entry.second << '\n';
     }
   }

Variations on ``std::map``
--------------------------
The standard library provides related ordered and unordered containers:

:container:`multimap`
   A ``map`` in which duplicate keys are allowed.

:container:`unordered_map`
   A map of unique keys organized by a :term:`hash function`, not by sorted
   order. Each key still maps to one mapped value.
   Added in C++11.

   A key type needs a hash function and an equality predicate. The standard
   library provides these for many built-in and library types. For a user type,
   provide a ``std::hash<Key>`` specialization or a custom hash object, and
   provide equality through ``operator==`` or a custom equality object.
  
:container:`unordered_multimap`
   An ``unordered_map`` in which duplicate keys are allowed.
 


-----

.. admonition:: More to Explore

   - :cpp:`Standard library containers <container>`
   - :container:`std::map <map>`
   - :container:`std::unordered_map <unordered_map>`
   - :wiki:`Red-black tree <Red-black_tree>` on Wikipedia

.. topic:: Footnotes

 .. [1]  Sometimes this is abbreviated as 'KVP'.  
         On cppreference.com you'll see it shortened even further to just ``P``
