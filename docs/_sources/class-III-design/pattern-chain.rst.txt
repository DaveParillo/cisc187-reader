..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   pair: design pattern; chain of responsibility

Chain of Responsibility pattern
===============================
Sometimes we need to give more than one object a chance to handle a request.
The Chain of Responsibility pattern is a 'behavioral' software design pattern. 
The goal of the pattern is to separate request senders and request handlers,
while giving more than one object a chance to handle the request.

The Chain of Responsibility design pattern allows an object to send a command 
without knowing what object will receive and handle it. 
The request is sent from one object to another making them parts of a chain and
each object in this chain can handle the command, pass it on or do both.
The most usual example of a machine using the Chain of Responsibility is the 
vending machine coin slot: rather than having a slot for each type of coin, 
the machine has only one slot for all of them. 
The dropped coin is routed to the appropriate storage place that is determined 
by the receiver of the command.

Instead of calling a single function to satisfy a request, 
multiple functions in the chain have a chance to satisfy the request.
Since the chain is effectively a list, 
it can be dynamically created,
so you could also think of it as a more general,
dynamically-built switch statement.

.. mermaid::
   :alt: chain of responsibility UML diagram

   classDiagram
      client ..> handler
      handler --> handler : next

      handler <|-- receiver1
      handler <|-- receiver2
      handler <|-- receiver3
      class handler {
         <<interface>>
         +handle()
      }
      class receiver1 {
         +handle() override
      }
      class receiver2 {
         +handle() override
      }
      class receiver3 {
         +handle() override
      }

The 'classic' implementation of the chain of responsibility implements the design
shown in the UML diagram with a handler interface and an abstract handler to encapsulate
maintenance of the chain.

.. tabbed:: cor_pattern_cppguru_tab

   .. tab:: Interface

      The Handler interface declares methods for building the chain of handlers
      and for executing a request.

      .. code-block:: cpp

         struct handler {
             virtual handler* next(handler* handler) = 0;
             virtual std::string handle(std::string request) = 0;
             virtual ~handler() = default;
         };


      The AbstractHandler manages the chain maintenance common to all handlers.

      .. code-block:: cpp

         class abstract_handler : public handler {
           private:
             handler* next_handler_ = nullptr;

           public:
             abstract_handler() : next_handler_(nullptr) {
             }
             handler* next(handler* link) override {
               next_handler_ = link;
               return link;
             }
             std::string handle(std::string request) override {
               if (next_handler_ != nullptr) {
                 return this->next_handler_->handle(request);
               }
               return {};
             }
         };

   .. tab:: Implementing classes

      All Concrete Handlers either handle a request or pass it
      to the next handler in the chain.

      .. code-block:: cpp

         struct monkey_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Banana") {
                 return "Monkey: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };

         struct squirrel_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Nut") {
                 return "Squirrel: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };

         struct dog_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Meatball") {
                 return "Dog: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };



   .. tab:: Client

      A client uses the handler to process its data.
      The client passes each item to be process to the handler one at a time,
      but it unaware that anything other than the handler is involved.

      .. code-block:: cpp

         void client(handler& food_handler) {
           std::vector<std::string> food = {"Nut", "Banana", "Cup of coffee"};
           for (const std::string &snack : food) {
             std::cout << "Client: Who wants a " << snack << "?\n";
             const std::string result = food_handler.handle(snack);
             if (!result.empty()) {
               std::cout << "  " << result;
             } else {
               std::cout << "  " << snack << " was left untouched.\n";
             }
           }
         }

         int main() {
           auto monkey = new monkey_handler;
           auto squirrel = new squirrel_handler;
           auto dog = new dog_handler;
           monkey->next(squirrel)->next(dog);

           client(* monkey);

           delete monkey;
           delete squirrel;
           delete dog;

           return 0;

         }


      However, the linked list of handlers needs to be manually constructed
      somewhere before it can be used.
      This gives users flexibility in what is included in the list,
      but requires knowledge of the internal workings of the chain which are
      better kept private.

      And the memory is the responsibility of users to clean up.

   .. tab:: Run It

      .. activecode:: ac_class_design_pattern_chain_of_responsibility_classic
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <string>
         #include <vector>

         struct handler {
             virtual handler* next(handler* handler) = 0;
             virtual std::string handle(std::string request) = 0;
             virtual ~handler() = default;
         };

         class abstract_handler : public handler {
           private:
             handler* next_handler_ = nullptr;

           public:
             abstract_handler() : next_handler_(nullptr) {
             }
             handler* next(handler* link) override {
               next_handler_ = link;
               return link;
             }
             std::string handle(std::string request) override {
               if (next_handler_ != nullptr) {
                 return this->next_handler_->handle(request);
               }
               return {};
             }
         };

         struct monkey_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Banana") {
                 return "Monkey: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };

         struct squirrel_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Nut") {
                 return "Squirrel: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };

         struct dog_handler : public abstract_handler {
             std::string handle(std::string request) override {
               if (request == "Meatball") {
                 return "Dog: I'll eat the " + request + ".\n";
               } else {
                 return abstract_handler::handle(request);
               }
             }
         };


         void client(handler& food_handler) {
           std::vector<std::string> food = {"Nut", "Banana", "Cup of coffee"};
           for (const std::string &snack : food) {
             std::cout << "Client: Who wants a " << snack << "?\n";
             const std::string result = food_handler.handle(snack);
             if (!result.empty()) {
               std::cout << "  " << result;
             } else {
               std::cout << "  " << snack << " was left untouched.\n";
             }
           }
         }

         int main() {
           auto monkey = new monkey_handler;
           auto squirrel = new squirrel_handler;
           auto dog = new dog_handler;

           monkey->next(squirrel)->next(dog);

           client(* monkey);

           delete monkey;
           delete squirrel;
           delete dog;

           return 0;

         }



The 'classic' Chain of Responsibility in the 'Gang of Four' Patterns book
does some work that is not needed - specifically the code related to creating and
managing a linked list from scratch.
The standard library provides several containers that will work just as well.

Keeping in mind that the essence of Chain of Responsibility is 
to try a number of solutions until you find one that works, 
you'll realize that the implementation of the sequencing mechanism is not 
an essential part of the pattern.

.. tabbed:: cor_pattern_refactor_tab

   .. tab:: Interface

      The interface declares methods for building the chain of handlers
      and for executing a request.

      .. code-block:: cpp

         struct food_handler {
             const std::string empty;
             virtual std::string handle(std::string request) const = 0;
             virtual ~handler() = default;
         };

      Notice the code to visit the next node has been removed and the
      abstract handler that had been used to encapsulate the linked list is
      no longer needed.


   .. tab:: Implementing classes

      The implementing classes are mostly the same. Differences:

      - Classes now inherit directly from the interface type.
      - Instead of returning the value from the next link in the chain,
        classes return an empty string if they do not handle anything.

        The string is used as an early exit condition from the chain:
        as soon as some link in the change returns a non-empty string
        the chain can return the result to the client.

      .. code-block:: cpp

         struct monkey_food_handler : food_handler {
           std::string handle(std::string request) const override {
             if (request == "Banana") {
               return "Monkey: I'll eat the " + request + ".\n";
             }
             return empty;
           }
         };
         struct squirrel_food_handler : food_handler {
           std::string handle(std::string request) const override {
             if (request == "Nut") {
               return "Squirrel: I'll eat the " + request + ".\n";
             }
             return empty;
           }
         };
         struct dog_food_handler : food_handler {
           std::string handle(std::string request) const override {
             if (request == "MeatBall") {
               return "Dog: I'll eat the " + request + ".\n";
             }
             return empty;
           }
         };

      The abstract handler class is no longer abstract and uses a vector to
      manage the handlers.
      Any iterable standard library container could be used here, but 
      :container:`vector`, :container:`array`, and :container:`list` would be
      typical choices.

      The constructor builds the chain, which is now completely private.

      The big improvement here is no the chain is responsible for managing it's own memory.
      It defers the task to :memory:`unique_ptr`, but in contrast wi the earlier example,
      all the memory needed to be managed by everyt *user* of the chain.

      .. code-block:: cpp

         class food_handlers : food_handler
         {
           std::vector<std::unique_ptr<food_handler>> chain;
           public:
             food_handlers() {
               chain.push_back(std::unique_ptr<food_handler>(new monkey_food_handler));
               chain.push_back(std::unique_ptr<food_handler>(new squirrel_food_handler));
               chain.push_back(std::unique_ptr<food_handler>(new dog_food_handler));
             }
             std::string handle(std::string food_item) const override {
               std::string reply;
               for(const auto& link: chain) {
                 reply = link->handle(food_item);
                 if(!reply.empty()) { return reply; }
               }
               return reply;
             }
         };


      No other code needs to know what classes are actually in the chain.


   .. tab:: Client

      The signature of the client function has changed slightly to reflect passing
      in a different type, but the client is essentially untouched.
      It still loops on each data item and sends each one to the handler
      for processessing.

      .. code-block:: cpp

         void client(const food_handlers& eaters) {
           std::vector<std::string> food = {"Nut", "Banana", "Cup of coffee"};
           for (const auto& snack : food) {
             std::cout << "Client: Who wants a " << snack << "?\n";
             const std::string result = eaters.handle(snack);
             if (result.empty()) {
               std::cout << ' ' << snack << " was left untouched.\n";
             } else {
               std::cout << ' ' << result;
             }
           }
         }


      The big change is in main, which no longer contains any boilerplate code
      to build individual links in the chain, or clean up after the chain.

      .. code-block:: cpp

         int main() {
           food_handlers eaters;
           client(eaters);
           return 0;
         }

   .. tab:: Run It

      .. activecode:: ac_class_design_pattern_chain_of_responsibility_refactor
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <memory>
         #include <string>
         #include <vector>

         struct food_handler {
             const std::string empty;
             virtual std::string handle(std::string request) const = 0;
             virtual ~food_handler() = default;
         };

         struct monkey_food_handler : food_handler {
             std::string handle(std::string request) const override {
               if (request == "Banana") {
                 return "Monkey: I'll eat the " + request + ".\n";
               }
               return empty;
             }
         };
         struct squirrel_food_handler : food_handler {
             std::string handle(std::string request) const override {
               if (request == "Nut") {
                 return "Squirrel: I'll eat the " + request + ".\n";
               }
               return empty;
             }
         };
         struct dog_food_handler : food_handler {
             std::string handle(std::string request) const override {
               if (request == "MeatBall") {
                 return "Dog: I'll eat the " + request + ".\n";
               }
               return empty;
             }
         };
         class food_handlers : food_handler
         {
           std::vector<std::unique_ptr<food_handler>> chain;
           public:
             food_handlers() {
               chain.push_back(std::unique_ptr<food_handler>(new monkey_food_handler));
               chain.push_back(std::unique_ptr<food_handler>(new squirrel_food_handler));
               chain.push_back(std::unique_ptr<food_handler>(new dog_food_handler));
             }
             std::string handle(std::string food_item) const override {
               std::string reply;
               for(const auto& dude: chain) {
                 reply = dude->handle(food_item);
                 if(!reply.empty()) { return reply; }
               }
               return reply;
             }
         };

         void client(const food_handlers& eaters) {
           std::vector<std::string> food = {"Nut", "Banana", "Cup of coffee"};
           for (const auto& item : food) {
             std::cout << "Client: Who wants a " << item << "?\n";
             const std::string result = eaters.handle(item);
             if (result.empty()) {
               std::cout << ' ' << item << " was left untouched.\n";
             } else {
               std::cout << ' ' << result;
             }
           }
         }

         int main() {
           food_handlers eaters;
           client(eaters);
           return 0;
         }


This fun example is adapted from Thinking in C++, Vol 2.
It uses some non-standard vocabulary to define the basic elements of the chain,
but it is still a chain of responsibility.

.. tabbed:: cor_pattern_ticpp_tab

   .. tab:: Interface

      First we define an interface each handler
      in the chain of responsibility must implement. 

      .. code-block:: cpp

         #include <iostream>
         #include <memory>
         #include <vector>

         enum class Answer { NO, YES };
          
         // This is our handler interface.
         // Every class that inherits from this
         // must implement the canIHave function
         struct GimmeStrategy {
           virtual Answer canIHave() = 0;
           virtual ~GimmeStrategy() = default;
         };
          

      Rather than a ``bool``, in this case, our early termination
      criteria is an enumerated type.


   .. tab:: Implementing classes

      For a chain to be a chain, at least two classes must implement the interface.
      (It's not much of a chain with only 1 link).

      .. code-block:: cpp

         struct AskMom : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Mommy? Can I have this?\n";
             return Answer::NO;
           }
         };
          
         struct AskDad : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Dad, I really need this!\n";
             return Answer::NO;
           }
         };
          
         struct AskGrandpa : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Grandpa, is it my birthday yet?\n";
             return Answer::NO;
           }
         };
          
         struct AskGrandma : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Grandma, I really love you!\n";
             return Answer::YES;
           }
         };

   .. tab:: Building the chain

      Much discussion related to this pattern is about how to create 
      the chain of responsibility as a linked list.
      However, when you look at the pattern it really shouldn't matter how 
      the chain is created: that's an implementation detail.
      The only important part is that *some* kind of
      :term:`iterable` type is used to visit each handler.
      How that is implemented should be invisible to users.

      While the ``Gimme`` class also is derived from the ``GimmeStrategy``
      it is used to construct the chain of all the other strategies
      used.

      .. code-block:: cpp

         class Gimme : public GimmeStrategy {
            private:
               std::vector<std::unique_ptr<GimmeStrategy>> chain;
            public:
              Gimme() {
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskMom));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskDad));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskGrandpa));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskGrandma));
              }
              Answer canIHave() {
                for (const auto& it: chain) {
                  if (it->canIHave() == Answer::YES) {
                     return Answer::YES;
                  }
                }
                // Reached end without success...
                std::cout << "Waaaaaahh!!\n";
                return Answer::NO;
              }
         };

   .. tab:: Run It

      Once the abstract and implementing classes have been defined,
      then calling the chain is easy:

      .. code-block:: cpp

         int main() {
           Gimme chain;
           chain.canIHave();
         }

      .. activecode:: ac_class_design_pattern_chain_of_responsibility_ticpp
         :language: cpp
         :compileargs: ['-Wall', '-Wextra', '-pedantic', '-std=c++20']
         :nocodelens:

         #include <iostream>
         #include <memory>
         #include <vector>

         enum class Answer { NO, YES };
          
         struct GimmeStrategy {
           virtual Answer canIHave() = 0;
           virtual ~GimmeStrategy() = default;
         };
          
         struct AskMom : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Mommy? Can I have this?\n";
             return Answer::NO;
           }
         };
          
         struct AskDad : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Dad, I really need this!\n";
             return Answer::NO;
           }
         };
          
         struct AskGrandpa : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Grandpa, is it my birthday yet?\n";
             return Answer::NO;
           }
         };
          
         struct AskGrandma : public GimmeStrategy {
           Answer canIHave() {
             std::cout << "Grandma, I really love you!\n";
             return Answer::YES;
           }
         };

         class Gimme : public GimmeStrategy {
            private:
               std::vector<std::unique_ptr<GimmeStrategy>> chain;
            public:
              Gimme() {
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskMom));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskDad));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskGrandpa));
                chain.push_back(std::unique_ptr<GimmeStrategy>(new AskGrandma));
              }
              Answer canIHave() {
                for (const auto& it: chain) {
                  if (it->canIHave() == Answer::YES) {
                     return Answer::YES;
                  }
                }
                // Reached end without success...
                std::cout << "Waaaaaahh!!\n";
                return Answer::NO;
              }
         };

         int main() {
           Gimme chain;
           chain.canIHave();
         }


-----

.. admonition:: More to Explore

   - `Chain of Responsibility Design Pattern <http://www.oodesign.com/chain-of-responsibility-pattern.html>`__ on oodesign.com
     and on :wiki:`Wikipedia <Chain-of-responsibility_pattern>`.
   - Bruce Eckel. Thinking in C++, Vol 2.,  section 3.3.10.

