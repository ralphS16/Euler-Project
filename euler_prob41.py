# Project Euler - Problem #41 : https://projecteuler.net/problem=41

f = open("listprimes.txt","rU")
text = f.readlines()
primes = map(int,text)


def is_pan(n):
    return sorted(str(n)) == [str(i+1) for i in range(len(str(n)))]

i = 1
big = i
for i in primes:
	if is_pan(i):
		big = i
print big