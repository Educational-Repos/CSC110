# This program demonstrates how the == operator can
# be used to compare strings.

# from Tony  Gaddis

def main():
    # Get a password from the user.
    password = raw_input('Enter the password: ')

    # Determine whether the correct password
    # was entered.
    if password == 'prospero':
        print 'Password accepted.'
    else:
        print 'Sorry, that is the wrong password.'

# Call the main function.
main()

    
