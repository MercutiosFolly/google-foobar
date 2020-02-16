#####################################################################
# @file     solution1.py
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
#####################################################################

#####################################################################
# @brief    Parse a list to remove any entry that occurs more than "n" times
#           while preserving the list order
# @param data   List to parse through
# @param n      The threshold at which to remove entries
# @return       A list with all entries occuring more than "n" times removed
def solution( data, n ):
    # determine all the entries in data that appear more than n times
    # add them to a list so we can remove them later
    remove_list = []
    for i in data:
        if i not in remove_list:
            count = 0
            for j in data:
                if i == j:
                    count += 1
                if count > n:
                    remove_list.append( i )
                    break
    # We now have a list of items to remove from data. Return a list
    # with all occurrences of these entries removed from data.
    return [ y for y in data if y not in remove_list ]
