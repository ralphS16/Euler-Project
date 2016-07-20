# Project Euler - Problem#20 : https://projecteuler.net/problem=20
"""
Find the sum of the digits in 100!
"""

def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

digits = [int(i) for i in str(fact(100))]
print sum(digits)