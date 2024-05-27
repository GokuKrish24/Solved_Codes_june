nums=[1,3,2]

ind=-1
# [2 1 5 4 3 0 0]
n=len(nums)
for i in range(n-1,0,-1):
    if(nums[i-1]<nums[i]):
        ind=i-1
        break
if(ind==-1):
    nums=list(reversed(nums))
else:
    for i in range(n-1,ind,-1):
        if(nums[i]>nums[ind]):
            nums[i],nums[ind]=nums[ind],nums[i]
            break
    for i in range((n-ind)//2):
        nums[ind+1+i],nums[n-i-1]=nums[n-i-1],nums[ind+1+i]
print(nums)

'''
leetcode solution by me
beats 92.5%

ind=-1
n=len(nums)
for i in range(n-1,0,-1):
    if(nums[i-1]<nums[i]):
        ind=i-1
        break
if(ind==-1):
    for i in range(0,n//2):
        nums[i],nums[n-i-1]=nums[n-i-1],nums[i]
else:
    for i in range(n-1,ind,-1):
        if(nums[i]>nums[ind]):
            nums[i],nums[ind]=nums[ind],nums[i]
            break
    for i in range((n-ind)//2):
        nums[ind+1+i],nums[n-i-1]=nums[n-i-1],nums[ind+1+i]
'''
