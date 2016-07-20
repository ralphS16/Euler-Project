# Project Euler - Problem #3 : https://projecteuler.net/problem=3
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math
def list_prime_factors(num):
	facts = []
	while num % 2 == 0: # commencer par factoriser les deux
		num /= 2
		facts.append(2)
	for i in range(3,int(math.sqrt(num)+1),2):
		while num % i == 0:
			num /= i
			facts.append(i)
		
	if num > 2:
		facts.append(num)
	return facts

print list_prime_factors(600851475143)
		