# ChenChunWeiHW1.py
# Chun-Wei Chen
# CSC 110.03
# Spring 2011 04/12
# This program plays a Mad-Lib game, which asks the user to insert several
# kinds of words (e.g noun, verb, color, adjective). Those words will be
# inserted into a story in predefined place. The result could be a strange or
# a funny story.

# input section
print 'Welcome to the Mad-Lib game! I hope you will enjoy the game.'
progressive_tense_verb = raw_input('Please enter a progressive tense verb: ')
preposition = raw_input('Please enter a preposition: ')
past_tense_verb = raw_input('Please enter a past tense verb: ')
adjective = raw_input('Please enter an adjective: ')
singular_noun = raw_input('Please enter a singular noun: ')
verb = raw_input('Please enter a verb: ')
number = raw_input('Please enter a number: ')
electronic_product = raw_input('Please enter an electronic product: ')
drink = raw_input('Please enter a kind of drink: ')
another_adjective = raw_input('Please enter an adjective: ')

# output section
print 'Yesterday, I did nothing but ' + progressive_tense_verb + ' NBA ' + \
      'games ' + preposition + ' TV because it was Sunday. I ' + \
      past_tense_verb + ' it would be a ' + adjective + ' day; however, ' + \
      'I found that I had to turn in a ' + singular_noun + ' tomorrow ' + \
      'before I went to ' + verb + '. After I typed ' + number + ' words, ' + \
      'my ' + electronic_product + ' was out of order because I ' + \
      'accidentally spilt the ' + drink + ' on it. What a ' + \
      another_adjective + ' day!'
print 'Thank you for playing the game!'
