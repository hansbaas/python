fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
adressen = list()
woorden = list()

for line in fh :
    line = line.rstrip()
    woorden = line.split()
    if len(woorden) == 0 : continue
    if woorden[0] != 'From' : continue
    count = count + 1
    adressen.append(woorden[1])

email = dict()
for adres in adressen :
    email[adres] = email.get(adres,0) + 1

#print email

bigcount = None
bigword = None
for item,nummer in email.items() :
    if bigcount == None or nummer > bigcount :
        bigword = item
        bigcount = nummer

print bigword, bigcount

