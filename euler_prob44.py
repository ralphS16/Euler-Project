#Project Euler - Problem #44 : https://projecteuler.net/problem=44
import math
pent_pairs = []
def distance(t):
	return t[1]-t[0]

def is_pentagonal(n):
	return (math.sqrt(24*n+1)+1)%6 == 0

def parse_pairs(list_pairs):
	for i in list_pairs:
		if is_pentagonal(i[1]-i[0]) and is_pentagonal(i[1]+i[0]):
			print i
			return i[1]-i[0]
	return 0
#Generate Pentagon Numbers
pent = [(n*(3*n-1))/2 for n in range(1000,3000)]

#Generate Pentagon Pairs

for i in pent:
	for j in pent:
		if i != j and is_pentagonal(abs(i-j)) and is_pentagonal(i+j):
			pent_pairs.append((i,j))

print sorted(pent_pairs, key=distance)