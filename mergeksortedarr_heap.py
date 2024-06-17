from sys import *
from collections import *
from math import *
from heapq import heappush,heappop

def mergeKSortedArrays(kArrays, k:int):
	heap=[]
	ans=[]
	while(True):
		c=0
		for i in kArrays:
			if(len(i)!=0):
				heappush(heap,i.pop(0))
			else:
				c+=1
		if(c==k):
			break
		ans.append(heappop(heap))
	while(len(heap)!=0):
		ans.append(heappop(heap))
	return ans
	pass
