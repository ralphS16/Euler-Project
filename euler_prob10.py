# Project Euler - Problem #10 : https://projecteuler.net/problem=10

primes = [2]
nxint = 3
sum = 0
while primes[-1] < 2000000:
	prime = True
	for i in primes:
		if nxint % i == 0:
			prime = False
			break;
	if prime:
		primes.append(nxint)
		sum += nxint
	nxint += 2
sum += 2
print sum - primes[-1]