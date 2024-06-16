import sys
def kthElement(arr1, arr2, n, m, k):
        n1=n
        n2=m
        if(n1>n2):
            return kthElement(arr2,arr1,m,n,k)
        low=max(0,k-m)
        high=min(k,n)
        while(low<=high):
            cut1=(low+high)//2
            cut2=k-cut1
            l1=-sys.maxsize-1 if cut1==0 else arr1[cut1-1]
            l2=-sys.maxsize-1 if cut2==0 else arr2[cut2-1]
            r1=sys.maxsize if cut1==n1 else arr1[cut1]
            r2=sys.maxsize if cut2==n2 else arr2[cut2]
            if(l1<=r2 and l2<=r1):
                return max(l1,l2)
            elif(l1>r2):
                high=cut1-1
            elif(l2>r1):
                low=cut1+1
        return 1.0123

arr1=[|100, 112, 256, 349, 770]
arr2=[72|, 86, 113, 119, 265, 445, 892]
k=1
