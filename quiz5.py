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
    i=num1
    while i<num2:
        list1.append(i)
        i+=num3
    return(list1)

print(penultimate([1,2,3,4]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
print(decimalRange(4,10,0.5))
