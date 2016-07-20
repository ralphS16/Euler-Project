# Project Euler - Problem #33 : https://projecteuler.net/problem=33

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to 
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
def simple_fraction(frac):
	num, denum = frac
	snum = str(num)
	sdenum = str(denum)
	if not "0" in snum+sdenum:
		for i in range(2):
			for j in range(2):
				if snum[i] == sdenum[j] and snum[i] != "0" and float(snum[2/(i+1)-1])/float(sdenum[2/(j+1)-1]) == float(num)/float(denum):
					return True
	return False

simple_fractions = []
for i in range(10,100):
	for j in range(i+1,100):
		if simple_fraction((i,j)):
			simple_fractions.append((i,j))


num = 1
denum = 1
for i,j in simple_fractions:
	print "%s/%s" %(i,j)
	num*=i
	denum*=j
print "\nGives : %s/%s" %(num,denum)