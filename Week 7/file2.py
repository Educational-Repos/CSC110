
# Code developed in class on Monday, 5/16
# Illustrates reading and writing numbers from a file

def main():
    # Open files for reading and writing
    infile = open('test1.txt', 'r')
    bignums = open('big.txt', 'w')
    smallnums = open('small.txt', 'w')

    count = 0 # initialization
    line = infile.readline() # priming read
    while line != '':
        num = int(line)
        count += 1
        # print num
        if num > 10:
            bignums.write(str(num / 2) + '\n')
        else:
            smallnums.write(str(num) + '\n')
        line = infile.readline() # UPDATE

    # Close files and show output
    infile.close()
    bignums.close()
    smallnums.close()
    print 'There were %d numbers in the file.' % count

main()

