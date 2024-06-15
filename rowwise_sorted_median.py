def median(matrix, R, C):
        def countless(mat,t,start,end):
            while(start<=end):
                mid=(start+end)//2
                if(mat[mid]<=t):
                    start=mid+1
                else:
                    end=mid-1
            return start
        
        low=2000
        high=-2000
        for i in range(R):
            low=min(low,matrix[i][0])
            high=max(high,matrix[i][C-1])
        while(low<=high):
            mid=(low+high)//2
            cnt=0
            for i in range(R):
                cnt+=countless(matrix[i],mid,0,C-1)
            if(cnt<=(C*R)//2):
                low=mid+1
            else:
                high=mid-1
        return low
mat=[
    [1,4,9], 
    [2,5,6],
    [3,8,7]
]
print(median(mat,3,3))
