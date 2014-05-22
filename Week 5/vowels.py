# counts how many of each vowel there are in a string

# CSC 110

phrase = raw_input('Enter some text: ')

# initialize all accumulators
countA = 0
countE = 0
countI = 0
countO = 0
countU = 0

for char in phrase:
    if char.upper() == 'A':
        countA += 1
    elif char.upper() == 'E':
        countE += 1
    elif char.upper() == 'I':
        countI += 1
    elif char.upper() == 'O':
        countO += 1
    elif char.upper() == 'U':
        countU += 1

print "The number of A's = %d" % countA
print "The number of E's = %d" % countE
print "The number of I's = %d" % countI
print "The number of O's = %d" % countO
print "The number of U's = %d" % countU
