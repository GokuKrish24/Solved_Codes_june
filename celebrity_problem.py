def celebrity(self, M, n):
        stack=[]
        for i in range(n):
            stack.append(i)
        while(len(stack)!=1):
            k=stack.pop()
            if(M[stack[-1]][k]==1):
                stack.pop()
                stack.append(k)
        flag=0
        for i in range(n):
            if(M[stack[-1]][i]==1 and stack[-1]!=i ):
                flag=1
                break
            if(M[i][stack[-1]]==0 and stack[-1]!=i):
                flag=1
                break
        if(flag==1):
            return -1
        else:
            return stack[-1]
