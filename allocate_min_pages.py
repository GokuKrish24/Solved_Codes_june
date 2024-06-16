arr=[25, 46, 28, 49, 24]
n=5
m=4
for i in range(max(arr),sum(arr)):
    nstu=1
    msum=0
    for j in range(n):
        if(msum+arr[j]<=i):
            msum+=arr[j]
        else:
            nstu+=1
            msum=arr[j]
    if(nstu==m):
        print(i)
        break
