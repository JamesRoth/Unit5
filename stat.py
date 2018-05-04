#James Roth
#4/25/18
#stat.py - median, mode, min, max, and mean of a list

def median(): #finds the median
    numbers.sort()
    if len(numbers)%2==0:
        print("Median: ", (numbers[(len(numbers)-1)/2]+numbers[len(numbers)/2])/2) #if the list has an even length
    else:
        print("Median: ", numbers[(len(numbers)+1)/2-1])

def mode(): #finds the mode of the list
    storeLong=[0,0] #[the number, how many times it occurs]
    for item in numbers:
        num=numbers.count(item)
        if num>storeLong[1]:
            storeLong[0]=item
            storeLong[1]=num
    print("Mode:", storeLong[0])

numbers=[]

while True: #loop for entering numbers into the list
    num=input("Enter a number to add to a list, type q when finished. ")
    if num == "q":
        break
    numbers.append(int(num))
print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Mean: ", sum(numbers)/len(numbers))
median()
mode()