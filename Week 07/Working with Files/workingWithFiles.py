# Lab Activity -- Working with Files

# Chun-Wei Chen
# CSC 110.03
# Spring 2011 5/17

def main():
    # ask the user to enter a file name
    file_name = raw_input('Please enter a file name: ')

    # open the files
    infile = open(file_name + '.txt', 'r')
    even = open('even.txt', 'w')
    odd = open('odd.txt', 'w')

    sum = 0 # initialize counter
    count = 0 # initialize counter
    line = infile.readline() # priming read
    while line != '':
        num = int(line)
        if num % 2 == 0:
            even.write(str(num) + '\n')
            sum += num
        else:
            odd.write(str(num) + '\n')
        if num < 0:
            count +=1
        line = infile.readline() # update
        
    # display some results
    print 'The sum of the even numbers is %d.' % sum
    print 'The amount of negative numbers is %d.' % count
    
    # close the files
    infile.close()
    even.close()
    odd.close()
    
main()
