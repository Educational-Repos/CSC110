# prints a multiplication table based on user input
# CSC 110

print 'This program will print out a multiplication table'
print
print

top = input('Enter a number between 2 and 20: ')
while top < 2 or top > 20:
    print 'Sorry, but', top, 'is not valid input'
    top = input('Enter a number between 2 and 20: ')

# the outer loop is for each row
for row in range (1, top + 1):

    # the inner loop prints every column in the row
    for col in range(1, top + 1):
        print row*col, '\t',

    # after the loop is done, print again to move to the next line
    print
