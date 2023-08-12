fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    setje = line.split()
    tel = len(setje)
    while tel != 0 :
        woord = setje[(tel-1)]
        if woord not in lst :
            lst.append(woord)
        tel = tel - 1
lst.sort()
print lst
