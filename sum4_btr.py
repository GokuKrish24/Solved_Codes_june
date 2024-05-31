arr=[1,0,-1,0,-2,2]
dic={arr[0]:0}
ans=[]
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if(-(arr[i]+arr[j]+arr[k]) in dic):
                an=[arr[i],arr[j],arr[k],-(arr[i]+arr[j]+arr[k])]
                an.sort()
                if(an not in ans):
                    ans.append(an)
    dic[arr[i]]=i
print(ans)

