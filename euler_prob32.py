# Project Euler - Problem #32 : https://projecteuler.net/problem=32

"""
Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.
"""

def is_pandigital(multiplicand,multiplier,product):
	digs = [0,0,0,0,0,0,0,0,0] #1,2,3,4,5,6,7,8,99
	if not 0 in map(int, str(multiplicand)+str(multiplier)+str(product)):
		for i in map(int, str(multiplicand)):
			digs[i-1] += 1
		for i in map(int, str(multiplier)):
			digs[i-1] += 1
		for i in map(int, str(product)):
			digs[i-1] += 1
		if digs == [1 for i in range(9)]:
			print multiplicand,multiplier,product
			return product
		else:
			return 0
	else:
		return 0
def single_digital(n):
	digs = map(int, str(n))
	if sorted(list(set(digs))) == sorted(digs):	
		return True
	else:
		return False

pands = []
for i in range(1,2500):
	for j in range(1,600):
		if single_digital(i) and single_digital(j) and not list(set(str(i)) & set(str(j))):
			pands.append(is_pandigital(i,j,i*j))
print sum(list(set(pands)))
print list(set(pands))