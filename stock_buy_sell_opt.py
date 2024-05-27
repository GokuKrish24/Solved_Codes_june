L=[7,1,5,3,6,4]
profit=0
mini=100000
for i in range(len(L)):
    if(L[i]<mini):
        mini=L[i]
    if(L[i]-mini>profit):
        profit=L[i]-mini
print(profit)
