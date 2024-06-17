from heapq import heappush,heappop

def solve(A, B, C):
        A=sorted(A,reverse = True)
        B=sorted(B,reverse = True)
        
        def Add_ele(heap,A,B,i,j,visited):
            if(i<len(A) and j<len(B) and (i,j) not in visited ):
                heappush(heap,(-A[i]-B[j],(i,j)))
                visited.add((i,j))
        heap=[(-A[0]-B[0],(0,0))]
        ans=[]
        visited=set()
        for i in range(C):
            res,index=heappop(heap)
            Add_ele(heap,A,B,index[0]+1,index[1],visited)
            Add_ele(heap,A,B,index[0],index[1]+1,visited)
            ans.append(-res)
        return ans
A=[ 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83 ]
B=[ 59, 63, 65, 6, 46, 82, 28, 62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83 ]
C=10
print(solve(A,B,C))
