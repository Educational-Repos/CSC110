# Retirement Planning, Part 2

# ChenChunWeiHW5.py
# Chun-Wei Chen
# CSC 110.03
# 2011 Spring 5/23

# This program displays a retirement planning table which has 10 starting ages
# and 4 interest rates after the user input annual savings.

def main():
    print 'Welcome to the retirement planning tool!'
    print
    annual_savings = input('Enter annual savings (at least $100): $')
    # ask the user to input the annual savings
    while annual_savings < 100:
        annual_savings = input('Try again! Enter annual savings ' \
                                   '(at least $100): $')
        # if the annual savings is less than $100, ask the user to enter again
    print 'Retirement Savings Table:\n'
    print ' Starting\tAssumed Interest Rate'
    print '   Age\t\t  4%   \t\t 6%  \t\t 8%  \t\t10%'
    age = 20 #  initialize counter
    interest_rate = 4
    while age < 70:
        print '%6s  ' % age,
        for interest_rate in range(4, 12, 2):
            print '$%10.2f  \t' % \
                  calc_final_balance(age, annual_savings, interest_rate),
        age += 5
        print'\n',
        
    print
    print 'When are YOU going to start saving for your retirement?'
    
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

main()

# Documented Test Results -- test if there is any logic error in the program

# Test 1:
# starting age = 25
# annual savings = $ 2500
# interest rate = 8%

# Result 1:
# $ 1043565.17

# Test 2:
# starting age = 40
# annual savings = $ 4000
# interest rate = 6%

# Result 1:
# $ 335206.71

# Test 3:
# starting age = 50
# annual savings = $ 3500
# interest rate = 10%

# Result 3:
# $ 220508.75

# These results are agree with the results from the engineering calculator
