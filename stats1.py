inp = "hello"
count = 0
total = 0

while inp is not "fuck":
    inp = raw_input('Give us a number: ')
    if inp == "fuck":
        break

    try:
        num = float(inp)
        count = count + 1
        total = total + num
        print "Insert fuck to stop."
    except:
        print "That's not a number, doof"

print total, count, total/count
