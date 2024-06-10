def maximumMeetings(n,start,end):
        newL=[]
        for i in range(n):
            newL.append([end[i],start[i]])
        newL.sort()
        nend=newL[0][0]
        nm=1
        for i in range(1,len(newL)):
            if(newL[i][1]>nend):
                nm+=1
                nend=newL[i][0]
        return nm
