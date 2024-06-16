def aggre_cows(arr,k):
    low=1
    high=max(arr)-min(arr)
    arr.sort()
    def funct(arr,mid):
        nc=1
        prev=arr[0]
        for i in range(1,len(arr)):
            if(arr[i]-prev>=mid):
                nc+=1
                prev=arr[i]
        return nc
    mx=-10000
    while(low<=high):
        mid=(low+high)//2
        k1=funct(arr,mid)
        if(k1<k):
            high=mid-1
        else:
            if(k1==k):
                mx=max(mx,mid)
            low=mid+1
    return mx


arr=[0,3,4,7,10,9]
k=4
print(aggre_cows(arr,k))
