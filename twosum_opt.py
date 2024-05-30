def twoSum(nums, target):
        nums1=nums.copy()
        nums1.sort()
        left=0
        right=len(nums1)-1
        num1=-1
        num2=-1
        while(left<right):
            if(nums1[left]+nums1[right]>target):
                right-=1
            elif(nums1[left]+nums1[right]<target):
                left+=1
            elif(nums1[left]+nums1[right]==target):
                nums2=list(reversed(nums))
                return [nums.index(nums1[left]),len(nums)-1-nums2.index(nums1[right])]
