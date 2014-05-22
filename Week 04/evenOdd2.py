# Even/odd program v2.
# displays whether user input is even or odd and positive or negative

# CSC 110
# Spring 2010

print "How odd is this?"

# get a user number
number = input("Please enter an integer: ")

# determine the characteristics
if number < 0:
    if number % 2 == 0:
        print '%d is a negative, even value' % number
    else:
        print '%d is a negative, odd value' % number
elif number > 0:
    if number % 2 == 0:
        print '%d is a positive, even value' % number
    else:
        print '%d is a positive, odd value' % number
else:
    print 'you entered 0'
