# -*- coding: utf-8 -*-
import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
specials = "!£$&/()='+*-.,;:_<>"
upperalphabet = alphabet.upper()
pw_len = 12
pwlist = []

for i in range(pw_len//3):
    pwlist.append(alphabet[random.randrange(len(alphabet))])
    pwlist.append(specials[random.randrange(len(specials))])
    pwlist.append(upperalphabet[random.randrange(len(upperalphabet))])
    pwlist.append(str(random.randrange(10)))
for i in range(pw_len-len(pwlist)):
    pwlist.append(alphabet[random.randrange(len(alphabet))])

random.shuffle(pwlist)
pwstring = "".join(pwlist)

print(pwstring)
