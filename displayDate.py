#James Roth
#4/23/18
#displayDate.py - current date with words

from datetime import *

today=date.today()

days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]

print("Today is", days[today.weekday()] + ",", months[today.month], today.day, today.year)
