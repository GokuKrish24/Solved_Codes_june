def findMaxLength(nums):  
        length=0
        for i in range(len(nums)):
            s=1
            if(nums[i]==0):
                s=-1
            for j in range(i+1,len(nums)):
                if(nums[j]==0):
                    s+=-1
                else:
                    s+=1
                if(s==0):
                    length=max(length,j-i+1)
        return length
'''
[1 1 1 1 0 1 1 1 1 0 ]
[0 1 2 3 4 3 4 5 6 7 6]
'''
