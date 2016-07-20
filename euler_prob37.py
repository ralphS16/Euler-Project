# Project Euler - Problem #37 : https://projecteuler.net/problem=37
import math
f = open("listprimes.txt","rU")
primes = []
read = 0
while read < 1000000:
	read = int(f.readline())
	primes.append(read)

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

def is_trunc(p):
	if p > 10:
		if binary_search(p,primes,0,len(primes)-1) and is_trunc(int(str(p)[1:])):
			return True
		else:
			return False
	elif p == 2 or p == 3 or p == 5 or p == 7:
		return True
	else:
		return False

def is_r_trunc(p):
	if p >= 10:
		if binary_search(p,primes,0,len(primes)-1) and is_r_trunc(int(str(p)[:-1])):
			return True
		else:
			return False
	elif p == 2 or p == 3 or p == 5 or p == 7:
		return True
	else:
		return False

sums = 0
num = 9
truncs = 0
while truncs < 11:
	num += 1
	if is_trunc(num) and is_r_trunc(num):
		print num
		truncs += 1
		sums+=num
	if num = 1000000:
		print 
print sums