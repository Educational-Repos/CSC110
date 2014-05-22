def main():
    file_name = raw_input("Please enter a file's name: ")

    infile = open(file_name + '.txt', 'r')

    line_num = 1
    line = infile.readline()
    while line != '':
        print '%d: %s' %(line_num, line),
        line_num += 1
        line = infile.readline()

    infile.close()

main()
