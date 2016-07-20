# Project Euler - Problem #43 : https://projecteuler.net/problem=43

import itertools
primes = [2,3,5,7,11,13,17]
pands = [i for i in sorted(itertools.permutations([0,1,2,3,4,5,6,7,8,9])) if i[0] != 0]

sums = 0
for p in pands:
	to_add = True
	for i in range(7):
		if (p[i+1]*100 + p[i+2]*10 + p[i+3]) % primes[i] != 0:
			to_add = False
	if to_add:
		sums += int("".join(map(str,p)))
print sums