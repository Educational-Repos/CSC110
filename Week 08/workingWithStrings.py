# Lab Activity -- Working with Strings

# Chun-Wei Chen
# CSC 110.03
# Spring 2011 5/24

# 1
phrase = raw_input('Please enter a short phrase: ')
for ch in phrase:
    print ch
print

# 2
s = ''
for ch in phrase:
    s = ch + s
print s
print

# 3
s = ''
for ch in phrase:
    if ch == ' ':
        if s != '':
            print s
            s = ''
    else:
        s += ch
print s
print

# 4
s = ''
vowels = 'AEIOUaeiou'
for ch in phrase:
    if ch == ' ':
        if s != '':
            print s
            s = ''
    elif ch not in vowels:
        s += ch
print s
print

# 5
s = ''
for ch in phrase:
    if ch == ' ':
        if s != '':
            print s,
            s = ''
    else:
        if s != 'bee':
            s += ch
            if s == 'b':
                s = 'bee'
print s
print
