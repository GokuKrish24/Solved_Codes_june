def majorityElement(nums):
        ele1=float('-inf')
        ele2=float('-inf')
        cnt1=0
        cnt2=0
        for i in range(len(nums)):
            if(cnt1==0 and ele2!=nums[i]):
                cnt1+=1
                ele1=nums[i]
                continue
            elif(cnt2==0 and ele1!=nums[i]):
                cnt2+=1
                ele2=nums[i]
                continue
            elif(nums[i]==ele1):
                cnt1+=1
            elif(nums[i]==ele2):
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for i in range(len(nums)):
            if(ele1==nums[i]):
                cnt1+=1
            elif(ele2==nums[i]):
                cnt2+=1
        ans=[]
        if(cnt1>len(nums)/3):
            ans.append(ele1)
        if(cnt2>len(nums)/3):
            ans.append(ele2)
        return ans
