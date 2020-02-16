#####################################################################
# @file     solution2.py
# @author   James Hind
# @date     2/11/2020
#
# @details
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

import itertools    # permutations()

#####################################################################
# @brief    Organizes a given list of digits (up to nine) to create 
#           the largest number that is divisible by three.
# @param    l A list containing up to 9 digits
# @return   The largest integer custructed from L which is divisible
#           by 3. Each element of L is used only once.
# @return   0 if no combination is divisible by three
def solution( l ):
    # Input Handling
    if len( l ) <= 1 or len(l) > 9:
        raise Exception( "Invalid Input: Please provide a list of up to"\
                " nine integers")

    if [x for x in l if int(x) < 0 or int(x) > 9]:
        raise Exception( "Invalid Input: All values in list must be [0-9]" )

    # Define Locals
    ltoi = lambda l: int( "".join( map( str, l ) ) )

    # Find largest integer divisible by 3. Sort list for performance
    l.sort( reverse=True )

    for r in range( len(l), 0, -1 ):
        permute = itertools.permutations( l, r )
        while True:

            try:
                res = ltoi( permute.next() )
            except StopIteration:
                break

            if res % 3 == 0:
                return res

    return 0

#####################################################################
# @brief    Executes a few test cases for `solution(L)`
# @todo     This a a bit verbose and can be cleaned up with decorators
#           to perform pass/fail eval
# @todo     Can iterate over tests cases to perform a generic number
#           of tests
def main( ):
    test1 = [3, 1, 4, 1]
    test2 = [3, 1, 4, 1, 5, 9]
    test3 = [4, 1, 4]

    try:
        solution( [] )
    except Exception as e:
        print "[Pass] Test: List Argument Empty"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Argument Empty"
        return 1

    try:
        solution( [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] )
    except Exception as e:
        print "[Pass] Test: List Argument Exceeded Allowable Length"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Argument Exceeded Allowable Length"
        return 1

    try:
        solution( [1, 22, 3] )
    except Exception as e:
        print "[Pass] Test: List Value Exceeded Maximum Value"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Value Exceeded Maximum Value"
        return 1

    try:
        solution( [1, -1, -2] )
    except Exception as e:
        print "[Pass] Test: List Value Below Minimum Value"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Value Below Minimum Value"
        return 1

    res = solution( test1 )
    if res == 4311:
        print "[Pass] Test {0} with solution {1}".format( test1, res )
    else:
        print "[Fail] Test {0} with solution {1}".format( test1, res )
        return 1

    res = solution( test2 )
    if res == 94311:
        print "[Pass] Test {0} with solution {1}".format( test2, res )
    else:
        print "[Fail] Test {0} with solution {1}".format( test2, res )
        return 1

    res = solution( test3 )
    if res == 441:
        print "[Pass] Test {0} with solution {1}".format( test3, res )
    else:
        print "[Fail] Test {0} with solution {1}".format( test3, res )
        return 1

    return 0

if __name__ == "__main__":
    if main() == 0:
        print "\n\nPASS\n\n"
    else:
        print "\n\nFAIL\n\n"


