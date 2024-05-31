A=[5, 6, 7, 8, 9]
dic={0:1}
B=5
xor=0
cnt=0
for i in range(len(A)):
    xor^=A[i]
    if(xor^B in dic):
        cnt+=dic[xor^B]
    if(xor not in dic):
        dic[xor]=0
    dic[xor]+=1
print(dic)
print(cnt)
