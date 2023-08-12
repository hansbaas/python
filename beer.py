beer = 0
orders = raw_input("How many beers would you like to drink?\n")
orders = float(orders) + 1

for i in range(int(orders)) :
    print "I had", beer, "beer"
    beer = beer + 1

if beer < 5 :
    print "I'm somewhat tipsy..."
elif beer < 10 :
    print "I had too many..."
else :
    print "I'm terribly drunk now!"
