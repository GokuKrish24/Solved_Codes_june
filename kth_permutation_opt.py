def kthpermu(n,k):
    num=[]
    for i in range(1,n+1):
        num.append(str(i))
    res=[]
    n1=n
    p=k-1
    while(len(res)!=n):
        z=1
        for i in range(1,n1):
            z*=i
        q=num.pop(p//z)
        res.append(q)
        n1-=1
        p=p%z
    return ''.join(res)
print(kthpermu(4,9))


        
