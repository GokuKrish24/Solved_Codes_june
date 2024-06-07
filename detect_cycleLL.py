def hasCycle(self, head):
        dic={}
        x=head
        while(x!=None):
            if(x in dic):
                break
            dic[x]=1
            x=x.next
        if(x==None):
            return False
        else:
            return True
