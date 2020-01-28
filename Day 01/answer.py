a=[]
nums=int(input('How many numbers in list a: '))
for i in range(nums):
    numbers=int(input('Enter the numbers: '))
    a.append(numbers)
    a.sort()
print(a)
b=[]
numz=int(input('How many numbers in list b: '))
for i in range(numz):
    numbers=int(input('Enter the numbers: '))
    b.append(numbers)
    b.sort()
print(b)

##for median of a:
y=len(a)
x=(y%2)

if x == 0:  
    mid=(y//2)   
    d=int(a[mid])
    e=int(a[mid-1])
    median_1=(d+e)/2
    print('The median of the list a is ', median_1)
else:
    mid=(y//2) 
    median_1=int(a[mid])
    print('The median of the list a is ', median_1)
    
##for median of b:
y=len(b)
x=(y%2)

if x == 0:  
    mid=(y//2)   
    d=int(b[mid])
    e=int(b[mid-1])
    median_2=(d+e)/2
    print('The median of the list b is ', median_2)
else:
    mid=(y//2) 
    median_2=int(b[mid])
    print('The median of the list b is ', median_2)

median =((median_1 + median_2)/2)
print('The median of the two sorted lists is ', median)
