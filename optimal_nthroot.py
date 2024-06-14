def NthRoot(n: int, m: int) -> int:
    def findn(start,end,n):
        if(start<=end):
            mid=(start+end)//2
            if(mid**n==m):
                return mid
            elif(mid**n>m):
                return findn(start,mid-1,n)
            else:
                return findn(mid+1,end,n)
        return -1
    return findn(1,m,n)
    pass
