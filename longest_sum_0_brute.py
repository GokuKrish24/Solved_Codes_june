arr=[9, -3, 3, -1, 6, -5]
flag=False
for i in range(len(arr),0,-1):
    if(flag==True):
        break
    for j in range(len(arr)-i+1):
        if(sum(arr[j:j+i])==0):
            print(i)
            flag=True
            break

'''
prefix
[0,9,6,9,8,14,9]
from typing import List

def solve(a: List[int]) -> int:
    maxx = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i, len(a)):
            sum += a[j]
            if sum == 0:
                maxx = max(maxx, j-i+1)
    return maxx

if __name__ == "__main__":
    a = [9, -3, 3, -1, 6, -5]
    print(solve(a))


'''
