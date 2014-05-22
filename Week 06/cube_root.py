
# Sample program illustrating programmer-defined functions
# along with code that calls the functions
#
# The 'cube_root' function uses a 'return' statement.  Its
# only job is to calculate and "return" the cube root of a
# number.  It does not print anything.  Notice that statements
# that "call" the 'cube_root' function need to USE the value
# returned.  They can do this by a) saving it in a variable,
# b) using it in a 'print' statement, or c) using the value in
# ANY general expression.  Imagine that the value returned by
# the function REPLACES the function call wherever it occurs.
# This is EXACTLY the same way you use built-in functions like
# 'input()', 'abs()', 'round()', etc.
#
# The 'show_table' function does NOT use a 'return' statement.
# It's job is to PRINT a table.  Different functions may be
# used in different ways.
#
# CSC 110
# Spring, 2011

# The cube_root function calculates and RETURNS the cube root
# of a number.  The value of 'x' must not be negative.
def cube_root(x):
    result = x ** (1.0/3.0)
    return result

# Main program
def main():
    print 'Let\'s examine the cube roots of some numbers.\n'

    # CALL the function and save the value returned in a variable:
    num = 27
    root = cube_root(num)  # The ARGUMENT is a variable
    print 'The cube root of %d is %.1f' % (num, root)
    root = cube_root(num + 98)  # The argument is an expression
    print root

    # Use the function call directly in a 'print' statement:
    print 'The cube root of %d is %.1f' % (num, cube_root(num))

    # Use multiple function calls in an expression:
    print 'The answer is', cube_root(8) + cube_root(1000) / 2

    # Here is a table of some cube roots:
    print
    print ' n\tcube_root(n)'  # print header row
    print '%.1f\t%.3f' % (8, cube_root(8))
    print '%.1f\t%.3f' % (31, cube_root(31))
    print '%d\t%.3f' % (1727, cube_root(1727))
    print '%d\t%.3f' % (1728, cube_root(1728))
    print '%d\t%.3f' % (1729, cube_root(1729))

    # Here are a couple of longer tables:
    show_table(0, 1000, 10)
    show_table(42875, 1000000, 20)

# This function shows a table of cube roots.
# The first two parameters are the minimum and maximum values for 'n'.
# The third parameter is the number of rows to show in the table.
def show_table(minN, maxN, rows):
    # Calculate the step size.  There are (rows - 1) intervals:
    step = (maxN - minN) / (rows - 1.0)
    
    print '\n       n     cube_root(n)'  # print header row
    
    # Loop 'rows' times to print the rows in the table:
    for i in range(rows):
        n = minN + i * step  # calculate the value of 'n' for row 'i'
        print '%12.3f %8.3f' % (n, cube_root(n))
 

# Run the program
main()
