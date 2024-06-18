class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        ans=[-1]*len(A)
        stack=[]
        for i in range(len(A)):
            while(len(stack)!=0 and A[i]<=stack[-1]):
                stack.pop()
            if(len(stack)==0):
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(A[i])
        return ans
        
