#Project Euler - Problem #26 : https://projecteuler.net/problem=26
"""
Find the value of d < 1000 for which 1/d contains 
the longest recurring cycle in its decimal fraction part.
"""
def find_recurring(num,denom):
	found = False
	mods = []
	while not found:
		if num < denom:
			num*= 10
		else:
			num -= int(num/denom)*denom
			if num == 0:
				found = True
				recc = []
			elif num in mods:			
				found = True
				recc = mods[mods.index(num):]
			else:
				mods.append(num)
	return recc
bignum = 0
biglen = 0
for i in range(2,1000):
	if  len(find_recurring(1,i)) > biglen:
		biglen = len(find_recurring(1,i))
		bignum = i
print bignum, biglen