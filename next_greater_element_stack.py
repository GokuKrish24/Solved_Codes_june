class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:  
        stack=[]
        n=len(nums)
        ans=[-1]*n
        if(n==0 or n==1):
            if(n==0):
                return []
            return[-1]
        for i in range(n*2-1,-1,-1):
            while(len(stack)!=0 and nums[i%n]>=stack[-1]):
                stack.pop()
            if(i<n):
                if(len(stack)==0):
                    ans[i]=-1
                else:
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans
