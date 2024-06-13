def permutation(n,k):
    num=[]
    for i in range(1,n+1):
        num.append(str(i))
    res=[]
    count=[k]
    def permu(num,k):
        if(len(res)==n):
            count[0]-=1
            if(count[0]==0):
                return res
            return None
        g=None
        for i in range(len(num)):
            k=num.pop(i)
            res.append(k)
            g=permu(num,k)
            if(g!=None):
                return res
            res.pop()
            num.insert(i,k)
        return None
    j=permu(num,k)
    return j 
print(permutation(3,1))   
