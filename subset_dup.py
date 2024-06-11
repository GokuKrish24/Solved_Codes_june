def Subsetsum(arr,n):
    res=[]
    def subopt(ind,suii):
        if(ind==n):
            res.append(tuple(suii))
            return
        suii.append(arr[ind])
        subopt(ind+1,suii)
        suii.pop()
        subopt(ind+1,suii)
    subopt(0,[])
    return res



arr=[1,2,5]
k=Subsetsum(arr,len(arr))
print(k)
