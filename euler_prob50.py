#Project Euler - Problem #50 : https://projecteuler.net/problem=50

def binary_search(n,list, imin, imax):
	if imax <= imin:
		return False
	else:
		imid = (imax-imin)/2+imin
		if list[imid] > n:
			return binary_search(n,list,imin,imid-1)
		elif list[imid] < n:
			return binary_search(n,list,imid+1,imax)
		else:
			return True	

f = open("listprimes.txt","rU")
primes = map(int,f.readlines())

primes = primes[:primes.index(1000003)]

biggest = 1
terms = 1
while biggest > 0:
	million = False
	for i in range(len(primes)-terms-1):
		if sum(primes[i:i+terms]) < 1000000:
			if binary_search(sum(primes[i:i+terms]),primes,0,len(primes)):
				biggest = sum(primes[i:i+terms])
			million = True
	if not million:
		biggest = 0 - biggest
	terms+=1
print biggest