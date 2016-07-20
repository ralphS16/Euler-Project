# Project Euler - Problem #11 : https://projecteuler.net/problem=11

import re
f = open('.\euler_prob11_table.txt', 'rU')
text = f.read()

match = re.findall(r'\d\d', text)
ind = 0
table = [[0 for i in range(22)] for j in range(22)]
for i in range(22):
	for j in range(22):
		if i == 21 or i == 0 or j == 21 or j == 0:
			table[i][j] = -1
		else:
			table[i][j] = int(match[ind])
			ind += 1
			
# table is a 2-dimensionnal array that contains the table in the file .\euler_prob11_table.txt with zero values sur le contour
bigprod = 0
for i in range(1,21):
	for j in range(1,21):
		prod = [1,1,1,1] #[right,down,down-right,down-left]
		(right,down,down_left,down_right) = (True,True,True,True)
		for k in range(0,4):
			if right:
				prod[0] *= table[i+k][j]
				if table[i+k+1][j] == -1:
					right = False
			if down:
				prod[1] *= table[i][j+k]
				if table[i][j+k+1] == -1:
					down = False
			if down_right:
				prod[2] *= table[i+k][j+k]
				if table[i+k+1][j+k+1] == -1:
					down_right = False
			if down_left:
				prod[3] *= table[i-k][j+k]
				if table[i-k-1][j+k+1] == -1:
					down_left = False
		if max(prod) > bigprod:
			bigprod = max(prod)
			
print bigprod
			
			