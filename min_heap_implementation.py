from sys import *
from collections import *
from math import *

def minHeap(N: int, Q: [[]]) -> []:
    ans=[]
    heap=[]
    for i in range(N):
        if(Q[i][0]==0):
            heap.append(Q[i][1])
            p=len(heap)-1
            while(p!=0 and heap[p]<heap[(p-1)//2]):
                heap[p],heap[(p-1)//2]=heap[(p-1)//2],heap[p]
                p=(p-1)//2
        else:
            if(len(heap)==0):
                continue
            elif(len(heap)==1):
                ans.append(heap.pop(0))
                continue
            heap[0],heap[-1]=heap[-1],heap[0]
            ans.append(heap.pop())
            index=0
            while True:
                smallest=index
                left=2*index+1
                right=2*index+2
                if(left<len(heap) and heap[left]<heap[smallest]):
                    smallest=left
                if(right<len(heap) and heap[right]<heap[smallest]):
                    smallest=right
                if(smallest!=index):
                    heap[index],heap[smallest]=heap[smallest],heap[index]
                    index=smallest
                else:
                    break
                
    return ans
    pass

