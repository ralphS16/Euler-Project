# Project Euler - Problem #40 : https://projecteuler.net/problem=40

digs = 1
num = 0
prod = 1
while digs < 1000000:
	num += 1
	digits = range(digs,digs+len(str(num)))
	if 1 in digits:
		prod *= int(str(num)[digits.index(1)])
	if 10 in digits:
		prod *= int(str(num)[digits.index(10)])
	if 100 in digits:
		prod *= int(str(num)[digits.index(100)])
	if 1000 in digits:
		prod *= int(str(num)[digits.index(1000)])
	if 10000 in digits:
		prod *= int(str(num)[digits.index(10000)])
	if 100000 in digits:
		prod *= int(str(num)[digits.index(100000)])
	if 1000000 in digits:
		prod *= int(str(num)[digits.index(1000000)])
	digs += len(str(num))

print prod