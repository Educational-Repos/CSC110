# This program demonstrates how the < operator can
# be used to compare strings.

# from Tony Gaddis

def main():
    # Get two names from the user.
    name1 = raw_input('Enter a name (last name first): ')
    name2 = raw_input('Enter another name (last name first): ')
    
    # Display the names in alphabetical order.
    print 'Here are the names, listed alphabetically.'
    if name1 < name2:
        print name1
        print name2
    else:
        print name2
        print name1

# Call the main function.
main()

    
