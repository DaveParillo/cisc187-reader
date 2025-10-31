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

.. fillintheblank:: begin_fitb1

   Given the following plain english statements:

   - Create a variable x with value 8
   - Create a variable y with value 5
   - Add x and y, storing the result in y

   If they were implemented as a program,
   then what value is ``y`` when finished? 

   - :13: Correct.
     :5: No, because the variable y is modified.
     :8: No. ``y`` is the sum of x and y, not simply ``x``.
     :x: Try again.

.. parsonsprob:: begin_parson1
   :adaptive:
   :noindent:
   :language: c

   Place these statements in their proper order
   so that the program prompts for input, computes the area,
   and displays the results.
   -----
   double h = 0;
   double w = 0;
   =====
   std::cout << "Enter height:\t";
   =====
   std::cin >> h;
   =====
   std::cout << "Enter width:\t";
   =====
   std::cin >> w;
   =====
   double area = h*w;
   =====
   std::cout << area << '\n';
 

.. activecode:: begin_ac1
   :language: cpp
   :compileargs: ['-Wall', '-std=c++20']
   :nocodelens:
 
   Fix this program so that it compiles.

   ~~~~
   int main() {
     21 = value;
     double value;

     std::cout << value << '\n';
   }

.. fillintheblank:: begin_fitb2

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

   - :4: Correct.
     :7: No, because the variable a is always modified in this program.
     :99: No. Since a is greater than b, the code on line 6 is never executed.
     :.*: Sorry, no. What is happening in the else block?


.. activecode:: begin_ac2
   :language: cpp
   :compileargs: ['-Wall', '-std=c++20']
   :nocodelens:

   Write a program that accumulates the sum of the 
   numbers 1 - 10 and prints the result.

   ~~~~
   int main() {

   }

.. parsonsprob:: begin_parson2
   :adaptive:
   :language: c

   When assembled in its proper order, the following program segment 
   prints 'Odd numbers:' followed by all the odd numbers from 1 - 100, one per line.
   -----
   int main () {
   =====
     std::cout << "Odd numbers:\n";
   =====
     for(int num=1; num<=100; ++num) {
   =====
       if(num * 2 == 0) {  #distractor
   =====
       if(num % 2 != 0) {
   =====
         std::cout << '\t' << num << '\n';
   =====
       }
   =====
     }
   }


.. mchoice:: begin_mc_initializing_1
   :multiple_answers:
   :correct: b,d
   :answer_a: int a;
   :answer_b: a = b;
   :answer_c: size_t sz = 10;
   :answer_d: cin >> a;
   :answer_e: int if = a;
   :feedback_a: This is a declaration
   :feedback_b: Correct.
   :feedback_c: This is a declaration with initialization
   :feedback_d: This may not look like an assignment, but it is.
   :feedback_e: Does not compile. The word 'if' is a reserved word and can't be used.

   Which of the following statements represent **assignment to** a variable?  Check all that apply.


.. activecode:: begin_type_check
   :language: cpp
   :compileargs: ['-Wall', '-std=c++20']
   :caption: Write a program that prints your name
   :nocodelens:

   Write a program that stores your name in a local variable and then prints it.

   ~~~~
   #include <iostream>

   int main() {

   }

.. mchoice:: begin_mc_initializing_2
  :multiple_answers:
  :correct: a,b,e
  :answer_a: int inner_product_of_a_and_b;
  :answer_b: double* p2;
  :answer_c: char 1st_letter;
  :answer_d: long large num;
  :answer_e: long double _d;
  :feedback_a: A ridiculously long, but valid name.
  :feedback_b: Correct.
  :feedback_c: A variable may not start with a number
  :feedback_d: A variable can't contain spaces or most special characters
  :feedback_e: Correct. 'long double' is a single type. 

  Which of the following are legal variable names? Check all that apply.

.. mchoice:: mc_shorcut_op_1
   :answer_a: x = -1, y = 1, z = 4
   :answer_b: x = -1, y = 2, z = 3
   :answer_c: x = -1, y = 2, z = 2
   :answer_d: x = -1, y = 2, z = 2
   :answer_e: x = -1, y = 2, z = 4
   :correct: e
   :feedback_a: This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   :feedback_b: This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   :feedback_c: This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   :feedback_d: This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.
   :feedback_e: This code subtracts one from x, adds one to y, and then sets z to to the value in z plus the current value of y.

   What are the values of x, y, and z after the following code executes?

   .. code-block:: cpp 

      int x = 0;
      int y = 1;
      int z = 2;
      --x;
      ++y;
      z+=y;

.. mchoice:: begin_mc_mod_1
   :answer_a: 15
   :answer_b: 16
   :answer_c: 8
   :correct: c
   :feedback_a: This would be the result of 158 divided by 10.  Modulus gives you the remainder.
   :feedback_b: Modulus gives you the remainder after the division.
   :feedback_c: When you divide 158 by 10 you get a remainder of 8.  

   What is the result of 158 % 10?

.. mchoice:: begin_mc_mod_2
   :answer_a: 3
   :answer_b: 2
   :answer_c: 8
   :correct: a
   :feedback_a: 8 goes into 3 no times so the remainder is 3.  The remainder of a smaller number divided by a larger number is always the smaller number!
   :feedback_b: This would be the remainder if the question was 8 % 3 but here we are asking for the reminder after we divide 3 by 8.
   :feedback_c: What is the remainder after you divide 3 by 8?  

   What is the result of 3 % 8?

.. mchoice:: begin_mc_op_2
   :answer_a: x = 6, y = 2.5, z = 2
   :answer_b: x = 4, y = 2.5, z = 2
   :answer_c: x = 4, y = 2, z = 3
   :answer_d: x = 4, y = 2.5, z = 3
   :answer_e: x = 6, y = 2, z = 3
   :correct: c
   :feedback_a: This code sets x to z * 2 (4), y to y divided by 2 (5 / 2 = 2) and z = to z + 1 (2 + 1 = 3).
   :feedback_b: Variable y must be an int, z is incremented
   :feedback_c: Correct
   :feedback_d: This code sets x to z * 2 (4), y must be an int
   :feedback_e: This code sets x to z * 2 (4)

   What are the values of x, y, and z after the following code executes?

   .. code-block:: java 
 
      int x = 3;
      int y = 5;
      int z = 2;
      x = z * 2;
      y /= 2;
      ++z;

.. fillintheblank:: begin_fitb3

   Given the following statement:

   .. code-block:: cpp

      double x = 2 + 2^3
 
   What is value stored in ``x``? 

   - :7: Correct.
     :10: No. ``^`` is not the exponent operator.
          There is no such operator in C++.
          It is the *exclusive or* operator.
     :64: No. ``^`` is not the exponent operator.
          There is no such operator in C++.
          It is the *exclusive or* operator.
     :3: No. The spaces here are misleading.
         Addition has higher precedence than exclusive or.
     :x: Try again.



