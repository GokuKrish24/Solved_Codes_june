def findMaxLength(nums):  
        dic={0:0}
        longest=0
        prefix=0
        for i in range(len(nums)):
            k=1
            if(nums[i]==0):
                k=-1
            prefix+=k
            if(prefix not in dic):
                dic[prefix]=i+1
                continue
            longest=max(longest,i+1-dic[prefix])
        return longest
