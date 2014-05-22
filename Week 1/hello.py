# Chun-Wei Chen
# CSC 110.03 Lab 1
# Program to prompt the user for their names, countries,
# hobbies, and favorite sports and music, then say hello to the user
# Spring 2011 4/6

# input section
name = raw_input('Please enter your name: ')
country = raw_input('Hi, ' + name + '! Where are you from? ')
hobby = raw_input('I wonder what your hobby is. ')
sport = raw_input('Which sport is your favorite? ')
music = raw_input('What kind of music do you like? ')

# output section
print "Hello", name, "--  Nice to meet you!"
print name, "is from", country + "."
print name + "'s hobby is", hobby + "."
print name + "'s favorite sport is", sport + \
      ". Maybe we can play together somtimes."
print name, "likes", music, "music. Sounds great!"
