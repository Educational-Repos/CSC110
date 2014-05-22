#program to display the type garden depending on amount of sunlight

# CSC 110
#  Spring 2010

print "How does your garden grow?"

# get amount of sunlight
hours = input("Please enter the number of hours of sunlight in your garden ")

# display based on a decision
if hours >= 6:
    print "You've got a sunny garden.  Plant sun-loving flowers"
elif hours > 2.5:
    print "You've got a part-shade garden."
else:
    print "You've got a shade garden. Plant hostas and coleus"
        
