arr=[1, 3, -5, 6, -2]
prefix=[0]
dic={0:0}
cnt1=0
for i in range(len(arr)):
    if(prefix[-1]+arr[i] not in dic):
        dic[prefix[-1]+arr[i]]=i+1
        prefix.append(arr[i]+prefix[-1])
        continue
    prefix.append(arr[i]+prefix[-1])
    if(prefix[-1] in dic):
        cnt1=max(cnt1,i-dic[prefix[-1]]+1)
print(dic)
print(prefix)
print(cnt1)
