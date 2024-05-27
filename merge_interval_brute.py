
intervals=[[1,3],[2,6],[8,10],[15,18]]
ans=[]
intervals.sort()
i=0
for i in range(len(intervals)):
    start=intervals[i][0]
    end=intervals[i][1]
    if(len(ans)!=0 and ans[-1][1]>=end):
        continue
    for j in range(i+1,len(intervals)):
        if(intervals[j][0]<=end):
            end=max(end,intervals[j][1])
        else:
            break
    ans.append([start,end])
print(ans)
