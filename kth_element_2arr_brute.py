arr1=[100, 112, 256, 349, 770]
arr2=[72, 86, 113, 119, 265, 445, 892]
k=7
p1=0
p2=0
cnt=0
while(p1<len(arr1) and p2<len(arr2)):
    if(arr1[p1]<arr2[p2]):
        cnt+=1
        if(cnt==k):
            print(arr1[p1])
        p1+=1
    else:
        cnt+=1
        if(cnt==k):
            print(arr2[p2])
        p2+=1
while(p1<len(arr1)):
    cnt+=1
    if(cnt==k):
        print(arr1[p1])
    p1+=1
while(p2<len(arr2)):
    cnt+=1
    if(cnt==k):
        print(arr2[p2])
    p2+=1
