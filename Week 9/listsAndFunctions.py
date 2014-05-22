# Lab Activity -- Lists and Functions

# Chun-Wei Chen
# CSC 110.03
# Spring 2011 06/03

# this function is passed in a list and 2 index numbers and swap
# the values at those index locations
def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    return arr

# this function is passed in a list of strings and returns a new list
# with all the strings of the original list with length 2
# (the original list is not changed)
def length_2(arr):
    result = []
    for str in arr:
        if len(str) == 2:
            result.append(str)
    return result

def main():
    stuff_1 = [20, 40, 60, 80, 100]
    stuff_2 = ['that', 'is', 'my', 'list', 'of', 'string']
    print swap(stuff_1, 1, 4)
    print length_2(stuff_2)

main()

