#James Roth
#4/23/18
#longestWord.py - prints the longest word in a list

words=input("Enter some words: ").split(" ")

longest=""
for item in words:
    if len(item)>=len(longest):
        longest=item
print(longest)
