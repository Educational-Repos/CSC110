# Lab 3 -- One Possible Solution

# CSC 110
# 5/11/2011

import math

def main():
    print '\n\n========Part 1========='
    # Demonstrate several different ways to call the areaTrapezoid() function
    area1 = areaTrapezoid(4, 5, 8)
    print "For 4, 5, 8, the area is", area1
    print "For 2, 7, 9, the area is", areaTrapezoid(2, 7, 9)
    print 'For 2, 4, 6, the area is ' + str(areaTrapezoid(2, 4, 6))
    print 'For 2.3, 4.1, 6.99, the area is %.2f' % areaTrapezoid(2.3, 4.1, 6.99)

    # The function sin_cos_squared() is defined below; this code tests it.
    # Some rows in the output show expected representational error.
    print '\n\n========Part 2========='
    sin_cos_squared(8)
    sin_cos_squared(20)
    
  

# a trapezoid has a height and a top length and bottom length.
# The top and bottom lengths are typically referred to as base2 and base1
# See this website for a picture  http://math.com/tables/geometry/areas.htm
def areaTrapezoid(base1, base2, height):
    area = height / 2.0 * (base1 + base2)
    return area

# displays ("prints") a table containing (intervals + 1) rows
# showing values for 'n' ranging from 0 to 2pi and sin(n), cos(n), and
# (sin^2(n) + cos^2(n)) for each value of 'n'.
def sin_cos_squared(intervals):
    first = 0.0
    last = math.pi * 2
    step = (last - first) / intervals
    print '\n\n  n\t sin(n)\t cos(n)\tsin^2(n) + cos^2(n)'
    for i in range(intervals + 1):
        num = i * step
        ans = math.sin(num) ** 2 + math.cos(num) ** 2
        print '%.4f\t%6.3f\t%6.3f\t%.17f' % \
              (num, math.sin(num), math.cos(num), ans)


main() # call 'main' method -- starts the program
