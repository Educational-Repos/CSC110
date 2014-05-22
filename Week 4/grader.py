# This program gets a numeric test score from the
# user and displays the corresponding letter grade.

def main():
    # Get a test score from the user.
    score = input('Enter your test score: ')

    # Determine the grade.
    if score < 60:
        print 'Your grade is F.'
    elif score < 70:
        print 'Your grade is D.'
    elif score < 80:
        print 'Your grade is C.'
    elif score < 90:
        print 'Your grade is B.'
    else:
        print 'Your grade is A.'

# Call the main function.
main()
