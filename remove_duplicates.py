def removeDuplicates(nums):
        i=0
        n=len(nums)
        j=0
        while(i<n):
            if(i==0):
                i+=1
                j+=1
                continue
            while(i<n and nums[i]==nums[i-1]):
                i+=1
            if(i>=n):
                break
            nums[j]=nums[i]
            j+=1
            i+=1
        return j
