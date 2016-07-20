#Project Euler - Problem #27 : https://projecteuler.net/problem=27

"""
n^2 + an + b, where |a| < 1000 and |b| < 1000
Find the product of the coefficients, a and b, for the 
quadratic expression that produces the maximum number 
of primes for consecutive values of n, starting with n = 0.
"""


primes = [2,3,5]
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
# print primes[-1]
bign = 0
for a in range(-999,1000):
	for b in list(set(range(a,1000)) & set(primes)):
		n = 0
		prime = True
		while prime:
			quad = n**2+a*n+b
			if  quad > 1 and quad%2 != 0 and quad%3 != 0 and quad%5 != 0 and quad in primes[3:]:
				n+=1
			else:
				prime = False
		if n > bign:
			print "Done:", n, a,b
			bign = n
			coeff = (a,b)
print coeff