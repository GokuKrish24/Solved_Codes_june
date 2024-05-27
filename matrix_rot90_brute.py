L=[[5,1,9,11],
   [2,4,8,10],
   [13,3,6,7],
   [15,14,12,16]]

nL=[]
for i in range(len(L[0])):
    k=[]
    for j in range(len(L)):
        k.append(L[len(L)-1-j][i])
    nL.append(k)
print(nL)
