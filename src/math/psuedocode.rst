..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: pseudocode

Pseudocode conventions and definitions
======================================
Some examples use 'pseudocode' to represent
program logic independent of any mainstream programming language.
When pseudocode is used, the objective is to understand the algorithm
using simplified representations.

The following notations and conventions are used.

#. Symbol names generally follow C++ snake_case conventions
#. A function is a symbol name followed by ``()``
#. Function arguments, if present, will specify a type and a symbol name.
   For example: ``int: x`` or ``array: a``.
#. The function ``print()`` denotes a function that sends its arguments
   to standard output.
   Generally, the format of the output is not important.
#. The ``operator[]`` is used in the same manner as a C or C++ array.
   Arrays are zero-based. 
   **Array overflow is still possible**.
#. Pseudo code operators:

   - ``←`` denotes assignment.
     The statement x ← y means "assign the value of y to x"
     You can also read  ``←`` as "becomes", as in "x *becomes* y"
   - ``≡`` denotes the equivalence relation.
     The statement x ≡ y means 
     or "the object x is equivalent to the object y"
   - ``⊕`` denotes the ``exclusive or`` as defined in C++.
     The statement a ← x ⊕ y means
     "the bits in the integer x are combined with the bits of y
     and the result is assigned to a" 
   - ``+`` denotes numeric addition or concatenation, depending on context.
     If a statement contains a string and a number,
     then assume the number is concatenated to the string.

#. Other math and logical operations should be interpreted as they are defined in C++.
#. Loop and conditional constructs are formatted as 
   ``keyword . . . done keyword``, for example: 

   .. code-block:: bash

      while (value < 10)
          print (value)
          value ← value + 1
      done while

      if (value ≡ x)
          print (value)
      else
          print (value)
      done if


Types without an explicit definition can be assumed as defined on first use or 
the example should explain the initial value. 




