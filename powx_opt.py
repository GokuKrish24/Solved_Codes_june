def pow(x,n):
    if(n==0):
        return 1
    if(n%2==0):
        return pow(x*x,n//2)
    else:
        return x*pow(x,n-1)

'''
2^10

4^5
4*4^4
4*16^2
4*256*1
'''
n=-1
x=2
if(n<0):
    n*=-1
    print("{:.5f}".format(1/pow(x,n)))
else:
    print("{:.5f}".format(pow(x,n)))
