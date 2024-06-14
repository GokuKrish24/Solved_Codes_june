n=4
m=[ [0, 1, 1, 1],
    [1, 1, 1, 0], 
    [1, 0, 1, 1],
    [0, 0, 1, 1]]

def solve(n,m):
    res=[]
    des=[]
    mat=[]
    for i in range(n):
        k=[]
        for j in range(n):
            k.append(0)
        mat.append(k)
    mat[0][0]=1
    def maze(i,j,m,n,mat):
        if(i==n-1 and j==n-1):
            res.append("".join(des))
            return 
        if(i+1<=n-1 and j<=n-1 and mat[i+1][j]==0 and m[i+1][j]==1):
            des.append("D")
            mat[i+1][j]=1
            maze(i+1,j,m,n,mat)
            mat[i+1][j]=0
            des.pop()
        if(i>=0 and j-1>=0 and mat[i][j-1]==0 and  m[i][j]==1):
            des.append("L")
            mat[i][j-1]=1
            maze(i,j-1,m,n,mat)
            mat[i][j-1]=0
            des.pop()   
        if(i<=n-1 and j+1<=n-1 and mat[i][j+1]==0 and m[i][j+1]==1):
            des.append("R")
            mat[i][j+1]=1
            maze(i,j+1,m,n,mat)
            mat[i][j+1]=0
            des.pop()
        if( i-1>=0 and j>=0 and mat[i-1][j]==0 and m[i-1][j]==1):
            des.append("U")
            mat[i-1][j]=1
            maze(i-1,j,m,n,mat)
            mat[i-1][j]=0
            des.pop()
        return
    maze(0,0,m,n,mat)
    if(m[0][0]==0 or len(res)==0):
        return [-1]
    return res
print(solve(n,m))

