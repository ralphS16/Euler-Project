# Project Euler - Problem #42 : https://projecteuler.net/problem=42
import re,math

f = open("euler_prob42_words.txt", "rU")
text = f.read()
words = re.findall('[A-Z]+',text)

def sum_letters(word):
	return sum([ord(c)-ord("A")+1 for c in word])

def is_triangle(n):
	return int(math.sqrt(2*n)) * int(math.sqrt(2*n)+1) == 2*n
sums = 0
for w in words:
	if is_triangle(sum_letters(w)):
		sums += 1
print sums