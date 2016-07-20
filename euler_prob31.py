# Project Euler - Problem #31 : https://projecteuler.net/problem=31
"""
How many different ways can 2 pounds be made using any number of coins?
"""
def find_comb(valid_coins,value):
	combs = []
	if len(valid_coins) > 1:
		if value == 0:
			return  [[0]+j for j in find_comb(valid_coins[1:],value) if j[-1] != -1]
		for i in range(value/valid_coins[0]+1):
			combs += [[i]+j for j in find_comb(valid_coins[1:],value-i*valid_coins[0]) if j[-1] != -1]
		return combs
	else:
		if value == 0:
			return [[0]]
		elif value/valid_coins[0] != 0 and not value%valid_coins[0]:
			return [[value/valid_coins[0]]]
		else:
			return [[-1]]

coins = [1,2,5,10,20,50,100,200] #value of coins in pences
print len(find_comb(coins,200))
