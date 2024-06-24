def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        ans=[]
        for i in range(len(nums)):
            if(len(ans)!=0 and ans[0]==i-k):
                ans.pop(0)
            while(len(ans)!=0 and nums[ans[-1]]<=nums[i]):
                ans.pop()
            ans.append(i)
            if(i>=k-1):
                res.append(nums[ans[0]])
        return res
