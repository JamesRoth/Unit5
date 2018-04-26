#James Roth
#4/25/18
#stat.py - median, mode, min, max, and mean of a list

def median():
    numbers.sort()
    if len(numbers)%2==0:
        print("Median: ", (numbers[(len(numbers)-1)/2]+numbers[len(numbers)/2])/2) 
    else:
        print("Median: ", numbers[(len(numbers)+1)/2])

numbers=[]

while True:
    num=input("Enter a number to add to a list, type q when finished. ")
    if num == "q":
        break
    numbers.append(int(num))
print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Mean: ", sum(numbers)/len(numbers))
median()
