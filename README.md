# Google Foobar

## Table of Contents

  1. [Introduction](#Introduction)
  2. [Foobar Process](#foobar-process)
  3. [Generating Documentation](#generating-documentation)

## Introduction

During a routine google search to explore various programming concepts, 
a message appeared saying something along the lines of "You're speaking 
our language, would you like a challenge?" After saying yes, the search 
page falls away revealing a terminal-like interface with a story and a 
set of challenges. These are the attempted solutions to those challenges.

This is not meant to be used as a guide for anyone undergo the challenge,
please leave this project if that is the case. This is simply a workspace
to test ideas before submitting them as solutions.

google.com/foobar

## Foobar Process

The challenge erects an entertaining story about infiltrating Commander 
Lambda's forces to prevent him from destroying the Bunny Planet. There
are 5 levels to the challenge, with each level presenting progressively
harder programming challenges. Once a challenge is requested, you are
given a time limit (a generous one, however) and, a assume, there are
no retries. There is a utility built into the emulated terminal to
test your solution and one to submit it. If it passes the test suite
set up behind the scene, you are sent to the next level.

The challenges can be undertaken in both Java and Python 2.7. My solutions
will be done in Python as I am much more comfortable in that language.

    - Level 1:

      Challenge 1: 48 Hour time limit 

    - Level 2:

      Challenge 1: 72 Hour time limit

      Challenge 2: 72 Hour time limit

## Verification and Testing

The terminal for Google foobar give you two commands, `verify` and `submit`.
The verify command runs your solution through a set of test cases (of which you
are only shown a selection) then tells you if it passes or fails, the submit 
button does the same thing but is final. 

Since it is much easier for me to have vim and the ability to execute at will, 
I tended to write the code on my own system and then copy it over to Google's. 
Because of this you will see some test code built into the solution modules. If 
you are looking for examples of code verification, Start with the later programs as
my procedures got increasingly better as I went through the challenges and got
tired of repeating myself.

## Generating Documentation

If you would like to use Doxygen to review the documentation:

```bash
sudo apt-get install doxygen graphviz
cd ~/path/to/this/repo
doxygen
firefox ./doc/html/index.html &
```

