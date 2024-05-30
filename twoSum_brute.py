arr=[2,6,5,8,11]
target=15
ind1=-1
ind2=-1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]+arr[j]==target):
            ind1=i
            ind2=j
            break
print(ind1,ind2)
