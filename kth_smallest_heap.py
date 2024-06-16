from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap=[]
        for i in nums:
            heappush(max_heap,-i)
        p=0
        for i in range(k):
            p=heappop(max_heap)
        return -p
