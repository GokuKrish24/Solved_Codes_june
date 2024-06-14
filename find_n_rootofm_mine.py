import math
def NthRoot(n, m):
    j=pow(m,1/n)
    j1=math.ceil(j)
    j2=math.floor(j)
    if(pow(j1,n)==m):
        return j1
    elif(pow(j2,n)==m):
        return j2
    else:
        return -1
    pass
