#Project Euler - Problem #6: https://projecteuler.net/problem=6


sum = 0
sums = 0
for i in range(1,101):
	sum += i
	sums += i**2
	
print sum**2-sums