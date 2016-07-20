# Project Euler - Problem #15 : https://projecteuler.net/problem=15

"""
Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?
"""

initGrid = [20,20] #moves [left,down]
def find_paths(grid):
	if grid[0] == grid[1]:
		table = [[0 if i != 0 and i != grid[0]+2 else -1 for i in range(grid[0]+3)] if j != 0 and j != grid[0]+2 else [-1 for i in range(grid[0]+3)] for j in range(grid[1]+3)] #leaves a zero line around the whole table
		# first move gives only one option left and one option right
		table[1][2] = 1
		table[2][1] = 1
		blocked = False
		print()
		ntable = list(table)
		while not blocked:
			table = list(ntable)
			for i,rows in enumerate(table):
				for j,case in enumerate(rows):
					blocked = True
					if case >=1:
						if table[i+1][j] != -1:
							ntable[i+1][j] += table[i][j]
							blocked = False
						if table[i][j+1] != -1:
							ntable[i][j+1] += table[i][j]
							blocked = False
						if not blocked:
							ntable[i][j] = 0
		return ntable[-2][-2]
					

def print_table(listx):
	"""returns a grid of a list of lists of numbers list of list -> grid"""
	for lists in listx:
		for i in lists:
			print str(i) , '\t',
		print()


print find_paths(initGrid)