import sys

m=-sys.maxsize-1
s=0
L=[-2,1,-3,4,-1,2,1,-5,4]

start=0
nstart=-1
nend=-1
for i in range(len(L)):
    s+=L[i]
    if(s>m):
        m=s
        nstart=start
        nend=i
    if(s<0):
        s=0
        start=i+1
print(m)
print(nstart,nend)
