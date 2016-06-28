#directory with price of the fruit
prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}

#directory with amount of the fruits
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

#for loop to print out what is in stock
for key in prices:
    print key
    print "price: %0.1f" % prices[key]
    print "stock: %d" % stock[key]

#store the total amount
total = 0

#count total amount
for fruit in prices:
    total+=prices[fruit]*stock[fruit]
print total
