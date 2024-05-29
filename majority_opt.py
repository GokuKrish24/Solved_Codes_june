nums=[2,2,1,1,1,2,2]
element=nums[0]
count=1
for i in range(1,len(nums)):
    if(count==0):
        element=nums[i]
        count+=1
        continue
    if(nums[i]==element):
        count+=1
    else:
        count-=1
print(element)
