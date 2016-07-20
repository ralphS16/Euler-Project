#Project Euler - Problem #48 : https://projecteuler.net/problem=48

sums = 0
for i in range(0,1001):
	sums += i**i
print str(sums)[-10:]