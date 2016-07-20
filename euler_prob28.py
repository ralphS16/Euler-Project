# Project Euler - Problem #28 : https://projecteuler.net/problem=28

n = 1
sums = 1
side = 2
bigside = 1001
for i in range((bigside-1)/2):
	for j in range(4):
		n = n+side
		sums += n
	side += 2
print sums