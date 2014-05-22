
# ChenChunWeiHW2.py

# Pyramid Construction

# This is a program which uses the side length and the height of the pyramid
# provided by the user to compute the overall ground area covered by the
# pyramid, the total volume of the pyramid, the number of stone blocks needed
# to build the pyramid, and the total mass of the pyramid.

# Chun-Wei Chen
# CSC 110.03
# Spring 2011/04/16


# constant -- info. we already know
BLOCK_VOLUME = 1.5 * 2 * 2.5  # cubic meters
BLOCK_MASS = 15000  # kilograms

# input section -- get the information from the user
pyramid_length = input('Please enter the side \'length\' of the pyramid ' + \
                       'in meters.\n(The length is the length of the ' + \
                       'bottom square of the pyramid): ')
print
pyramid_height = input('Please enter the height of the pyramid in meters.\n'
                       '(The height is the distance between the top and ' + \
                       'the bottom of the pyramid)\n: ')

# processing section -- execute calculations
ground_area_covered = pyramid_length**2  # square meters
                    # the formula for square
pyramid_volume = 1.0/3 * ground_area_covered * pyramid_height  # cubic meters
                # the formula for square based pyramid
block_number = pyramid_volume/BLOCK_VOLUME
pyramid_mass = int(block_number) * BLOCK_MASS  # kilograms

# output section -- show the results of calculations
print
print 'The overall ground area covered of the pyramid is %.0f square meters.'% \
      ground_area_covered

print
print 'The total volume of the pyramid is %.0f cubic meters.' % pyramid_volume
print
print 'You need', int(block_number), 'blocks to build the pyramid.'
print
print 'The total mass of the pyramid is', pyramid_mass, 'kilograms.'

# Documented Test Results -- test if there is any logic error in the program

# The first input data:
# pyramid side length = 100 meters
# pyramid height = 300 meters

# The first result:

# The overall ground area covered of the pyramid = 10000 square meters
# The total volume of the pyramid = 1000000 cubic meters
# The number of stone blocks needed to build the pyramid = 133333
# The total mass of the pyramid = 1999995000 kilograms

# The second input data:
# pyramid side length = 517 meters
# pyramid height = 1992 meters

# The second result:

# The overall ground area covered of the pyramid = 267289 square meters
# The total volume of the pyramid = 177479896 cubic meters
# The number of stone blocks needed to build the pyramid = 23663986
# The total mass of the pyramid = 354959790000 kilograms

# These results agree with hand calculations.
