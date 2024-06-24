arr=[4,0,-1,3,5,3,6,8]
karr=[]
k=3
res=[]
for i in range(len(arr)):
    if(i<k):
        karr.append(arr[i])
        continue
    res.append(sum(karr))
    karr.pop(0)
    karr.append(arr[i])
res.append(sum(karr))
print(res)
