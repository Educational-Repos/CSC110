# Assignment 7 -- Working with Lists

# ChenChunWeiHW7.py
# Chun-Wei Chen
# CSC 110.03
# 2011 Sping 06/10

# This program analyzes the monthly sales figures for each division --
# highest & lowest number (sales leader & loser), average number, etc.

def return_string(arr):
    s = ''  # empty string
    for value in arr:
        s += str(value) + ' '  # add up all the values in the list into sting
    return s   # show the string

def max2(arr):
    highest = arr[0]  # initialize the first value is the highest value
    i = 1    # start from the second value to the last value in the list
             # to find the highest value
             
    while i < len(arr):
        if arr[i] > highest:
            highest = arr[i]
        i += 1   # update the index in order to check the next value

    return highest   # show the highest value

def min2(arr):
    lowest = arr[0]   # initialize the first value is the lowest value
    i = 1   # start from the second value to the last value in the list
            # to find the lowest value
            
    while i < len(arr):
        if arr[i] < lowest:
            lowest = arr[i]
        i += 1   # update the index in order to check the next value

    return lowest   # show the lowest value

def total(arr):
    sum = 0.0   # initialize accumulator

    for value in arr:
        sum += value  # sum up all the number in the list

    return sum   # show the total

def awards_threshold(arr, num):
    result = []   # empty list

    for value in arr:
        if value >= num:
            result.append(value)  # add the value in the new list if
                                  # it is greater or equal to num (threshold)
    return result

def main():
    list = []   # empty list
    sales_figures = input('Please enter a monthly sales amount' + \
                              '(enter negative number to stop): ')
    
    while sales_figures >= 0:
        list.append(sales_figures)   # add the user's input in the list
        sales_figures = input('Please enter another monthly sales amount' + \
                              '(enter negative number to stop): ')
        
        
    average = total(list) / len(list)

    print
    print 'This is the list:', list
    print
    print 'Show all the values:', return_string(list)
    print    
    print 'The sales amount of sales leader is', max(list)
    print 'Show again. The sales amount of sales leader is', max2(list)
    print
    print 'The sales amount of sales loser is', min(list)
    print 'Show again. The sales amount of sales loser is', min2(list)
    print
    print 'The total sales for the company for the month is', total(list)
    print
    print 'The average sales for the company for the month is', average
    print
    
    threshold = input('Please enter a number for threshold of ' + \
                      'getting awards: ')
    
    print awards_threshold(list, threshold), \
          'These divisions get awards for high sales!'

main()

# Documented Test

# Input 1:
# sales_figures: 50
#                60
#                70
#                -1
# threshold: 60

# Output 1:
# This is the list: [50, 60, 70]
#
# Show all the values: 50 60 70
#
# The sales amount of sales leader is 70
# Show again. The sales amount of sales leader is 70
#
# The sales amount of sales loser is 50
# Show again. The sales amount of sales loser is 50
#
# The total sales for the company for the month is 180.0
#
# The average sales for the company for the month is 60.0
#
# [60, 70] These divisions get awards for high sales!


# Input 2:
# sales_figures:  100
#                  75
#                  98
#                  66
#                 123
#                  35
#                  -1
# threshold: 95
#
# Output 2:
# This is the list: [100, 75, 98, 66, 123, 35]
#
# Show all the values: 100 75 98 66 123 35
#
# The sales amount of sales leader is 123
# Show again. The sales amount of sales leader is 123
#
# The sales amount of sales loser is 35
# Show again. The sales amount of sales loser is 35
#
# The total sales for the company for the month is 497.0
#
# The average sales for the company for the month is 82.8333333333
#
# [100, 98, 123] These divisions get awards for high sales!


# Input 3:
# sales_figures:  32
#                486
#                257
#                 95
#                333
#                 62
#                 -1
# threshold: 257
#
# Output 3:
# This is the list: [132, 486, 257, 95, 333, 62]
#
# Show all the values: 132 486 257 95 333 62
#
# The sales amount of sales leader is 486
# Show again. The sales amount of sales leader is 486
#
# The sales amount of sales loser is 62
# Show again. The sales amount of sales loser is 62
#
# The total sales for the company for the month is 1365.0
#
# The average sales for the company for the month is 227.5
#
# [486, 257, 333] These divisions get awards for high sales!


# These results agree with hand calculations.
