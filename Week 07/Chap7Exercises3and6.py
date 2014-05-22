# Programming exercise 7-3 (p. 272)
# Show the contents of a file with each line
# preceded by a line number and a colon.
filename = raw_input('Enter file name: ')
infile = open(filename, 'r')
count = 0;

line = infile.readline()  # priming read
while line != '':
    count += 1 # we have another line
    line = line.rstrip() # remove trailing newline
    print str(count) + ': ' + line
    line = infile.readline()  # update read

infile.close()

# Programming exercise 7-6 (p. 272)
# Read a series of numbers from a file and
# calculate and report the average value.
filename = raw_input('Enter file name: ')
infile = open(filename, 'r')
count = 0;
sum = 0.0; # deliberately a floating point number

line = infile.readline()  # priming read
while line != '':
    count += 1 # we have another number
    num = float(line) # extract number from the line
    sum += num
    line = infile.readline()  # update read

infile.close()
if count == 0:
    print 'File was empty'
else:
    print 'The average value is', (sum/count)
