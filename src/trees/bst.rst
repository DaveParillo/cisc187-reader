..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: binary search trees

Binary Search Trees
=================== 
A binary tree T is a binary search tree if, for each node ``n``
with sub-trees ``left`` and ``right``,

- The value in ``n`` is **greater than** the values in every node in ``left``.
- The value in ``n`` is **less than** the values in every node in ``right``.
- Both ``left`` and ``right`` are binary search trees.

This page uses unique keys, like ``std::set``. If a value equivalent to an
existing value is inserted, the insertion has no effect. Two values are
equivalent when neither compares less than the other.
The comparisons are assumed to define a :req:`strict weak ordering <Compare>`,
as they do for the keys in an ordered standard-library container. A production
tree would usually make that ordering an explicit comparator type.

These assertions define the **binary search tree property**.

.. include:: bst.dot

.. tb-reveal::
   :name: reveal-bst-1
   :showlabel: Is this a BST?

   Yes.

   Each node is greater than all of its left descendants,
   and is less than all of its right descendants.
   Equivalent values are not inserted.

The Binary Search Tree ADT
--------------------------
Structurally, a BST contains pointers to its left and right children.
As discussed in :doc:`../recursion/index`,
a binary tree can be implemented simply as a recursive data structure.
A binary search tree can also be implemented recursively.

It is a bit simpler to define the tree nodes as a separate type.
Whether you design this class as a completely independent
class, like this one,
or implement it as a nested (inner) class, is largely a matter of
choice.

Since a ``tree_node`` is a data structure that can exist independently
of a tree that enforces the binary search tree property,
it makes sense in this case to define it as a completely separate
struct with no invariants.

The ``tree_node`` encapsulates the general characteristics
common to all binary trees:

- A variable to store the node value
- Links to the left and right child nodes,
  which might themselves be sub-trees.

.. tb-group::

   .. tb-tab:: BST node

      The node stores a value and owns its children. A null ``unique_ptr``
      means that the corresponding child is absent. The node itself does not
      enforce the binary search tree property; the tree operations do that.

      .. code-block:: cpp
         :name: bst-tree-node

         #include <memory>

         template<class T>
         struct tree_node {
           T value;
           std::unique_ptr<tree_node> left;
           std::unique_ptr<tree_node> right;

           explicit tree_node(const T& value) : value{value} {}
         };

   .. tb-tab:: Print

      An in-order traversal function allows us to print values
      in ascending order for a binary search tree.

      .. code-block:: cpp
         :name: bst-print-in-order

         #include <iostream>

         template<class T>
         void print_in_order(const tree_node<T>* node) {
           if (node == nullptr) {
             return;
           }
           print_in_order(node->left.get());
           std::cout << node->value << ' ';
           print_in_order(node->right.get());
         }

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: bst_node_traversal
         :include:
            NODE: bst-tree-node
            PRINT: bst-print-in-order

         {{NODE}}

         {{PRINT}}

         int main() {
           auto root = std::make_unique<tree_node<int>>(4);
           root->left = std::make_unique<tree_node<int>>(2);
           root->right = std::make_unique<tree_node<int>>(6);
           root->left->left = std::make_unique<tree_node<int>>(1);
           root->left->right = std::make_unique<tree_node<int>>(3);
           root->right->left = std::make_unique<tree_node<int>>(5);
           root->right->right = std::make_unique<tree_node<int>>(7);

           print_in_order(root.get());
           std::cout << '\n';
         }

In other words, a ``tree_node`` is a general purpose
binary tree data structure and has no knowledge of
any binary search tree properties or behavior.

Much like our earlier tree objects, all of the functions used to manipulate
a ``tree_node`` will be free functions.
To avoid collision with other similarly named functions,
all the functions will be defined in the ``mesa::tree`` namespace.

The binary search tree is built up from individual ``tree_node`` objects.
An owning ``bstree`` should store its root in a ``std::unique_ptr`` so that
destroying the root recursively destroys its children. This makes ownership
explicit and prevents the leaks that are easy to introduce with raw owning
pointers.

The default copy operations of a class containing ``std::unique_ptr`` are
deleted. A class with ``std::set``-like copyable behavior would need to write
a deep-copy operation; that ownership detail is separate from the search-tree
algorithms. The complete examples below use move-only ownership and return
non-owning node pointers as temporary position handles. The next page replaces
those handles with proper tree iterators.

Our primary focus for the rest of this section is on the functions
that define the key operations associated with a BST:

- contains and find
- insert and erase

Searching binary trees
----------------------
Efficient search of a binary tree uses the same algorithm
you would use when playing the 'number guessing' game.
If asked to guess a random number between ``1`` and ``100`` in the
fewest possible tries, with a hint ``higher`` or ``lower``
after each attempt, few people would start at ``1``,
then guess ``2``, ``3``, and so on until they guessed correctly.
Most people would start with ``50`` and continue to split the
remaining unknown partition in half until they found the correct number.

The strategy most people apply to this problem intuitively is known
as the :term:`binary search` algorithm.
This algorithm is easily applied to binary search trees.

The running time of a search is :math:`O(h)`, where ``h`` is the height of
the tree. A balanced BST has height :math:`O(\log N)`, while a tree built from
already sorted input can have height :math:`O(N)` -- in other words, a list.

.. tb-group::
   :name: contains_tab

   .. tb-tab:: contains

      We always search a binary search tree by comparing the value we're
      searching for to the 'current' node value. 
      If the target value is smaller,
      then we search the left subtree. 
      If the target value is larger, then we search the right subtree.

      If it is neither of these things, then we found the value.

      .. tb-code:: cpp
         :name: bst_contains_ac
         :run-before: bst-tree-node

         #include <iostream>

         template<class T>
         bool contains(const tree_node<T>* node, const T& query_value) {
           if (node == nullptr) {
             return false;
           }
           if (query_value < node->value) {
             return contains(node->left.get(), query_value);
           }
           if (node->value < query_value) {
             return contains(node->right.get(), query_value);
           }
           return true;
         }

         int main() {
           auto root = std::make_unique<tree_node<int>>(4);
           root->left = std::make_unique<tree_node<int>>(2);
           root->right = std::make_unique<tree_node<int>>(6);
           root->left->left = std::make_unique<tree_node<int>>(1);
           root->left->right = std::make_unique<tree_node<int>>(3);

           std::cout << std::boolalpha
                     << contains(root.get(), 3) << ' '
                     << contains(root.get(), 5) << '\n';
         }

Inserting into binary trees
---------------------------
Inserting into a binary tree means adding a new node in the tree
such that the binary search tree property remains intact.

Insertion also takes :math:`O(h)` time, where ``h`` is the tree height. A
balanced BST therefore supports insertion in :math:`O(\log N)` time, while an
unbalanced tree can require :math:`O(N)` time.


.. tb-group::
   :name: insert_tab

   .. tb-tab:: insert

      The insert process begins with a search for a place to insert a new value.
      But how do we find the place at which to insert that new node? 
      Ask "where would we go if we were searching for this data in the tree?"
      This process is identical to the search used for the contains function.

      The standard ``std::set::insert`` contract returns a pair containing
      a position and a Boolean. The Boolean is true only when insertion took
      place; inserting an equivalent value has no effect. This example uses
      a non-owning node pointer as the position until the next page introduces
      a real tree iterator.

      .. code-block:: cpp
         :name: bst-insert

         template<class T>
         std::pair<tree_node<T>*, bool>
         insert(std::unique_ptr<tree_node<T>>& node, const T& value) {
           if (node == nullptr) {
             node = std::make_unique<tree_node<T>>(value);
             return {node.get(), true};
           }
           if (value < node->value) {
             return insert(node->left, value);
           }
           if (node->value < value) {
             return insert(node->right, value);
           }
           return {node.get(), false};
         }

      There are a few important things to notice about this function.

      The insert function receives the current owning pointer by reference.
      It can replace that pointer when traversal reaches an empty child link.
      A new node is inserted at that null link, below a leaf or in place of an
      empty child of an internal node.

      When the value is equivalent to an existing value, the function returns
      the existing node and ``false``.
      It does not overwrite the value, which is an implementation choice.
      Another container implementation might have chosen to overwrite, but in
      this case, we are matching the standard library behavior.

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :run-before: bst-tree-node, bst-print-in-order

         template<class T>
         std::pair<tree_node<T>*, bool>
         insert(std::unique_ptr<tree_node<T>>& node, const T& value) {
           if (node == nullptr) {
             node = std::make_unique<tree_node<T>>(value);
             return {node.get(), true};
           }
           if (value < node->value) {
             return insert(node->left, value);
           }
           if (node->value < value) {
             return insert(node->right, value);
           }
           return {node.get(), false};
         }

         int main() {
           std::unique_ptr<tree_node<int>> root;
           insert(root, 4);
           insert(root, 2);
           insert(root, 6);
           auto result = insert(root, 4);

           std::cout << std::boolalpha
                     << "inserted duplicate: " << result.second << '\n';
           print_in_order(root.get());
           std::cout << '\n';
         }

.. admonition:: Try This!

   Walk through this algorithm yourself with different sets of values.

   Experiment with inserting nodes into binary search trees. 
   Take particular note of what happens if you insert data in
   ascending or descending order, as opposed to inserting unordered data.


Erasing binary tree nodes
-------------------------
The erase process also begins with a search for the place to erase.
This process is identical to the search used for contains and insert.

The tricky part of removing a value from a binary search tree
is what to do when we actually find the value we want to delete.
We can't just delete the tree node. 
Consider the following tree.

.. include:: bst.dot

If we remove values ``10``, ``40``, or ``60`` 
by simply deleting the tree node, that might work.
However, deleting any other node would break the links between tree nodes.

We have three cases to consider:

- Removing a leaf
- Removing a node that has only one child

  - only a left child
  - only a right child

- Removing a node that has two children


Removing a leaf node
....................

It's easy to see that we can always remove any leaf in a
binary search tree without affecting anything else.
That is, if we remove any leaf from a binary search tree,
we still have a valid binary search tree.
There is nothing else to do.

When ``node`` points to a leaf that contains the data we want to remove
we replace the owning pointer in ``node`` with an empty pointer.
With ``std::unique_ptr``, assigning ``nullptr`` automatically destroys the
removed node.

In other words, leaf nodes are replaced with the null pointer.

Removing a non-leaf node with a null child
..........................................
Removing nodes from the interior of the tree is a bit more work
as we need to maintain links between nodes.

Given the same tree we have been working with so far:

.. include:: bst.dot

**Question**
Suppose we wanted to remove the ``20`` or the ``70`` from this tree.
What would we have to do so that the
remaining nodes would still be a valid BST?

.. tb-reveal::
   :name: reveal-bst-2

   There is one pointer to the node being deleted, 
   and one pointer from that node to its only child.

   So this is actually a bit like deleting a node from 
   the middle of a linked list. 

   All we need to do is to update the pointer from the 
   parent ``30`` node.
   That pointer should point to the child of the node we are going to remove.

   .. digraph:: a_bst
      :align: center
      :alt: a binary search tree

      graph [
             nodesep=0.25, ranksep=0.3;
          ];
      node [fontname = "Bitstream Vera Sans", fontsize=14,
            style=filled, fillcolor=lightblue,
            shape=circle, fixedsize=true, width=0.3];
      edge [weight=1, arrowsize=0.5, dir=none];

      a, b, am, c, d, bm, f, l, cm, dm, fm, m;
      am, bm, cm, dm, fm [style=invis, label=""];

      a [label=30]
      b [label=20, fillcolor=wheat]
      d [label=10]

      c [label=70, fillcolor=wheat]
      f [label=50]
      l [label=40]
      m [label=60]

      a -> d [style=dotted];
      a->b 
      a->c;
      b->d [weight=2]; // nudge b: trees b & c are not balanced
      c->f
      f->l,m;

      a -> f [style=dotted];

         edge [style=invis, weight=100];
         d->dm; 
         b->bm;
         f->fm;
         c->cm;
         a->am;

Verify that if we remove either ``20`` or ``70``,
the resulting tree is still a valid binary search tree.

+------------------------+------------------------+
| .. include:: bst20.dot | .. include:: bst70.dot |
+------------------------+------------------------+

The code we used to remove a leaf also works when there is only one child.

If we reach this code, we know there is at most
one non-null child.
In the previous case of a leaf node,
both children are null,
but the same ownership replacement works for one child also.

If the left child is not null, 
then reassign the left child to the current node,
otherwise assign the right child.

Removing a non-leaf node with two children
............................................
Suppose we wanted to remove the ``50`` or the ``30`` from this tree.
What must we do so that the remaining nodes would still be a valid BST?

This is a hard case.
If we remove either the ``50`` or ``30`` nodes,
then we break the tree into pieces,
with no obvious place to put the now-detached subtrees.

.. include:: bst.dot

There is an efficient solution to this problem.
Instead of deleting the node when we find it, 
is there some other data value that we could put into that node that would 
preserve the BST property?

There are, in fact,
two values that we could safely put in there:

- the smallest value from the right subtree
- the largest value from the left subtree

We can find the **largest** value on the **left** by

- taking one step to the left
- then running as far down to the right as we can go

We can find the **smallest** value on the **right** by

- taking one step to the right
- then running as far down to the left as we can go

+-----------------------------+------------------------------+
| .. include:: bst30x20.dot   | .. include:: bst30x40.dot    |
+-----------------------------+------------------------------+

At this point, we haven't deleted or created any nodes.
We simply copy a value from one node to another.
Now we have two nodes in our tree with the same value,
either ``20`` or ``40``,
depending on which approach we used.

We still need to delete the smallest right node
or the largest left node.
What makes this last step simple is that it falls under our
previous case: it is by definition either a leaf,
or has at most one child.

+-----------------------------+------------------------------+
| .. include:: bst30-20.dot   | .. include:: bst30-40.dot    |
+-----------------------------+------------------------------+


.. tb-group::
   :name: erase_tab

   .. tb-tab:: erase

      Putting it all together.

      Recall that ``std::unique_ptr`` is not copyable or copy constructible.
      Moving a ``unique_ptr`` is allowed.

      .. tb-code:: cpp
         :name: bst_erase
         :run-before: bst-tree-node, bst-print-in-order, bst-insert

         template<class T>
         void erase(std::unique_ptr<tree_node<T>>& node, const T& value) {
           if (node == nullptr) {
             return;
           }
           if (value < node->value) {
             erase(node->left, value);
             return;
           }
           if (node->value < value) {
             erase(node->right, value);
             return;
           }

           if (node->left == nullptr) {
             node = std::move(node->right);
             return;
           }
           if (node->right == nullptr) {
             node = std::move(node->left);
             return;
           }

           const tree_node<T>* successor = node->right.get();
           while (successor->left != nullptr) {
             successor = successor->left.get();
           }
           node->value = successor->value;
           erase(node->right, successor->value);
         }

         int main() {
           std::unique_ptr<tree_node<int>> root;
           for (int value : {50, 30, 70, 20, 40, 60, 80}) {
             insert(root, value);
           }

           erase(root, 20);  // leaf
           erase(root, 60);  // leaf
           erase(root, 70);  // one child: 80 remains
           erase(root, 50);  // two children
           print_in_order(root.get());
           std::cout << '\n';
         }

      Lines 6-13 handle the search we discussed initially.
      Here we recursively search for our target value to remove.

      The last ``if`` block handles the case with 2 children.
      We find the smallest node in the right subtree
      and assign its value to the current node.
      Then we erase this value from the right subtree
      of the current node.

      The final block handles the leaf and the one child cases.
      This is the only case where a node is actually removed from the tree.
      This block will also ultimately get called when the
      case handling two child nodes needs to delete the 
      smallest value from the right subtree.

-----

.. admonition:: More to Explore

   - The content on this page was adapted from
     `Binary Search Trees <https://www.cs.odu.edu/~zeil/cs361/latest/Public/bst/index.html>`__,
     by Steven J. Zeil for his data structures course CS361.
   - MyCodeSchool video: 
     `Data structures: binary search trees <https://www.youtube.com/watch?v=pYT9F8_LFTM&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=27>`__ 
   - Wikipedia

     - :wiki:`binary search tree <Binary_search_tree>`

   - `Binary tree visualizer <http://btv.melezinek.cz>`__
