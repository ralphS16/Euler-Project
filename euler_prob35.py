# Project Euler - Problm #34 : https://projecteuler.net/problem=34

"""
The number, 197, is called a circular prime because 
all rotations of the digits: 
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
f = open("listprimes.txt","rU")
primes = []
read = 0
while read < 1000000:
	read = int(f.readline())
	primes.append(read)

def permutations(list):
	perms = []
	for i in range(len(list)):
		perms.append(list[i:]+list[:i])
	return perms

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
			
def is_circular(p):
	if [False for i in map(int,str(p)) if i == 0 or i ==2 or i == 4 or i == 5 or i == 6 or i == 8] == [False]*len(map(int,str(p))):
		return False
	else:
		for i in permutations(map(int,str(p))):
			perm_num = int(''.join(map(str,i)))
			if not binary_search(perm_num,primes,0,len(primes)-1):
				return False
		return True

num_circ = 0
next = 100
i = 11
while i < 1000000:
	if binary_search(i,primes,0,len(primes)-1):
		if is_circular(i):
			num_circ += 1
	i+= 2
print num_circ +4