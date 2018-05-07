#James Roth
#5/7/18
#quiz5.py

def penultimate(list):
    return(list[-2])
    
def plusEquals(list, num):
    for i in range(0,len(list)):
        list[i]+=num
    return(list)

def smallest(list):
    small=list[0]
    for i in range(1,len(list)):
        if list[i]<small:
            small=list[i]
    return(small)

def decimalRange(num1, num2, num3):
    list1=[]
    if num1<num2:
        for i in range(num1, num2, num3):
            list1.append(i)
