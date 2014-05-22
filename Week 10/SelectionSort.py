# Selection Sort demo
#
# CSC 110
# W'11

def sort(numbers):
    # This outer loop keeps track of where the
    # unsorted portion of the list begins.
    for idx in range(len(numbers)-1):
        # Each time we come into the body of this outer loop, we are doing 
        # one pass.  Remember that a pass is made up of a search and a swap.
        #
        # Here is the code to search for and find the smallest value. We've 
        # seen this before and know that it uses a for loop (so we've got
        # nested loops).
        # What we really need to know is the INDEX of the smallest value,
        # so we'll keep track of that. As long as we have an index, we can
        # go back into the list to get the value.
        #
        # Remember, we only want to search in the unsorted portion of the
        # list.  Where does that section begin?  At index idx.

        idxSmallest = idx;  # initialization
        for i in range(idx + 1, len(numbers)):
            if numbers[i] < numbers[idxSmallest]:# found a new smallest value,
                idxSmallest = i;                 # so remember its subscript

        # now that we've found the index of the smallest value, swap it into place
        temp = numbers[idx]
        numbers[idx] = numbers[idxSmallest]
        numbers[idxSmallest] = temp
    # End of function, but nothing to "return" -- the list itself has been changed!

# Main Program
test = [3, 6, 1, 8, 4, 5]  # fill a list with some numbers
print 'Original:', test
sort(test)
print '  Sorted:', test
