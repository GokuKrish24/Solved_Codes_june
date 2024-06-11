
ar=[]
def Subset(arr,res):
    global ar
    if(sum(res) not in ar):
        ar.append(sum(res))
    if(len(arr)==0):
        return
    for i in range(len(arr)):
        k=arr.pop(i)
        res.append(k)
        Subset(arr,res)
        res.pop()
        arr.insert(i,k)
Subset([5,2,1],[])
print(sorted(ar))
