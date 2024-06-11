def Subsetsum(arr,n):
    res=[]
    def subopt(ind,suii):
        if(ind==n):
            res.append(suii)
            return
        subopt(ind+1,suii+arr[ind])
        subopt(ind+1,suii)
    subopt(0,0)
    return res



arr=[5,2,1]
k=Subsetsum(arr,len(arr))
print(k)
