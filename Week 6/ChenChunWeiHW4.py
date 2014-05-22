# Retirement Planning, Part 1

# ChenChunWeiHW4.py
# Chun-Wei Chen
# CSC 110.03
# Spring 2011 5/15

# This program calculates the final balance at age 70 in a retirement account
# after annual savings and interest earning for a number of years.

def calc_final_balance(starting_age, amount_saved_each_year, \
                       percentage_interest_rate):
    
    # starting_age -- when does the saving start
    # amount_saved_each_year -- how much money is saved each year
    # percentage_interest_rate -- how many percents of the money of the
    # account will be added in the account every year
    
    rate = percentage_interest_rate / 100.0
    # change the number into percentage
    age = starting_age  # initialize counter
    final_balance = 0   # initialize accumulator
    
    while age < 70:
        final_balance += amount_saved_each_year
        final_balance *= (1 + rate)
        age += 1
    return final_balance  # display the final_balance after the loop

def main():
    print '$%.2f' % calc_final_balance(30, 3000, 6)
    print '$%.2f' % calc_final_balance(20, 2000, 5.5)
    print '$%.2f' % calc_final_balance(25, 2500, 7.5)
    print '$%.2f' % calc_final_balance(40, 4000, 4.5)
    print '$%.2f' % calc_final_balance(50, 3500, 4)
    # display results of several situations

main()

# Documented Test Results -- test if there is any logic error in the program

# Test 1:
# starting_age = 25
# amount_saved_each_year = 2500
# percentage_interest_rate = 7.5

# Result 1:
# $892423.38.

# Test 2:
# starting_age = 40
# amount_saved_each_year = 4000
# percentage_interest_rate = 4.5

# Result 2:
# $255009.55.

# Test 3:
# starting_age = 50
# amount_saved_each_year = 3500
# percentage_interest_rate = 4

# Result 3:
# $108392.21.

# These results are agree with the results from the engineering calculator
