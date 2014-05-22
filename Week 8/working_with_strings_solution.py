
# This is one possible solution for the "Working with Strings"
# lab exercise.
#
# CSC 110
# Sp'11


def main():
    # Part 1: Get the phrase from the user
    phrase = raw_input('Enter a phrase: ')
    
    # Part 2: Print the phrase one character per line
    for ch in phrase:
        print ch

    # Part 3: Print the phrase in reverse order, all on one line
    #         Version 1 -- Written using a string accumulator.
    reverse_phrase = '' # initialize to the empty string
    for ch in phrase:
        reverse_phrase = ch + reverse_phrase # add ch in FRONT
    print reverse_phrase

    # Part 3: Print the phrase in reverse order, all on one line
    #         Version 2 -- reverse iteration
    reverse_phrase = '' # initialize to the empty string
    i = len(phrase) - 1 # initialize index
    while i >= 0:
        reverse_phrase += phrase[i] # add character at the end
        i -= 1 # update loop counter
    print reverse_phrase

    # Part 4: Print one word per line
    word = '' # initialize to the empty string
    for ch in phrase:
        if ch == ' ':   # when you see a space, print the word and reset
            print word
            word = ''
        else:           # otherwise add the character to the word
            word += ch
    if word != '':      # print the last word
        print word

    # Optional Part 5 -- not included here

    # Optional Part 6: Replace 'b' words with 'bee'
    word = '' # initialize to the empty string
    phrase += ' ' # add a space at the end of the phrase
                  # to ensure the last word gets flushed out
    for ch in phrase:
        if ch == ' ':   # when you see a space, print the word and reset
            if len(word) > 0:
                if word[0] == 'b' or word[0] == 'B':
                    print 'bee'
                else:
                    print word
            word = ''
        else:           # otherwise add the character to the word
            word += ch

    
    
main()
