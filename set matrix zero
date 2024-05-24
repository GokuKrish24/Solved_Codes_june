#approach 1

import sys

arr=[[0,1,2,0],
     [3,4,5,2],
     [1,3,1,5]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]==0):
            for i1 in range(len(arr[i])):
                arr[i][i1]=arr[i][i1]*sys.maxsize
            for i1 in range(len(arr)):
                arr[i1][j]=arr[i1][j]*sys.maxsize

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]>=sys.maxsize):
            arr[i][j]=0
print(arr)            
            

'''
approach 2
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==0):
                    for i1 in range(len(matrix[i])):
                        if(matrix[i][i1]!=0):
                            matrix[i][i1]=sys.maxsize
                    for i1 in range(len(matrix)):
                        if(matrix[i1][j]!=0):
                            matrix[i1][j]=sys.maxsize

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==sys.maxsize):
                    matrix[i][j]=0
'''


'''
Approach 3

1 1 1
1 0 1
1 1 1

r=[0,1,0]
c=[0,1,0]




import sys

arr=[[0,1,2,0],
     [3,4,5,2],
     [1,3,1,5]]


frow=0
fcol=0
for i in range(len(arr)):
    if(arr[i][0]==0):
        fcol=1
for i in range(len(arr[0])):
    if(arr[0][i]==0):
        frow=1

for i in range(1,len(arr)):
    for j in range(1,len(arr[i])):
        if(arr[i][j]==0):
            arr[0][j]=0
            arr[i][0]=0

zer=[0]*len(arr[0])
for i in range(1,len(arr[0])):
    if(arr[0][i]==0):
        for j in range(len(arr)):
            arr[j][i]=0

for i in range(1,len(arr)):
    if(arr[i][0]==0):
        arr[i]=zer
if(frow==1):
    arr[0]=zer
if(fcol==1):
    for i in range(len(arr)):
        arr[i][0]=0
print(arr)

'''
