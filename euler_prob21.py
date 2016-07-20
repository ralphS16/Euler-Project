# Project Euler - Problem#21 : https://projecteuler.net/problem=21
"""
d(n) = sum(divisors of n)
Amical numbers d(a) = b and d(b) = a a!=b
Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n):
	div = []
	for i in range(1,n):
		if n%i == 0:
			div.append(i)
	return div

def d(n):
	return sum(divisors(n))

def is_amicable(a,b):
	if a != b and b<10000:
		if d(b) == a:
			return True
		else:
			return False
	else:
		return False
sums = 0
for i in range(10000):
	if is_amicable(i,d(i)):
		sums += i
print sums