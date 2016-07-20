#Project Euler - Problem #4 : https://projecteuler.net/problem=4
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def ispal(num):
	text = str(num)
	pal = True
	for i in range(int(len(text)/2)):
		if text[i] != text[-1*i-1]:
			pal = False
	return pal
bigpal = 0 
for i in range(1000):
	for j in range(1000):
		if ispal(i*j):
			if bigpal < i*j:
				bigpal = i*j
print bigpal