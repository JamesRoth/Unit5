#James Roth
#4/23/18
#fwordDemo.py - printing words with an f in them

words=input("Enter some words: ").split(" ")

for item in words:
    if "f" in item or "F" in item:
        print(item)
