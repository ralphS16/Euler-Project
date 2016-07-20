#Project Euler - Problem #18 : https://projecteuler.net/problem=18
import re

def first_sums(line,nxline):
	sums = []
	if len(nxline) == len(line)+1:
		for idx,i in enumerate(line):
			sums.append(i+nxline[idx])
			sums.append(i+nxline[idx+1])
	return sums

def calc_sums(triangle,sums,A,B):
	newsum = []
	for idx,i in enumerate(triangle[-1]):
		newsum += [j+i for j in sums[idx*A:idx*A+B]]

	if len(triangle) != 1:
		return calc_sums(triangle[:-1],newsum,A*2,B*2)
	else:
		return newsum

f = open("inputeuler_prob18.txt","rU")
triangle = []

for line in f:
	matches = re.findall('\d\d',line)
	triangle.append(map(int,matches))


triangle_sums = calc_sums(triangle[:-2],first_sums(triangle[-2],triangle[-1]),2,4)
print max(triangle_sums)