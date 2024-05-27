L=[4,3,6,2,1,1]
n=len(L)
s=int((n*(n+1))/2)
s2=int((n*(n+1)*(2*n+1))/6)
sL=0
sL2=0
for i in range(n):
    sL+=L[i]
    sL2+=L[i]**2
eq1=sL-s
eq2=sL2-s2
print(eq1)
print(eq2)
eq2=int(eq2/eq1)
x=int((eq1+eq2)/2)
y=eq2-x
print(x,y)
