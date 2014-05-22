# Assignment 6 -- Pig Latin

# ChenChunWeiHW6.py
# Chun-Wei Chen
# CSC 110.03
# 2011 Spring 5/27

# This program allows the user to translate a series of words contained in
# a file into a form of "Pig Latin," a language game modifies the normal
# English words and makes them sound differently.

def pig_latin(word):
    vowels = 'aeiouAEIOU'   # store all the vowels in a variable
    num = 0   # initialize the character number
    
    if word.isalpha() == True:
        # the rule for the word only composed of alphabet's letters

        while word[0] in vowels:   # the rule for the first letter is vowel
            if word == 'I':   # special case
                return word + 'way'
            return word + 'hay'
        
        while word[num] not in vowels:
            # the rule for the word whose first letter is not vowel

            if word[0].isupper() == True:
                # the rule for the first letter is capitalized
                
                if word[:2] == 'Qu':   # special case
                    return word[2].upper() + word[3:] + word[0].lower() + \
                           word[1] + 'ay'
                if word[num + 1] in vowels:
                    return word[num + 1].upper() + word[num + 2:] + \
                           word[0].lower() + word[1:num + 1] + 'ay'
                else:
                    num += 1
                    
            else:
                # the rule for the first letter is capitalized
                
                if word[:2] == 'qu':   # special case
                    return word[2:] + word[:2] + 'ay'
                if word[num + 1] in vowels:
                    return word[num + 1:] + word[:num + 1] + 'ay'
                else:
                    num += 1
                    
    else:
        # the rule for the word only composed of alphabet's letters
        return word

def main():
    file_name = raw_input("Please enter a file's name(for example: " \
                          "name.txt): ")
    
    infile = open(file_name, 'r')
    outfile = open(file_name[:len(file_name)-4] + 'PigLatin' + \
                   file_name[len(file_name)-4:], 'w')
    
    line = infile.readline()   # priming read
    s = ''
    space_newline_punctuation = ' \n,.:;"!?()[]'
    # store ' ', '\n', and punctuation in a variable
    
    while line != '':
        for ch in line:
            if ch not in space_newline_punctuation:
                # let the program be able to convert the content word by word
                s += ch
            else:
                outfile.write(pig_latin(s) + ch)
                s = ''
                   
        line = infile.readline()   # update
        
    infile.close()
    outfile.close()
    # close all the opened files
    
    print pig_latin('cat')
    print pig_latin('ink')
    print pig_latin('Sprite')
    print pig_latin('I')
    print pig_latin('Quite')
    print pig_latin('51618')
    # display some results
    
main()

# Documented Test

# Sample Words Test:

# Tset 1:
# word = 'ink'

# Result 1:
# inkhay

# Test 2:
# word = 'Quite'

# Result 2:
# Itequay

# Test 3:
# word = 'I'

# Result 3:
# Iway

# Test 4:
# word = '51618'

# Result 4:
# 51618

# File Test:

# data.txt:
# I have 3 classes during weekdays.
# I spend 4 hours on watching television everyday.
# The English assignment took me 5 hours to complete.
# Listening to the music makes me very happy!
# I got 96 on test.
# Is there any problem with the program?

# Result:
# dataPigLatin.txt:
# Iway avehay 3 assesclay uringday eekdaysway.
# Iway endspay 4 ourshay onhay atchingway elevisiontay everydayhay.
# Ethay Englishhay assignmenthay ooktay emay 5 ourshay otay ompletecay.
# Isteninglay otay ethay usicmay akesmay emay eryvay appyhay!
# Iway otgay 96 onhay esttay.
# Ishay erethay anyhay oblempray ithway ethay ogrampray?
