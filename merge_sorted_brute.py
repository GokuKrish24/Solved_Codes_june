arr1=[1,4,8,10] 
arr2=[2,3,9]

i=0
while(i<len(arr1)):
    for j in range(len(arr2)):
        if(arr2[j]<arr1[i]):
            arr1[i],arr2[j]=arr2[j],arr1[i]
    i+=1
arr2.sort()
print(arr1)
print(arr2)

'''
arr1=[1,4,8,10] 
arr2=[2,3,9]

res=[]

i=0
j=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]<arr2[j]):
        res.append(arr1[i])
        i+=1
    else:
        res.append(arr2[j])
        j+=1
while(i<len(arr1)):
    res.append(arr1[i])
    i+=1
while(j<len(arr2)):
    res.append(arr2[j])
    j+=1

for i in range(len(res)):
    if(i<len(arr1)):
        arr1[i]=res[i]
    else:
        arr2[i-len(arr1)]=res[i]
print(arr1)
print(arr2)

'''
