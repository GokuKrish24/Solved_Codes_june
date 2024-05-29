from collections import Counter

arr=[1,1,1,2,2,2,2,2,2,2,4,4]
c=Counter(arr)
for i in c.keys():
    if(c[i]>len(arr)/2):
        print(i)
        break
