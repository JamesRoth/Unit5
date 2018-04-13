#James Roth
#4/13/18
#middleWord.py - printing the middle word of a list

words=intput("Enter some words: ").split(" ")

if len(words)%2==0:
    print(words[len(words)/2], words[len(words)/2+1])
