list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
x=len(list1)
for n in range(int(x/2)):
    swap=list1[n]
    list1[n]=list1[int(x/2)+n]
    list1[int(x/2)+n]=swap
print(list1)

number=int(input("input a number: "))
for n in range(number):
    print(n)
    
