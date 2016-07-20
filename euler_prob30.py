# Project Euler - Problem #30 : https://projecteuler.net/problem=30
"""
Find the sum of all the numbers that can be 
written as the sum of fifth powers of their digits.
"""

allsum = 0
for i in range(1,9**5*4):
	sums = 0
	for j in map(int,str(i)):
		sums += j**5
	if sums == i:
		print i
		allsum += i
print allsum