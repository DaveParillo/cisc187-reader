..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index::
   single: binary trees
   pair: recursion; binary trees

The Binary Tree ADT
===================
Unlike the linear sequences covered so far,
a :term:`tree` is a *hierarchical* abstract data type.
Conceptually, it can be thought of as a collection of
*nodes* defined by parent-child relationships.

Refer to :doc:`../trees/trees` to review the basic vocabulary and structure of binary trees.

So far, we have discussed trees only at a conceptual level.
In this section we will program one.

In a binary tree, one node is the :term:`root`.
It serves as the 'trunk' of the tree and serves the same
function as the :term:`head` of a :term:`list`
The root node is the *only* node in a tree without a parent.
All other nodes in a :term:`tree` refer to exactly 1 parent.
In a :term:`binary tree`,
the children are commonly referred to as the **left** and **right** children.

A simple binary tree can be implemented as a recursive data structure:

.. code-block::
   :caption: A simple recursive tree
   :name: recursion-tree
   
   template <class T>
    struct tree {
       T value;
       tree<T>* left = nullptr;
       tree<T>* right = nullptr;
   };

This tree stores a single value of type ``T``
and has two pointers to potential children.
It is important to remember when working with a recursive tree such as this
that a child might be a ``nullptr``.

.. index:: tree traversal

Binary tree traversal
---------------------
Traversal of a data structure means visit elements of the structure.
It might mean visiting a subset, but can also involve visiting each element
from the first to last.

For sequential containers, identifying the start and end of the container is simple.
But where are the *first* and *last* elements of a tree?

The short answer is that there is no single answer.
Since a tree is not a sequential data structure,
a tree allows for different sequences (or traversals).
There are several different types of traversals.
The most common tree traversals are:

- Preorder
- Postorder
- Inorder
- Level order

Given the following binary tree,
let's implement functions that traverse the tree using each of the four methods.

In each traversal deck, the ``node`` indicator identifies the current node.
The printed sequence beneath the tree grows whenever a value is visited.
Moving the indicator during recursive descent or return does not always print
a value; the traversal determines when to visit it. Calls for missing children
return without printing. Level order uses a queue to choose the next node.

.. tb-graph::
   :style: compact-tree
   :align: center
   :name: recursion_btree
   :caption: Subject of the next 4 traversals
   :alt: Tree diagram showing the subject of the next 4 traversals

   a['a'] -left-> b['b']
   a -right-> c['c']
   b -right-> d['d']
   c -left-> e['e']
   c -right-> f['f']
   e -left-> g['g']
   f -left-> h['h']
   f -right-> i['i']

.. tb-code:: cpp
   :name: make-tree
   :hidden:

   tree<char>* make_tree() {
     static tree<char> a;
     static tree<char> b;
     static tree<char> c;
     static tree<char> d;
     static tree<char> e;
     static tree<char> f;
     static tree<char> g;
     static tree<char> h;
     static tree<char> i;

     a = {'a'};
     b = {'b'};
     c = {'c'};
     d = {'d'};
     e = {'e'};
     f = {'f'};
     g = {'g'};
     h = {'h'};
     i = {'i'};

     a.left  = &b;
     a.right = &c;
     b.right = &d;
     c.left  = &e;
     c.right = &f;
     e.left  = &g;
     f.left  = &h;
     f.right = &i;

     return &a;
   }


Preorder traversal
..................
A depth first traversal.

Visit all nodes **before** visiting children:

.. tb-group::
   :name: preorder

   .. tb-tab:: Preorder

      In this generic code block,
      the function ``visit`` represents the action to take on the current
      node.

      .. code-block:: cpp

         void preorder(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           visit(node);
           preorder(node->left);
           preorder(node->right);
         }

      .. tb-deck::
         :name: preorder-traversal-process
         :caption: Preorder traversal: print the node, traverse left, then traverse
            right

         .. tb-card::
            :caption: Print the root, a.

            Start at the root, a. Print a before traversing its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a``

         .. tb-card::
            :caption: Descend to b; print b.

            Move from a to its left child, b. Print b before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b``

         .. tb-card::
            :caption: Descend to d; print d.

            Move from b to its right child, d. Print d before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to d.
               :indicators: node=d
               :highlight: tree.node[d]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d``

         .. tb-card::
            :caption: Return from d to b.

            The call for d has returned to b, completing b's right subtree. b was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d``

         .. tb-card::
            :caption: Return from b to a.

            The call for b has returned to a, completing a's left subtree. a was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d``

         .. tb-card::
            :caption: Descend to c; print c.

            Move from a to its right child, c. Print c before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c``

         .. tb-card::
            :caption: Descend to e; print e.

            Move from c to its left child, e. Print e before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e``

         .. tb-card::
            :caption: Descend to g; print g.

            Move from e to its left child, g. Print g before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to g.
               :indicators: node=g
               :highlight: tree.node[g]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g``

         .. tb-card::
            :caption: Return from g to e.

            The call for g has returned to e, completing e's left subtree. e was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g``

         .. tb-card::
            :caption: Return from e to c.

            The call for e has returned to c, completing c's left subtree. c was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g``

         .. tb-card::
            :caption: Descend to f; print f.

            Move from c to its right child, f. Print f before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f``

         .. tb-card::
            :caption: Descend to h; print h.

            Move from f to its left child, h. Print h before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to h.
               :indicators: node=h
               :highlight: tree.node[h]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h``

         .. tb-card::
            :caption: Return from h to f.

            The call for h has returned to f, completing f's left subtree. f was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h``

         .. tb-card::
            :caption: Descend to i; print i.

            Move from f to its right child, i. Print i before traversing its
            children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to i.
               :indicators: node=i
               :highlight: tree.node[i]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h i``

         .. tb-card::
            :caption: Return from i to f.

            The call for i has returned to f, completing f's right subtree. f was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h i``

         .. tb-card::
            :caption: Return from f to c.

            The call for f has returned to c, completing c's right subtree. c was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h i``

         .. tb-card::
            :caption: Return from c to a.

            The call for c has returned to a, completing a's right subtree. a was
            printed before its children; returning to it leaves the printed sequence
            unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h i``

         .. tb-card::
            :caption: Preorder traversal is complete.

            The call for the root has returned. Every node has been printed once.
            The node indicator has no current target.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Preorder traversal. Traversal complete; there is no current node.
               :indicators: node=none

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b d c e g f h i``

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: ac-trees-preorder
         :run-before: recursion-tree, make-tree

         #include <iostream>

         template <class T>
         void print(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           std::cout << node->value << ' ';
           print(node->left);
           print(node->right);
         }

         int main() {
           std::cout << "Preorder: ";
           print(make_tree());

           return 0;
         }





Postorder traversal
...................
A depth first traversal.

Visit all nodes **after** visiting children:

.. tb-group::
   :name: postorder

   .. tb-tab:: Postorder

      .. code-block:: cpp

         void postorder(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           postorder(node->left);
           postorder(node->right);
           visit(node);
         }

      .. tb-deck::
         :name: postorder-traversal-process
         :caption: Postorder traversal: traverse left, traverse right, then print the
            node

         .. tb-card::
            :caption: Start at a.

            Start at the root, a. Traverse the children before printing a. The call
            for a waits for both subtrees to finish.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** (none)

         .. tb-card::
            :caption: Descend to b.

            Move from a to its left child, b. Traverse the children before printing
            b. The call for b waits for both subtrees to finish.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** (none)

         .. tb-card::
            :caption: Descend to d; print d.

            Move from b to its right child, d. d is a leaf. Both child calls return
            immediately, so print d.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to d.
               :indicators: node=d
               :highlight: tree.node[d]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d``

         .. tb-card::
            :caption: Return to b; print b.

            The call for d has returned to b, completing b's right subtree. Both
            subtrees are complete, so print b after its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b``

         .. tb-card::
            :caption: Return from b to a.

            The call for b has returned to a, completing a's left subtree. The right
            subtree still needs to be traversed. Keep a unprinted until that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b``

         .. tb-card::
            :caption: Descend to c.

            Move from a to its right child, c. Traverse the children before printing
            c. The call for c waits for both subtrees to finish.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b``

         .. tb-card::
            :caption: Descend to e.

            Move from c to its left child, e. Traverse the children before printing
            e. The call for e waits for both subtrees to finish.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b``

         .. tb-card::
            :caption: Descend to g; print g.

            Move from e to its left child, g. g is a leaf. Both child calls return
            immediately, so print g.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to g.
               :indicators: node=g
               :highlight: tree.node[g]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g``

         .. tb-card::
            :caption: Return to e; print e.

            The call for g has returned to e, completing e's left subtree. Both
            subtrees are complete, so print e after its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e``

         .. tb-card::
            :caption: Return from e to c.

            The call for e has returned to c, completing c's left subtree. The right
            subtree still needs to be traversed. Keep c unprinted until that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e``

         .. tb-card::
            :caption: Descend to f.

            Move from c to its right child, f. Traverse the children before printing
            f. The call for f waits for both subtrees to finish.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e``

         .. tb-card::
            :caption: Descend to h; print h.

            Move from f to its left child, h. h is a leaf. Both child calls return
            immediately, so print h.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to h.
               :indicators: node=h
               :highlight: tree.node[h]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h``

         .. tb-card::
            :caption: Return from h to f.

            The call for h has returned to f, completing f's left subtree. The right
            subtree still needs to be traversed. Keep f unprinted until that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h``

         .. tb-card::
            :caption: Descend to i; print i.

            Move from f to its right child, i. i is a leaf. Both child calls return
            immediately, so print i.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to i.
               :indicators: node=i
               :highlight: tree.node[i]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h i``

         .. tb-card::
            :caption: Return to f; print f.

            The call for i has returned to f, completing f's right subtree. Both
            subtrees are complete, so print f after its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h i f``

         .. tb-card::
            :caption: Return to c; print c.

            The call for f has returned to c, completing c's right subtree. Both
            subtrees are complete, so print c after its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h i f c``

         .. tb-card::
            :caption: Return to a; print a.

            The call for c has returned to a, completing a's right subtree. Both
            subtrees are complete, so print a after its children.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h i f c a``

         .. tb-card::
            :caption: Postorder traversal is complete.

            The call for the root has returned. Every node has been printed once.
            The node indicator has no current target.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Postorder traversal. Traversal complete; there is no current
                  node.
               :indicators: node=none

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``d b g e h i f c a``

   .. tb-tab:: Run It

      The only difference between the preorder example and this
      is the order of the function calls in the ``print`` function.

      .. tb-code:: cpp
         :name: ac-trees-postorder
         :run-before: recursion-tree, make-tree

         #include <iostream>

         template <class T>
         void print(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           print(node->left);
           print(node->right);
           std::cout << node->value << ' ';
         }

         int main() {
           std::cout << "Postorder: ";
           print(make_tree());

           return 0;
         }




Inorder traversal
.................
A depth first traversal.

Visit the left child (and the left child subtree),
then visit the current node,
then 
visit the right child (and the right child subtree),


.. tb-group::
   :name: inorder

   .. tb-tab:: Inorder

      .. code-block:: cpp

         void inorder(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           inorder(node->left);
           visit(node);
           inorder(node->right);
         }

      .. tb-deck::
         :name: inorder-traversal-process
         :caption: Inorder traversal: traverse left, print the node, then traverse
            right

         .. tb-card::
            :caption: Start at a.

            Start at the root, a. The call for a waits while its left subtree is
            traversed. Its value will be printed after that subtree returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** (none)

         .. tb-card::
            :caption: Descend to b; print b.

            Move from a to its left child, b. b has no left child, so its
            left-subtree call returns immediately. Print b before traversing its
            right subtree.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b``

         .. tb-card::
            :caption: Descend to d; print d.

            Move from b to its right child, d. d has no left child, so its
            left-subtree call returns immediately. Print d before traversing its
            right subtree.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to d.
               :indicators: node=d
               :highlight: tree.node[d]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d``

         .. tb-card::
            :caption: Return from d to b.

            The call for d has returned to b, completing b's right subtree. b was
            printed before its right subtree; returning to it leaves the printed
            sequence unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d``

         .. tb-card::
            :caption: Return to a; print a.

            The call for b has returned to a, completing a's left subtree. Print a
            now, between its left and right subtrees.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a``

         .. tb-card::
            :caption: Descend to c.

            Move from a to its right child, c. The call for c waits while its left
            subtree is traversed. Its value will be printed after that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a``

         .. tb-card::
            :caption: Descend to e.

            Move from c to its left child, e. The call for e waits while its left
            subtree is traversed. Its value will be printed after that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a``

         .. tb-card::
            :caption: Descend to g; print g.

            Move from e to its left child, g. g has no left child, so its
            left-subtree call returns immediately. Print g before traversing its
            right subtree.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to g.
               :indicators: node=g
               :highlight: tree.node[g]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g``

         .. tb-card::
            :caption: Return to e; print e.

            The call for g has returned to e, completing e's left subtree. Print e
            now, between its left and right subtrees.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e``

         .. tb-card::
            :caption: Return to c; print c.

            The call for e has returned to c, completing c's left subtree. Print c
            now, between its left and right subtrees.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c``

         .. tb-card::
            :caption: Descend to f.

            Move from c to its right child, f. The call for f waits while its left
            subtree is traversed. Its value will be printed after that subtree
            returns.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c``

         .. tb-card::
            :caption: Descend to h; print h.

            Move from f to its left child, h. h has no left child, so its
            left-subtree call returns immediately. Print h before traversing its
            right subtree.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to h.
               :indicators: node=h
               :highlight: tree.node[h]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h``

         .. tb-card::
            :caption: Return to f; print f.

            The call for h has returned to f, completing f's left subtree. Print f
            now, between its left and right subtrees.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f``

         .. tb-card::
            :caption: Descend to i; print i.

            Move from f to its right child, i. i has no left child, so its
            left-subtree call returns immediately. Print i before traversing its
            right subtree.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to i.
               :indicators: node=i
               :highlight: tree.node[i]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f i``

         .. tb-card::
            :caption: Return from i to f.

            The call for i has returned to f, completing f's right subtree. f was
            printed before its right subtree; returning to it leaves the printed
            sequence unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f i``

         .. tb-card::
            :caption: Return from f to c.

            The call for f has returned to c, completing c's right subtree. c was
            printed before its right subtree; returning to it leaves the printed
            sequence unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f i``

         .. tb-card::
            :caption: Return from c to a.

            The call for c has returned to a, completing a's right subtree. a was
            printed before its right subtree; returning to it leaves the printed
            sequence unchanged.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f i``

         .. tb-card::
            :caption: Inorder traversal is complete.

            The call for the root has returned. Every node has been printed once.
            The node indicator has no current target.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Inorder traversal. Traversal complete; there is no current node.
               :indicators: node=none

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``b d a g e c h f i``

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: ac-trees-inorder
         :run-before: recursion-tree, make-tree

         #include <iostream>

         template <class T>
         void print(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           print(node->left);
           std::cout << node->value << ' ';
           print(node->right);
         }

         int main() {
           std::cout << "Inorder: ";
           print(make_tree());

           return 0;
         }



Level order traversal
.....................
Differs from the previous traversals: it is a 'breadth first' traversal.
Also, this algorithm is easier to implement iteratively than recursively.

Visit each node on each level of the tree
then visit the children one level deeper.

.. tb-group::
   :name: levelorder

   .. tb-tab:: Level order

      This is an iterative, not a recursive function.

      .. code-block:: cpp

         void levelorder(tree<T>* node) {
           if (node == nullptr) {
             return;
           }
           std::queue<tree<T>*> q;
           q.push(node);
           while (!q.empty()) {
             auto tmp = q.front();
             visit(tmp);
             q.pop();
             if(tmp->left)  q.push(tmp->left);
             if(tmp->right) q.push(tmp->right);
           }
         }


      .. tb-deck::
         :name: levelorder-traversal-process
         :caption: Level order traversal: print each level from left to right

         .. tb-card::
            :caption: Start with the root in the queue.

            Put a in the queue. The node indicator points to the next value to
            process. The queue is shown with its front on the left; no value has
            been printed yet.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** (none)

            **Queue (front first):** ``a``

         .. tb-card::
            :caption: Print a; process its children.

            The node indicator marks a, the front item. Print a, remove it from the
            queue, then process its children. Enqueue b and c at the back, with the
            left child before the right child.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to a.
               :indicators: node=a
               :highlight: tree.node[a]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a``

            **Queue (front first):** ``b c``

         .. tb-card::
            :caption: Print b; process its children.

            The node indicator marks b, the front item. Print b, remove it from the
            queue, then process its children. Enqueue d at the back.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to b.
               :indicators: node=b
               :highlight: tree.node[b]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b``

            **Queue (front first):** ``c d``

         .. tb-card::
            :caption: Print c; process its children.

            The node indicator marks c, the front item. Print c, remove it from the
            queue, then process its children. Enqueue e and f at the back, with the
            left child before the right child.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to c.
               :indicators: node=c
               :highlight: tree.node[c]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c``

            **Queue (front first):** ``d e f``

         .. tb-card::
            :caption: Print d; process its children.

            The node indicator marks d, the front item. Print d, remove it from the
            queue, then process its children. This node has no children to enqueue.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to d.
               :indicators: node=d
               :highlight: tree.node[d]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d``

            **Queue (front first):** ``e f``

         .. tb-card::
            :caption: Print e; process its children.

            The node indicator marks e, the front item. Print e, remove it from the
            queue, then process its children. Enqueue g at the back.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to e.
               :indicators: node=e
               :highlight: tree.node[e]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e``

            **Queue (front first):** ``f g``

         .. tb-card::
            :caption: Print f; process its children.

            The node indicator marks f, the front item. Print f, remove it from the
            queue, then process its children. Enqueue h and i at the back, with the
            left child before the right child.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to f.
               :indicators: node=f
               :highlight: tree.node[f]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e f``

            **Queue (front first):** ``g h i``

         .. tb-card::
            :caption: Print g; process its children.

            The node indicator marks g, the front item. Print g, remove it from the
            queue, then process its children. This node has no children to enqueue.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to g.
               :indicators: node=g
               :highlight: tree.node[g]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e f g``

            **Queue (front first):** ``h i``

         .. tb-card::
            :caption: Print h; process its children.

            The node indicator marks h, the front item. Print h, remove it from the
            queue, then process its children. This node has no children to enqueue.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to h.
               :indicators: node=h
               :highlight: tree.node[h]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e f g h``

            **Queue (front first):** ``i``

         .. tb-card::
            :caption: Print i; process its children.

            The node indicator marks i, the front item. Print i, remove it from the
            queue, then process its children. This node has no children to enqueue.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. The node indicator points to i.
               :indicators: node=i
               :highlight: tree.node[i]

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e f g h i``

            **Queue (front first):** (empty)

         .. tb-card::
            :caption: Level order traversal is complete.

            The queue is empty. Every node has been printed once, one level at a
            time from left to right. The node indicator has no current target.

            .. tb-graph:: tree
               :style: compact-tree
               :align: center
               :alt: Level order traversal. Traversal complete; there is no current
                  node.
               :indicators: node=none

               a['a'] -left-> b['b']
               a -right-> c['c']
               b -right-> d['d']
               c -left-> e['e']
               c -right-> f['f']
               e -left-> g['g']
               f -left-> h['h']
               f -right-> i['i']

            **Printed:** ``a b c d e f g h i``

            **Queue (front first):** (empty)

   .. tb-tab:: Run It

      .. tb-code:: cpp
         :name: ac-trees-levelorder
         :run-before: recursion-tree, make-tree

         #include <iostream>
         #include <queue>

         template <class T>
         void print(tree<T>* node) {
           if (!node) return;

           std::queue<tree<T>*> q;
           q.push(node);
           while (!q.empty()) {
             auto tmp = q.front();
             std::cout << tmp->value << ' ';
             q.pop();
             if(tmp->left)  q.push(tmp->left);
             if(tmp->right) q.push(tmp->right);
           }
         }

         int main() {
           std::cout << "Level order: ";
           print(make_tree());

           return 0;
         }





-----

.. admonition:: More to Explore

   - :cpp:`Containers library <container>`
   - `Visualgo: binary heap <https://visualgo.net/en/heap?slide=1>`_
