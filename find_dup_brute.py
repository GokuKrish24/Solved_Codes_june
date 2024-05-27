L=[1,3,4,2,2]

count=[0]*(len(L)-1)
for i in L:
    if(count[i-1]==0):
        count[i-1]+=1
    else:
        print(i)
