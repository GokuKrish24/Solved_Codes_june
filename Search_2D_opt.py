
def bind(arr,target,start,end,m):
    if(start<=end):
        mid=(start+end)//2
        if(arr[mid//m][mid%m]==target):
            return mid
        elif(target<arr[mid//m][mid%m]):
            return bind(arr,target,start,mid-1,m)
        else:
            return bind(arr,target,mid+1,end,m)
    return -1


arr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(bind(arr,12,0,11,4))
