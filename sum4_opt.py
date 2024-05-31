nums=[1,0,-1,0,-2,2]
# [-2,-1,0,0,1,2]
nums.sort()
ans=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        k=j+1
        l=len(nums)-1
        while(k<l):
            if(nums[i]+nums[j]+nums[k]+nums[l]>0):
                l-=1
            elif(nums[i]+nums[j]+nums[k]+nums[l]<0):
                k+=1
            else:
                an=[nums[i],nums[j],nums[k],nums[l]]
                an.sort()
                l-=1
                k+=1
                if(an not in ans):
                    ans.append(an)
                while(k<l and nums[k]==nums[k-1]):
                    k+=1
                while(k<l and nums[l]==nums[l+1]):
                    l-=1
print(ans)
