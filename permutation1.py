def permute(nums):
        res=[]
        des=[]
        n=len(nums)
        def permu(nums,n):
            if(len(des)==n):
                res.append(des[:])
                return
            for i in range(len(nums)):
                k=nums.pop(i)
                des.append(k)
                permu(nums,n)
                des.pop()
                nums.insert(i,k)
        permu(nums,n)
        return res
