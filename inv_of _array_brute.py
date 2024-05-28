nums=[5,4,3,2,1]

count=0
lcount=0
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if(nums[j]<nums[i]):
            count+=1
    if(nums[i]>nums[i+1]):
        lcount+=1
print(count)
print(lcount)
