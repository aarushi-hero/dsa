#Brute Force
#Method 1
a = [7, 11, 2, 15]
target = 9

aSort=sorted(a)
for i in range (2):
    if(aSort[i]+aSort[i+1]==target):
        print(aSort[i])
        print(aSort[i+1])
        break
    else:
        print("Not possible")

#Method2
a=list(map(int,input("Enter numbers").split()))

a.sort()

size=len(a)
target = int(input("What is your target value: "))

for i in range(0,size - 1):
    for j in range (1,size-1):
        if(a[i]+a[j]==target):
            print(a[i])
            print(a[j])
        else:
            print("Not found")
#Uisng Dictionary
a = list(map(int, input("Enter list of numbers: ").split()))
target = int(input("Please enter target number: "))

hashMap = {}

for i in range(len(a)):
    complement = target - a[i]
    
    if complement in hashMap:
        print(complement, a[i])
        break
    
    hashMap[a[i]] = i
else:
    print("Not possible")
#Using 2 pointer
a=list(map(int,input("Pls enter the numbers").split()))
target=int(input("Pls enter the target value"))
# #Sorting the array
sortB=sorted(a)
sum=0
i=0
j=len(sortB)-1
while(i<j):
    if(sortB[i]+sortB[j]==target):
        print(sortB[i],sortB[j])
        break
    elif(sortB[i]+sortB[j]<target):
        i+=1
    elif(sortB[i]+sortB[j]>target):  
        j-=1
else:
    print("Not results found")
