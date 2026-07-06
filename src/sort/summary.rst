..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Summary of sorting algorithms
=============================
As a convenience, a summary of the key characteristics
of the sorts discussed in this chapter are presented in 
the following table.

.. math::

   \begin{array}{llll}
   \textbf{Sort} &\textbf{Best Case} &\textbf{Average Case} &\textbf{Worst Case}\\
   \hline
   \textbf{Comparisons:}\\
   \textrm{Bubble}    & \Theta(n^2) & \Theta(n^2) & \Theta(n^2) \\
   \textrm{Heap}      & O(n\log(n)) & O(n\log(n)) & 2n\log(n)+O(n) \\
   \textrm{Insertion} & \Theta(n) & \Theta(n^2) & \Theta(n^2) \\
   \textrm{Merge}     & \Omega(n\log(n)) & \Theta(n\log(n)) & \Omega(n\log(n)) \\
   \textrm{Quick}     & \Theta(n) & \Theta(n\log(n)) & \Theta(n^2) \\
   \textrm{Radix}     & \Omega(n\log(n)) & \cdots & \Omega(kn) \\
   \textrm{Selection} & \Theta(n^2) & \Theta(n^2) & \Theta(n^2) \\
   \textrm{Shell}     & O(n\log(n)) & \cdots & O(n^2) \\
   \\
   \textbf{Swaps:}\\
   \textrm{Bubble}    &  0     & \Theta(n^2) & \Theta(n^2) \\
   \textrm{Heap}      & \cdots & \cdots & 2n\log(n)+O(nn)) \\
   \textrm{Insertion} &  0     & \Theta(n^2) & \Theta(n^2) \\
   \textrm{Quick}     & 0    & \Theta(n\log(n)) & \Theta(n^2) \\
   \textrm{Radix}     & k         & \Theta(d(n+k)) & \Theta(d(n+k)) \\
   \textrm{Selection} & \Theta(n) & \Theta(n) & \Theta(n) \\
   \hline
   \end{array}

.. admonition:: More to Explore

   - TBD

