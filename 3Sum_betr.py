arr=[-1,0,1,2,-1,-4]
dic={arr[0]:0}
for i in range(1,len(arr)):
    for j in range(i+1,len(arr)):
        if(0-arr[i]-arr[j] in dic):
            print([arr[i],arr[j],0-arr[i]-arr[j]])
    if(arr[i] not in dic):
        dic[arr[i]]=i
