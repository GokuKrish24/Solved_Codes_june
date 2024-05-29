def majorityElement(nums):
        d={}
        ans=[]
        for i in range(len(nums)):
            if(len(ans)==2):
                break
            if(nums[i] not in ans):
                if(nums[i] not in d):
                    d[nums[i]]=0
                d[nums[i]]+=1
                if(d[nums[i]]>len(nums)/3):
                    ans.append(nums[i])
        return ans
