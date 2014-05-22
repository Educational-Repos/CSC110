def main():
    infile = open('number.txt', 'r')

    sum = 0
    amount = 0
    line = infile.readline()
    while line != '':
        sum += float(line)
        amount += 1
        line = infile.readline()
        
    average = sum / amount

    infile = open('number.txt', 'a')
    infile.write('The average of all the numbers is %.2f.' % average + '\n')

    infile.close()

main()
