class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        p=0
        while(len(arr)!=1):
            p+=k-1
            g=len(arr)
            arr.pop(p%g)
            p=p%g
        return arr[0]
