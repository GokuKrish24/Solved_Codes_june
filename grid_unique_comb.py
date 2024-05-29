ans=1
m=10
n=10
N=m+n-2
r=min(m,n)-1
for i in range(1,r+1):
    ans*=(N-r+i)/i
print(ans)
