from heapq import heappop, heappush
import math
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
    def addNum(self, num: int) -> None:
        heappush(self.maxheap,-num)
        heappush(self.minheap,-heappop(self.maxheap))
        if(len(self.minheap)>len(self.maxheap)):
            heappush(self.maxheap,-heappop(self.minheap))

    def findMedian(self) -> float:
        if((len(self.minheap)+len(self.maxheap))%2==0):
            return (self.minheap[0]-self.maxheap[0])/2
        else:
            return -self.maxheap[0]
