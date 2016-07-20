# Project Euleur - Problem #36 : https://projecteuler.net/problem=36
import math

def ispal(text):
	pal = True
	for i in range(int(len(text)/2)):
		if text[i] != text[-1*i-1]:
			pal = False
	return pal

def b10_to_b2(n):
	binary = ""
	pow = int(math.log(n,2))
	while pow >= 0:
		if n >= 2**pow:
			n -= 2**pow
			binary += "1"
		else:
			binary += "0"
		pow -= 1
	return binary

sums = 0

for i in range(1,1000000):
	if ispal(str(i)) and ispal(b10_to_b2(i)):
		sums += i
print sums