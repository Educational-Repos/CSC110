# program to calculate area and circumference of a circle
# NOTE: we import the math module so we can use the built-in definition for pi
# CSC 110
# Spring 2010

import math

print "This program will ask for the radius of a circle then calculate the area and circumference"
print
print

# get radius
radius = input('Please enter radius: ')

# do the math.  Notice the syntax for using pi
area = math.pi * radius ** 2
circumference = math.pi * radius * 2

# output results
print 'Given a circle with radius =', radius
print 'The area =', area, ' and the circumference =', circumference


# test cases, confirmed by hand
# radius of 10 produces an area = 314.159265359 and circumference =  62.8318530718
# radius of 1 gives area  = 3.14159265359 and circumference = 6.2831853078
