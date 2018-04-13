#James Roth
#4/13/18
#listDemo.py - orint first and last words in a list

words=input("Enter some words: ").split(" ")

print("The first word was: ", words[0])
print("The last word was: ", words[-1])

#print out the list one at a time:

for item in words:
    print(item)
