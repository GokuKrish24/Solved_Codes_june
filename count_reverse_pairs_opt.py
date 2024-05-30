
count=0
def merge(arr,left,mid,end):
    global count
    start=left
    right=mid+1
    temp=[]
    r=mid+1
    for i in range(left,mid+1):
        while(r<=end and arr[i]>arr[r]*2):
            r+=1
        count+=r-(mid+1)

    while(start<=mid and right<=end):
        if(arr[start]<=arr[right]):
            temp.append(arr[start])
            start+=1
        else:
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

arr=[5,4,3,2,1]


mergesort(arr,0,len(arr)-1)
print(count)
