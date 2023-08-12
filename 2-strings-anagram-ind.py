#!/bin/python

import sys
def number_needed(a, b):
    total=0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        total+=abs(a.count(letter)-b.count(letter))
    return total

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
