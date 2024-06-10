arr=[4,2,0,3,2,5]
ans=0

for i in range(len(arr)):
    j=0
    left=0
    while(j<=i):
        left=max(left,arr[j])
        j+=1
    j=len(arr)-1
    right=0
    while(j>=i):
        right=max(right,arr[j])
        j-=1
    ans+=min(left,right)-arr[i]

print(ans)
