..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

Self Check
===========
The questions in this section provide a chance to demonstrate
your understanding of the concepts discussed so far.

After reading the material in this chapter,
you should be able to answer these questions.

.. tb-blank::
   :name: begin_fitb1

   Given the following plain english statements:

   - Create a variable x with value 8
   - Create a variable y with value 5
   - Add x and y, storing the result in y

   If they were implemented as a program,
   then what value is ``y`` when finished? 

   {{blank}}

   .. tb-answer::
      :match: 13
      :feedback: Correct.
      :hint: 5; No, because the variable y is modified.
      :hint: 8; No. ``y`` is the sum of x and y, not simply ``x``.
      :hint: x; Try again.

.. tb-parsons::
   :name: begin_parson1
   :no-indent:

   Place these statements in their proper order
   so that the program prompts for input, computes the area,
   and displays the results.

   .. code-block:: c

      {{group}}
      double h = 0;
      double w = 0;
      {{endgroup}}
      {{group}}
      std::cout << "Enter height:\t";
      {{endgroup}}
      {{group}}
      std::cin >> h;
      {{endgroup}}
      {{group}}
      std::cout << "Enter width:\t";
      {{endgroup}}
      {{group}}
      std::cin >> w;
      {{endgroup}}
      {{group}}
      double area = h*w;
      {{endgroup}}
      {{group}}
      std::cout << area << '\n';
      {{endgroup}}

Fix this program so that it compiles.

.. tb-code:: cpp
   :name: begin_ac1

   int main() {
     21 = value;
     double value;

     std::cout << value << '\n';
   }

.. tb-blank::
   :name: begin_fitb2

   Given the following program:

   .. code-block:: cpp
      :linenos:

      int main() {
        int a = 7;
        int b = 4;

        if (a<=b) { 
          a = 99;
        } else {    
          int t = a;
          a = b;
          b = t;
        }
        return a;                                     
      }

   What value is returned? 

   {{blank}}

   .. tb-answer::
      :match: 4
      :feedback: Correct.
      :hint: 7; No, because the variable a is always modified in this program.
      :hint: 99; No. Since a is greater than b, the code on line 6 is never executed.
      :incorrect: Sorry, no. What is happening in the else block?

Write a program that accumulates the sum of the 
numbers 1 - 10 and prints the result.

.. tb-code:: cpp
   :name: begin_ac2

   int main() {

   }

.. tb-parsons::
   :name: begin_parson2

   When assembled in its proper order, the following program segment 
   prints 'Odd numbers:' followed by all the odd numbers from 1 - 100, one per line.

   .. code-block:: c

      {{group}}
      int main () {
      {{endgroup}}
      {{group}}
        std::cout << "Odd numbers:\n";
      {{endgroup}}
      {{group}}
        for(int num=1; num<=100; ++num) {
      {{endgroup}}
      {{distractor}}
      {{group}}
          if(num * 2 == 0) {  #distractor
      {{endgroup}}
      {{group}}
          if(num % 2 != 0) {
      {{endgroup}}
      {{group}}
            std::cout << '\t' << num << '\n';
      {{endgroup}}
      {{group}}
          }
      {{endgroup}}
      {{group}}
        }
      }
      {{endgroup}}

.. tb-choice::
   :name: begin_mc_initializing_1

   Which of the following statements represent **assignment to** a variable?  Check all that apply.


   - [ ] int a;

     This is a declaration
   - [x] a = b;

     Correct.
   - [ ] size_t sz = 10;

     This is a declaration with initialization
   - [x] cin >> a;

     This may not look like an assignment, but it is.
   - [ ] int if = a;

     Does not compile. The word 'if' is a reserved word and can't be used.

Write a program that stores your name in a local variable and then prints it.

.. tb-code:: cpp
   :name: begin_type_check
   :caption: Write a program that prints your name

   #include <iostream>

   int main() {

   }

.. tb-choice::
   :name: begin_mc_initializing_2

   Which of the following are legal variable names? Check all that apply.

   - [x] int inner_product_of_a_and_b;

     A ridiculously long, but valid name.
   - [x] double* p2;

     Correct.
   - [ ] char 1st_letter;

     A variable may not start with a number
   - [ ] long large num;

     A variable can't contain spaces or most special characters
   - [x] long double _d;

     Correct. 'long double' is a single type.

.. tb-choice::
   :name: mc_shorcut_op_1

   What are the values of x, y, and z after the following code executes?

   .. code-block:: cpp 

      int x = 0;
      int y = 1;
      int z = 2;
      --x;
      ++y;
      z+=y;

   - [ ] x = -1, y = 1, z = 4

     This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   - [ ] x = -1, y = 2, z = 3

     This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   - [ ] x = -1, y = 2, z = 2

     This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   - [ ] x = -1, y = 2, z = 2

     This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   - [x] x = -1, y = 2, z = 4

     This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.

.. tb-choice::
   :name: begin_mc_mod_1

   What is the result of 158 % 10?

   - [ ] 15

     This would be the result of 158 divided by 10.  Modulus gives you the remainder.
   - [ ] 16

     Modulus gives you the remainder after the division.
   - [x] 8

     When you divide 158 by 10 you get a remainder of 8.

.. tb-choice::
   :name: begin_mc_mod_2

   What is the result of 3 % 8?

   - [x] 3

     8 goes into 3 no times so the remainder is 3.  The remainder of a smaller number divided by a larger number is always the smaller number!
   - [ ] 2

     This would be the remainder if the question was 8 % 3 but here we are asking for the reminder after we divide 3 by 8.
   - [ ] 8

     What is the remainder after you divide 3 by 8?

.. tb-choice::
   :name: begin_mc_op_2

   What are the values of x, y, and z after the following code executes?

   .. code-block:: java 

      int x = 3;
      int y = 5;
      int z = 2;
      x = z * 2;
      y /= 2;
      ++z;

   - [ ] x = 6, y = 2.5, z = 2

     This code sets x to z * 2 (4), y to y divided by 2 (5 / 2 = 2) and z = to z + 1 (2 + 1 = 3).
   - [ ] x = 4, y = 2.5, z = 2

     Variable y must be an int, z is incremented
   - [x] x = 4, y = 2, z = 3

     Correct
   - [ ] x = 4, y = 2.5, z = 3

     This code sets x to z * 2 (4), y must be an int
   - [ ] x = 6, y = 2, z = 3

     This code sets x to z * 2 (4)

.. tb-blank::
   :name: begin_fitb3

   Given the following statement:

   .. code-block:: cpp

      double x = 2 + 2^3

   What is value stored in ``x``? 

   {{blank}}

   .. tb-answer::
      :match: 7
      :feedback: Correct.
      :hint: 10; No. ``^`` is not the exponent operator. There is no such operator in C++. It is the *exclusive or* operator.
      :hint: 64; No. ``^`` is not the exponent operator. There is no such operator in C++. It is the *exclusive or* operator.
      :hint: 3; No. The spaces here are misleading. Addition has higher precedence than exclusive or.
      :hint: x; Try again.

