#Project Euler - Problem #49 : https://projecteuler.net/problem=49
from itertools import permutations

def binary_search(n,list, imin, imax):
	if imax < imin:
		return False
	else:
		imid = (imax-imin)/2+imin
		if list[imid] > n:
			return binary_search(n,list,imin,imid-1)
		elif list[imid] < n:
			return binary_search(n,list,imid+1,imax)
		else:
			return True	
def distance(tup):
	return abs(tup[1]-tup[0])

f = open("listprimes.txt","rU")
primes = map(int,f.readlines())

n = primes.index(1009)
all_perms = []
while primes[n] < 10000:
	perms = []
	for i in map(int,map("".join,permutations(str(primes[n])))):
		if binary_search(i,primes,0,len(primes)) and i > 999:
			perms.append(i)
	perms = sorted(list(set(perms)))
	if len(perms) >= 3 and not perms in all_perms:
		all_perms.append(perms)
	n += 1

for perm in all_perms:
	perm_pairs = []
	for i in perm:
		for j in perm:
			if i != j and (j,i) not in perm_pairs:
				perm_pairs.append((i,j))
	perm_pairs_distance = map(distance,perm_pairs)
	for i in range(len(perm_pairs_distance)):
		j = perm_pairs_distance.index(perm_pairs_distance[i])
		if j != i:
			if len(list(set(perm_pairs[i]) & set(perm_pairs[j]))):
				print perm_pairs[i],perm_pairs[j]
			
			
	