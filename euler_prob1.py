# Project Euler : Problem 1 ->https://projecteuler.net/problem=1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
restime = []
for j in range(10):
	time1 = time.clock()
	res = []
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			res.append(i)

	sumres = sum(res)
	time2 = time.clock()
	restime.append(time2-time1)

print sumres
print sum(restime)/float(len(restime))
