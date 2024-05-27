# Brute force repeating and missing numbers
L=[3,1,2,5,4,6,7,5]
count=[0]*len(L)
for i in range(len(L)):
    count[L[i]-1]+=1
ans=[0]*2
for i in range(len(count)):
    if(count[i]==0):
        ans[0]=i+1
    elif(count[i]==2):
        ans[1]=i+1
print(ans)
