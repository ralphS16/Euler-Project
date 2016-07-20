#Project Euler - Problem #5 - https://projecteuler.net/problem=5

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
found = False
num = 2520
while not found:
	num+=20
	found = True
	for j in range(1,21):
		if num % j != 0:
			found = False
print num