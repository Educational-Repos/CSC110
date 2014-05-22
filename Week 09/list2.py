
# Code developed during class on Thursday, 6/2/11

##grades = []
##num = input('Enter a grade: ')
##while num >= 0:
##    grades.append(num)
##    num = input('Enter another grade (<0 to end): ' )
##
##print 'The grades are', grades

def main():
    fruits = ['apple', 'banana', 'pear', 'orange']
    print fruits
    print 'Vowel words:', vowel_words2(fruits)
    print fruits

# Returns a list of all words in 'arr'
# that begin with a vowel AND makes them
# all caps in the orginal list
def vowel_words2(arr):
    vowels = 'aeiouAEIOU'
    result = []
    i =0
    while i < len(arr):
        if arr[i][0] in vowels:
            result.append(arr[i])
            arr[i] = arr[i].upper()
        i += 1
    return result

# Returns a list of all words in 'arr'
# that begin with a vowel
def vowel_words(arr):
    vowels = 'aeiouAEIOU'
    result = []
    for word in arr:
        if word[0] in vowels:
            result.append(word)
    return result

main()
