import math

arr1=[1,4,8,10]
arr2=[2,3,9] 

n=len(arr1)
m=len(arr2)

gap=math.ceil((n+m)/2)
while(gap>0):
    left=0
    right=left+gap
    while(right<n+m):
        if(left<n and right>=n):
            if(arr2[right-n]<arr1[left]):
                arr2[right-n],arr1[left]=arr1[left],arr2[right-n]
        elif(left>=n):
            if(arr2[right-n]<arr2[left-n]):
                arr2[right-n],arr2[left-n]=arr2[left-n],arr2[right-n]
        else:
            if(arr1[right]<arr1[left]):
                arr1[right],arr1[left]=arr1[left],arr1[right]
        right+=1
        left+=1
    if(gap==1):
        break
    gap=math.ceil(gap/2)
print(arr1)
print(arr2)

