L=[4,3,6,2,1,1]
xor=0
n=len(L)
for i in range(n):
    xor=xor^L[i]
    xor=xor^i+1
bitno=0
while(True):
    if((1<<bitno)&xor!=0):
        break
    bitno+=1
zero=0
one=0
for i in range(n):
    if(L[i]&(1<<bitno)!=0):
        one=one^L[i]
    else:
        zero=zero^L[i]
    if((i+1)&(1<<bitno)!=0):
        one=one^(i+1)
    else:
        zero=zero^(i+1)
count=0
for i in range(n):
    if(L[i]==zero):
        count+=1
if(count==0):
    print(zero,one)
else:
    print(one,zero)
