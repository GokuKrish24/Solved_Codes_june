
L=[]
def permutation(arr,l,n):
    global L
    if(len(l)==n):
        L.append(l.copy())
    else:
        for i in range(len(arr)):
            l.append(arr.pop(i))
            permutation(arr,l,n)
            arr.insert(i,l.pop())

if(__name__=="__main__"):
    arr=[1,3,2]
    arr1=arr.copy()
    arr1.sort()
    permutation(arr1,[],len(arr1))
    print(L[(L.index(arr)+1)%len(L)])
