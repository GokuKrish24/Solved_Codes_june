import sys

L=[7,6,4,3,1]

profit=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if(L[j]-L[i]>=0 and L[j]-L[i]>profit):
            profit=L[j]-L[i]
print(profit)
