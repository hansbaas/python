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

for item in adressen :
    print item

print "There were", count, "lines in the file with From as the first word"

