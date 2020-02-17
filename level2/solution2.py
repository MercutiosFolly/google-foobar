#####################################################################
# @file     level2/solution2.py
# @author   James Hind
# @date     2/15/2020
#
# @details
#   As Commander Lambda's personal assistant, you've been assigned the task of 
#   configuring the LAMBCHOP doomsday device's axial orientation gears. It should
#   be pretty simple - just add gears to create the appropriate rotation ratio. But
#   the problem is, due to the layout of the LAMBCHOP and the complicated system of 
#   beams and pipes supporting it, the pegs that will support the gears are fixed 
#   in place.
#   
#   The LAMBCHOP's engineers have given you lists identifying the placement of
#   groups of pegs along various support beams. You need to place a gear on each 
#   peg (otherwise the gears will collide with unoccupied pegs). The engineers have 
#   plenty of gears in all different sizes stocked up, so you can choose gears of 
#   any size, from a radius of 1 on up. Your goal is to build a system where the 
#   last gear rotates at twice the rate (in revolutions per minute, or rpm) of the 
#   first gear, no matter the direction. Each gear (except the last) touches and 
#   turns the gear on the next peg to the right.
#   
#   Given a list of distinct positive integers named pegs representing the location
#   of each peg along the support beam, write a function solution(pegs) which, if 
#   there is a solution, returns a list of two positive integers a and b 
#   representing the numerator and denominator of the first gear's radius in its 
#   simplest form in order to achieve the goal above, such that radius = a/b. The 
#   ratio a/b should be greater than or equal to 1. Not all support configurations 
#   will necessarily be capable of creating the proper rotation ratio, so if the 
#   task is impossible, the function solution(pegs) should return the list [-1, -1].
#   
#   For example, if the pegs are placed at [4, 30, 50], then the first gear could
#   have a radius of 12, the second gear could have a radius of 14, and the last one
#   a radius of 6. Thus, the last gear would rotate twice as fast as the first one. 
#   In this case, pegs would be [4, 30, 50] and solution(pegs) should return [12, 1].
#   
#   The list pegs will be given sorted in ascending order and will contain at least
#   2 and no more than 20 distinct positive integers, all between 1 and 10000 inclusive.
#
#####################################################################

import functools    # @functools.wraps()
import fractions    # Fraction()

#####################################################################
# @brief    Given a List of gear heights, finds the radius of the first
#           gear such that the final gear will rotate twice as fast
# @details
#   Given
#       {x_1,...,x_n} are the heights of the gear centroids
#       {y_1,...,y_1} are the radii of gears 1,...,n
#
#       The equation for the radius of the final gear:
#  (1)  y_n = y_1 / 2
#
#       Calculating the radii of all other gears:
#  (2)  y_(i-1) = [ x_i - x_(i-1) ] - y_i, for 1 < i <= n
#
#       Using the contraint (1) on (2) and extrapolating:
#       y_(n-1) = [ x_n - x_(n-1) ] - y_n
#   =>  y_(n-1) = [ x_n - x_(n-1) ] - y_1 / 2
#
#       y_(n-2) = [ x_(n-1) - x_(n-2) ] - y_(n-1)
#   =>  y_(n-2) = [ x_(n-1) - x_(n-2) ] - ( [ x_n - x_(n-1) ] - y_1 / 2 )
#   =>  y_(n-2) = [ -x_n + 2*x_(n-1) - x_(n-2) ] + y_1 / 2
#
#       y_(n-3) = [ x_(n-2) - x_(n-3) ] - y_(n-2)
#   =>  y_(n-3) = [ x_(n-2) - x_(n-3) ] - ( [ -x_n + 2*x_(n-1) - x_(n-2) ] + y_1 / 2 )
#   =>  y_(n-3) = [ x_n - 2*x_(n-1) + 2*x_(n-2) - x_(n-3) ] - y_1 / 2
#
#       We obtain the following equation for determining the radius of gear 1:
#       y_1 = [ (-1)^n * x_n + SUM{ (-1)^(i) * 2*x_i , 1 < i < n } - x_1 ] - (-1)^n * y_1 / 2
# (3)=> y_1 = 2/(2 + (-1)^n) * [ (-1)^n * x_n + SUM{ (-1)^(i) * 2*x_i , 1 < i < n } - x_1 ]
#
#       A negative solution of y_1 is invalid, indicating there is no solution
#       to the peg configuration
#
# @param pegs       A list containing at least 2 and no more than 20 distinct
#                   positive integers between 1 and 10000, representing height.
# @return [a,b]     The radius (a/b >= 1) of the first gear such that the final
#                   gear can be made to rotate twice as fast as the first.
# @return [-1,-1]   If there exists no configuration such that the final
#                   gear can rotate twice as fast as the first
# @todo             Exit function as soon as invalid occurs to save time
# @todo             Since we're back in 2.7, xrange is probably the better option
# @note             Tricky one. Had me scratching my head until I dug through
#                   `fractions` for That limit_denominator().
def solution(pegs):
    # Input Handling
    pegs.sort()
    if len( pegs ) < 2 or len( pegs ) > 20:
        raise Exception( "Invalid Input: List must contain at least"\
                " 2 and no more than 20 entries" )

    if [x for x in pegs if int(x) < 1 or int(x) > 10000]:
        raise Exception( "Invalid Input: All values in list must be"\
                " between 1 and 10000, inclusive" )

    # Implementation of equation (3) of the details section
    radii = [-1]
    n = len(pegs)
    coef = 2. / (2. + (-1)**n)
    radii[0] = coef * ( (-1)**n * pegs[n-1]
                    + float(sum( [(-1)**(i) * 2 * x for i,x in enumerate(pegs,1) if 1 < i < n] ))
                    - pegs[0] )

    for i in range( n - 1 ):
        radii.append( pegs[i+1] - pegs[i] - radii[i] )

    # Perform Validity Checks
    flag_invalid = False

    if radii[0] < 1. or radii[0] > pegs[1] - pegs[0] - 1.:
        flag_invalid = True

    for i in range( 0, n-2 ):
        if ( radii[i+1] < 1. or radii[i+1] > pegs[i+1] - pegs[i] - 1. or 
                radii[i+1] > pegs[i+2] - pegs[i+1] - 1 ):
            flag_invalid = True

    if ( radii[-1] < 1. or radii[-1] > pegs[-1] - pegs[-2] - 1. ):
        flag_invalid = True

    # Translate Data to Proper Form
    if not flag_invalid:
        try:
            firstRadiusFraction = fractions.Fraction( radii[0] ).limit_denominator()
            num, den = firstRadiusFraction.numerator, firstRadiusFraction.denominator
        except OverflowError:
            num, den = -1, -1
        except ValueError:
            num, den = -1, -1
    else:
        num, den = -1, -1

    return [num, den]

#####################################################################
# @brief    decorator for test cases
# @param 1  The name of the test being performed
# @param 2  A list containing the input to the solution fn as the
#           first entry and the expected result of the solution fn as
#           the second
def tester( func ):
    @functools.wraps( func )
    def wraps( *args, **kwargs ):
        res = func( args[1][0] )
        if res == args[1][1]:
            print "[Pass] Test {0}: {1}".format( args[0], args[1][0])
            print "\tResult vs. Expected: {0} = {1}\n".format( res, args[1][1] )
            return 0
        else:
            print "[Fail] Test {0}: {1}".format( args[0], args[1][0] )
            print "\tResult vs. Expected: {0} = {1}\n".format( res, args[1][1] )
            return 1
    return wraps

#####################################################################
# @brief    Executes a few test cases for `solution( pegs )`
def main( ):

    # Declare Tests: { "Test Name": [ [Input List], [Expected Result] ] }
    # These will be iterated over so no need to change anything else
    tests = { "test1": [ [4, 30, 50], [12,1] ],
              "test2": [ [4, 17, 50], [-1,-1] ],
              "test3": [ [11, 53, 72, 94], [30,1] ],
              "test4": [ [22, 78], [112, 3] ] }

    # Decorate solution with the tester
    solTest = tester( solution )

    flag_fail = False

    # Perform Input Handling Tests
    print "\nInput Handling Tests\n"
    try:
        solution( [1] )
    except Exception as e:
        print "[Pass] Test: List Size (Small)"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Size (Small)"
        flag_fail = True
    print

    try:
        solution( [10]*21 )
    except Exception as e:
        print "[Pass] Test: List Size (Large)"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Size (Large)"
        flag_fail = True
    print

    try:
        solution( [10001, 1, 2] )
    except Exception as e:
        print "[Pass] Test: List Contains Invalid Value (Large)"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Contains Invalid Value (Large)"
        flag_fail = True
    print

    try:
        solution( [5, -1, 2] )
    except Exception as e:
        print "[Pass] Test: List Contains Invalid Value (Small)"
        print "\tException Caught( {0} )".format( str(e) )
    else:
        print "[Fail] Test: List Contains Invalid Value (Small)"
        flag_fail = True
    print

    # Perform Functional Tests
    print "\nFunction Tests\n"
    for key,val in tests.items():
        res = solTest( key, val )
        if res != 0:
            flag_fail = True

    # Try other test cases
    #pegs = [11, 53, 72, 94]
    #print "Testing: {}".format( pegs )
    #print solution( pegs )

    if flag_fail:
        return 1

    return 0

#####################################################################
if __name__ == "__main__":
    if main() == 0:
        print "\n\nPASS\n\n"
    else:
        print "\n\nFAIL\n\n"


