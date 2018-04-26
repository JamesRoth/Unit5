#James Roth
#4/25/18
#stat.py - median, mode, min, max, and mean of a list

numbers=[]

while True:
    num=input("Enter a number to add to a list, type q when finished. ")
    if num == "q":
        break
    numbers.append(str(num))
print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Mean: ", sum(numbers)/len(numbers))
