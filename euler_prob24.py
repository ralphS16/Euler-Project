#Project Euler - Problem #24 : https://projecteuler.net/problem=24

"""
What is the millionth lexicographic permutation 
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

def lexicographic(digs):
	if len(digs) == 1:
		return digs
	else:
		perms = []
		for i in digs:
			for j in lexicographic(list(set(digs)-set([i]))):
				if type(j) == list:
					perms.append([i]+j)
				else:
					perms.append([i,j])
		return perms
print sorted(lexicographic([0,1,2,3,4,5,6,7,8,9]))[1000000-1]
	