#Project Euler - Problem #45 : https://projecteuler.net/problem=45
import math

f = open("listprimes.txt","rU")
primes = map(int,f.readlines())

def is_twice_square(n):
	return math.sqrt(n/2)%1 == 0

odd = 9
smallest = 0
while not smallest:
	if odd not in primes:
		smallest = odd
		for i in primes:
			if i < odd:
				if is_twice_square(odd-i):
					smallest = 0
			else:
				break;
	odd+=2
print smallest