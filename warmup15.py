#James Roth
#5/4/18
#warmup15.py - doubling numbers in a list

numbers=[8,3,2,6,4,7]

def double(list):
    doubled=[]
    for i in range(0, len(list)):
        doubled.append(list[i]*2)
    print(doubled)

double([4,3,7])
