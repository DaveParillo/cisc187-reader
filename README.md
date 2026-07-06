# Intermediate Modern C++: Interactive Edition
[![sphinx-touchbook](https://img.shields.io/pypi/v/sphinx-touchbook.svg)](https://pypi.org/project/sphinx-touchbook/)
[![Docs](https://img.shields.io/github/actions/workflow/status/daveparillo/cisc187-reader/publish-docs.yml?branch=main&label=docs)](https://github.com/daveparillo/cisc187-reader/actions/workflows/publish-docs.yml)
[![License: GFDL 1.3](https://img.shields.io/badge/license-GFDL%201.3-blue.svg)](https://github.com/DaveParillo/cisc187-reader/blob/main/LICENSE.txt)

A C++ textbook based on [sphinx-touchbook](https://github.com/DaveParillo/sphinx-touchbook).

This project began with an effort to choose a suitable textbook specifically 
for students in my CISC187 C++ course.
The goals of this project are to produce a text book that:

* Covers C++ programming at the _intermediate_ level - not too basic, but not
  too advanced.
* Places an emphasis on Getting the most out of 'modern' C++ - that is C++11
  and later.
  * There are plenty of places to learn standard C or C++98.
* Is highly interactive and supports active learning.
  * Programming is not a "spectator sport".  
    It is something you do, something you participate in. 
    It makes sense, then, that the book you use to learn programming allows you
    to be active.

This book tries to provide you with an interactive experience as you learn C++.
You can read the text, watch videos, answer questions, write and run code.

# Using this book
If you simply want to check it out, read it or whatever,
then you're done.
You can see and read this book [online](https://daveparillo.github.io/cisc187-reader).

# Building this book from source
We have tried to make it easy for you to build and use this book.  
You can build it and host it yourself in just a few simple steps.

## Install and make a Python virtualenv
 
* Documentation here:  https://virtualenv.pypa.io/en/stable/
* Video here:  https://www.youtube.com/watch?v=IX-v6yvGYFg
* For the impatient:

```
$ python -m pip install venv
$ python -m venv .venv
$ source .venv
```
     
**NOTE:**

You will need to do the last command **every time** you want to work on the
book in your virtual environment.

If you have not used Python virtual environments before I strongly recommend
reading the docs or watching the video
 
With the virtual environment installed and configured you can continue.

```
$ python -m pip install ".[docs]"
$ python -m sphinx -b html src build/html
```

Open your favorite web browser and open `build/html/index.html`.

