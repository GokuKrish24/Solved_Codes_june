intervals=[[1,4],[4,5]]

ans=[]
intervals.sort()
i=0
n=len(intervals)
while(i<n):
    if(len(ans)==0):
        ans.append(intervals[i])
        i+=1
        continue
    if(ans[-1][1]>=intervals[i][0]):
        ans[-1][1]=max(ans[-1][1],intervals[i][1])
    else:
        ans.append(intervals[i])
    i+=1
print(ans)
'''
intervals=[[1,3],[2,6],[8,10],[15,18]]

ans=[]
intervals.sort()
n=len(intervals)
for i in range(n):
    if(len(ans)==0 or ans[-1][1]<intervals[i][0]):
        ans.append(intervals[i])
    else:
        ans[-1][1]=max(ans[-1][1],intervals[i][1])
print(ans)

'''
