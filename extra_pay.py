# payroll calculator

# parameters
extra_factor = 1.5

# user input
try :
    hours = raw_input('Number of hours you worked: ')
    hours = float(hours)
    rate = raw_input('Base rate for your job: ')
    rate = float(rate)
except :
    print 'Please only enter numerical data, doofus.'
    quit()

extra_rate = rate * extra_factor

if hours <= 40 :
    base_hours = hours
    base_pay = hours * rate
    extra_hours = 0
    extra_pay = 0
else :
    base_hours = 40
    base_pay = hours * rate
    extra_hours = hours - base_hours
    extra_pay = base_hours * extra_rate

total_pay = base_pay + extra_pay

# check and presentation of the outcome
print 'Your base pay is:'
print str(base_hours), '*', str(rate), '=', str(base_pay)
print 'Your extra pay is:'
print str(extra_hours), '*', str(extra_rate), '=', str(extra_pay)
print 'Your total pay is ', str(total_pay)
print 'Enjoy!!!'
