def atmost(nums,goal):
    prefix=0
    i=0
    j=0
    count=0
    while(j<len(nums)):
        prefix+=nums[j]
        while(prefix>goal and i<=j):
            print(prefix,goal)
            prefix-=nums[i]
            i+=1
        count+=j-i+1
        j+=1
    return count
nums=[0,0,0,0,0]
goal=0
print(atmost(nums,goal)-atmost(nums,goal-1))
