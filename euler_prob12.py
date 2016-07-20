# Project Euler - Problem #12 : https://projecteuler.net/problem=12

"""
The sequence of triangle numbers is generated by adding the natural numbers.
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?
"""
import math
def list_div(num):
	divs = 0
	for i in range(1,int(math.sqrt(num))+1):
		if num % i == 0:
			divs += 2
	return divs

ndiv = 500
count = 0
found = False
while not found:
	count += 1
	trinum = sum(range(count+1))
	if list_div(trinum) > ndiv:
		found = True

print trinum
	