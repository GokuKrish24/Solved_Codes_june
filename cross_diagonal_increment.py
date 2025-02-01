L=[[0]*4 for i in range(4)]
j=0
cnt=1
while(j<4):
    i=0
    j1=j
    while(i<4 and j1>=0):
        L[i][j1]=cnt
        cnt+=1
        i+=1
        j1-=1
    j+=1

ni=1
while(ni<4):
    j=3
    i=ni
    while(i<4 and j>=0):
        L[i][j]=cnt
        cnt+=1
        i+=1
        j-=1
    ni+=1
for i in L:
    print(i)
    
        
    
    
