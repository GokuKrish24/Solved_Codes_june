class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        arr=[]
        ones=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j]==2):
                    arr.append((i,j))
                elif(grid[i][j]==1):
                    ones+=1
        mint=0
        while(len(arr)!=0):
            flag=0
            for i1 in range(len(arr)):
                i,j=arr.pop(0)
                if(i-1>=0):
                    if(grid[i-1][j]==1):
                        grid[i-1][j]=2
                        arr.append((i-1,j))
                        flag=1
                        ones-=1
                if(i+1<len(grid)):
                    if(grid[i+1][j]==1):
                        grid[i+1][j]=2
                        arr.append((i+1,j))
                        flag=1
                        ones-=1
                if(j+1<len(grid[i])):
                    if(grid[i][j+1]==1):
                        grid[i][j+1]=2
                        arr.append((i,j+1))
                        flag=1
                        ones-=1
                if(j-1>=0):
                    if(grid[i][j-1]==1):
                        grid[i][j-1]=2
                        arr.append((i,j-1))
                        flag=1
                        ones-=1
            if(flag==1):
                mint+=1
        if(ones!=0):
            return -1
        return mint
