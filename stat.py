#James Roth
#4/25/18
#stat.py - median, mode, min, max, and mean of a list

numbers=[]

while True:
    num=int(input("Enter a number to add to a list, type q when finished. "))
    if str(num) == "q":
        break
    numbers.append(num)
