# Program to calculate sales commission, and to accumulate a total
# uses loops and functions

def main():
    print 'You will be asked to enter sales and commission rate for each employee'
    print 'The program will display the commission amount for each and the total for the company'
    print

    repeat = 'y'
    companyTotal = 0

    # repeated get the data for an employee and keep a running total
    while repeat == 'y' or repeat == 'Y':
        companyTotal += processOneEmp()
        print
        repeat = raw_input('Is there another employee? Enter y for yes ')

   # display
    print
    print
    print "The company's total commissions = $%.2f" % companyTotal

# this function gets the data for one employee, calculates commission, and displays it
# returns the commission for the employee
def processOneEmp():

    #input
    print
    name = raw_input("What is the employee's name? ")
    sale = input('Enter the sales for ' + name + ' $')
    rate = input("Enter the commission percentage rate for " + name + ": ")

    #calculation
    total = sale * rate/100.0   #convert from percent to decimal

    # output
    print '%s earned $%.2f in commissions' % (name, total)

    return total

main()
