#Project Euler - Problem #45 : https://projecteuler.net/problem=45
import math
def is_pentagonal(n):
	return (math.sqrt(24*n+1)+1)%6 == 0

def is_triangle(n):
	return int(math.sqrt(2*n)) * int(math.sqrt(2*n)+1) == 2*n

def is_hexagonal(n):
	return (math.sqrt(8*n+1)+1)%4 == 0
n = 144
next = 0
while not next:
	if is_pentagonal(n*(2*n-1)) and is_triangle(n*(2*n-1)):
		next = n*(2*n-1)
	n+=1
print next