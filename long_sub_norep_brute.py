S="takeUforward"
ls=list(set(S))
length=0
for i in range(len(S)):
    t=ls.copy()
    cnt=0
    for j in range(i,len(S)):
        if(S[j] in t):
            cnt+=1
            t.remove(S[j])
        else:
            break
    length=max(length,cnt)
print(length)
