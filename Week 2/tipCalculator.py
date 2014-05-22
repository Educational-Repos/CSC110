# Chun-Wei Chen
# CSC 110.03 Lab 1
# Spring 2011/04/12
# This program serves as a tip calculator. After the user enter the dollar
# amount of the bill and the percentage tip, the program will calculate the
# dollar amount of the tip and the total amount to pay, including the tip.

# Input Section
money = input('Please enter the dollar amount of the bill: ')
percentage = input('Please enter the percentage of the tip: ')

# Processing
tip = money * float(percentage) / 100
total = money + tip
tip = round(tip, 2)
total = round(total, 2)

# Output Section
print 'The dollar amount of the tip is ' + str(tip) + '.'
print 'The total amount to pay is ' + str(total) + '.'
