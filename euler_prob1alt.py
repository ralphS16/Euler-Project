# Project Euler : Problem 1 ->https://projecteuler.net/problem=1 One Line code
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time
restime = []
for j in range(10):
	time1 = time.clock()
	sumres = sum([x for x in range(1000) if x%3==0 or x%5==0])
	time2 = time.clock()
	restime.append(time2-time1)

print sumres
print sum(restime)/float(len(restime))