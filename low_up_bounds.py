def searchRange(nums, target):
        def binaryup(start,end,arr,target,high):
            if(start<=end):
                mid=(start+end)//2
                if(arr[mid]==target):
                    return binaryup(mid+1,end,nums,target,mid)
                elif(arr[mid]>target):
                    return binaryup(start,mid-1,nums,target,high)
                else:
                    return binaryup(mid+1,end,nums,target,high)
            return high
        def binarydown(start,end,arr,target,down):
            if(start<=end):
                mid=(start+end)//2
                print(start,end)
                print(mid)
                if(arr[mid]==target):
                    return binarydown(start,mid-1,nums,target,mid)
                elif(arr[mid]>target):
                    return binarydown(start,mid-1,nums,target,down)
                else:
                    return binarydown(mid+1,end,nums,target,down)
            return down
        return [binarydown(0,len(nums)-1,nums,target,-1),binaryup(0,len(nums)-1,nums,target,-1),]

nums=[5,7,7,8,8,10]
target=8
print(searchRange(nums,target))
