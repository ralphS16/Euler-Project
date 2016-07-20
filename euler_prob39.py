# Project Euler - Problem #39 : https://projecteuler.net/problem=39

perim = [0 for i in range(1001)]
for p in range(1001):
	for a in range(int(p/2)+1):
		for b in range(p-a):
			c = (a**2+b**2)**(0.5)
			if c.is_integer():
				if a + b + c == p:
					perim[p] += 1
print perim.index(max(perim))
