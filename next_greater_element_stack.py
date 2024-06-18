class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        stack=[]
        n=len(nums)
        if(n==0 or n==1):
            if(n==0):
                return []
            return[-1]
        for i in range(n*2-1,-1,-1):
            while(len(stack)!=0 and nums[i%n]>=stack[-1]):
                stack.pop()
            if(len(stack)==0):
                ans.insert(0,-1)
            else:
                ans.insert(0,stack[-1])
            stack.append(nums[i%n])
        return ans[0:n]
