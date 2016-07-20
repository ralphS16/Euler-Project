# Project Euler - Problem #14 : https://projecteuler.net/problem=14

"""
n is even : n/2
n is odd: 3n + 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
"""
i = 100000
bigtots = 0
while i < 1000001:
	nxt = i
	tots = 0
	while nxt != 1:
		tots += 1
		if nxt % 2 == 0:
			nxt /= 2
		else:
			nxt = 3*nxt + 1
	if tots > bigtots:
		bigtots = tots
		bigtotn = i
	i += 1

print bigtots
print bigtotn