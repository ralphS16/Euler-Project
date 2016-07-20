# Project Euler - Problem #9 : https://projecteuler.net/problem=9
import math
for a in range(1,500):
	for b in range(1,500):
		if a + b + math.sqrt(a**2+b**2) == 1000:
			print a,b, math.sqrt(a**2+b**2), a*b*math.sqrt(a**2+b**2)
