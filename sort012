L=[0,2,1,1,0,2]
# [0,2,1,1,0,2]
i=0
p=0
n=len(L)
while(i<n and p<=n):
    if(L[i]==2):
        L.pop(i)
        L.append(2)
        p+=1
    elif(L[i]==0):
        L.pop(i)
        L.insert(0,0)
        p+=1
        i+=1
    else:
        i+=1
        p+=1
print(L)
