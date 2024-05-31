arr=[-1,0,1,2,-1,-4]
ans=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if(arr[i]+arr[j]+arr[k]==0 and (sorted([arr[i],arr[j],arr[k]]) not in ans)):
                print(arr[i],arr[j],arr[k])
                ans.append(sorted([arr[i],arr[j],arr[k]]))
