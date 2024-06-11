class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w

def fractionalknapsack(w,arr,n):
        arr.sort(key=lambda x:x.value/x.weight,reverse=True)
        mval=0
        k=w
        for i in range(n):
            # print(arr[i].weight,arr[i].value)
            # print(k)
            if(k==0):
                break
            elif(arr[i].weight<=k):
                mval+=arr[i].value
                k-=arr[i].weight
            else:
                mval+=(arr[i].value/arr[i].weight)*k
                k=0
                break
        # print(mval)
        return mval
