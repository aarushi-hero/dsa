# Square of Sorted Array

#Brute force
lst=list(map(int,input("Enter list of numbers").split()))
squaredList=[]
for i in range(len(lst)):
    squaredList.append(lst[i]**2)
    
squaredListA=sorted(squaredList)
print(squaredListA)


#2pointer approach
lst1 = list(map(int, input("Enter list: ").split()))

pos = []
neg = []

for i in range(len(lst1)):
    if lst1[i] < 0:
        neg.append(lst1[i] * lst1[i])
    else:
        pos.append(lst1[i] * lst1[i])

neg.reverse()  # ✅ move here

i = 0
j = 0
squared = []

while i < len(pos) and j < len(neg):
    if pos[i] <= neg[j]:
        squared.append(pos[i])
        i += 1
    else:
        squared.append(neg[j])
        j += 1

while i < len(pos):
    squared.append(pos[i])
    i += 1

while j < len(neg):
    squared.append(neg[j])
    j += 1

print(squared)


#Sort 2 arrays in correct order in new array using 2 pointer approach
lst1 = list(map(int, input("Enter list 1: ").split()))
lst2 = list(map(int, input("Enter list 2: ").split()))

i = 0
j = 0
new = []

while i < len(lst1) and j < len(lst2):
    if lst1[i] <= lst2[j]:
        new.append(lst1[i])
        i += 1
    else:
        new.append(lst2[j])
        j += 1

# Add remaining elements
while i < len(lst1):
    new.append(lst1[i])
    i += 1

while j < len(lst2):
    new.append(lst2[j])
    j += 1

print(new)
