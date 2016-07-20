#Project Euler - Problem #17: https://projecteuler.net/problem=17

"""
If the numbers 1 to 5 are written out in words: one, two, three, 
four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 
(three hundred and forty-two) contains 23 letters and 115 
(one hundred and fifteen) contains 20 letters. The use of 
"and" when writing out numbers is in compliance with British usage.
"""

units = ['','one','two','three','four','five','six','seven','eight','nine']
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen', 'seventeen','eighteen','nineteen']
tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', 'eighty','ninety']
hundred = 'hundred'
thousand = 'thousand'
def num_to_word(num):
	word = ""
	if num < 10:
		word = units[num]
	elif num < 20:
		word = teens[-20+num]
	elif num < 100:
		word = tens[int(num/10)] + units[num-int(num/10)*10]
	elif num < 1000:
		word = units[int(num/100)] + 'hundredand' + num_to_word(num-int(num/100)*100)
	elif num == 1000:
		word = units[1] + thousand
	return word

sum = 0
for i in range(1,1001):
	print num_to_word(i)
	sum += len(num_to_word(i))
print sum
	
