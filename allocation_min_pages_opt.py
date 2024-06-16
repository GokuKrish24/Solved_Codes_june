def min_pages(A,B):
    n=len(A)
    if(B>n):
        return -1
    def funct(mid,A,n):
        mstu=1
        pages=0
        for i in range(n):
            if(pages+A[i]<=mid):
                pages+=A[i]
            else:
                pages=A[i]
                mstu+=1
        return mstu
    low=max(A)
    high=sum(A)
    while(low<=high):
        mid=(low+high)//2
        k=funct(mid,A,n)
        if (k<=B):
            high=mid-1
        else:
            low=mid+1
    return low

print(min_pages([25, 46, 28, 49, 24],4))
