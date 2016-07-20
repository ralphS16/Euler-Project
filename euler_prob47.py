#Project Euler - Problem #47 : https://projecteuler.net/problem=47
import math
"""
Find the first four consecutive integers to have 
four distinct prime factors. 
What is the first of these numbers?
"""

def list_prime_factors(num):
	facts = []
	while num % 2 == 0:
		num /= 2
		facts.append(2)
	for i in range(3,int(math.sqrt(num)+1),2):
		while num % i == 0:
			num /= i
			facts.append(i)
		
	if num > 2:
		facts.append(num)
	return facts

def compare_prime_factors(fact1,fact2):
	return len(list(set(fact1)-set(fact2))) >= 4 and len(list(set(fact2)-set(fact1))) >= 4

n = 0
fcons = 0
while not fcons:
	n += 1
	fcons = n
	for i in range(3):
		if not compare_prime_factors(list_prime_factors(n+i),list_prime_factors(n+i+1)):
			fcons = 0
print fcons