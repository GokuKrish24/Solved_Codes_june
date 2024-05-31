arr=[-1,0,1,2,-1,-4]
arr.sort()
se=set([])
for i in range(len(arr)):
    if(i!=0 and arr[i]==arr[i-1]):
        continue
    j=i+1
    k=len(arr)-1
    while(j<k):
        if(arr[j]+arr[k]+arr[i]>0):
            k-=1
        elif(arr[j]+arr[k]+arr[i]<0):
            j+=1
        else:
            ans=[arr[j],arr[k],arr[i]]
            ans.sort()
            se.add(tuple(ans))
            j+=1
            k-=1
            while(j<k and arr[j]==arr[j-1]):
                j+=1
            while(k>j and arr[k]==arr[k+1]):
                k-=1
print(se)
