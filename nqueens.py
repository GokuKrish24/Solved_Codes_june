def issafe(arr,row,col):
    drow=row
    dcol=col
    while(drow>=0 and dcol>=0):
        if(arr[drow][dcol]=='Q'):
            return False
        drow-=1
        dcol-=1
    drow=row
    dcol=col
    while(drow<n and dcol>=0):
        if(arr[drow][dcol]=='Q'):
            return False
        drow+=1
        dcol-=1
    drow=row
    while(drow>=0):
        if(arr[drow][col]=='Q'):
            return False
        drow-=1
    dcol=col
    while(dcol>=0):
        if(arr[row][dcol]=='Q'):
            return False
        dcol-=1
    return True



def nqueens(arr,n,col):
    if(col==n):
        for i in arr:
            print(i)
        print()
        return
    for i in range(n):
        if(issafe(arr,i,col)):
            arr[i][col]='Q'
            nqueens(arr,n,col+1)
            arr[i][col]='.'


n=4
arr=[]
for i in range(n):
    k=[]
    for j in range(n):
        k.append(".")
    arr.append(k)
nqueens(arr,n,0)
