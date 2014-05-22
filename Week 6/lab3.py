# Lab 3 starter code
# Lab Activity -- Functions

# Chun-Wei Chen
# CSC 110.03
# Spring 2010 5/10

# part 1
# this program calls the function three times and displays results of
# area = height / 2.0 * (base1 + base2)

import math

print 'base1\tbase2\theight\tarea'
def main():
    # put your function calls here
    print '4.00\t5.00\t8.00\t%.2f' %areaTrapezoid(4.0, 5.0, 8.0)
    print '2.00\t7.00\t9.00\t%.2f' %areaTrapezoid(2.0, 7.0, 9.0)
    print '3.20\t4.20\t2.00\t%.2f' %areaTrapezoid(3.2, 4.2, 2.0)
    print
    
# a trapezoid has a height and a top length and bottom length.
# The top and bottom lengths are typically referred to as base2 and base1
# See this website for a picture  http://math.com/tables/geometry/areas.htm
def areaTrapezoid(base1, base2, height):
    area = height / 2.0 * (base1 + base2)
    return area


main()

# part 2
# this program displays a table of the following identity:
# sin2(n) + cos2(n) = 1 for any number 'n'

import math

def sin_cos_squared(count):
    print '  n\tsin(n)\tcos(n)\tsin^2(n) + cos^2(n)'
    start = 0
    for n in range(start, count + 1):
        print '%.4f\t%.3f\t%.3f\t%.17f' % \
              (start, math.sin(start), math.cos(start), \
               math.sin(start)**2 + math.cos(start)**2)
        start += 2 * math.pi / count
        

def main():
    sin_cos_squared(8)
    print
    sin_cos_squared(20)


main()
