def grid(i,j,m,n,dp):
    if(i<m and j<n):
        if(i==m-1 and j==n-1):
            return 1
        if(dp[i][j]!=-1):
            return dp[i][j]
        dp[i][j]=grid(i+1,j,m,n,dp)+grid(i,j+1,m,n,dp)
        return dp[i][j]
    return 0


dp=[]
m=23
n=12
for i in range(m):
    l=[]
    for j in range(n):
        l.append(-1)
    dp.append(l) 
print(grid(0,0,m,n,dp))
