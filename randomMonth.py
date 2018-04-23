#James Roth
#4/23/18
#randomMonth.py - prints a random month

from random import randint

months=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]
print(months[randint(0,len(months)-1)])
