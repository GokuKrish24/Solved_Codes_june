import sys

L=[-2,1,-3,4,-1,2,1,-5,4]
n=len(L)
s=-sys.maxsize-1
for i in range(n):
    for j in range(i,n):
        su=0
        for i1 in range(i,j+1):
            su+=L[i1]
            s=max(su,s)
print(s)
