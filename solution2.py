#####################################################################
# @file     solution2.py
# @author   James Hind
# @date     2/11/2020
#
# @brief
#   During a routine google search to explore the intricacies of
#   Python, a message appeared saying something along the lines of
#   "You're speaking our language, would you like a challenge?"
#   After saying yes, the search page fall away revealing a terminal-
#   like interface with a story and a set of challenges.
#   These are the attempted solutions to those challenges.
#
#   google.com/foobar
#
# @detailS
#   You need to pass a message to the bunny prisoners, but to avoid detection, the
#   code you agreed to use is... obscure, to say the least. The bunnies are given 
#   food on standard-issue prison plates that are stamped with the numbers 0-9 for 
#   easier sorting, and you need to combine sets of plates to create the numbers 
#   in the code. The signal that a number is part of the code is that it is 
#   divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger 
#   numbers like 144 and 414 are a little trickier. Write a program to help 
#   yourself quickly create large numbers for use in the code, given a limited 
#   number of plates to work with.
#   
#   You have L, a list containing some digits (0 to 9). Write a function
#   solution(L) which finds the largest number that can be made from some or all 
#   of these digits and is divisible by 3. If it is not possible to make such a 
#   number, return 0 as the solution. L will contain anywhere from 1 to 9 digits.  
#   The same digit may appear multiple times in the list, but each element in the
#   list may only be used once.
#
#####################################################################


#####################################################################
# @breif    Organizes a given list of digits (up to nine) to create 
#           the largest number that is divisible by three.
# @param    L A list containing up to 9 digits
# @return   The largest integer custructed from L which is divisible
#           by 3. Each element of L is used only once.
# @return   0 if no combination is divisible by three
def solution( L ):
