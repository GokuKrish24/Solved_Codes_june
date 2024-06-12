arr=[2,3,6,7]
target=7

def combination(arr,target):
    ar=[]
    su=[]
    def combi(ind,target):
        if(ind>=len(arr)):
            return
        elif(sum(su)==target):
            if(sorted(su) not in ar):
                ar.append(su[:])
            return
        elif(sum(su)>target):
            return
        su.append(arr[ind])
        combi(ind,target)
        combi(ind+1,target)
        su.pop()
        combi(ind+1,target)
    combi(0,target)
    print(ar)
combination(arr,target)
