# Find the minimum number of characters we need to delete from two strings in order to get anagrams

a = "1"
b = "2"

while not (len(a) <= 1000 and len(b) <= 1000 and len(a) > 0 and len(b) > 0 and sum(1 for c in a if c.islower()) == len(a) and sum(1 for d in b if d.islower()) == len(b)):
    print "Enter two strings that only contain lower case letters and have a maximum length of 1000."
    a = raw_input("Enter first string: ")
    b = raw_input("Enter second string: ")
    
a1 = list(a)
b1 = list(b)
a2 = list(a)

for i in range(len(a2)):
    if a2[i] in b1:
        na = a1.index(a2[i])
        nb = b1.index(a2[i])
        del b1[nb]
        del a1[na]
        
print a1
print b1

print "You need to delete ", len(a1)+len(b1), " letters."
