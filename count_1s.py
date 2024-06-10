    def findMaxConsecutiveOnes(nums):
        curr=0
        maxc=0
        for i in range(len(nums)):
            if(nums[i]==1):
                curr+=1
                maxc=max(curr,maxc)
            else:
                curr=0
        return maxc
