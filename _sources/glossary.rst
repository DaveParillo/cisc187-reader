..  Copyright (C)  Dave Parillo, Brad Miller, David Ranum, Jeffrey Elkner, 
    Peter Wentworth, Allen B. Downey, Chris Meyers, and Dario Mitchell.  
    Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

..  Some content from the OpenDSA eTextbook project. See
    http://algoviz.org/OpenDSA for more details.
    Copyright (c) 2012-2013 by the OpenDSA Project Contributors, and
    distributed under an MIT open source license.

.. _glossary:

Glossary
--------

.. glossary::
   :sorted:

   abstraction
      A technique used to reduce the complexity of systems and data.
      An abstraction often involves a simplified model of the
      'real world' for the purposes of achieving goals
      within a specific problem domain. 

      Data abstraction enforces a clear separation between the 
      abstract properties of a :term:`data type` and the concrete details 
      of its implementation. 

   abstract base class
      A class in which some functions are not implemented.
      Abstract bases classes cannot be instantiated --- a derived class
      must override the abstract virtual function with an implementation.

   abstract data type
      Abbreviated :term:`ADT`. The realization of a :term:`data type`
      as a software component.

   activation record
      The entity that is stored on the :term:`runtime stack` during
      program execution.
      It stores any active :term:`local variable` and the return
      address from which a new subroutine is being called, so that
      this information can be recovered when the subroutine
      terminates.

   activecode
      A unique interpreter environment that allows code to be executed within a web browser.

   adjacent
      Two :term:`nodes <node>` of a :term:`tree` or two
      :term:`vertices <vertex>` of a :term:`graph` are said to be
      adjacent if they have an :term:`edge` connecting them.
      If the edge is directed from :math:`a` to :math:`b`,
      then we say that :math:`a` is adjacent to :math:`b`,
      and :math:`b` is adjacent from :math:`a`.

   adjacency list
      An implementation for a :term:`graph` that uses an (array-based)
      :term:`list` to represent the :term:`vertices <vertex>` of the
      graph, and each vertex is in turn represented by a
      (linked) list of the vertices that are
      :term:`neighbors <neighbor>`.

   adjacency matrix
      An implementation for a :term:`graph` that uses a 2-dimensional
      array where each row and each column corresponds to a
      :term:`vertex` in the :term:`graph`. A given row and column in
      the matrix corresponds to an edge from the :term:`vertex`
      corresponding to the row to the vertex corresponding to the
      column.

   ADT
      Abbreviation for :term:`abstract data type`.

   adversary argument
      A type of :term:`lower bounds proof` for a problem where a
      (fictional) "adversary" is assumed to control access to an
      algorithm's input, and which yields information about that input
      in such a way
      that will drive the cost for any proposed algorithm to solve the
      problem as high as possible.
      So long as the adversary never gives an answer that conflicts
      with any previous answer, it is permitted to do whatever
      necessary to make the algorithm require as much cost as
      possible.


   address
      A location in memory.

   aggregate type
      A :term:`data type` whose :term:`members <member>` have subparts.
      For example, a typical database record.
      Another term for this is :term:`composite type`. 

   algorithm
      A general step by step process for solving a :term:`problem`.

   algorithm analysis
      :to-term: growth rate :label: key concept
      :to-term: upper bound :label: key concept
      :to-term: lower bound :label: key concept
      :to-term: asymptotic analysis :label: synonym
      :to-term: asymptotic algorithm analysis :label: formal synonym

      A less formal version of the term
      :term:`asymptotic algorithm analysis`, generally used as a
      synonym for :term:`asymptotic analysis`.

   alphabet trie
      A :term:`trie` data structure for storing variable-length
      strings.
      Level :math:`i` of the tree corresponds to the letter in
      position :math:`i` of the string.
      The root will have potential branches on each intial letter of
      string.
      Thus, all strings starting with "a" will be stored in the "a"
      branch of the tree.
      At the second level, such strings will be separated by branching
      on the second letter.

   ancestor
      In a tree, for a given node :math:`A`, any node on a
      path from :math:`A` up to the root is an ancestor of
      :math:`A`.

   antisymmetric
      In set notation, relation :math:`R` is antisymmetric if whenever
      :math:`aRb` and :math:`bRa`, then :math:`a = b`, for all
      :math:`a, b \in \mathbf{S}`.

   anti-pattern
      A common response to a recurring problem that is generally ineffective.
      Anti-patterns represent examples that you **should not** emulate!
      As bad as they are, they can still be instructive.
      Compare to :term:`design pattern`.

   api
   API
      An Application Programming Interface (API) is a set of functions, 
      or classes used by a program.
      Often an API provides a family of functions or classes that work
      together to provide a complete set of capabilities.

   approximation algorithm
      An algorthm for an :term:`optimization problem` that finds a
      good, but not necessarily cheapest, solution.

   array-based list
      An implementation for the :term:`list` ADT that uses an array to
      store the list elements.

   array-based stack
      Analogous to an :term:`array-based list`, this uses an array to
      store the elements when implementing the :term:`stack` ADT.

   array-based queue
      Analogous to an :term:`array-based list`, this uses an array to
      store the elements when implementing the :term:`queue` ADT.

   ASCII character coding
      American Standard Code for Information Interchange.
      A commonly used method for encoding characters using a binary code.
      Standard ASCII uses an 8-bit code to represent upper and lower
      case letters, digits, some punctuation, and some number of
      non-printing characters (such as carrage return).
      Now largely replaced by UTF-8 encoding.

   assembly code
      :to-term: intermediate code :label: form of

      A form of  :term:`intermediate code` created by a :term:`compiler` that
      is easy to convert into the final form that the computer can
      execute.
      An assembly language is typically a direct mapping of one or a
      few instructions that the CPU can execute into a mnemonic form
      that is relatively easy for a human to read.

   assignable
      A :term:`type` is *assignable* if the type can be copy-assigned
      a new value as the left-hand side of the operation.

      References are not assignable because once initialized,
      they cannot be assigned a new value.

   associative container
      A set of sorted data structures that can be quickly searched.
      ``map`` and ``set`` are examples.

   asymptotic algorithm analysis
      A more formal term for :term:`asymptotic analysis`.

   asymptotic analysis
      :to-term: algorithm analysis :label: synonym
      :to-term: asymptotic algorithm analysis :label: formal synonym

      A method for estimating the efficiency of an algorithm or
      computer program by identifying its :term:`growth rate`.
      Asymptotic analysis also gives a way to
      define the inherent difficulty of a :term:`problem`.
      We frequently use the term :term:`algorithm analysis` to mean
      the same thing.

   attribute
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a synonym for :term:`data member`.

   average case
      In :term:`algorithm analysis`, the average of the costs for all
      :term:`problem instances <problem instance>` of a given input
      size :math:`n`. If not all problem
      instances have equal probability of occurring, then average case
      must be calculated using a weighted average.

   backing storage
   backing store
      The underlying storage for an :term:`ADT`.

   bag
      In set notation, a bag is a collection of elements with no order
      (like a set), but which allows for duplicate-valued elements
      (unlike a set).
      A synonym for :term:`multilist`.

   balanced tree
      A :term:`tree` where the :term:`subtrees <subtree>` meet some
      criteria for being balanced.
      Two possibilities are that the tree is
      :term:`height balanced`, or that the tree has a roughly equal
      number of :term:`nodes <node>` in each subtree.

   base
      Synonym for :term:`radix`.

   base case
      In :term:`recursion`, the base case is the termination condition.
      This is a simple input or value that can be solved
      without resorting to a recursive call.

   base class
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a class from which another class :term:`inherits <inherit>`.
      The class that inherits is called a :term:`subclass` or :term:`derived class`.
  
   base type
      The :term:`data type` for the elements in a set.
      For example, the set might consist of the integer values 3, 5, and 7.
      In this example, the base type is integers.

   best case
      In algorithm analysis, the :term:`problem instance` from among
      all problem instances for a given input size :math:`n` that has
      least cost. Note that the best case is **not** when :math:`n` is
      small, since we are referring to the best from a class of inputs
      (i.e, we want the best of those inputs of size :math:`n`).

   big-O notation
   big-Oh notation
      In algorithm analysis, a shorthand notation for describing the
      upper bound for an algorithm or problem.

   binary search
      A standard :term:`recursive <recursion>` algorithm for finding
      the :term:`record` with a given :term:`key` within
      a sorted list.
      It runs in :math:`O(\log n)` time.
      At each step, look at the middle of the current sublist, and throw
      away the half of the records whose keys are either too small or
      too large.
      
   binary tree
      A non-linear data structure with a set of nodes which is either empty, 
      or else has a root node together two binary trees, called the left and right
      :term:`subtrees <subtree>`, which are disjoint from each
      other and from the :term:`root`.

   binary trie
      A :term:`binary tree` whose structure is that of a :term:`trie`.
      Generally this is an implementation for a :term:`search tree`.
      This means that the :term:`search key` values are thought of a
      binary digits, with the digit in the position corresponding to
      this a node's :term:`level` in the tree indicating a left branch
      if it is "0", or a right branch if it is "1".
      Examples include the :term:`Huffman coding tree` and the
      :term:`bintree`.

   binning
      In :term:`hashing`, binning is a type of :term:`hash function`.
      Say we are given keys in the range 0 to 999, and have a hash
      table of size 10.
      In this case, a possible hash function might simply divide the
      key value by 100.
      Thus, all keys in the range 0 to 99 would hash to slot 0, keys
      100 to 199 would hash to slot 1, and so on.
      In other words, this hash function "bins" the first 100 keys to
      the first slot, the next 100 keys to the second slot, and so
      on.
      This approach tends to make the hash function dependent on the
      distribution of the high-order bits of the keys.

   bintree
      :to-term: flyweight :label: uses

      A :term:`spatial data structure` in the form of binary
      :term:`trie`, typically used to store point data in two or more
      dimensions.
      Similar to a :term:`PR quadtree` except that at each level, it
      splits one dimension in half.
      Since many leaf nodes of the PR quadtree will contain no data
      points, implementation often makes use of the :term:`flyweight`
      :term:`design pattern`.

   block
      Defines a :term:`scope` within a program.
      A synonym for :term:`code block`.

   boolean variable
      A variable that takes on one of the two values ``true`` and
      ``false``.

   bucket
      In :term:`bucket hashing`, a bucket is a sequence of
      :term:`slots <slot>` in the :term:`hash table` that are grouped
      together.

   bucket hashing
      A method of :term:`hashing` where multiple :term:`slots <slot>`
      of the :term:`hash table` are grouped together to form a
      :term:`bucket`.
      The :term:`hash function` then either hashes to some bucket, or
      else it hashes to a :term:`home slot` in the normal way, but
      this home slot is part of some bucket.
      :term:`Collision resolution <collision resolution>` is handled
      first by attempting to find a free position within the same
      bucket as the home slot.
      If the bucket if full, then the record is placed in an
      :term:`overflow bucket`.

   bug
      An error in a program.

   call stack
      Known also as execution stack. A stack that stores the function
      call sequence and the return address for each function.

   cartesian product
      For sets, this is another name for the :term:`set product`.

   ceiling
      Written :math:`\lceil x \rceil`, for real value :math:`x` the
      ceiling is the least integer :math:`\geq x`.

   child
      In a tree, the set of :term:`nodes <node>` directly pointed to
      by a node :math:`R` are the :term:`children <child>` of :math:`R`.

   class
      In the :term:`object-oriented programming paradigm`
      an ADT and its implementation together make up a class.
      An instantiation of a class within a program is termed an
      :term:`object`.

   class hierarchy
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a set of classes and their interrelationships.
      One of the classes is the :term:`base class`, and the others are
      :term:`derived classes <derived class>` that :term:`inherit` either
      directly or indirectly from the base class.

   class invariant
   type invariant
   invariants
      A class invariant is an assertion about conditions which must be true
      in order for a class to remain valid.

   client
      The user of a service.

   closed
      A set is closed over a (binary) operation if,
      whenever the operation is applied to two members of the set, the
      result is a member of the set.

   closed-form solution
      An algebraic equation with the same value as a :term:`summation`
      or :term:`recurrence relation`.
      The process of replacing the summation or
      recurrence with its closed-form solution is known as solving the
      summation or recurrence.

   closed hashing
   closed hash system
      A :term:`hash system` where all records are stored in slots of
      the :term:`hash table`.
      This is in contrast to an :term:`open hash system`.

   code block
      Defines a :term:`scope` within a program.
      A synonym for :term:`block`.

   code generation
      A phase in a :term:`compiler` that transforms
      :term:`intermediate code` into the final executable form of the
      code.
      More generally, this can refer to the process of turning a parse
      tree (that determines the correctness of the structure of the
      program) into actual instructions that the computer can execute.

   codelens
      An interactive environment that allows the user to control the 
      step by step execution of a program

   code optimization
      :to-term: assembly code :label: changes

      A phase in a :term:`compiler` that makes changes in the code
      (typically :term:`assembly code`) with the goal of replacing
      it with a version of the code that will run faster while
      performing the same computation.

   cohesion
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a term that refers to the degree to which a class has a single 
      well-defined role or responsibility.

   collision
      In a :term:`hash system`, this refers to the case where two
      search :term:`keys <key>` are mapped by the
      :term:`hash function` to the same 
      slot in the :term:`hash table`.
      This can happen on insertion or search when another record has
      already been hashed to that slot.
      In this case, a :term:`closed hash system` will require a
      process known as :term:`collision resolution` to find the
      location of the desired record.

   collision resolution
      The outcome of a :term:`collision resolution policy`.

   collision resolution policy
      In :term:`hashing`, the process of resolving a
      :term:`collision`.
      Specifically in a :term:`closed hash system`, this is the
      process of finding the proper position in a :term:`hash table`
      that contains the
      desired record if the :term:`hash function` did not return the
      correct position for that record due to a :term:`collision` with
      another record.

   comment
      Information in a program that is meant for other programmers (or anyone
      reading the source code) and has no effect on the execution of the
      program.

   comparable
      The concept that two objects can be compared to determine if they
      are equal or not, or to determine which one is greater than the
      other. 
      In set notation, elements :math:`x` and :math:`y` of a set are
      comparable under a given relation :math:`R` if either
      :math:`xRy` or :math:`yRx`.
      To be reliably compared for a greater/lesser relationship,
      the values being compared must belong to a :term:`total order`.
      In programming, the property of a data type such that two
      elements of the type can be compared to determine if they the
      same (a weaker version), or which of the two is larger (a
      stronger version).

   comparator
      A function given as a parameter to a method of a library
      (or alternatively, a parameter for a C++ template or a Java
      generic).
      The comparator function concept provides a generic way
      encapulates the process of performing a comparison between two
      objects of a specific type.
      For example, if we want to write a generic sorting routine, that
      can handle any record type, we can require that the user of the
      sorting routine pass in a comparator function
      to define how records in the collection are to be compared.

   comparison
      The act of comparing two :term:`keys <key>` or
      :term:`records <record>`.
      For many :term:`data types <data type>`, a comparison has
      constant time cost.
      For others, such as :term:`linked list` the cost often increases
      as the number of elements increases.

   compile
      To translate a program written in a high-level language into a
      low-level language all at once, in preparation for later execution.

   compiler
      A computer program that reads computer programs and converts
      them into a form that can be directly excecuted by some form of
      computer.
      The major phases in a compiler include :term:`lexical analysis`,
      :term:`syntax analysis`, :term:`intermediate code generation`,
      :term:`code optimization`, and :term:`code generation`.
      More broadly, a compiler can be viewed as :term:`parsing
      <parser>` the program to verify that it is syntactically
      correct, and then doing :term:`code generation` to convert the
      hig-level program into something that the computer can execute.

   compile-time error
      Errors detected by the compiler.
      Compare to :term:`runtime error`, :term:`link error`,
      and :term:`semantic error`.

   compile-time polymorphism
   Compile-time polymorphism
      A form of :term:`polymorphism` known as Overloading.
      Overloaded methods have the same names, but different signatures
      as a method available elsewhere in the class.
      Compare to :term:`runtime polymorphism`.

   complete binary tree
      A binary tree where the nodes are filled in row by row, with the
      bottom row filled in left to right.
      Due to this requirement, there is only one tree of :math:`n`
      nodes for any value of :math:`n`.
      Since storing the records in an array in row order leads to a
      simple mapping from a node's position in the array to its
      :term:`parent`, :term:`siblings <sibling>`, and
      :term:`children <child>`, the array representation is most 
      commonly used to implement the complete binary tree.
      The :term:`heap` data structure is a complete binary tree with
      partial ordering constraints on the node values.

   Composite design pattern
      Given a class hierarchy representing a set of objects, and a
      container for a collection of objects, the composite
      :term:`design pattern` addresses the relationship between the
      object hierarchy and a bunch of behaviors on the objects.
      In the composite design, each object is required to implement
      the collection of behaviors.
      This is in contrast to the procedural approach where a behavior
      (such as a tree :term:`traversal`) is implemented as a
      method on  the object collection (such as a :term:`tree`).
      Procedural tree traversal requires that the tree have a method
      that understands what to do when it encounters any of the object
      types (:term:`internal <internal node>` or
      :term:`leaf nodes <leaf node>`) that the tree might contain.
      The composite approach would have the tree call the "traversal"
      method on its root node, which then knows how to perform the
      "traversal" behavior.
      This might in turn require invoking the traversal method of
      other objects (in this case, the children of the root).

   composite type
      A type whose :term:`members <member>` have subparts.
      For example, a typical database record.
      Another term for this is :term:`aggregate type`.

   composition
      Relationships between classes based on usage rather than 
      :term:`inheritance <inherit>`, i.e. a **HAS-A** relationship.
      For example, some code in class 'A' has a reference to some
      other class 'B'.

   compound type
      A :term:`data type` built up from simpler parts.
      Compare to :term:`simple type` and :term:`composite type`.

   constant running time
   constant time
      The cost of a function whose running time is not related to its
      input size.
      In Theta notation, this is traditionally written as
      :math:`\Theta(1)`.

   container
   container class
      A :term:`data structure` that stores a collection of
      :term:`records <record>`.
      Typical examples are arrays and
      :term:`hash tables <hash table>`.

   cost
      The amount of resources that the solution consumes.

   cost model
      In :term:`algorithm analysis`, a definition for the cost of each
      basic operation performed by the algorithm,
      along with a definition for the size of the input.
      Having these definitions allows us to calculate the :term:`cost`
      to run the algorithm on a given input, and from there determine
      the :term:`growth rate` of the algorithm.
      A cost model would be considered "good" if it yields predictions
      that conform to our understanding of reality.

   CPU
      Acronym for Central Processing Unit, the primary processing
      device for a computer.

   current position
      A property of some list ADTs, where there is maintained a
      "current position" state that can be referred to later.

   data field
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a synonym for :term:`data member`.

   data item
      A piece of information or a record whose value is drawn from a type.

   data member
      The variables that together define the space required by a data
      item are referred to as data members.
      Some of the commonly used synonyms include :term:`data field`,
      :term:`attribute`, and :term:`instance variable`.

   data structure
      The implementation for an :term:`ADT`.

   data type
      A type together with a collection of operations to manipulate
      the type.

   debugging
      The process of finding and removing any of the three kinds of
      programming errors.

   decision tree
      A theoretical construct for modeling the behavior of algorithms.
      Each point at which the algorithm makes a decision (such as an
      if statement) is modeled by a branch in the tree that represents
      the algorithms behavior.
      Decision trees can be used in
      :term:`lower bounds proofs <lower bounds proof>`,
      such as the proof that sorting requires
      :math:`\Omega(n \log n)` comparisons in the :term:`worst case`.

   declaration
     A declaration introduces a new :term:`name` 
     and :term:`type` into a :term:`scope`.

   depth
     The depth of a node :math:`M` in a tree is the length
     of the path from the root of the tree to :math:`M`.

   depth-first search
     :to-term: DFS :label: abbreviation
     :to-term: depth-first search tree :label: generates

     A :term:`graph` :term:`traversal` algorithm.
     Whenever a :math:`v` is :term:`visited <visit>` during the
     traversal, DFS will :term:`recursively <recursion>` visit all of
     :math:`v` 's :term:`unvisited` :term:`neighbors <neighbor>`.

   depth-first search tree
      A :term:`tree` that can be defined by the operation of a
      :term:`depth-first search` (DFS) on a :term:`graph`.
      This tree would consist of the :term:`nodes <node>` of the graph
      and a subset of the :term:`edges <edge>` of the graph that was
      followed during the DFS.

   dequeue
      A specialized term used to indicate removing an element from a queue.

   derived class
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      any class within a :term:`class hierarchy` that
      :term:`inherits <inherit>` from some other class.
      A synonym for :term:`derived class`.

   descendant
      In a tree, the set of all nodes that have a node :math:`A` as an
      :term:`ancestor` are the descendants of :math:`A`.
      In other words, all of the nodes that can be reached from
      :math:`A` by progressing downwards in tree.
      Another way to say it is: The
      :term:`children <child>` of :math:`A`, their children, and so
      on.

   derivation
      In formal languages, the process of executing a series of
      :term:`production rules <production rule>` from a :term:`grammar`.
      A typical example of a derivation would be the series of
      productions executed to go from the :term:`start symbol` to a
      given string.

   deserialization
      The process of returning a :term:`serialized <serialization>`
      representation for a data structure back to its original
      in-memory form.

   design pattern
      An abstraction for describing the design of programs,
      that is, the interactions of objects and classes.
      Experienced software designers learn and reuse patterns
      for combining software components, and design patterns allow
      this design knowledge to be passed on to new programmers more quickly.
      Examples are :term:`Composite design pattern`,
      :term:`flyweight`,
      :term:`iterator`,
      :term:`strategy`, and
      :term:`visitor`.

   dictionary
      An abstract data type or interface for a data structure or
      software subsystem that supports insertion, search, and deletion
      of records.

   discriminator
      A part of a :term:`multi-dimensional search key`.
      Certain tree data structures such as the :term:`bintree` and the
      :term:`kd tree` operate by making branching decisions at nodes
      of the tree based on a single attribute of the multi-dimensional
      key, with the attribute determined by the level of the node in
      the tree.

      For example, in 2 dimensions, nodes at the odd levels in the
      tree might branch based on the :math:`x` value of a coordinate,
      while at the even levels the tree would branch based on the
      :math:`y` value of the coordinate.
      Thus, the :math:`x` coordinate is the discriminator for the odd
      levels, while the :math:`y` coordinate is the discriminator for
      the even levels.

   disjoint
      Two parts of a :term:`data structure` or two
      collections with no objects in common are disjoint.
      This term is often used in conjunction with a data structure
      that has :term:`nodes <node>` (such as a :term:`tree`).
      Also used in the context of :term:`sets <set>`, where two
      :term:`subsets <subset>` are disjoint if they share no elements.

   disjoint sets
      A collection of :term:`sets <set>`, any pair of which share no
      elements in common.
      A collection of disjoint sets partitions some objects
      such that every object is in exactly one of the disjoint sets.

   divide and conquer
      A technique for designing algorithms where a solution is found
      by breaking the problem into smaller (similar) subproblems,
      solving the subproblems, then combining the subproblem solutions
      to form the solution to the original problem.
      This process is often implemented using :term:`recursion`.

   divide-and-conquer recurrences
      A common form of :term:`recurrence relation`
      that have the form

      .. math::

         {\bf T}(n) = a{\bf T}(n/b) + cn^k; \quad {\bf T}(1) = c

      where :math:`a`, :math:`b`, :math:`c`, and :math:`k` are constants.
      In general, this recurrence describes a problem of size :math:`n`
      divided into :math:`a` subproblems of size :math:`n/b`,
      while :math:`cn^k` is the amount of work necessary to combine the
      partial solutions.

   domain
      The set of possible inputs to a function.

   double hashing
      A :term:`collision resolution` method. A second hash
      function is used to generate a value :math:`c` on the key.
      That value is then used by this key as the step size in
      :term:`linear probing by steps`.
      Since different keys use different step sizes (as generated by
      the second hash function), this process avoids the clustering
      caused by standard linear probing by steps.

   doubly linked list
      A :term:`linked list` implementation variant where each list
      node contains access pointers to both the previous element and
      the next element on the list.

   dynamic array
      Arrays, once allocated, are of fixed size. A dynamic array puts
      an interface around the array so as to appear to allow the array
      to grow and shrink in size as necessary. Typically this is done
      by allocating a new copy, copying the contents of the old array,
      and then returning the old array to :term:`free store`.
      In some programming languages, the term
      :term:`vector` is used as a synonym for dynamic array.

   dynamic memory allocation
      A programming technique where linked objects in a data structure
      are created from :term:`free store` as needed. When no longer
      needed, the object is either returned to :term:`free store` or
      left as :term:`garbage`, depending on the programming language.

   edge
      The connection that links two :term:`nodes <node>` in a
      :term:`tree`, :term:`linked list`, or :term:`graph`.

   element
      One value or member in a set.

   empty
      For a :term:`container` class, the state of containing no
      :term:`elements <element>`.

   encapsulation
      In programming, the concept of hiding implementation details
      from the user of an ADT, and protecting
      :term:`data members <data member>` of an
      object from outside access.

   enqueue
      A specialized term used to indicate inserting an element onto a queue.

   enumeration
      The process by which a :term:`traversal` lists every object in
      the :term:`container` exactly once.
      Thus, a traversal that prints the :term:`nodes <node>` is said
      to enumerate the nodes.
      An enumeration can also refer to the actual listing that is
      produced by the traversal 
      (as well as the process that created that listing).

   equivalence class
      An :term:`equivalence relation` can be used to partition a set
      into equivalence classes.

   equivalence relation
      Relation :math:`R` is an equivalence relation on set
      :math:`\mathbf{S}` if it is :term:`reflexive`,
      :term:`symmetric`, and :term:`transitive`.

   exception
      Another name for a runtime error.

   exchange
      A swap of adjacent records in an array.

   executable
      Another name for object code that is ready to be executed.

   exponential growth rate
      A :term:`growth rate` function where :math:`n` (the input size)
      appears in the exponent. For example, :math:`2^n`.

   external fragmentation
      A condition that arises when a series of memory requests
      result in lots of small :term:`free blocks <free block>`, no one
      of which is useful for servicing typical requests.

   external sort
      A sorting algorithm that is applied to data stored outside
      the program, such as a disk file.
      This is in contrast to an :term:`internal sort` that is meant to
      work on data stored in memory.

   FIFO
      Abbreviation for "first-in, first-out".
      This is the access paradigm for a :term:`queue`,
      and an old terminolgy for the queue is "FIFO list".

   fixed-length coding
      Given a collection of objects, a fixed-length coding scheme
      assigns a code to each object in the collection using codes that
      are all of the same length.
      Standard ASCII and Unicode representations for characters are
      both examples of fixed-length coding schemes.
      This is in contrast to :term:`variable-length coding`.

   floor
      Written :math:`\lfloor x \rfloor`, for real value :math:`x` the
      floor is the greatest integer :math:`\leq x`.

   flyweight
      A :term:`design pattern` that is meant to solve the following
      problem:
      You have an application with many objects.
      Some of these objects are identical in the information that
      they contain, and the role that they play.
      But they must be reached from various places, and conceptually they
      really are distinct objects.
      Because there is so much duplication of the same information,
      we want to reduce memory cost by sharing that space. 
      For example, in document layout, 
      the letter "C" might be represented by an object that
      describes that character's strokes and bounding box.
      However, we do not want to create a separate "C" object everywhere
      in the document that a "C" appears.
      The solution is to allocate a single copy of the shared representation
      for "C" objects.
      Then, every place in the document that needs a "C" in a given font,
      size, and typeface will reference this single copy.
      The various instances of references to a specific form of "C" are
      called flyweights.

   folding method
      In :term:`hashing`, an approach to implementing a
      :term:`hash function`.
      Most typically used when the key is a string, the folding method
      breaks the string into pieces (perhaps each letter is a piece,
      or a small series of letters is a piece), converts the letter(s)
      to an integer value (typically by using its underlying encoding
      value), and summing up the pieces.

   free block
      A block of unused space in a memory pool.

   free block list
      In a memory manager, the list that stores the necessary
      information about the current :term:`free blocks <free block>`.
      Generally, this is done with some sort of :term:`linked list`,
      where each node of the linked list indicates the start position
      and length of the free block in the memory pool.

   free store
      Space available to a program during runtime to be used for
      :term:`dynamic memory allocation` of objects.
      The free store is distinct from the :term:`runtime stack`.
      The free store is sometimes referred to as the :term:`heap`,
      which can be confusing because :term:`heap` more often refers to
      a specific data structure. Most programming languages provide
      functions to allocate (and maybe to deallocate) objects from the
      free store, such as ``new`` in C++ and Java.

   full tree
      A :term:`binary tree` is full if every :term:`node` is either a
      :term:`leaf node` or else it is an :term:`internal node` with
      two non-empty :term:`children <child>`.

   function
      In programming, a subroutine that takes input parameters and
      uses them to compute and return a value.
      In this case, it is usually considered bad practice for a
      function to change any global variables
      (doing so is called a side effect).

   fundamental type
      One of the :term:`simple types <simple type>` 
      provided by the language.
      Examples are ``bool``, ``char``, ``int``, and ``double``.
      Types provided by the STL, such as ``std::string`` and ``std::vector``
      are not considered 'fundamental' types.

   garbage
      In memory management, any memory that was previously (dynamically)
      allocated by the program during runtime, but which is no longer
      accessible since all pointers to the memory have been deleted or
      overwritten.
      In some languages, garbage can be recovered by
      :term:`garbage collection`.
      In languages such as C and C++ that do not provide built-in garbage
      collection, so creating garbage is considered a
      :term:`memory leak`.

   garbage collection
      Languages with garbage collection such
      Java, JavaScript, Lisp, and Scheme will periodically reclaim
      :term:`garbage` and return it to :term:`free store`.

   general tree
      A tree in which any given node can have any number of
      :term:`children <child>`.
      This is in contrast to, for example, a :term:`binary tree` where
      each node has a fixed number of children (some of which might be
      ``null``).
      General tree nodes tend to be harder to implement for this reason.
   
   generic programming
      A computer programming style in which functions are written 
      using *placeholders for* types. In C++ this is accomplished
      using :term:templates<template>`.
      Templates are used to create actual functions for specific types
      as needed. 

   grammar
      A formal definition for what strings make up a :term:`language`,
      in terms of a set of :term:`production rules <production rule>`.

   graph
      A :term:`graph` :math:`\mathbf{G} = (\mathbf{V}, \mathbf{E})`
      consists of a set of :term:`vertices <vertex>`
      :math:`\mathbf{V}` and a set of :term:`edges <edge>`
      :math:`\mathbf{E}`, such that each edge in :math:`\mathbf{E}` is
      a connection between a pair of vertices in :math:`\mathbf{V}`.

   greedy algorithm
      An algorithm that makes locally optimal choices at each step.

   growth rate
      :to-term: lower bound :label: type
      :to-term: upper bound :label: type

      In :term:`algorithm analysis`, the rate at which the cost
      of the :term:`algorithm` grows as the size of its input grows.

   hash function
      In a :term:`hash system`, the function that converts a
      :term:`key` value to a position in the :term:`hash table`.
      The hope is that this position in the hash table contains the
      record that matches the key value.

   hash system
      The implementation for search based on hash lookup in a
      :term:`hash table`.
      The :term:`key` is processed by a
      :term:`hash function`, which returns a position in a
      :term:`hash table`, which hopefully is the correct position in
      which to find the record corresponding to the search key.

   hash table
      The data structure (usually an array) that stores data
      records for lookup using :term:`hashing`.

   hashing
      A search method that uses a :term:`hash function` to convert a
      :term:`key` into a position within a
      :term:`hash table`. 
      In a properly implemented :term:`hash system`, that position in
      the table will have high probability of containing the record
      that matches the key value.
      Sometimes, the hash function will return an position that does
      not store the desired key, due to a process called
      :term:`collision`.
      In that case, the desired record is found through a process
      known as :term:`collision resolution`.

   head
      The beginning of a :term:`list`.

   header guard
      In C and C++, used to prevent definitions copied into a file
      using the ``#include`` directive from being defined
      more than once.

      .. code-block:: cpp

         #ifndef FOO_H_INCLUDED // any name uniquely mapped to file name
         #define FOO_H_INCLUDED
         // contents of the file are here
         #endif

   header node
      Commonly used in implementations for a :term:`linked list` or
      related structure, this :term:`node` precedes the first element
      of the list.
      Its purpose is to simplify the code implementation by
      reducing the number of special cases that must be programmed
      for.

   heap
      This term has two different meanings.
      Sometimes, it is a synonym for :term:`free store`.

      A heap may also refer to a particular data structure.
      This data structure is a :term:`complete binary tree` with the
      requirement that every :term:`node` has a value greater than its
      :term:`children <child>` (called a :term:`max heap`), or else
      the requirement that every node has a value less than its
      children (called a :term:`min heap`).
      Since it is a complete binary tree, a heap is nearly always
      implemented using an array rather than an explicit tree
      structure.
      To add a new value to a heap, or to remove the extreme value
      (the max value in a max-heap or min value in a min-heap) and
      update the heap,
      takes :math:`\Theta(\log n)` time in the worst case.
      However, if given all of the values in an unordered array,
      the values can be re-arranged to form a heap in only
      :math:`\Theta(n)` time. 
      Due to its space and time efficiency, the heap is a
      popular choice for implementing a :term:`priority queue`.

   height
      The height of a tree is one more than the :term:`depth` of the
      deepest :term:`node` in the tree.

   height balanced
      The condition the :term:`depths <depth>` of each :term:`subtree`
      in a tree are roughly the same.

   high-level language
      A programming language that is designed to be easy for
      humans to read and write.

   heuristic
      A way to solve a problem that is not guarenteed to be optimal.
      While it might not be guarenteed to be optimal, it is generally
      expected (by the agent employing the heuristic) to provide a
      reasonably efficient solution.

   heuristic algorithm
      A type of :term:`approximation algorithm`, that uses a
      :term:`heuristic` to find a good, but not necessarily cheapest,
      solution to an :term:`optimization problem`.

   home position
      In :term:`hashing`, a synonym for :term:`home slot`.

   home slot
      In :term:`hashing`, this is the :term:`slot` in the
      :term:`hash table` determined for a given key by the
      :term:`hash function`.

   Huffman coding tree
      A Huffman coding tree is a :term:`full binary tree <full tree>`
      that is used to represent letters (or other symbols)
      efficiently.
      Each letter is associated with a node in the tree, and is then
      given a :term:`Huffman code <Huffman codes>` based on the
      position of the associated node.
      A Huffman coding tree is an example of a binary :term:`trie`.

   Huffman codes
      The codes given to a collection of letters (or other symbols)
      through the process of Huffman coding.
      Huffman coding uses a :term:`Huffman coding tree` to generate
      the codes.
      The codes can be of variable length, such that the letters which
      are expected to appear most frequently are shorter.
      Huffman coding is optimal whenever the true frequencies are
      known, and the frequency of a letter is independent of the
      context of that letter in the message.

   Huffman tree
      Shorter form of the term :term:`Huffman coding tree`.

   identifier
      An identifier is used to name a type introduced into a program by a :term:`declaration`.

      An identifier is an arbitrarily long sequence of digits, underscores, 
      lowercase and uppercase Latin letters. 
      A valid identifier must begin with a non-digit character (Latin letter, underscore, 
      Identifiers are case-sensitive (lowercase and uppercase letters are distinct), 
      and every character is significant.

   image-space decomposition
      A from of :term:`key-space decomposition` where the
      :term:`key space` splitting points is predetermined (typically
      by splitting in half).
      For example, a :term:`Huffman coding tree` splits the letters
      being coded into those with codes that start with 0 on the left
      side, and those with codes that start with 1 on the right side.
      This regular decomposition of the key space is the basis for a
      :term:`trie` data structure.
      An image-space decomposition is in opposition to an
      :term:`object-space decomposition`.

   indexing
      The process of associating a :term:`search key` with the
      location of a corresponding data record.
      The two defining points to the concept of an index is the
      association of a key with a record, and the fact that the index
      does not actually store the record itself but rather it stores a
      :term:`reference` to the record.

      In this way, a collection of records can be supported by
      multiple indices, typically a separate index for each key field
      in the record.

   induction step
      Part of a :term:`proof by induction`.
      In its simplest form, this is a proof of the implication that if
      the theorem holds for $n-1$, then it holds for $n$.
      As an alternative, see :term:`strong induction`.

   inherit
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      the process by which a :term:`subclass` gains
      :term:`data members <data member>` and :term:`methods <method>`
      from a :term:`base class`.

   inorder traversal
      In a :term:`binary tree`, a :term:`traversal` that first
      :term:`recursively <recursion>` :term:`visits <visit>` the left
      :term:`child`, then visits the :term:`root`,
      an then recursively visits the right child.

   instance variable
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      a synonym for :term:`data member`.

   integrated development environment
   IDE
      A software suite that consolidates many tools developers need to 
      write and test software.
      An IDE normally consists of a source code editor, version control,
      build automation tools, and a debugger. 
      Most also automatically complete partially typed keywords and
      create commonly used code from templates.

   interface
      An interface is a class-like structure that only contains method
      signatures and fields. An interface does not contain an implementation
      of the methods or any :term:`data members <data member>`.

   intermediate code
      A step in a typical :term:`compiler` is to transform the
      original high-level language into a form on which it is easier
      to do other stages of the process.
      For example, some compilers will transform the original
      high-level source code into :term:`assembly code` on which it
      can do :term:`code optimization`, before translating it into its final
      executable form.

   intermediate code generation
      :to-term: Parse tree :label: walks through
      :to-term: intermediate code :label: produces

      A phase in a :term:`compiler`, that walks through a
      :term:`parse tree` to produce simple :term:`assembly code`.
      
   internal fragmentation
      A condition that occurs when more than :math:`N` bytes
      are allocated to service a memory request for :math:`N`
      bytes, wasting free storage.
      This is often done to simplify memory management.

   internal node
      In a tree, any node that has at least one non-empty
      :term:`child` is an  internal node.

   internal sort
      A sorting algorithm that is applied to data stored in memory.
      This is in contrast to an :term:`external sort` that is meant to
      work on data stored on disk.

   interpreter
      In contrast to a :term:`compiler` that translates a high-level
      program into something that can be repeatedly executed to
      perform a computation, an interpreter directly performs
      computation on the high-level langauge.

      This tends to make the computation much slower than if it were
      performed on the directly executable version produced by a
      compiler.

   irreflexive
      In set notation, binary relation :math:`R` on set :math:`S` is
      irreflexive if :math:`aRa` is never in the relation for
      any :math:`a \in \mathbf{S}`.

   iterable
      A :term:`container` in which each element
      can be visited using an :term:`iterator`.

   iterator
      In a :term:`container` such as a :container:`vector`
      or :container:`set`, a separate class that
      indicates position within the container, with support for
      :term:`traversing <traversal>` through all
      :term:`elements <element>` in the container.

   kd tree
      :to-term: discriminator :label: uses

      A :term:`spatial data structure` that uses a binary tree to
      store a collection of data records based on their (point)
      location in space.
      It uses the concept of a :term:`discriminator` at each level to
      decide which single component of the
      :term:`multi-dimensional search key` to branch on at that level.
      It uses a :term:`key-space decomposition`, meaning that all data
      records in the left subtree of a node have a value on the
      corresponding discriminator that is less than that of the node,
      while all data records in the right subtree have a greater
      value.

   key
      :to-term: key space :label: has

      A field or part of a larger record used to represent that record
      for the purpose of searching or comparing.

   key sort
      :to-term: key :label: uses

      Any sorting operation applied to a collection of
      :term:`key-value pairs <key-value pair>` where the value in this
      case is a :term:`reference` to a complete record (that is, a
      pointer to the record in memory or a position for a record on
      disk).
      This is in contrast to a sorting operation that works directly
      on a collection of records.
      The intention is that the collection of key-value pairs is far
      smaller than the collection of records themselves.
      As such, this might allow for an :term:`internal sort` when
      sorting the records directly would require an :term:`external
      sort`.
      The collection of key-value pairs can also act as an
      :term:`index <indexing>`.

   key space
      The range of values that a :term:`key` value may take on.

   key-space decomposition
      :to-term: object-space decomposition :label: type
      :to-term: image-space decomposition :label: type

      The idea that the range for a :term:`search key` will be split
      into pieces.
      There are two general approaches to this:
      :term:`object-space decomposition` and
      :term:`image-space decomposition`.

   key-value pair
      A standard solution for solving the problem of how to relate a
      :term:`key` value to a record (or how to find the key for a
      given record) within the context of a particular index.
      The idea is to simply store as records in the index pairs of
      keys and records.
      Specifically, the index will typically store a copy of the key
      along with a reference to the record.
      The other standard solution to this problem is to pass a
      :term:`comparator` function to the index.

   LIFO
      Abbreviation for "Last-In, First-Out".
      This is the access paradigm for a :term:`stack`,
      and an old terminolgy for the stack is "LIFO list".

   language
      A set of strings with specific meanings.

   leaf node
      In a :term:`binary tree`, leaf node is any node that has two
      empty :term:`children <child>`.
      (Note that a binary tree is defined so that every
      node has two children, and that is why the leaf node has to have
      two empty children, rather than no children.)
      In a general tree, any node is a leaf node if it has no children.

   level
      In a tree, all nodes of :term:`depth` :math:`d` are at
      level :math:`d` in the tree.
      The root is the only node at level 0, and its depth is 0.

   lexical analysis
      :to-term: interpreter :label: is

      A phase of a :term:`compiler` or :term:`interpreter` responsible
      for reading in characters of the program or language and grouping
      them into :term:`tokens <token>`.
      
   lexical scoping
      Within programming languages, the convention of allowing access
      to a variable only within the block of code in which the
      variable is defined.
      A synonym for static scoping.

   lifetime
      For a variable, lifetime is the amount of time it will exist
      before it is destroyed.

   linear growth rate
      For input size :math:`n`, a growth rate of :math:`cn` (for
      :math:`c` any positive constant).
      In other words, the cost of
      the associated function is linear on the input size.

   linear order
      Another term for :term:`total order`.

   linear probing
      In :term:`hashing`, this is the simplest
      :term:`collision resolution` method.
      Term :math:`i` of the :term:`probe sequence` is simply
      :math:`i`, meaning that collision resolution works by moving
      sequentially through the hash table from the :term:`home slot`.
      While simple, it is also inefficient, since it quickly leads to
      certain free :term:`slots <slot>` in the hash table having
      higher probability of being selected during insertion or
      search.

   linear probing by steps
      In :term:`hashing`, this :term:`collision resolution` method is
      a variation on simple :term:`linear probing`.
      Some constant :math:`c` is defined such that
      term :math:`i` of the :term:`probe sequence` is
      :math:`ci`.
      This  means that collision resolution works by moving
      sequentially through the hash table from the :term:`home slot`
      in steps of size :math:`c`.
      While not much improvement on linear probing, it forms the basis
      of another collision resolution method called
      :term:`double hashing`, where each key uses a value for
      :math:`c` defined by a second :term:`hash function`.

   link error
      After compiling, a link error occurs when each compilation unit compiles correctly, 
      but in the next stage, the linker is unable to combine all 
      the object code into a single valid executable file.
      Compare to :term:`compile-time error`, :term:`runtime error`, 
      and :term:`semantic error`.


   linked list
      An implementation for the list ADT that uses
      :term:`dynamic memory allocation`
      of link nodes to store the list elements. Common variants are the
      :term:`singly linked list` and :term:`doubly linked list`.

   list
      A finite, ordered sequence of data items known as
      :term:`elements <element>`.
      This is close to the mathematical concept of a :term:`sequence`.
      Note that "ordered" in this definition means that the list
      elements have position.
      It does not refer to the relationship
      between :term:`key` values for the list elements (that is,
      "ordered" does not mean "sorted").

   literal
      In a boolean expression, a ``literal`` is a
      boolean variable or its negation.

      In the context of compilers, it is any constant value.
      Similar to a :term:`terminal`.

   load factor
      In a :term:`hash table`, the number of items contained 
      in the table divided by the table size.

   local variable
      A variable declared within a function or method.
      It exists only from the time when the function is called to when
      the function exits.
      When a function is suspended (due to calling another function),
      the function's local variables are stored in an
      :term:`activation record` on the :term:`runtime stack`.

   logical form
      The definition for a data type in terms of an ADT. Contrast to
      the :term:`physical form` for the data type.

   low-level language
      A programming language that is designed to be easy for a computer to
      execute; also called machine language or assembly language.

   lower bound
      In :term:`algorithm analysis`, a :term:`growth rate` that is
      always less than or equal to the growth rate of the
      :term:`algorithm` in question.
      In practice, this is the fastest-growing function that we know
      grows no faster than all but a constant number of inputs.
      It could be a gross under-estimate of the truth.
      Since the lower bound for the algorithm can be very different
      for different situations (such as the :term:`best case` or
      :term:`worst case`), we typically have to specify which
      situation we are referring to.

   lower bounds proof
      :to-term: adversary argument :label: example
      :to-term: sorting lower bound :label: example
      :to-term: search lower bound :label: example

      A proof regarding the lower bound, with this term most typically
      referring to the lower bound for any possible algorithm to solve
      a given :term:`problem`.
      Many problems have a simple lower bound based on the concept
      that the minimum amount of processing is related to looking at
      all of the problem's input.
      However, some problems have a higher lower bound than that.
      For example, the lower bound for the problem of sorting
      (:math:`\Omega(n \log n)`) is greater than the input size to
      sorting (:math:`n`).
      Proving such "non-trivial" lower bounds for problems is
      notoriously difficult.

   lvalue
      An expression that identifies a non-temporary object.

   lvalue reference
      An alias or synonymn for an existing object.
      Often just referred to as a reference.

   map
      A :term:`data structure` that relates a :term:`key` to a
      :term:`record`.

   mapping
      A :term:`function` that maps every element of a given
      :term:`set` to a unique element of another set; a
      correspondence.

   max heap
      A :term:`heap` where every :term:`node` has a :term:`key` value
      greater than its :term:`children <child>`.
      As a consequence, the node with maximum key value is
      at the :term:`root`.

   member
      In set notation, this is a synonym for :term:`element`. 
      In abstract design, a :term:`data item` is a member of a :term:`type`.
      In an object-oriented language,
      :term:`data members <data member>` are data fields in an
      object.

   member function
      Each operation associated with the ADT is implemented by a
      member function or :term:`method`.

   memory leak
      In programming, the act of creating :term:`garbage`.
      In languages such as C and C++ that do not support
      :term:`garbage collection`, repeated memory leaks will evenually
      cause the program to terminate.

   method
      In the :term:`object-oriented programming paradigm`,
      a method is an operation on a :term:`class`.
      A synonym for :term:`member function`.

   min heap
      A :term:`heap` where every :term:`node` has a :term:`key` value
      less than its :term:`children <child>`.
      As a consequence, the node with minimum key value is
      at the :term:`root`.

   mod
      Abbreviation for the :term:`modulus` function.

   modulus
      The modulus function returns the
      remainder of an integer division.
      Sometimes written :math:`n \bmod m` in mathematical expressions,
      the syntax in many programming languages is ``n % m``.

   multi-dimensional search key
      A search key containing multiple parts, that works in
      conjunction with a :term:`multi-dimensional search structure`.
      Most typically, a :term:`spatial` search key representing a
      position in multi-dimensional (2 or 3 dimensions) space.
      But a multi-dimensional key could be used to organize data within
      non-spatial dimensions, such as temperature and time.

   multi-dimensional search structure
      :to-term: multi-dimensional search key :label: uses

      A data structure used to support efficient search on a
      :term:`multi-dimensional search key`.
      The main concept here is that a multi-dimensional search
      structure works more efficiently by considering the multiple
      parts of the search key as a whole, rather than making
      independent searches on each one-dimensional component of the
      key.
      A primary example is a :term:`spatial data structure` that can
      efficiently represent and search for records in
      multi-dimensional space.

   multilist
      A list that may contain sublists.
      This term is sometimes used as a synonym to the term
      :term:`bag`.

   name
      See :term:`identifier`.

   natural language
      Any one of the languages that people speak that evolved naturally.

   natural order
      An ordering of a sequence of objects that seems 'natural' to most people.
      The 'natural order' of whole numbers is the sequence used to count things:
      1,2,3,4,5,6...
      The natural order for words is sorted alphabetically.

   neighbor
      :to-term: adjacent :label: is
      :to-term: graph :label: context

      In a :term:`graph`, a :term:`node` :math:`w` is said to be a
      neighbor of :term:`node` :math:`v` if there is an :term:`edge`
      from :math:`v` to :math:`w`.

   node
      The objects that make up a linked structure such as a linked
      list or binary tree.
      Typically, nodes are allocated using
      :term:`dynamic memory allocation`.

   non-strict partial order
      In set notation, a relation that is :term:`reflexive`,
      :term:`antisymmetric`, and :term:`transitive`.

   non-terminal
      In contrast to a :term:`terminal`, a non-terminal is an abstract
      state in a :term:`production rule`. Begining with the
      :term:`start symbol`, all non-terminals must be converted into
      terminals in order to complete a :term:`derivation`.

   object
      An instance of a class, that is, something that is created and
      takes up storage during the execution of a computer program.
      In the :term:`object-oriented programming paradigm`, objects
      are the basic units of operation.
      Objects have state in the form of :term:`data members <data member>`,
      and they know how to perform certain actions
      (:term:`functions <function>`).

   object code
      The output of the compiler after it translates the program.

   object-oriented programming
   object-oriented programming paradigm
      An approach to problem-solving where all computations are
      carried out using :term:`objects <object>`.

   object-space decomposition
      A from of :term:`key-space decomposition` where the
      :term:`key space` is determined
      by the actual values of keys that are found.
      For example, 
      a binary search tree stores a key value in its root,
      and all other values in the tree with lesser value are in the
      left :term:`subtree`.
      Thus, the root value has split (or decomposed) the
      key space for that key based on its value into left
      and right parts.
      An object-space decomposition is in opposition to an
      :term:`image-space decomposition`.

   octree
      The three-dimensional equivalent of the :term:`quadtree` would
      be a tree with :math:`2^3` or eight branches.

   Omega notation
      In :term:`algorithm analysis`,
      :math:`\Omega` notation is used to describe a :term:`lower bound`.
      Roughly (but not completely) analogous to
      :term:`big-Oh notation` used to define an :term:`upper bound`.

   open addressing
      A synonym for :term:`closed hashing <closed hash system>`.

   open hashing
   open hash system
      A :term:`hash system` where multiple records might be associated
      with the same slot of a :term:`hash table`.
      Typically this is done using a linked list to store the records.
      This is in contrast to a :term:`closed hash system`.

   operating system
      The control program for a computer.
      Its purpose is to control hardware, manage resources, and
      present a standard interface to these to other software
      components.

   optimization problem
      Any problem where there are a (typically large) collection of
      potential solutions, and the goal is to find the best solution.
      An example is the Traveling Salesman Problem, where
      visiting :math:`n` cities in some order has a cost, and the goal
      is to visit in the cheapest order.

   overflow
      The condition where the amount of data stored in an entity has
      exceeded its capacity.
      For example, a node in a array can store a certain
      number of records.
      If a record is attempted to be inserted into a node that is
      full, then something has to be done to handle this case.

   overflow bucket
      In :term:`bucket hashing`, this is the :term:`bucket` into which
      a record is placed if the bucket containing the record's
      :term:`home slot` is full.
      The overflow bucket is logically considered to have infinite
      capacity, though in practice search and insert will become
      relatively expensive if many records are stored in the overflow
      bucket.

   parameter
   parameters
      The values making up an input to a :term:`function`.

   parent
      In a tree, the :term:`node` :math:`P` that directly links to a
      node :math:`A` is the parent of :math:`A`. :math:`A` is the
      :term:`child` of :math:`P`.

   parent pointer representation
      For :term:`trees <tree>`, a :term:`node` implementation where
      each node stores only a pointer to its :term:`parent`, rather
      than to its :term:`children <child>`.
      This makes it easy to go up the tree toward the :term:`root`,
      but not down the tree toward the :term:`leaves <leaf node>`.

   parity
      The concept of matching even-ness or odd-ness, the basic idea
      behind using a :term:`parity bit` for error detection.

   parity bit
      A common method for checking if transmission of a
      sequence of bits has been performed correctly.
      The idea is to count the number of 1 bits in the sequence, and
      set the parity bit to 1 if this number is odd, and 0 if it is
      even.
      Then, the transmitted sequence of bits can be checked to see if
      its parity matches the value of the parity bit.
      This will catch certain types of errors, in particular if the
      value for a single bit has been reversed.
      This was used, for example, in early versions of
      :term:`ASCII character coding`.

   parse
      To examine a program and analyze the syntactic structure.

   parse tree
      A tree that represents the syntactic structure of an input
      string, making it easy to compare against a :term:`grammar` to
      see if it is syntactically correct.

   parser
      :to-term: compiler :label: part of
      :to-term: parse tree :label: build

      A part of a :term:`compiler` that takes as input the program
      text (or more typically, the tokens from the :term:`scanner`),
      and verifies that the program is syntactically correct.
      Typically it will build a :term:`parse tree` as part of the
      process.

   partial order
      In set notation, a binary relation is called a partial order if
      it is :term:`antisymmetric` and :term:`transitive`.
      If the relation is also :term:`reflexive`, then it is a
      :term:`non-strict partial order`.
      Alternatively, if the relation is also :term:`irreflexive`, then
      it is a :term:`strict partial order`.

   partially ordered set
      The set on which a :term:`partial order` is defined is called a
      partially ordered set.

   partition
      The process of splitting a set into two parts, typically centering
      around a predicate expression or a value.

      In quick sort, the central value is called the ``pivot`` value.
      One partition will contain values less then the pivot,
      while the other partition will contain values greater than the
      pivot value.

   pass by value
      A copy of a variable is passed to the called function. So, any
      modifications will not affect the original variable.

   pass by reference
      A :term:`reference` to the variable is passed to the called
      function. So, any modifications will affect the original
      variable.

   path
      :to-term: tree :label: In
      :to-term: vertex :label: sequence of

      In :term:`tree` or :term:`graph` terminology,
      a sequence of :term:`vertices <vertex>`
      :math:`v_1, v_2, ..., v_n`
      forms a path of length :math:`n-1` if there exist edges from
      :math:`v_i` to :math:`v_{i+1}` for :math:`1 \leq i < n`.

   permutation
      A permutation of a sequence :math:`\mathbf{S}`
      is the :term:`elements <element>` of :math:`\mathbf{S}` arranged
      in some order.

   physical form
      The implementation of a data type as a data structure.
      Contrast to the :term:`logical form` for the data type.

   Pigeonhole Principle
      A commonly used lemma in Mathematics. A typical variant states:
      When :math:`n+1` objects are stored in :math:`n` locations, at
      least one of the locations must store two or more of the objects.

   POD
      An abbreviation for 'plain old data'.
      Used to indicate a data structure containing no member functions
      and only publicly accessible data.

   pop
      A specialized term used to indicate removing an :term:`element`
      from a :term:`stack`. 

   pointer
      A variable whose value is the :term:`address` of another variable;
      a link.

   pointer-based implementation for binary tree nodes
      A common way to implement :term:`binary tree` :term:`nodes
      <node>`.
      Each node stores a data value (or a reference to a data value),
      and pointers to the left and right children.
      If either or both of the children does not exist, then a null
      pointer is stored.

   polymorphism
   Polymorphism
      An :term:`object-oriented programming <object-oriented programming paradigm>`
      term meaning *one name, many forms*.
      It describes the ability of software to change its behavior
      dynamically.  Two basic forms exist:
      :term:`runtime polymorphism` and :term:`compile-time polymorphism`.

   portability
      A property of a program that can run on more than one kind of computer.

   position
      The defining property of the list ADT, this is the concept that
      list elements are in a position. Many list ADTs support access
      by position.

   poset
      An abbreviation for a :term:`partially ordered set`.

   postorder traversal
      In a :term:`binary tree`, a :term:`traversal` that first
      :term:`recursively <recursion>` :term:`visits <visit>` the left
      :term:`child`, 
      then recursively visits the right child, and then visits the
      :term:`root`.

   powerset
      For a :term:`set` :math:`\mathbf{S}`, the power set is the set
      of all possible :term:`subsets <subset>` for :math:`\mathbf{S}`.

   predicate
   predicate function
      A function that returns a boolean value.

   PR quadtree
      A type of :term:`quadtree` that stores point data in two
      dimensions.
      The root of the PR quadtree represents some square region of 2d
      space.
      If that space stores more than one data point, then the region
      is decomposed into four equal subquadrants, each represented
      :term:`recursively <recursion>` by a subtree of the PR quadtree.
      Since many leaf nodes of the PR quadtree will contain no data
      points, implementation often makes use of the :term:`flyweight`
      :term:`design pattern`.
      Related to the :term:`bintree`.

   preorder traversal
      In a :term:`binary tree`, a :term:`traversal` that first
      :term:`visits <visit>` the :term:`root`, then
      :term:`recursively <recursion>` visits the left :term:`child`,
      then recursively visits the right child.

   primary clustering
      In :term:`hashing`, the tendency in certain
      :term:`collision resolution`
      methods to create clustering in sections of the hash table.
      The classic example is :term:`linear probing`.
      This tends to happen when a group of keys follow the same
      :term`probe sequence` during collision resolution.

   primitive element
      In set notation, this is a single element that is a member of
      the base type for the set. This is as opposed to an element of
      the set being another set.

   primitive type
      A :term:`data type` whose values contain no subparts.
      An example is the integers.
      A synonym for :term:`simple type` 
      and :term:`code block`.

   priority
      A quantity assigned to each of a collection of
      tasks that indicate importance for order of processing.
      For example, in an operating system, there could be a collection
      of processes (jobs) ready to run.
      The operating system must select the next task to execute, 
      based on their priorities.

   priority queue
      An ADT whose primary operations of insert of records, and
      deletion of the greatest (or, in an alternative implementation,
      the least) valued record.
      Most often implemented using the :term:`heap` data structure.
      The name comes from a common application where the records being
      stored represent tasks, with the ordering values based on the
      :term:`priorities <priority>` of the tasks.

   probe function
      In :term:`hashing`, the function used by a
      :term:`collision resolution` method to calculate where to look
      next in the :term:`hash table`.

   probe sequence
      In :term:`hashing`, the series of :term:`slots <slot>` visited
      by the :term:`probe function` during
      :term:`collision resolution`.

   problem
      A task to be performed.
      It is best thought of as a :term:`function` or a mapping of
      inputs to outputs.

   problem instance
      A specific selection of values for the parameters to a problem.
      In other words, a specific set of inputs to a problem.
      A given problem instance has a size under some
      :term:`cost model`.

   problem solving
      The process of formulating a problem, finding a solution, and
      expressing the solution.

   procedural
      Typically referring to the
      :term:`procedural programming paradigm`, in contrast to the
      :term:`object-oriented programming paradigm`.

   procedural programming paradigm
      Procedural programming uses a list of instructions (and
      procedure calls) that define a series of computational steps to
      be carried out.
      This is in contrast to the 
      :term:`object-oriented programming paradigm`.
     
   production
   production rule
      A :term:`grammar` is comprised of production rules.
      The production rules consist of :term:`terminals <terminal>` and
      :term:`non-terminals <non-terminal>`, with one of the non-terminals
      being the :term:`start symbol`.
      Each production rule replaces one or more non-terminals (perhaps
      with associated terminals) with one or more terminals and
      non-terminals.
      Depending on the restrictions placed on the form of the rules,
      there are classes of languages that can be represented by
      specific types of grammars.
      A :term:`derivation` is a series of productions that results in
      a string (that is, all non-terminals), and this derivation can
      be represented as a :term:`parse tree`.

   proof
      :to-term: lower bounds proof :label: example
      :to-term: NP-Completeness proof :label: example
      :to-term: proof by contradiction :label: type
      :to-term: proof by induction :label: type

      The establishment of the truth of anything, a demonstration.

   proof by contradiction
      A mathematical proof technique that proves a theorem by first
      assuming that the theorem is false, and then uses a chain of
      reasoning to reach a logical contradiction.
      Since when the theorem is false a logical contradiction arises,
      the conclusion is that the theorem must be true.

   proof by induction
      A mathematical proof technique similar to :term:`recursion`.
      It is used to prove a parameterized theorem $S(n)$, that is,
      a theorem where there is a induction variable involved
      (such as the sum of the numbers from 1 to $n$).
      One first proves that the theorem holds true for a
      :term:`base case`, then one proves the implication that
      whenever $S(n)$ is true then $S(n+1)$ is also true.
      Another variation is :term:`strong induction`.

   program
      An instance, or concrete representation, of an algorithm in some
      programming language.
      A sequence of instructions that specifies to a computer actions and
      computations to be performed.
      A program can refer to the :term:`compiled <compile>` system
      :term:`object code`, or to the original :term:`source code`.

   programming language
      A formal notation for representing solutions.

   pseudo-random probing
      In :term:`hashing`, this is a :term:`collision resolution`
      method that stores a random permutation of the values 1 through
      the size of the :term:`hash table`.
      Term :math:`i` of the :term:`probe sequence` is simply the value
      of position :math:`i` in the permuation.

   push
      A specialized term used to indicate inserting an :term:`element`
      onto a :term:`stack`.

   push_back
      A specialized term used to indicate appending an :term:`element`
      onto a :term:`vector`.

   quadratic growth rate
      A growth rate function of the form :math:`cn^2` where :math:`n`
      is the input size and :math:`c` is a constant.

   quadtree
      A :term:`full tree` where each internal node has four children.
      Most typically used to store two dimensional
      :term:`spatial data`.
      Related to the :term:`bintree`.
      The difference is that the quadtree splits all dimensions
      simultaneously, while the bintree splits one dimension at each
      level.
      Thus, to extend the quadtree concept to more dimensions requires
      a rapid increase in the number of splits (for example, 8 in
      three dimensions).

   quadratic probing
      In :term:`hashing`, this is a :term:`collision resolution`
      method that computes term :math:`i` of the
      :term:`probe sequence` using some quadratic equation
      :math:`ai^2 _ bi + c` for suitable constants :math:`a, b, c`.
      The simplest form is simply to use :math:`i^2` as term :math:`i`
      of the probe sequence.

   queue
      A list-like structure in which elements are inserted only at one
      end, and removed only from the other one end.

   radix
      Synonym for :term:`base`. The number of digits in a number
      representation. For example, we typically represent numbers in
      base (or radix) 10. Hexidecimal is base (or radix) 16.

   RAII
      Resource Acquisition Is Initialization
      is the C++ term for a programming style in which critical resources are
      tied to the object which owns them.
      Because they are typically allocated in class constructors and 
      destroyed in class destructors, in other languages, this is
      sometimes called *Constructor Acquires, Destructor Releases*

   range
      The set of possible outputs for a function.

   record
      A collection of information, typically implemented as an
      :term:`object` in an
      :term:`object-oriented programming language <object-oriented programming paradigm>`.
      Many data structures are organized containers for a collection
      of records.

   recurrence relation
      A recurrence relation (or less formally,
      recurrence) defines a function by means of an
      expression that includes one or more (smaller) instances of
      itself.
      A classic example is the :term:`recursive <recursion>`
      definition for the
      factorial function, :math:`F(n) = n*F(n-1)`.

   recursion
      The process of using recursive calls.
      An algorithm is recursive if it calls itself to do part of
      its work.
      See :term:`recurrence relation`.

   recursive call
      Within a :term:`recursive function`, it is a call that the
      function makes to itself.

   recursive data structure
      A data structure that is partially
      composed of smaller or simpler instances of the same data structure.
      For example, :term:`linked lists <linked list>` and
      :term:`binary trees <binary tree>` can be viewed as recursive
      data structures.

   recursive function
      A function that includes a :term:`recursive call`.

   reference
      A value that enables a program to directly access some
      particular data item.
      An example might be a byte position within a file where the
      record is stored, or a pointer to a record in memory.
      (Note that Java makes a distinction between a reference and the
      concept of a pointer, since it does not define a reference to
      necessarily be a byte position in memory.)

   reference count algorithm
      An algorithm for :term:`garbage collection`.
      Whenever a reference is made from a variable to some memory
      location, a counter associated with that memory location is
      incremented.
      Whenever the reference is changed or deleted, the reference
      count is decremented.
      If this count goes to zero, then the memory is considered free
      for reuse.
      This approach can fail if there is a cycle in the chain of
      references.

   reflexive
      In set notation, binary relation :math:`R` on set :math:`S` is
      reflexive if :math:`aRa` for all :math:`a \in \mathbf{S}`.

   regular type
      A user defined :term:`type` that behaves like a 'regular'
      built-in (fundamental) type.
      Regular types support the following operations:

      ========================= ====================
       Operation                 Definition
      ========================= ====================
       Default constructor        T a;
       Copy constructor           T a = b;
       Destructor                 ~T (a);
       Assignment                 a = b;
       Equality                   a == b;
       Inequality                 a != b;
       Ordering                   a < b;
      ========================= ====================

   relation
      In set notation, a relation :math:`R` over set
      :math:`\mathbf{S}` is a set of ordered pairs from
      :math:`\mathbf{S}`.

   root
      In a :term:`tree`, the topmost :term:`node` of the tree.
      All other nodes in the tree are :term:`descendants <descendant>`
      of the root.

   runtime environment
      The environment in which a program (of a particular programming
      language) executes.
      The runtime environment handles such activities as managing the
      :term:`runtime stack`, the :term:`free store`, and the
      :term:`garbage collector <garbage collection>`,
      and it conducts the execution of the program.

   runtime error
      An error that does not occur until the program has started to execute
      but that prevents the program from continuing.
      Compare to :term:`compile-time error`, :term:`link error`, 
      and :term:`semantic error`.

   runtime polymorphism
   Runtime polymorphism
      A form of :term:`polymorphism` known as Overriding.
      Overridden methods are those which implement a new method
      with the same signature as a method inherited from its
      base class.
      Compare to :term:`compile-time polymorphism`.

   runtime stack
      The place where an :term:`activation record` is stored when a
      subroutine is called during a program's runtime.

   rvalue
      An expression that identifies a temporary object or
      a value not associated with any object, such as a literal.

   rvalue reference
      Sometimes called a forwarding reference.
      A reference that is allowed to refer to an rvalue.
      That is, a temporary object or an rvalue not associated with any object.

   scanner
      :to-term: compiler :label: part of
      :to-term: lexical analysis :label: responsible for

      The part of a :term:`compiler` that is responsible for doing
      :term:`lexical analysis`.

   scope
      A region of the program where a defined variable, definition, or function exists. 
      Beyond that point the variable can not be accessed. 

   search key
      A field or part of a record that is used to represent the record
      when searching. For example, in a database of customer records,
      we might want to search by name.
      In this case the name field is used as the search key.

   search lower bound
      The problem of searching in an array has provable lower bounds
      for specific variations of the problem.
      For an unsorted array, it is :math:`\Omega(n)`
      :term:`comparisons <comparison>` in the :term:`worst case`,
      typically proved using an :term:`adversary argument`.
      For a sorted array, it is :math:`\Omega(\log n)` in the worst
      case, typically proved using an argument similar to the
      :term:`sorting lower bound` proof.
      However, it is possible to search a sorted array in the average
      case in :math:`O(\log \log n)` time.

   search problem
      Given a particular key value :math:`K`, the search problem is to
      locate a :term:`record` :math:`(k_j, I_j)` in some collection of
      records **L** such that :math:`k_j = K` (if one exists).
      :term:`Searching <searching>` is a systematic method for
      locating the record (or records) with key value :math:`k_j = K`.

   search tree
      :to-term: Binary Search Tree :label: example
      :to-term: search trie :label: example

      A :term:`tree` data structure that makes search by :term:`key`
      value more efficient.
      A type of :term:`container`, it is common to implement an
      :term:`index <indexing>` using a search tree.
      A good search tree implementation will guarantee that insertion,
      deletion, and search operations are all :math:`\Theta(\log n)`.

   search trie
      :to-term: alphabet trie :label: example
      :to-term: binary trie :label: example

      Any :term:`search tree` that is a :term:`trie`.

   searching
      Given a :term:`search key` :math:`K` and some collection of
      records **L**, searching is a systematic method for locating the
      record (or records) in **L** with key value :math:`k_j = K`.

   secondary clustering
      In :term:`hashing`, the tendency in certain
      :term:`collision resolution`
      methods to create clustering in sections of the hash table.
      In :term:`primary clustering`, this is caused by a cluster of
      keys that don't necessarily hash to the same slot but which
      following significant portions of the same
      :term:`probe sequence` during collision resolution.
      Secondary clustering results from the keys hashing to the same
      slot of the table (and so a collision resolution method that is
      not affected by the key value must use the same probe sequence
      for all such keys).
      This problem can be resolved by :term:`double hashing` since its
      probe sequence is determined in part by a second hash function.

   semantic error
      An error in a program or expression that makes it do something other than what the
      programmer intended.
      Compare to :term:`compile-time error`, :term:`link error`, 
      and :term:`runtime error`.

   semantics
      The meaning of a program or piece of text.

   separate chaining
      In :term:`hashing`, a synonym for
      :term:`open hashing <open hash system>`

   sequence
      In set notation, a collection of elements with an order, and
      which may contain duplicate-valued elements.
      A sequence is also sometimes called a :term:`tuple` or a
      :term:`vector`.

   sequence container
      A container in which elements can be accessed sequentially.
      The underlying data may be a contiguous block of memory,
      as with ``vector`` and ``array``,
      or may be non-contiguous memory, as with ``list``.
      
   sequential tree representation
      A representation that stores a series of node values with the
      minimum information needed to reconstruct the tree structure.
      This is a technique for :term:`serializing <serialization>` a
      tree.

   serialization
      The process of taking a data structure in memory and
      representing it as a sequence of bytes.
      This is sometimes done in order to transmit the data structure
      across a network or store the data structure in a
      :term:`stream`, such as on disk.
      :term:`Deserialization <deserialization>` reconstructs the
      original data structure from the serialized representation.

   set
      A collection of distinguishable :term:`members <member>` or
      :term:`elements <element>`.

   set former
      A way to define the membership of a set, by using a text
      description.
      Example: :math:`\{x\ |\ x\ \mbox{is a positive integer}\}`.

   set product
      Written :math:`\mathbf{Q} \times \mathbf{P}`, the set product is
      a set of ordered pairs such that ordered pair :math:`(a, b)` is
      in the product whenever :math:`a \in \mathbf{P}` and
      :math:`b \in \mathbf{Q}`.
      For example, when :math:`\mathbf{P} = \{2, 3, 5\}` and
      :math:`\mathbf{Q} = \{5, 10\}`,
      :math:`\mathbf{Q} \times \mathbf{P} =
      \{(2, 5),\ (2, 10),\ (3, 5),\ (3, 10),\ (5, 5),\ (5, 10)\}`.

   shallow copy
      Copying a :term:`reference` or :term:`pointer`
      value without copying the actual content.

   sibling
      In a :term:`tree`, a sibling of :term:`node` :math:`A` is any
      other node with the same :term:`parent` as :math:`A`.

   signature
      In a programming language, the signature for a function is its
      return type and its list of parameters and their types.

   simple type
      A :term:`data type` whose values contain no subparts.
      An example is the integers.
      A synonym for :term:`primitive type`
      and :term"`fundamental type`.

   simulating recursion
      If a programming language does not support :term:`recursion`,
      or if you want to implement the effects of recursion more
      efficiently, you can use a :term:`stack` to maintain the
      collection of subproblems that 
      would be waiting for completion during the recursive process.
      Using a loop, whenever a recursive call would have been made,
      simply add the necessary program state to the stack.
      When a return would have been made from the recursive call, pop
      the previous program state off of the stack.

   singly linked list
      A :term:`linked list` implementation variant where each list
      node contains access an pointer only to the next element in the list.

   slot
      In :term:`hashing`, a position in a :term:`hash table`.

   software engineering
      The study and application of engineering to the design,
      development, and maintenance of software.

   software reuse
      In :term:`software engineering`, the concept of reusing a piece
      of software.
      In particular, using an existing piece of software (such as a
      function or library) when creating new software.

   sorting lower bound
      The lower bound for the :term:`problem` of
      :term:`sorting <sorting problem>` is :math:`\Omega(n \log n)`.
      This is traditionally proved using a :term:`decision tree` model
      for sorting algorithms, and recognizing that the minimum depth
      of the decision tree for any sorting algorithm is
      :math:`\Omega(n \log n)` since there are :math:`n!` permutations
      of the :math:`n` input records to distinguish between during the
      sorting process.

   sorting problem
      Given a set of records :math:`r_1`, :math:`r_2`, ..., :math:`r_n`
      with :term:`key` values :math:`k_1`, :math:`k_2`, ..., :math:`k_n`,
      the sorting problem is to arrange the records into any order
      :math:`s` such that records
      :math:`r_{s_1}`, :math:`r_{s_2}`, ..., :math:`r_{s_n}`
      have keys obeying the property
      :math:`k_{s_1} \leq k_{s_2} \leq ... \leq k_{s_n}`.
      In other words, the sorting problem is to arrange a set of
      records so that the values of their key fields are in
      non-decreasing order.
   
   source code
      A program, stored in a file, in a high-level language before being compiled or interpreted.

   spatial
      Referring to a position in space.

   spatial application
      An application what has spatial aspects.
      In particular, an application that stores records that need to
      be searched by location.

   spatial attribute
      An attribute of a record that has a position in space, such as
      the coordinate.
      This is typically in two or more dimensions.

   spatial data
      Any object or record that has a position (in space).

   spatial data structure
      :to-term: bintree :label: example
      :to-term: kd tree :label: example
      :to-term: PR quadtree :label: example

      A :term:`data structure` designed to support efficient
      processing when a
      :term:`spatial attribute` is used as the key.
      In particular, a data structure that supports efficient search
      by location, or finds all records within a given region in two
      or more dimensions.
      Examples of spatial data structures to store point data include
      the :term:`bintree`, the :term:`PR quadtree` and the
      :term:`kd tree`.

   stack
      A list-like structure in which elements may be inserted or
      removed from only one end.

   start symbol
      In a :term:`grammar`, the designated :term:`non-terminal` that
      is the initial point for :term:`deriving <derivation>` a string
      in the language.

   static scoping
      A synonym for :term:`lexical scoping`.

   strategy
      An approach to accomplish a task, often encapsulated as an
      algorithm.
      Also the name for a :term:`design pattern` that separates the
      algorithm for performing a task from the control for applying
      that task to each member of a collection.
      A good example is a generic sorting function that takes a
      collection of records (such as an array) and a "strategy" in the
      form of an algorithm that knows how to extract the key from a
      record in the array.
      Only subtly different from the :term:`visitor` design pattern,
      where the difference is primarily one of intent rather than
      syntax.
      The strategy design pattern is focused on encapsulating an
      activity that is part of a larger process, so that different
      ways of performing that activity can be substituted.
      The visitor design pattern is focused on encapsulating an
      activity that will be performed on all members of a collection
      so that completely different activities can be substituted
      within a generic method that accesses all of the collection
      members.

   stream
      The process of delivering content in a
      :term:`serialized <serialization>` form.

   strict partial order
      In set notation, a relation that is :term:`irreflexive`,
      :term:`antisymmetric`, and :term:`transitive`.

   strong induction
      An alternative formulation for the :term:`induction step` in a
      :term:`proof by induction`.
      The induction step for strong induction is:
      If **Thrm** holds for all :math:`k, c \leq k < n`, then
      **Thrm** holds for :math:`n`.

   subclass
      In :term:`object-oriented programming <object-oriented programming paradigm>`,
      any class within a :term:`class hierarchy` that
      :term:`inherits <inherit>` from some other class.
      A synonym for :term:`derived class`.

   subset
      In set theory, a set :math:`A` is a subset of a set
      :math:`B`, or equivalently :math:`B` is a :term:`superset` of
      :math:`A`, if all elements of :math:`A` are also elements of
      :math:`B`.

   subtree
      A subtree is a subset of the nodes of a binary tree that
      includes some node :math:`R` of the tree as the subtree
      :term:`root` along with all the :term:`descendants <descendant>`
      of :math:`R`.

   summation
      The sum of costs for some function applied to a
      range of parameter values.
      Often written using Sigma notation.
      For example, the sum of the integers from 1 to :math:`n` can be
      written as :math:`\sum_{i=1}^{n} i`.

   superset
      In set theory, a set :math:`A` is a :term:`subset` of a
      :term:`set` :math:`B`, or equivalently :math:`B` is a
      :term:`superset` of :math:`A`, if all :term:`elements <element>`
      of :math:`A` are also elements of :math:`B`.

   symbol table
      As part of a :term:`compiler`, the symbol table stores all of
      the identifiers in the program, along with any necessary
      information needed about the identifier to allow the compiler to
      do its job.

   symmetric
      In set notation, relation :math:`R` is symmetric if whenever
      :math:`aRb`, then :math:`bRa`, for all :math:`a, b \in \mathbf{S}`.

   symmetric matrix
      A square matrix that is equal to its :term:`transpose`.
      Equivalently, for a :math:`n \times n` matrix :math:`A`,
      for all :math:`i,j < n`, :math:`A[i, j] = A[j, i]`.

   syntax
      The set of rules that defines the valid symbol combinations
      that define valid statements or expressions in 
      a specific language.

   syntax analysis
      :to-term: parse tree :label: generates
      :to-term: tokens :label: accepts

      A phase of :term:`compilation <compiler>` that accepts
      :term:`tokens <token>`, checks if program is syntactically
      correct, and then generates a :term:`parse tree`.

   syntax error
      An error in a program that makes it impossible to parse --- and
      therefore impossible to interpret.

   tail
      The end of a :term:`list`.

   terminal
      A specific character or string that appears in a
      :term:`production rule`.
      In contrast to a :term:`non-terminal`, which represents an
      abstract state in the production.
      Similar to a :term:`literal`, but this is the term more
      typically used in the context of a :term:`compiler`.

   template
      A template is a specific way in C++ to write 
      :term:`generic <generic programming>` functions and classes.

      A template by itself is not a class, type, function, or any other entity.
      It defines a **recipe** for generating a class or function.

   test-driven development
      Test-driven development (TDD) is a software development process 
      that relies on the repetition of a very short development cycle: 
      requirements are turned into very specific test cases, 
      then the software is improved to pass the new tests, only. 
      This is opposed to software development that allows software to be 
      added that is not proven to meet requirements.

      Kent Beck, who is credited with having developed the technique, 
      stated in 2003 that TDD encourages simple designs and inspires confidence.

   token
      One of the basic elements of the syntactic structure of a program,
      analogous to a word in a natural language.

   total order
      A binary relation on a set where every pair of distinct elements
      in the set are :term:`comparable` (that is, one can determine
      which of the pair is greater than the other).

   trailing return type
      A C++11 language feature that allows a function or lambda expression
      to defer evaluating the function return type.  Example:

      .. code-block:: cpp

         template<class T>
         auto mul(T a, T b) -> decltype(a*b){
           return a*b;
         }

      or

      .. code-block:: cpp

         [](double x, double y) -> int {return x*y;}

   transitive
      In set notation, relation :math:`R` is transitive if whenever
      :math:`aRb` and :math:`bRc`, then :math:`aRc`, for all
      :math:`a, b, c \in \mathbf{S}`.

   traversal
   traverse
      Any process for visiting all of the objects in a collection
      (such as a :term:`tree` or :term:`list`) in some order.

   transpose
      In the context of linear algebra,
      the transpose of a matrix :math:`A` is
      another matrix :math:`A^T` created by writing the rows of
      :math:`A` as the columns of :math:`A^T`.

   tree
      A tree :math:`\mathbf{T}` is a finite set of one or more
      :term:`nodes <node>` such that there is one designated node
      :math:`R`, called the :term:`root` of :math:`\mathbf{T}`.
      If the set :math:`(\mathbf{T} -\{R\})` is not empty, these
      nodes are partitioned into :math:`n > 0`
      disjoint sets :math:`\mathbf{T}_0`,
      :math:`\mathbf{T}_1`, ..., :math:`\mathbf{T}_{n-1}`, 
      each of which is a tree, and whose :term:`roots <root>`
      :math:`R_1, R_2, ..., R_n`,
      respectively, are :term:`children <child>` of :math:`R`.

   tree traversal
      A :term:`traversal` performed on a tree.
      Traditional tree traversals include
      :term:`preorder <preorder traversal>` and
      :term:`postorder <postorder traversal>` traversals for both
      :term:`binary <binary tree>` and :term:`general <general tree>`
      trees, and :term`inorder traversal` for binary search trees.

   trie
      :to-term: alphabet trie :label: example
      :to-term: binary trie :label: example
      :to-term: search trie :label: example

      A form of :term:`search tree` where an internal node represents
      a split in the :term:`key space` at a predetermined location,
      rather than split based on the actual :term:`key` values seen.
      For example, a simple binary search trie for key values in the
      range 0 to 1023 would store all records with key values less
      than 512 on the left side of the tree, and all records with key
      values equal to or greater than 512 on the right side of the
      tree.
      A trie is always a :term:`full tree`.
      Folklore has it that the term comes from "retrieval", and should
      be pronounced as "try" (in contrast to "tree", to distinguish
      the differences in the space decomposition method of a search
      tree versus a search trie).
      The term "trie" is also sometimes used as a synonym for the
      :term:`alphabet trie`.

   truth table
      In symbolic logic, a table that contains as rows all possible
      combinations of the boolean variables, with a column that shows
      the outcome (true or false) for the expression when given that
      row's truth assignment for the boolean variables.

   tuple
      In set notation, another term for a :term:`sequence`.

      In C++, the class :utility:`tuple`.

   two's complement
      A mathematical operation on binary numbers, 
      as well as a binary signed number representation based on this operation. 

   type
      A collection of values.

   unary function
      A function that accepts one parameter.

   unit test
      A software test method in which a single *unit* of source code, 
      for example, a single function is tested in isolation.
      Unit tests are short code fragments, typically created by programmers 
      as part of the development process.
      In a process like :term:`test-driven development` the unit tests
      are written before any other code.

   unsorted list
      A :term:`list` where the records stored in the list can appear
      in any order (as opposed to a sorted list).
      An unsorted list can support efficient (:math:`\Theta(1)`)
      insertion time (since you can put the record anywhere
      convenient), but requires :math:`\Theta(n)` time for both search
      and deletion.

   unvisited
      In :term:`graph` algorithms, this refers to a node that has not
      been processed at the current point in the algorithm.

   upper bound
      In :term:`algorithm analysis`, a :term:`growth rate` that is
      always greater than or equal to the growth rate of the
      :term:`algorithm` in question.
      In practice, this is the slowest-growing function that we know
      grows at least as fast as all but a constant number of inputs.
      It could be a gross over-estimate of the truth.
      Since the upper bound for the algorithm can be very different
      for different situations (such as the :term:`best case` or
      :term:`worst case`), we typically have to specify which
      situation we are referring to.

   variable-length coding
      Given a collection of objects, a variable-length coding scheme
      assigns a code to each object in the collection using codes that
      can be of different lengths.
      Typically this is done in a way such that the objects that are
      most likely to be used have the shortest codes, with the goal of
      minimizing the total space needed to represent a sequence of
      objects, such as when representing the characters in a document.
      This is in contrast to :term:`fixed-length coding`.

   vector
      In set notation, another term for a :term:`sequence`.
      As a data structure, the term vector usually used as a synonym
      for a :term:`dynamic array`.

   vertex
      Another name for a :term:`node` in a :term:`graph`.

   visit
      During the process of a :term:`traversal` on a :term:`list` or
      :term:`tree` the action that takes place on each :term:`node`.

   visitor
      A :term:`design pattern` where a :term:`traversal` process is
      given a function (known as the visitor) that is applied to every
      object in the collection being traversed.
      For example, a generic tree or graph traversal might be
      designed such that it takes a function parameter,
      where that function is applied to each node.

   volatile
      In the context of computer memory, this refers to a memory that
      loses all stored information when the power is turned off.

   worst case
      In algorithm analysis, the :term:`problem instance` from among
      all problem instances for a given input size :math:`n` that has
      the greatest cost. Note that the worst case is **not** when
      :math:`n` is big, since we are referring to the worst from a
      class of inputs (i.e, we want the worst of those inputs of size
      :math:`n`).


