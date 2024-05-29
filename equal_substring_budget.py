import numpy as np


def atmost(s,t,goal):
    prefix=0
    i=0
    j=0
    cost=0
    max_length=0
    maxi=0
    while(j<len(s)):
        prefix+=np.absolute(ord(s[j])-ord(t[j]))
        while(prefix>goal):
            prefix-=np.absolute(ord(s[i])-ord(t[i]))
            max_length-=1
            i+=1
        cost+=j-i+1
        j+=1
        max_length+=1
        maxi=max(max_length,maxi)
    return maxi

s="abcd"
t="acde"

goal=0

print(atmost(s,t,goal))
