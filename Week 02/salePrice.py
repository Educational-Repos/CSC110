# This program gets an item's original price and
# calculates its sale price, with a 20% discount.

# Illustrates a named constant
# Illustrates format string and how to display the % character

# CSC 110
# Spring 2010

DISCOUNT_RATE = 0.2   

print "This program will ask you for an item's price, then display the sale price"

# Get the item's original price.
originalPrice = input("Enter the item's original price: ")

# Calculate the amount of the discount.
discount = originalPrice * DISCOUNT_RATE

# Calculate the sale price.
salePrice = originalPrice - discount

# Display the sale price.
print "Your product's original price is $%.2f" % originalPrice
print "With a %.1f%% discount of $%.2f, the sale price is $%.2f" % (DISCOUNT_RATE * 100, discount, salePrice)

