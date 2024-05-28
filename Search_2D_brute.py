def BinarySearch(arr,target,start,end):
    if(start<=end):
        mid=(start+end)//2
        if(arr[mid]==target):
            print(mid,end="")
        elif(target<arr[mid]):
            BinarySearch(arr,target,start,mid-1)
        else:
            BinarySearch(arr,target,mid+1,end)

arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

target=8
for i in range(len(arr)):
    if(target>=arr[i][0] and target<=arr[i][len(arr[i])-1]):
        print(i,end=" ")
        BinarySearch(arr[i],target,0,len(arr[i])-1)
