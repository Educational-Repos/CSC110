# This program demonstrates how a value can be
# formatted, rounded to different numbers of
# decimal places, using the %f placeholder


myValue = 1.123456789
print '%.1f' % myValue   # Rounded to 1 decimal place
print '%.2f' % myValue   # Rounded to 2 decimal places
print '%.3f' % myValue   # Rounded to 3 decimal places
print '%.4f' % myValue   # Rounded to 4 decimal places
print '%.5f' % myValue   # Rounded to 5 decimal places
print '%.6f' % myValue   # Rounded to 6 decimal places

raw_input("Please press enter to continue")
print
print

# Here are some examples where you can insert a value into a more interesting string
otherValue = 2.724565
print 'The other value = %f' % otherValue  # notice this doesn't round at all, just inserts the value
print 'Here %.4f is rounded to 4 decimal places' % otherValue
