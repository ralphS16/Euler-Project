# Project Euler - Problem #19 : https://projecteuler.net/problem=19

"""
You are given the following information, but you may 
prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month 
during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
MONTHS = ['January','February','March','April','May','June','July','August','September','October','November','December']
NMONTHS = [31,-1,31,30,31,30,31,31,30,31,30,31]
ONEDAY = (1,'January',1900,'Monday')

def n_in_month(month,year):
	if NMONTHS[MONTHS.index(month)] == -1:
		if is_leap(year):
			return 29
		else:
			return 28
	else:
		return NMONTHS[MONTHS.index(month)]

def is_leap(year):
	if year%4 == 0:
		if year %100 != 0:
			return True
		elif year%400 == 0:
			return True
		else:
			return False
	else:
		return False

def day_plus_num(day,num):
	tot = DAYS.index(day)
	tot += num
	return DAYS[tot%7]

def days_to_end_month(date):
	#date = (num,month,year)
	return n_in_month(date[1],date[2])-date[0]+1

def days_to_end_year(date):
	#date = (num,month,year)
	total_days = days_to_end_month(date)
	for i in MONTHS[MONTHS.index(date[1])+1:]:
		total_days += n_in_month(i,date[2])
	return total_days

def days_in_year(year):
	total_days = 0
	for i in MONTHS:
		total_days += n_in_month(i,year)
	return total_days

def days_between(date1,date2):
	#date = (num,month,year)
	if date2[2] > date1[2]:
		# this calculates the days between two dates in different years
		days_in_year1 = days_to_end_year(date1)
		days_in_year2 = days_in_year(date2[2]) - days_to_end_year(date2)
		total_days = days_in_year1 + days_in_year2
		for i in range(date1[2]+1,date2[2]):
			total_days += days_in_year(i)
		return total_days
	elif date2[2] == date1[2]:
		return days_to_end_year(date1) - days_to_end_year(date2)
		

def first_of_month_between(day,date1,date2):
	if date2[2] > date1[2]:
		# this calculates the number of first days between two dates in different years
		first_day_in_year1 = first_of_month_in_year(day,fjan(date1[2]),date1[2],date1[1])
		first_day_in_year2 = first_of_month_in_year(day,fjan(date2[2]),date2[2],'January',date2[1])
		total_first_days = first_day_in_year1 + first_day_in_year2
		for i in range(date1[2]+1,date2[2]):
			total_first_days += first_of_month_in_year(day,fjan(i),i)
		return total_first_days
	elif date2[2] == date1[2]:
		return first_of_month_in_year(day,fjan(date1[2]),date1[2],date1[1],date2[1])

def fjan(year):
	date1 = ONEDAY[:-1]
	oneday = ONEDAY[-1]
	date2 = (1,'January',year)
	newday = day_plus_num(oneday,days_between(date1,date2))
	return newday
	

def first_of_month_in_year(day,day_fjan,year,start = 'January',end = 'December'):
	date1 = (1,'January',year)
	first_days = []
	start = MONTHS.index(start)
	end = MONTHS.index(end)
	for i in MONTHS[start:end+1]:
		date2 = (1,i,year)
		first_days.append(day_plus_num(day_fjan,days_between(date1,date2)))
	return sum([1 for i in first_days if i == day])

print first_of_month_between('Sunday',(1,'January',1901),(31,'December',2000))