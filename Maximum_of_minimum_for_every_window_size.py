def maxMinWindow(N,l):
    # Write your code here
    # Return a list of integers
    arr=[-1000000000]*(l+1)
    stack=[]
    lefts=[]
    stack1=[]
    rights=[0]*l
    for i in range(l):
        while(len(stack)!=0 and N[stack[-1]]>=N[i]):
            stack.pop()
        while(len(stack1)!=0 and N[stack1[-1]]>=N[l-i-1]):
            stack1.pop()
        if(len(stack1)==0):
            stack1.append(l-i-1)
            rights[l-i-1]=l-1
        else:
            rights[l-i-1]=stack1[-1]-1
            stack1.append(l-i-1)
        if(len(stack)==0):
            stack.append(i)
            lefts.append(0)
        else:
            lefts.append(stack[-1]+1)
            stack.append(i)
        
    for i in range(l):
        k=rights[i]-lefts[i]+1
        arr[k]=max(arr[k],N[i])
    for i in range(l-1,-1,-1):
        arr[i]=max(arr[i],arr[i+1])
    return arr[1:]
