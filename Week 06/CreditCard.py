
# How long will it take to pay off a credit card balance??
# This program makes use of a loop to perform a SIMULATION
# of a real-world situation.

# CSC 110
# W'11

### Get and validate inputs

interest_multiplier = input('Enter an ANNUAL INTEREST RATE ' \
    + 'as a PERCENTAGE, greater than or equal to zero: ') / 1200.0
while interest_multiplier < 0:
    interest_multiplier = input('TRY AGAIN -- annual ' \
        + 'rate must be greater than or equal to zero:') / 1200.0

initial_balance = input('Enter an INITIAL ACCOUNT BALANCE ' \
    + 'in dollars, greater than or equal to 100: ')
while initial_balance < 100:
    initial_balance = input('TRY AGAIN -- initial balance ' \
        + 'must be greater than or equal to 100:')

payment = input('Enter the MONTHLY PAYMENT to be made, ' \
    + 'in dollars, greater than or equal to 10: ')
while payment < 10:
    payment = input('TRY AGAIN -- monthly payment ' \
        + 'must be greater than or equal to 10:')

### Simulate account changes until the account is paid in full

balance = initial_balance # initialize accumulator
months = 0                # initialize counter
total_payments = 0        # initialize accumulator;

# NOTICE that the loop continues as long as the balance is greater than
#        zero, BUT not longer than 1200 months -- a condition necessary
#        to prevent an infinite loop if the payment is too low.
while balance > 0 and months < 1200:
    balance = balance + (balance * interest_multiplier)
    balance -= payment
    total_payments += payment
    months += 1
    # print balance  # use to TRACE loop operation

years = months / 12  # integer division on purpose -- whole years only
months = months % 12


### Show results

print '\nAfter %d years and %d months' % (years, months)
if balance <= 0:
    print 'your debt is paid.'
    total_payments += balance # corrects for any excess payment (balance <= 0)
    print '\nTotal interest = $%.2f.' % (total_payments - initial_balance)
else:
    print 'your debt is still not paid off!'
    print 'Remaining balance = $%.2f.' % balance
print '\nTotal payments = $%.2f.\n' % total_payments
