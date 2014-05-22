# Even/odd program displays whether user input is even or odd

# CSC 110
# Spring 2010

print "How odd is this?"

# get a user number
number = input("Please enter an integer: ")

# test for even
if number % 2 == 0:
    print '%d is even' % number
else:
    print '%d is odd' % number
