# Project Euler - Problem #34 : https://projecteuler.net/problem=34

"""
Find the sum of all numbers which 
are equal to the sum of the factorial of their digits.
"""
from math import factorial

n = 9
sums = 0
while n < factorial(9)*3:
	n+= 1
	if sum(map(factorial,map(int,str(n)))) == n:
		sums += n
print sums