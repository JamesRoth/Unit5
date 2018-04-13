#James Roth
#4/13/18
#middleWord.py - printing the middle word of a list

words=input("Enter some words: ").split(" ")

if len(words)%2==0:
    print(words[len(words)/2-1], words[len(words)/2])
