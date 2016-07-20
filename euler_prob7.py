#Project Euler - Problem #7: https://projecteuler.net/problem=7

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

primes = [2]
nxint = 3
while len(primes) < 10001:
	prime = True
	if nxint%3 != 0 and nxint%5 != 0:
		for i in primes[2:]:
			if nxint % i == 0:
				prime = False
		if prime:
			primes.append(nxint)
	nxint += 2

print primes[-1]