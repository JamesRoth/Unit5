#James Roth
#5/7/18
#quiz5.py

def penultimate(list):
    return(list[-2])
    
def plusEquals(list, num):
    for i in range(0,len(list)):
        list[i]+=num

def smallest(list):
    small=list[0]
    for i in range(1,len(list)):
        if list[i]<small:
            small=list[i]
