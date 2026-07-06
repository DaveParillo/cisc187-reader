.. _build-tools_index: 

Development tools
=================
This chapter introduces the development environment used throughout
the book and what you need to do in order to complete assignments.

Understanding the first 3 section of this chapter are critical -
all assignments are turned in using ``git`` and are 
compiled and tested using ``cmake``.
People who plan to complete assignments on a system other than
the Mesa server may find the section
:ref:`local-compile-label` useful.

.. toctree::
   :maxdepth: 2

   git-setup.rst
   git-using.rst
   compiling.rst

The remaining sections in this chapter are useful at various times
throughout the course, but you should not try to master them all
in the first week.

If you plan to work mostly on the Mesa server or the docker image then
the introduction to GNU/Linux commands and the vim text editor
are highly recommended.

.. toctree::
   :maxdepth: 2

   linux.rst
   vim.rst


The ``gcc`` and ``make`` section is purely for reference,
but does provide some insight into how software gets built
and can help remove some of the 'magic' from the build process.

.. toctree::
   :maxdepth: 2

   make.rst

You may choose to defer reading about debugging until you actually need
to use it and can treat it like a quick primer.
When you are working on project 1 is a good time to read this section.

.. toctree::
   :maxdepth: 2

   debugging.rst

