#Project Euler - Problem #25 : https://projecteuler.net/problem=25
"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
fibo = [1,1]
while len(str(fibo[-1])) <1000:
	fibo.append(fibo[-1]+fibo[-2])
print fibo.index(fibo[-1])