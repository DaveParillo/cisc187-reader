..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: compiling
   single: cmake; make
   single: clang; clang-tidy; clang-format; gcc
   single: git; ssh
   single: doctest; catch2

Building software
=================
In this section we will learn one way to compile and run programs.
If you plan to use the Mesa Linux server,
then this section describes what you need to know.
If you plan to use other programs to compile and run your programs
you **still** need to review at least the section describing 
`CMake <https://cmake.org>`__.
All of the labs and projects use the *CMake* build system.

What do we really mean when we say "build software"?
A **software build** (when used as a verb)
is the process of converting a set of **text** and
related **build files** into machine-readable format.
Our job as programmers almost always boils down to converting
plain text files into something else.
A *build* often creates an executable file or a library that
can be included as part of a larger executable.
But just as often programmers convert text into some other 
form of text:

- Convert XML to HTML, for example with `XSLT <https://developer.mozilla.org/en-US/docs/Web/XSLT>`__
- Convert JSON to XML
- Convert a 
  `language independent interface definition <https://developers.google.com/protocol-buffers/docs/cpptutorial>`__
  into a language specific one
- Transpile `Java code into JavaScript <https://stackoverflow.com/a/51349655>`__

We could list more, but you get the point.
We generally do not perform these conversions manually, we use tools.

In this class we will be using a core set of tools to build and test programs:

CMake
   An open-source, cross-platform family of tools designed to build, 
   test and package software.
   CMake is used to control the software compilation process using simple platform
   and compiler independent configuration files. 
   It generates native makefiles, projects, and workspaces
   that can be used in the compiler environment of your choice.

Clang
   The Clang project provides a language front-end and tooling infrastructure for
   languages in the C language family.
   For our purposes the Clang project provides:

   - ``clang``: a C compiler
   - ``clang++``: a C++ compiler
   - ``clang-tidy``: a C++ "linter"

     A linting tools is a program that analyzes your source code statically
     (without running it) to check for possible issues or bugs.

   - ``clang-format``: a source code (re) formatter.
   - ``lldb``: a debugger.

     A debugger is a program that allows you to control and view internal
     details of your program.
     You can pause execution, view or change variables, and see source code.
     As the name implies, the tool is usually used to help find and fix bugs.


   There are many other tools in the Clang suite, but these are the ones
   you'll interact with most often.

   Clang is the default compiler on MacOS and is an option 
   on most Linux based systems.

Doctest
   `doctest <https://github.com/onqtam/doctest/blob/master/doc/markdown/tutorial.md>`__
   is a fast C++ testing framework based on the popular
   `Catch Unit Test <https://github.com/catchorg/Catch2>`__ framework.
   Most labs use doctest to assess your work as you progress through the lab.

GCC
   The GNU Compiler Collection (GCC) provides a tooling infrastructure for
   C, C++, FORTRAN, and a few other languages.
   For our purposes GCC provides:

   - ``gcc``: a C compiler
   - ``g++``: a C++ compiler
   - ``gdb``: a debugger.

   GCC is the default compiler for most Unix and Linux based systems.

Git
   `Git <https://git-scm.com>`__ is a distributed version-control system
   for tracking changes in source code during software development.
   It is designed for coordinating work among programmers,
   but it can be used to track changes in any set of files.

Make
   The ``make`` program is a tool used to help make things.
   Using *make* we define *targets* in a text file and each *target*
   runs a *recipe*. 
   Using targets and recipes in combination allows make to perform many
   complex tasks automatically.


On Linux based systems these tools work together like this:

- We use ``git`` to download the latest copy of our code.
- We use ``CMake`` to create our build files, which are generally Makefiles.
- Once the Makefile has been created, we use ``make`` to perform tasks.
  The simplest command ``make`` will try to build all the software in the
  current directory.

  Make will use either ``gcc`` or ``clang`` to actually compile code.

- Test cases are written using the ``doctest`` library and build using ``make``.

.. index:: 
   pair: ssh; secure shell
   pair: Linus Torvalds; Linux

How to access the Mesa Server
-----------------------------
All projects and some of the lab assignments are required to be handed in on the
San Diego Mesa College server **buffy**.
Access is only available using a *secure shell* client program (ssh).
There are a few ways to access the server using ``ssh``.
Unless you have a very old computer, then you already have ssh installed.

Open Git Bash, or a terminal window, or Power Shell, depending on your
operating system.
Then type the following in the *GIT Bash* to connect to the server:

.. code-block:: none

   ssh fireNN@209.129.16.61

where *fireNN** is the user name assigned to you by the instructor.


.. index:: build steps
   single: Windows System for Linux
   single: WSL

For the impatient: A quick summary
----------------------------------
Lab build files are generated using 
`CMake <https://cmake.org>`__.
Once you have a build file generated for your particular environment,
then you may compile the software and run tests.

.. note::

   All of these steps are demonstrated on a `*nix` style operating system:
   GNU/Linux, Unix, MacOS, or Cygwin on Windows.

   It also assumes you have already cloned your assignments repository.

1. First, open a terminal since all of the command that follow are typed
   on the command line.
2. Login to the Mesa server using ``ssh``.
3. Once logged in, change directory to the folder containing a lab

   For example:

   .. code-block:: none

      cd cisc187-sp23-fire40/lab01-hello

   Your fire number and semester will be different.

   If you do not have a directory starting with ``cisc187-`` 
   in your home directory then clone your repository.

4. Create a new directory to hold the build files and
   have ``cmake`` generate the makefiles:

   .. code-block:: none

      # make a directory to store build output and configure
      mkdir build
      cd build
      cmake ..

   You only need to do this step once when you make the build
   directory initially.

5. Now you can build the project:

   .. code-block:: none

      make

   and run the tests

   .. code-block:: none

      make test

That it!

There are many ways to run cmake and steps 4 and 5 above are what you commonly
see on the internet. One alternative is:

   .. code-block:: none

      # make a directory to store build output and configure
      cmake -S /path/to/lab01-hello -B build


      # build the project
      cmake --build build


      # run the tests
      cmake --build build --target test




This video demonstrates these steps and shows what normal results should look like.

.. youtube:: nQ31ApyU7_o
   :http: https


Most of the time you'll just be compiling code and running lab tests:

- `cd build`
- `make`
- `make test`

The make target ``test`` runs **all** the tests.
Usually when working on a lab, you just want to compile and test that step.
All labs are 'chunked' into steps with a separate test program to test it.

You can compile a single test step by referring to the numbered lab step,
for example:

.. code-block:: none

   make step1

You can run a single test using either the ``make`` target provided
or by running the test using the ``ctest`` program provided by ``CMake``.
for example:

.. code-block:: none

   test/step1
   ctest -R step1

Both of these commands return the exact same output.

.. index:: compiling locally
   single: IDE

.. _local-compile-label:

Compiling code on your local computer
=====================================
The following sections describe briefly how to get started with
a local development environment, if you wish.
One of the primary motivations for building locally is to avoid
a persistent internet connection running your SSH session.

If you have bad or intermittent internet connectivity,
then this section is for you.

If you plan to use the Mesa server,
then you can ignore the rest of this section.

As with all things C++, you have choices.
The options described here do not represent all of the many ways
one might build C++ programs locally, but are common choices
on Windows and MacOS machines.

In most cases, you still need to install 
`git <https://git-scm.com>`__ and
`CMake <https://cmake.org>`__.

This book does **not** explain how to install these :term:`IDE's<IDE>`.
Use the documentation provided with your IDE for that.

.. index:: 
   pair: compiling; Docker

Compiling using the CISC187 Docker image
----------------------------------------
Use git to clone your assignments repository to your computer.

The CISC187 Docker image provides an environment much like the
development environment on the Mesa server, but locally.

Currently, two compilers are installed on the image:

- GCC 14
- Clang 17

The image includes support tools, debuggers, vim plugins, and checking scripts
that are installed on the Mesa server.

.. tabbed:: tab_docker

   .. tab:: Install

      In order to use the docker image, you first need to
      `install docker <https://docs.docker.com/get-docker/>`__
      for your operating system.

      .. note:: Windows operating system requirements

         Windows 10 Professional or Enterprise is required for Docker on Windows
         using Hyper-V. 

         Docker uses a hypervisor with a VM, and the host server (your computer)
         must support virtualization.
         Since older Windows versions and Windows 10 Home edition do not support
         Hyper-V.

         For Windows Home or Education builds running under WSL2 is an option.
         See the install documentation for details.

         In any Windows build at least 4GB available RAM is recommended.

      Once docker is installed, open a Terminal window,
      or on Windows, a Powershell terminal and type:

      .. code-block:: none

         docker pull dparillo/cisc187

      This command will download the CISC187 docker image
      and make it available to run.

   .. tab:: Run

      To run the docker image on windows type:

      .. code-block:: none

         docker run --rm -it -v C:\Path\To\Source\Directory:/mnt/cisc187 dparillo/cisc187

      .. note::

         An important thing to notice is when mounting a volume with ``-v``
         on Windows, the Windows part, left of the ``:`` uses Windows
         Path separator characters (``\``), and on the Linux side, Linux
         Path separator characters are used (``/``).
         The Windows file path must include the drive letter.

      The same command on Mac or Linux:

      .. code-block:: none

         docker run --rm -it -v /path/to/source:/mnt/cisc187 dparillo/cisc187

      Meaning of these options:

      ``--rm``:
         Automatically remove the container when it exits.
         There is no need to save it.
         It is useful to think of docker containers as applications that
         perform some task and clean up when finished.
       
         One of the powerful things about this is that it is impossible
         to damage or corrupt your development environment.
         If you think you did something bad, exit the container and restart.
        
      ``-i``:
         Keep STDIN open even if not attached.
         Instead of the short ``-i``, you can use ``--interactive``.

      ``-t``:
         Allocate a pseudo TTY. This allows you to communicate with your docker
         container in the window where you started it. 
         Instead of the short ``-t``, you can use ``--tty``.

      ``-v``:
         Bind mount a volume from the local computer onto the host.
         The general syntax is ``-v /absolute/local/path:/absolute/container/path``
         Instead of the short ``-v``, you can use ``--volume``.

         The idea here is that your source code is never really inside the docker container.
         Your source code is separate, but visible to the running container.

      The container mount point was not chosen at random.
      The container is set up with ``/mnt/cisc187`` as the *WORKDIR*.
      When the container starts, you start in this directory.

      The run command has `many more options available <https://docs.docker.com/engine/reference/commandline/run/>`__
      and docker has many more commands other than the run command,
      but this is all you need to know to compile assignments.

Once the CISC187 docker container is running
you are ready to compile an assignment.
Builds are exactly the same as on the Mesa server:

.. code-block:: none

   mkdir build
   cd build
   cmake ..
   make
   make test

.. index:: 
   pair: compiling; Visual Stidio

Compiling with Visual Studio
----------------------------
In this course you need to be using Visual Studio 2022
at a minimum to complete all the assignments.

In order to enable CMake integration with Visual Studio
ensure you have the additional
`C++ CMake tools for Windows <https://learn.microsoft.com/en-us/cpp/build/cmake-projects-in-visual-studio?view=msvc-170>`__ installed.

Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

.. tabbed:: tab_msvc

   .. tab:: GUI

      These instructions describe how to build software using the
      Visual Studio Graphical User Interface (GUI).

      1. Open the windows file explorer and go to the location where
         you cloned your repository.
      2. Right-click on the lab you want to build, for example
         ``lab01-hello``.

         Do **not** open the entire cloned repository.

      3. Select 'Open in Visual Studio'

   .. tab:: Terminal

      These instructions describe how to build software using the
      Using the Visual Studio command line

      1. Create a directory named build adjacent, but **not in** your source directory.
      2. Open the Visual Studio Developer prompt.
         `cd` into the build directory created in the previous step.
      3. Type `cmake ..`

         This should create a standard Visual Studio solution that
         you can run from the command line or the IDE.

      4. Type `MSBuild lab1.sln` to build all projects in the **Debug** configuation
      5. Type `ctest -C Debug` to run all tests


      To remove all executable files:

      .. code-block:: none

         MSBuild lab1.sln -target:Clean
         MSBuild lab1.sln -t:Clean

      To build a single test:

      .. code-block:: none
         
         MSBuild lab1.sln -t:step1

      To build all files in **Release** configuration,
      without any Debug symbols:

      .. code-block:: none

         MSBuild lab1.sln -p:Configuration=Release
         # run tests
         ctest -C Release

      If this doesn't work, try
      `the instructions on the Microsoft site <https://docs.microsoft.com/en-us/cpp/build/walkthrough-compiling-a-native-cpp-program-on-the-command-line?view=vs-2019>`__


.. index:: 
   pair: compiling; Code Blocks

Compiling with Code Blocks
--------------------------
Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

1. Create a directory named build and open CMake GUI.
2. Select 'Browse Source' and select the folder containing 
   the lab you want to build.
3. Select 'Browse Build' and select the `build` folder.
4. In the lower left corner, select 'Configure' and
   select 'CodeBlocks - MinGW Makefiles' from the list of
   available generators.

   Leave the radio selections alone and
   press 'Finish` when done.

   Campus windows computers may complain about a `sh.exe` program in your path
   outside of CodeBlocks.
   To fix this error:

   - Delete the CMake variable `CMAKE_SH` in the variables list.
   - Press 'Configure' a second time.

5. Press 'Generate'. When finished ("Generating done")
   close CMake GUI.
6. Open the generated "CBP" file in CodeBlocks.
   It should be in the build folder you pointed at in step 3.

Build the 'all' target to compile and link programs and tests.
Test cases must be run individually - 
there is no target to run all the tests.

.. index:: 
   pair: compiling; Xcode
   pair: compiling; MacOS

Compiling with Xcode
--------------------
Use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

Open a terminal in the directory containing your lab, then:

.. code-block:: none

   mkdir build
   cd build
   cmake -G Xcode ..

Open the Xcode project and build as usual.

.. index:: 
   pair: compiling; Linux

Compiling on Linux
------------------
Use git to clone your assignments repository to your computer.

You'll need to install a C++ tool chain,
the details tend to vary by distribution, however,
most Linux distributions have good documentation for installing C++ tools.
The only thing you should verify is that your distro has a modern version
of a C++ compiler (C++14 at a minimum) available.
The GNU Compiler Collection (GCC) or Clang are preferred.

Once you have a tool chain installed,
use git to clone your assignments repository to your computer.
Now you are ready to compile an assignment.

The process is exactly the same as on the Mesa server.
Open a terminal in the directory containing your lab, then:

.. code-block:: none

   mkdir build
   cd build
   cmake ..
   make
   make test


Which option should I choose?
-----------------------------
There are a lot of options and the choices can be confusing.
The short answer is that there is no wrong choice.
Also, you can change you mind at any time and even
shift from one compile option to another as you prefer.

So how are these options really different from each other?

#. The **I** in IDE stands for *integrated*
   They frequently include a large collection of tools to help
   with many tasks professional programmers encounter often.

   For this reason they tend to be large and use 
   a fair amount of CPU and memory.

#. Accessing a remote server like buffy requires minimal
   CPU and memory locally.
   Most of the resources you are using are on the remote server.
   It is also the easiest to access.
   All the software you need is already installed on the server.
   You only need an ssh client.

   The main drawbacks are:

   - You have no control over the environment - you don't own the server.
   - Using the remote server requires good internet.
     If you lose your internet for any reason,
     then you will lose your connection.

#. Docker blends the two previous choices.
   You get a local server separate from your computer that has
   everything you need installed.
   It uses less resources than a typical IDE and if needed
   you can limit the resources it uses and like a local IDE,
   does not require persistent internet to work.
   Also, if you want you can modify the docker image
   and make your own custom version.

   The main drawbacks are:

   - After installing Docker there is anew persistent service
     running on your computer.
   - It is still not a real replacement for an IDE.

This decision chart may help.


.. digraph:: choices
   :align: center
   :alt: Choosing a build system

   node [fontname = "Bitstream Vera Sans", fontsize=14,
         style=filled, fillcolor=lightblue,
         shape=rect
   ]
  
   ide [
       label = "Already\nhave your\nown IDE?"
       shape = diamond
   ]
   ide_chain [
       label = "Your\nIDE grocks cmake\n& git?"
       shape = diamond
   ]
     
   simple [
       label = "Crave\nsimplicity?"
       shape = diamond
   ]
     
   docker [
       label = "Interested\nin docker?"
       shape = diamond
   ]
     
   cpu [
       label = "Computer can\nrun docker?"
       shape = diamond
   ]
     
   node [fillcolor="wheat"]
     
   git [
       label = "Install git"
   ]
   git2 [
       label = "Install git"
   ]
   cmake [
       label = "Install cmake"
   ]
   use_buffy [
       label = "Use buffy"
   ]
   use_docker [
       label = "Use docker"
   ]
   use_ide [
       label = "Use your IDE"
   ]


   ide -> ide_chain [ label = "Yes" ];
   ide_chain -> use_ide [ label = "Yes" ];
   ide_chain -> git [ label = "No"];
   ide_chain -> cmake [ label = "No"];
   ide -> simple [ label = "No" , constraint = false];
   simple -> docker [ label = "No" ];
   simple -> git2 [label="Yes",  constraint=false];
   git2 -> use_buffy;
   docker -> cpu [label="Yes"]
   docker -> use_buffy [label="No", constraint=false];
   docker->use_docker [style=invis, weight=0];
   cpu -> use_docker [ label = "Yes"];
   cpu:e -> use_buffy [ label = "No", constraint=false]
   cmake -> use_ide
   git -> use_ide




-----

.. admonition:: More to Explore

   - :wiki:`Sofware build <Software_build>`
   - `Git Documentation <https://git-scm.com/doc>`__
   - Clang docs

     - `clang-tidy <https://clang.llvm.org/extra/clang-tidy/>`__
     - `clang format <https://clang.llvm.org/docs/ClangFormat.html>`__
     - `Clang C++ status <https://clang.llvm.org/cxx_status.html>`__
   
   - :doc:`make`
   - :wiki:`Grok definition <Grok>`


