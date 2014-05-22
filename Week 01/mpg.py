# Program to calculate gas mileage in "miles per gallon"
# based on distance traveled and gallons used.
#
# mpg = miles/gallons
#
# CSC 110
# Spring 2011

print 'This program will calculate mpg based on your input'
print
print

# input section
miles = input('How many miles did you travel? ')
gallons = input('How many gallons did you use? ')

# processing (NOTE: The float() function is covered in Section 2.7.)
mpg = miles / float(gallons)  

#output section
print 'You travelled', miles, 'miles'
print 'You used', gallons, 'gallons'
print 'Your mpg = ', mpg

# Read Section 2.8 to see how you can format the output more nicely.
