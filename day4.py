3 sum
#Brute force
nums = [-1,0,1,2,-1,-4]
res=[]
i=0
j=1
nums.sort()

while(i<j):
    for j in range(len(nums)):
        c = nums[i] + nums[j]
        for item in range(len(nums)):
            if nums[item] == -c:
                triplet = [nums[i], nums[j], nums[item]]
                if triplet not in res:   # avoid duplicates
                    res.append(triplet)
        i += 1
        j += 1

print(res)

