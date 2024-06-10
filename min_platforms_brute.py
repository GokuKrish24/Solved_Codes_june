arr=[900, 1100, 1235]
dep=[1000, 1200, 1240]
res=[]
n=len(arr)
for i in range(n):
    res.append([arr[i],dep[i]])
res.sort()
print(res)
ans=[res[0][1]]
plt=1
for i in range(1,n):
    flag=0
    for j in range(len(ans)):
        if(res[i][0]>ans[j]):
            flag=1
            ans[j]=res[i][1]
            break
    if(flag==0):
        plt+=1
        ans.append(res[i][1])
print(plt)
