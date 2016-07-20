# Project Euler - Problem #38 : https://projecteuler.net/problem=38

def is_pan(n):
	digs = [0,0,0,0,0,0,0,0,0]
	if not 0 in map(int,str(n)):
		for i in map(int,str(n)):
			digs[i-1] += 1
		if digs == [1 for i in range(9)]:
			return True
		else:
			return False
	else:
		return False

def max_pan(n):
	maxed = False
	coef = 1
	string = ""
	laststring = ""
	while not maxed:
		string += str(coef*n)
		coef += 1
		if len(string) > 9:
			maxed = True
		else:
			laststring = string
	return int(laststring) 

num = 1
big_pan = 1
while num < 50000:
	m_pan = max_pan(num)
	if is_pan(m_pan) and m_pan > big_pan:
		big_pan = m_pan
	num += 1

print max_pan(9)
print is_pan(max_pan(9))
print big_pan
