def combination(candidates,target):
    res=[]
    des=[]
    candidates.sort()
    def combi(ind,target):
        if(ind>=len(candidates)):
            if(target==0):
                res.append(des[:])
            return
        print(ind)
        for i in range(ind,len(candidates)):
            if(i>ind and candidates[i]==candidates[i-1]):
                continue
            if(candidates[i]>target):
                break
            print(des,target)
            des.append(candidates[i])
            print(des)
            combi(i+1,target-candidates[i])
            des.pop()
    combi(0,target)
    return res
print(combination([1,2],4))
