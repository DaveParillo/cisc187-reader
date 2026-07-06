..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: binary search tree; iterators

Binary Search Tree iterators
============================
The recursive traversal algorithms work well for implementing 
tree-based ADT member functions, 
but if we are trying to hide the trees inside some ADT 
for example, using binary search trees to implement std::set
or using STL algorithms or range-for loops, 
then we need to provide iterators for walking though the contents of the tree.

Iterators for tree-based data structures can be more complicated than those 
for linear structures.

For arrays (and vectors and deques and other array-like structures)
and linked lists, a single pointer can implement an iterator.

Given the current position, it is easy to move forward to the next element.

For anything but a singly-linked list, we can also easily move backwards.

.. include:: bst.dot

But look at this binary search tree,
and suppose that you were implementing tree iterators as a single pointer.
Let's see if we can "think" our way through the process of traversing this tree
one step at a time,
without needing to keep a whole stack of unfinished recursive calls around.

We're going to try to visit the nodes in the same order we would process them
during an "in-order" traversal.
For a BST, in-order traversal means that we will visit the data in ascending order.

It's not immediately obvious what our data structure for storing the
"current position" (i.e., an iterator) will be.
We might suspect that a pointer to a tree node will be part of 
that data structure, because that worked with iterators over linked lists.

.. index:: 
   pair: binary search tree; begin()
   pair: binary search tree; end()

BST iterator ``begin()`` and ``end()``
--------------------------------------
As in any data structure, ``begin`` and ``end`` refer to the 
first element in the data structure and one past the last element.
In the last section, we said that 
a BST is sorted when a level order traversal is used.

So what algorithm should we use to find the beginning?

.. tb-reveal::
   :name: reveal_bst_it_1

   Start from the root and working our way down, 
   always taking left children, until we come to a node with no left child.

   The left-most child of a BST is always the minimum element.

So what algorithm should we use to find the end?

.. tb-reveal::
   :name: reveal_bst_it_2

   Just return the ``nullptr``.

   It's tempting to guess that you could do much the same as for ``begin()``,
   this time seeking out the right-most node.
   But that would leave you pointing to the **last** node in the tree,
   and ``end()``, must always refer to the position after the last element
   in the container.



.. index:: 
   pair: binary search tree; operator++()

BST iterator ``operator++()``
-----------------------------
A quick review of the definition of iterators and the iterator design pattern.
We have a few facts to deal with:

- A tree is a *hierarchical* data structure
- An *iterator* allows users to visit each element in a container
  *sequentially* - with no awareness of the underlying structure.
- In C++, iterators are implemented using pointer semantics.
  The function ``operator++()`` is used to move to the next element.

Given our familiar tree:

.. digraph:: a_bst
   :align: center
   :alt: a binary search tree

   graph [
          nodesep=0.25, ranksep=0.3, splines=line;
       ];
   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=circle, fixedsize=true, width=0.3];
   edge [weight=1, arrowsize=0.5, dir=none];

   a, b, am, c, d, bm, f, l, cm, dm, fm, m;
   am, bm, cm, dm, fm [style=invis, label=""];

   a [label=30]
   b [label=20]
   d [label=10]

   c [label=70]
   f [label=50]
   l [label=40, fillcolor=wheat]
   m [label=60]

   a->b 
   a->c;
   b->d [weight=2]; // nudge b: trees b & c are not balanced
   c->f
   f->l,m;

   edge [style=invis, weight=100];
   d->dm; 
   b->bm;
   f->fm;
   c->cm;
   a->am;

If we are iterating through our tree and are currently at the node
with value ``40``, then how do we get to the next node?

.. tb-reveal::
   :name: reveal_bst_it_3

   Well, we know that we should wind up at ``50``.
   But how can we get there?

   We can't, not with just a pointer to the node and 
   all the nodes pointing only to their children. 

   The only place you can go within this tree is down, 
   and there is no "down" from our current position.

In a binary tree, to get to the next node,
we need to know not only where we are,
but also how we got here.

One way is to do that is to implement the iterator as a 
stack of pointers containing the path to the current node.
The stack would be used to simulate the activation stack during
a recursive traversal.

But this solution is clumsy and inefficient.
Iterators tend to get assigned (copied) a lot,
and we'd really like that to be a constant time - an O(1) operation.
Having to copy an entire stack of pointers just isn't very attractive.


BST iterator using parent pointers
..................................
We can make the task of creating tree iterators much easier if we 
redesign the tree nodes to add pointers from each node to its parent.

.. code-block:: cpp

    // a binary tree node
    template<class T>
      struct tree_node {
        T value;
        tree_node<T>* left;
        tree_node<T>* right;
        tree_node<T>* parent; // link to parent simplifies iterators
        tree_node(const T& value = T{}, 
            tree_node<T>* left = nullptr,
            tree_node<T>* right = nullptr,
            tree_node<T>* parent = nullptr)
          : value{value}
        , left{left}
        , right{right}
        , parent{parent}
        { }
      };



These nodes are then used to implement a tree class, which, as usual,
keeps track of the root of our tree in a data member.

The outline for a tree iterator is similar to what we have covered before:

.. code-block:: cpp

     template <typename T>
       struct tree_iterator {
         typedef T value_type;
         typedef T* pointer;
         typedef T& reference;
         typedef std::ptrdiff_t difference_type;
         typedef std::bidirectional_iterator_tag iterator_category;

         const tree::tree_node<T>* node;
         tree_iterator() = default;
         tree_iterator(const tree::tree_node<T>* n);

         constexpr
            const T& operator*() const noexcept;
         tree_iterator& operator++(); 
         tree_iterator operator++(int);
         tree_iterator& operator--(); 
         tree_iterator operator--(int);
      };

There is a subtlety when using our tree iterator in a BST.

.. code-block:: cpp
   :emphasize-lines: 5,6

   template<class T>
    class bstree {
      public:
        typedef T value_type;
        typedef const tree_iterator<T> const_iterator;
        typedef const_iterator iterator;
        typedef const_iterator reverse_iterator;
        typedef const_iterator const_reverse_iterator;

        // remainder omitted . . .
    };

Note the type of all the iterators is ``const``.
We only want ``const`` behavior for this ADT.
If we provided a "true" non-const iterator,
it would allow reassigning data in the tree:

.. code-block:: cpp

   bstree<int>::iterator it = myTree.find(50);
   *it = 10000;

which would very likely break the internal ordering of data,
violating the binary search tree property,
and making it useless for any future searches.
A ``const`` iterator allows us to look at data in the container,
but not change that data.


Implementing BST iterators
--------------------------
As discussed earlier, ``begin()`` is implemented by finding
the minimum element in the tree.

A free function that works with the ``tree_node`` struct is enough:

.. code-block:: cpp

   template <class T>
     tree_node<T>* min_element(tree_node<T>* root )
     {
       if(root == nullptr || root->left == nullptr) {
         return root;
       }
       return min_element(root->left);
     }


``bstree::begin()`` can use this function directly:

.. code-block:: cpp

   constexpr
     const_iterator begin() const noexcept {
       return const_iterator(min_element(root));
     }


And ``end()`` uses the null pointer.

.. code-block:: cpp

   constexpr
     const_iterator end() const noexcept {
       return const_iterator(nullptr);
     }



Implementing ``operator++()``
.............................
Before implementing ``operator++``, let's think about what is should do.
Given the following tree:

.. include:: tree.dot

(Not a binary search tree, just a tree).

**Question:**
Suppose that we are currently at node E.
What is the in-order successor of E?
That is, the node that comes next during an in-order traversal of E?

.. tb-reveal::
   :name: reveal_bst_it_4

   G is the in-order successor of E. 

   If you answered F, remember that in an in-order traversal, 
   we visit a node only after visiting all of its left descendents 
   and before visiting any of its right descendents. 
   Since we're at E, we must have already visited F.

That example suggests that a node's in-order successor tends to be among 
its right descendants.

If our previous premise is correct, then what is the in-order successor to A?

.. tb-reveal::
   :name: reveal_bst_it_5

   F is the in-order successor of A.

   If we are at A during an in-order traversal,
   then we have already visited all of A's left descendents.
   So the answer has to be C or one of its descendents.
   It's tempting to pick C because it's only one step away from A.

   But, remember, during an in-order traversal,
   we visit a node only after visiting all of its left descendents and 
   before visiting any of its right descendents.

   We have not yet visited C's left descendants. 
   So have to run down from C to the left as far as we can go.

This suggests that, if a node has any right descendants, we should:

- Take a step down to the right, then
- Run as far down to the left as we can.

You can see how this would take us from A to F.
The same approach would take us from E to G as well.
So both of our prior examples are satisfied.

But that "step to the right, then run left" procedure raises a new question.
What happens if we are at a node with no right descendants?

**Question:**
Suppose that we are currently at node C. What is the in-order successor of C?

.. tb-reveal::
   :name: reveal_bst_it_6

   C does not *have* an in-order successor.
   C is actually the final node in an in-order traversal.
   After C is only ``end()``.


While node C is an interesting special case,
it doesn't make clear what should happen in the more general case
where we have no right child.

**Question:** What is the in-order successor of F?

.. tb-reveal::
   :name: reveal_bst_it_7

   E is the in-order successor of F.

   So, when we have no right child, we may need to move back up in the tree.

**Question:** What is the in-order successor of G?

.. tb-reveal::
   :name: reveal_bst_it_8

   C is the in-order successor of G.

Why did we move up two steps in the tree this time,
when from F we only moved up one step?
The answer lies in whether we moved back up over a left-child edge or a right-child edge.

If we move up over a right-child edge,
we're returning to a node that has already had all of its descendants,
left and right, visited.
So we must have already visited this node as well,
otherwise we would never have made it into its right descendants.

If we move up over a left-child edge,
then we're returning to a node that has already had all of its
left descendants visited but none of its right descendants.
That's the definition of when we want to visit a node during an 
in-order traversal, so it's time to visit this node.

So, if a node has no right child,
we move up in the tree (following the parent pointers)
until we move back over a left edge.
Then we stop.

When applying this procedure to C,
we move up to A (right edge), 
then try to move up again to A's parent. 
But since A is the tree root, 
it's parent pointer will be null,
which is our signal that C has no in-order successor.

To summarize:

- If the current node has a non-null right child,

  - Take a step down to the right
  - Then run down to the left as far as possible

- If the current node has a null right child,

  - Move up the tree until we have moved over a left child link

.. tb-group::
   :name: bst_it_operator

   .. tb-tab:: operator++

      Putting it all together.

      .. code-block:: cpp

         tree_iterator& operator++() { 
           if (node == nullptr) {
             return * this;
           }
           if (node->right != nullptr) {
              // find the smallest node on the right subtree
              node = mesa::tree::min_element(node->right);
           } else {
              // finished with right subtree and there is no right
              // search up for first parent with a non-null right child
              // or nullptr,
              auto parent = node->parent;
              while (parent != nullptr && node == parent->right) {
                node = parent;
                parent = parent->parent;
              }
              node = parent;
           }
           return * this; 
         }


One part of this iterator that needs closer inspection is the ``while`` loop.
This loop continues moving upwards in the tree until it finds:

- A ``node`` where the current node is in the left subtree of its parent, or
- The root of the tree (:code:`parent == nullptr`),
  indicating that there is no in-order successor (end of the traversal).

.. rubric:: Key Conditions

- :code:`parent != nullptr`: Ensures we do not dereference a nullptr when
  accessing :code:`parent->right`.
- :code:`node == parent->right`: Asserts the current node is the right child of
  its parent.
  When true, we need to keep moving upwards, as the in-order successor is not
  in this part of the tree.

The loop climbs up the tree until it finds a node for which the current
traversal has completed its right subtree. This ensures that the in-order
successor is correctly identified.

Consider an alternative approach that simply checks the immediate predecessor:

.. code-block:: cpp

   if (parent != nullptr && node == parent->right) {
       node = parent;
       parent = parent->parent;
   }

The issue with this approach is that it would only handle one level of
traversal upwards. If the current node is deeply nested in a right subtree, it
may skip multiple ancestors that need to be visited to find the in-order
successor. This can cause incorrect results when:

- The node is the rightmost descendant of a deep subtree, requiring multiple
  upward traversals to reach the root or an ancestor in a left subtree.
- Randomly generated trees or trees that have had many insertions and removals
  from the tree may have imbalanced structures with chains of right children,
  requiring multiple iterations of the while loop.


Consider this tree:

.. digraph:: a_bst
   :align: center
   :alt: a binary search tree

   graph [
       nodesep=0.25, ranksep=0.3, splines=line;
    ];
   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=circle, fixedsize=true, width=0.3];
   edge [weight=1, arrowsize=0.5, dir=none];

   a, b, am, c, bm, d, cm;
   am, bm, cm [style=invis, label=""];
   a [label=10]
   b [label=5]
   c [label=15]
   d [label=12]
   e [label=20, fillcolor=wheat]

   a->b 
   a->c
   c->d,e

   edge [style=invis, weight=100];
   b->bm;
   c->cm;
   a->am;

If the iterator is at ``20`` (the rightmost node):

- The while loop will correctly climb from 20 --> 15 --> 10, and stop when
  :code:`parent == nullptr`.
- A single conditional would move only one step (to 15) and fail to reach the
  root, leaving the iterator in an inconsistent state.


Using parent pointers
=====================
Using parent pointers does incur additional overhead.
We must store an additional pointer with every tree node.
It also means the functions used to manage the tree need to change.

Originally, inserting a node looked like this:

.. code-block:: cpp

   tree::tree_node<T>* 
    insert (const T& value, 
            tree::tree_node<T>*& node)
    {
      // add a new leaf
      if(node == nullptr) {
        node = new tree::tree_node<T>(value, nullptr, nullptr);
        return node;
      }
      if(value < node->value) {
        return insert(value, node->left);
      } 
      if(node->value < value) {
        return insert(value, node->right);
      }
      // else the value already exists in the tree
      node->value = value;
      return node;
    }

But now when inserting a new node, we also need to maintain
correct parent relationships.

.. code-block:: cpp
   :emphasize-lines: 5,9,13,15

   tree::tree_node<T>* 
     insert (const T& value, 
             tree::tree_node<T>*& node, 
             tree::tree_node<T>* parent)
     {
       // add a new leaf
       if(node == nullptr) {
         node = new tree::tree_node<T>(value, nullptr, nullptr, parent);
         return node;
       }
       if(value < node->value) {
         return insert(value, node->left, node);
       } 
       if(node->value < value) {
         return insert(value, node->right, node);
       }
       // else the value already exists in the tree
       node->value = value;
       return node;
     }

When we make a new node, we need to pass the parent into
the ``tree_node`` constructor.
Even though it won't have children initially, it will have a parent.

When we make our recursive calls, the parent node passed in
is the current node.


-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     `Binary Search Trees <https://www.cs.odu.edu/~zeil/cs361/latest/Public/treetraversal/index.html>`__,
     by Steven J. Zeil for his data structures course CS361.

   - `Binary tree visualizer <http://btv.melezinek.cz>`__

