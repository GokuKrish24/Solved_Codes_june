def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums1)>len(nums2)):
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=len(nums1)
        la1=len(nums1)
        la2=len(nums2)
        while(low<=high):
            cut1=(low+high)//2
            cut2=(la1+la2)//2-cut1
            l1= -1000001 if cut1==0 else nums1[cut1-1]
            l2= -1000001 if cut2==0 else nums2[cut2-1]
            r1= 1000001 if cut1==la1 else nums1[cut1]
            r2= 1000001 if cut2==la2 else nums2[cut2]
            if(l1>r2):
                high=cut1-1
            elif(l2>r1):
                low=cut1+1
            else:
                if(la1+la2)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return min(r1,r2)
