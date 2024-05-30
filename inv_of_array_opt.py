


count=0
#  [5,4,3] [2,1]
def merge(arr,left,mid,end):
    global count
    start=left
    right=mid+1
    temp=[]
    while(start<=mid and right<=end):
        if(arr[start]<=arr[right]):
            temp.append(arr[start])
            start+=1
        else:
            count+=mid-start+1    
            temp.append(arr[right])
            right+=1
    while(start<=mid):
        temp.append(arr[start])
        start+=1
    while(right<=end):
        temp.append(arr[right])
        right+=1
    for i in range(left,end+1):
        arr[i]=temp[i-left]

def mergesort(arr,left,end):
    if(left<end):
        mid=(left+end)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,end)
        merge(arr,left,mid,end)

arr=[1,2,0]
lcount=0
for i in range(len(arr)-1):
    if(arr[i]>arr[i+1]):
        lcount+=1
mergesort(arr,0,len(arr)-1)


print(lcount)
print(count)
