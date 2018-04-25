#James Roth
#4/25/18
#warmup13.py

from random import randint

numbers=[]

for i in range(1,21):
    numbers.append(randint(1,100))

print(sum(numbers))
print(min(numbers))
print(max(numbers))
