# enter scores between 0.0 and 1.0

# set value to enter loop
score = 0.0

while score <= 0 or score >= 1 :
    try :
        score = raw_input('Give a score between 0.0 and 1.0: ')
        score = float(score)
    except :
        print 'Please enter a number, doofus.'
    
if score >= 0.9 :
    vote = 'an A'
elif score >= 0.8 :
    vote = 'a B'
elif score >= 0.7 :
    vote = 'a C'
elif score >= 0.6 :
    vote = 'a D'
else :
    vote = 'an F'

print 'Your score was',score, 'so you got',vote
