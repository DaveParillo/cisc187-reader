..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".
.. This file is adapted from the OpenDSA eTextbook project. See
.. http://opendsa.org for more details.
.. Copyright (c) 2012-2020 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. index::
   single: factorial

Selected functions
==================
**Factorial**
The factorial function, written :math:`n!` for :math:`n` an
integer greater than 0, is the product of
the integers between 1 and :math:`n`, inclusive.
Thus, :math:`5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120`.
As a special case, :math:`0! = 1`.

.. math::

   \begin{aligned}
   &&  0! = 1 \\
   &&  n! = n \cdot (n-1)!\end{aligned}

.. note::
   Factorial is usually denoted with the symbol :math:`!`, which is not to
   be confused with the C++ logical operator ! which means NOT.

   Notice that when used to negate a boolean, the ``!``
   appears *before* the operand, while
   factorial appears *after* the operand.

The factorial function grows quickly as :math:`n` becomes larger.
Because computing the factorial function directly is a time-consuming
process, it can be useful to have an equation that provides a
good approximation.
Stirling's approximation states that
:math:`n! \approx \sqrt{2\pi n}(\frac{n}{e})^n`,
where :math:`e \approx 2.71828`
(:math:`e` is the base for the system of natural logarithms) [#]_.
Thus we see that while :math:`n!` grows
slower than :math:`n^n` (because :math:`\sqrt{2\pi n}/e^n < 1`),
it grows faster than :math:`c^n` for any positive integer constant
:math:`c`.

.. index::
   single: logic notation

**Logic notation**
We will occasionally make use of the notation of symbolic or boolean
logic.
:math:`A \Rightarrow B` means ":math:`A` implies :math:`B`" or
"If :math:`A` then :math:`B`".
:math:`A \Leftrightarrow B` means ":math:`A` if and only if :math:`B`"
or ":math:`A` is equivalent to :math:`B`".
:math:`A \vee B` means ":math:`A` or :math:`B`"
(useful both in the context of symbolic
logic or when performing a boolean operation).
:math:`A \wedge B` means ":math:`A` and :math:`B`".
:math:`\sim\!A` and :math:`\overline{A}` both mean "not :math:`A`" or
the negation of :math:`A` where :math:`A` is a boolean variable.

.. index::
   single: floor function
   single: ceiling function

**Floor and ceiling**
The :term:`floor` of :math:`x` (written :math:`\lfloor x \rfloor`)
takes real value :math:`x` and returns the greatest 
integer :math:`\leq x`.
For example, :math:`\lfloor 3.4 \rfloor = 3`,
as does :math:`\lfloor 3.0 \rfloor`, 
while :math:`\lfloor -3.4 \rfloor = -4` and
:math:`\lfloor -3.0 \rfloor = -3`.
The :term:`ceiling` of :math:`x` (written
:math:`\lceil x \rceil`) takes real value :math:`x` and returns the
least integer :math:`\geq x`.
For example, :math:`\lceil 3.4 \rceil = 4`, as does
:math:`\lceil 4.0 \rceil`,
while :math:`\lceil -3.4 \rceil = \lceil -3.0 \rceil = -3`.

.. [#] The symbol ":math:`\approx`" means "approximately equal."

.. admonition:: More to Explore

   - From cppreference.com

     - :numeric:`Common math functions <math>`
     - :lang:`types` - including ``bool``
     - :cmath:`floor` and :cmath:`ceil`


.. topic:: Acknowledgements

   This section is adapted from 
   `Open Data Structures (OpenDSA) <https://opendsa-server.cs.vt.edu>`__
   by Ville Karavirta and Cliff Shaffer
   which is distributed under the `MIT License <https://github.com/OpenDSA/OpenDSA/blob/master/MIT-license.txt>`__.



