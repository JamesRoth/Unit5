#James Roth
#4/25/18
#dictionaryDemo.py - more list practice

words=["computer", "mortify", "dog", "firetruck", "yes", "python", "cat"]

words.sort()

num=int(input("What number word do you want? "))

if num<1 or num>len(words):
    print("Invalid number")
else:
    print(words[num-1])
