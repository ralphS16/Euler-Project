#Project Euler - Problem #23: https://projecteuler.net/problem=23
"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that 
cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
def divisors(n):
	div = [1]
	for i in range(2,int(math.sqrt(n))+1):
		if n%i == 0:
			div.append(i)
			div.append(n/i)
	return list(set(div))

def d(n):
	return sum(divisors(n))

abundants = []
for i in range(1,28123):
	if d(i) > i:
		abundants.append(i)
print len(abundants)

numbers = range(28123)
for j in abundants:
	for i in abundants:
		if i+j <28123:
			numbers[i+j] = 0
print sum(numbers)