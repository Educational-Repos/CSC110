
# Sample code developed during class
# on Tuesday, 5/31
def main():
    my_list = [34, 18, 95, 46, 12]
    print my_list
    rotate_left(my_list)
    rotate_left(my_list)
    print my_list
    print 'Highest =', highest(my_list)
    print get_low_values(my_list, 40)
    print get_low_values(my_list, 100)
    print get_low_values(my_list, 10)

# Rotates the elements in the list
# one postition to the left
def rotate_left(arr):
    if len(arr) == 0:
        return
    temp = arr[0] # initialization
    i = 0
    while i < len(arr) - 1:
        arr[i] = arr[i + 1]
        i += 1
    arr[len(arr)-1] = temp# finalization

# Finds and returns the highest element
# in the list
def highest(arr):
    highest = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] > highest:
            highest = arr[i]
        i += 1
    return highest

# Returns a NEW list with all values less
# that 'limit' in the list 'arr'
def get_low_values(arr, limit):
    result = []
    for elem in arr:
        if elem < limit:
            result.append(elem)
    return result

main()
