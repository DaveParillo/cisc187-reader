..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: open hashing; collisions

Open hashing
============
One collision avoidance strategy is :term:`separate chaining`.
In separate chaining the hash table is implemented as an array of 
variable sized containers that can hold however many elements that have 
actually collided at each array location.

A linked list is a typical choices for implementing the chain,
which is where the term "chaining" actually originates.

.. tabbed:: tab_graph

   .. tab:: Example set

      .. digraph:: hashtable
         :alt: Fruit set
         :align: center

         graph [ 
           fontname = "Bitstream Vera Sans", 
           labelloc=b,
           label="Fruit set hash table"
           nodesep = .05;
           rankdir = LR;
         ];

         node[shape = record,  width = .1,  height = .1, 
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ",  height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | <p>}"];
         node2[label = "{<n> pear | <p>}"];
         node3[label = "{<n> apple | <p>}"];
         node4[label = "{<n> lemon | <p>}"];
         node5[label = "{<n> grape | <p>}"];
         node6[label = "{<n> lime | <p>}"];
         node7[label = "{<n> banana | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p:c->node6:n [arrowtail=dot, dir=both, tailclip=false];
         node4:p:c->node7:n [arrowtail=dot, dir=both, tailclip=false];

   .. tab:: Example map

      When the ADT is a map, the process is similar.
      In a map ADT, the value hashed is the map :term:`key`,
      since this is what uniquely identifies map items.

      Each :term:`bucket` provides access to one or more map entries
      (:term:`key-value pairs <key-value pair>`).

      .. digraph:: hashtable
         :alt: Fruit inventory map
         :align: center

         graph [ 
           fontname = "Bitstream Vera Sans", 
           labelloc=b,
           label="Fruit inventory hash table"
           nodesep = .05;
           rankdir = LR;
         ];

         node[shape = record,  width = .1,  height = .1, 
              fontsize=14, style=filled, fillcolor=lightblue];
         edge [arrowhead=vee, arrowsize=0.5];

         node0[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 ",  height = 2.5];

         node [width = 1.5];
         node1[label = "{<n> kiwi | 8 | <p>}"];
         node2[label = "{<n> pear | 5 | <p>}"];
         node3[label = "{<n> apple | 12 | <p>}"];
         node4[label = "{<n> lemon | 1 | <p>}"];
         node5[label = "{<n> grape | 13 | <p>}"];
         node6[label = "{<n> lime | 35 | <p>}"];
         node7[label = "{<n> banana | 3 | <p>}"];

         node0:f0->node1:n;
         node0:f1->node2:n;
         node0:f2->node3:n;
         node0:f5->node4:n;
         node0:f6->node5:n;
         node2:p:c->node6:n [arrowtail=dot, dir=both, tailclip=false];
         node4:p:c->node7:n [arrowtail=dot, dir=both, tailclip=false];


The linked lists allows the hash table to be dynamically sized,
and each array element is its own :term:`bucket`.

A :term:`set` provides a simple demonstration of the capabilities
of a hashed data structure.
Recall that :container:`set` defines a container that stores
unique items.

.. tabbed:: hash_set_tab_group

   .. tab:: hash_set

      The template variables for a hash set defines the type
      of data stored in the set: the ``Key``.
      This hash table will be fixed size, so we denote that with
      the non-type template parameter ``N``.
      The Comparator allows the template to accept a function
      used to find items in the chain.
      The default is :algorithm:`equal`, but another 
      :term:`binary predicate<predicate>` can be substituted.

      .. code-block:: cpp

         template <class Key,
                   size_t N,
                   class Comparator=std::equal_to<Key>>
         class hash_set 
         {
           public:
             using Container = std::list<Key>;
             using value_type = Key;
             using key_type   = Key;
             using iterator   = typename Container::iterator;
             using const_iterator  = const iterator;

             hash_set () = default;

           private:
             std::array<Container, N> buckets;
             Comparator compare;
             int sz = 0;

         };

   .. tab:: find

      Finding anything in a hash table using separate chaining
      is a two step process.  Consider the following :term:`hash table`:

      .. digraph:: hashtable
         :alt: Simple hash table
         :align: center

         graph [ 
           fontname = "Bitstream Vera Sans", 
           labelloc=b,
           label="Simple hash table"
           nodesep = .05;
           rankdir = LR;
         ];

         node [fontname = "Bitstream Vera Sans", fontsize=14,
               style=filled, fillcolor=lightblue,
               width = .1,  height = .1
               shape=record];
         edge [arrowhead=vee, arrowsize=0.5];

         bucket[label = "<f0>0 | <f1>1 | <f2>2 | <f3>3 | <f4>4 | <f5>5 | <f6>6 \
                         | <f7>7 | <f8>8 | <f9>9 ",  height = 2.5];

         a [label="{ <data> 8 | <ref>  }"];
         b [label="{ <data> 3 | <ref>  }"];
         c [label="{ <data> 21 | <ref>  }"];
         d [label="{ <data> 55 | <ref>  }"];
         e [label="{ <data> 5 | <ref>  }"];
         f [label="{ <data> 34 | <ref>  }"];
         g [label="{ <data> 89 | <ref>  }"];
         h [label="{ <data> 13 | <ref>  }"];

         bucket:f1 -> a:data:w;
         bucket:f2 -> b:data;
         bucket:f4 -> c:data;
         bucket:f5 -> d:data;
         bucket:f8 -> e:data:w;
         e:ref:c -> f:data [arrowtail=dot, dir=both, tailclip=false];
         f:ref:c -> g:data [arrowtail=dot, dir=both, tailclip=false];
         b:ref:c -> h:data [arrowtail=dot, dir=both, tailclip=false];


      How does the software find the value ``34`` in this data structure?

      First we need to find the right bucket.
      The ``hash`` override is used to compute the bucket.
      In this case the bucket is at index position ``8``.

      Note we use ``std::hash<>`` here.
      Any ``Key`` type stored in this set must override ``std::hash``.

      .. code-block:: cpp
         
         private:
            Container& find_bucket (const Key& value)
            {
              return buckets[std::hash<Key>()(value) % N];
            }

      Next, we search through the list stored in that bucket
      looking for a specific value.
      Each element in the list stored in the bucket is evaluated using
      ``operator==`` - the default for ``std::equal_to``.
      As soon as ``operator==`` evaluates to ``true`` the value is returned.

      .. code-block:: cpp

         iterator find (const Key& value)
         {
           Container& b = find_bucket(value);
           return find_if(b.begin(), b.end(),
                    [this, &value](Key x) { 
                      return compare(x, value);
                    });
         }

      It should be clear that the performance of this data structure is 
      highly dependent upon the quality of the :term:`hash function`.
      Always returning ``42`` is a *legitimate* value for a hash,
      but an extremely poor one,
      because your :term:`hash table` is no better than a :term:`linked list`.


   .. tab:: insert

      Insert is similar to find.
      We use ``find_bucket`` to get the correct array element,
      if it exists.
      The we search to see if the value already exists in the linked list.
      If it does, replace the existing value with the new one.
      Otherwise, we add it to the list.

      .. code-block:: cpp

         void insert (const Key& value)
         {
           Container& b = find_bucket(value);
           iterator pos =
             find_if(b.begin(), b.end(),
                 [this, &value](Key x) { return compare(x, value); });
           if (pos == b.end()) {
             b.push_back(value);
             ++sz;
           }
           else {
             *pos = value;
           }
         }

   .. tab:: erase

      Erase is similar to insert.

      1. Find the bucket
      2. Search for the value
      3. If you find it, erase it.

         Otherwise, do nothing.

      .. code-block:: cpp

         void erase (const Key& value)
         {
         Container& b = find_bucket(value);
         iterator pos =
           find_if(b.begin(), b.end(),
               [this, &value](Key x) { return compare(x, value); });
         if (pos != b.end()) {
           b.erase(pos);
           --sz;
           }
         }

   .. tab:: Run it

      .. activecode:: hash_table_open_ac
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <array>
         #include <algorithm>
         #include <cstddef>
         #include <functional>
         #include <iomanip>
         #include <iostream>
         #include <list>
         #include <utility>

         using std::list;
         using std::array;


         template <class Key,
                  size_t N,
                  class Comparator=std::equal_to<Key>>
         class hash_set
         {
           public:
             using Container = list<Key>;
             using value_type = Key;
             using key_type   = Key;
             using iterator   = typename Container::iterator;
             using const_iterator  = const iterator;

             hash_set() = default;

             iterator find (const Key& value)
             {
               Container& b = find_bucket(value);
               return find_if(b.begin(), b.end(),
                     [this, &value](Key x) { return compare(x, value); });
             }

             const_iterator find (const Key& value) const
             {
               const Container& b = find_bucket(value);
               return find_if(b.begin(), b.end(),
                     [this, &value](Key x) { return compare(x, value); });
             }

             int count (const Key& value) const
             {
               const Container& b = find_bucket(value);
               return (find_if(b.begin(), b.end(),
                     [this, &value](Key x) { return compare(x, value); })
                 == b.end()) ? 0 : 1;
             }

             void insert (const Key& value)
             {
               Container& b = find_bucket(value);
               iterator pos =
                 find_if(b.begin(), b.end(),
                     [this, &value](Key x) { return compare(x, value); });
               if (pos == b.end()) {
                 b.push_back(value);
                 ++sz;
               }
               else {
                 * pos = value;
               }
             }

             void erase (const Key& value)
             {
               Container& b = find_bucket(value);
               iterator pos =
                 find_if(b.begin(), b.end(),
                     [this, &value](Key x) { return compare(x, value); });
               if (pos != b.end()) {
                 b.erase(pos);
                 --sz;
               }
             }

             constexpr
               size_t size() const noexcept { return sz; }

             constexpr
               bool empty() const noexcept { return sz == 0; }

           private:
             array<Container, N> buckets;
             Comparator compare;
             size_t sz = 0;

             Container& find_bucket (const Key& value)
             {
               return buckets[std::hash<Key>()(value) % N];
             }

             constexpr
               const Container& find_bucket (const Key& value) const
               {
                 return buckets[std::hash<Key>()(value) % N];
               }

             friend
             std::ostream& operator<<(std::ostream& os, const hash_set& rhs)
             {
               os << '[';
               int i = 0;
               for (const auto& bucket: rhs.buckets) {
                 for (const auto& value: bucket) {
                   os << i << ':' << value << ',';
                 }
                 ++i;
               }
               return os << ']';
             }
         };

         int main() {
           auto foo = hash_set<int, 11>{};
           foo.insert(72);
           foo.insert(72);
           std::cout << "count: " << foo.count(72) << std::endl;

           foo.erase(72);
           std::cout << "count: " << foo.count(72) << std::endl;

           foo.insert(-1);
           foo.insert(0);
           foo.insert(1);
           foo.insert(2);
           foo.insert(9);
           foo.insert(81);
           foo.insert(121);
           foo.insert(572);
           foo.insert(999);
           std::cout << foo << std::endl;
           auto it = foo.find(572);
           std::cout << "value 572: " << *it << std::endl;
         }

.. foo*

-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     `Resolving Collisions <https://www.cs.odu.edu/~zeil/cs361/f16/Public/collisions/index.html>`__,
     by Steven J. Zeil for his data structures course CS361. 

