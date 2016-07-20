# Project Euler - Problem #13 : https://projecteuler.net/problem=13

"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

import re
f = open('.\euler_prob13_numbers.txt', 'rU')
text = f.read()
numbers = [int(i) for i in text.split('\n')]
print str(sum(numbers))[:10]