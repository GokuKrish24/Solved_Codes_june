arr=[2,3,6,7]
target=7
def combination(candidates,target):
    res=[]
    des=[]
    def combi(ind,target):
        if(ind==len(candidates)):
            if(target==0):
                res.append(des[:])
            return
        if(candidates[ind]<=target):
            des.append(candidates[ind])
            combi(ind,target-candidates[ind])
            des.pop()
        combi(ind+1,target)
    combi(0,target)
    return res
print(combination(arr,target))
