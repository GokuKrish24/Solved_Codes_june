class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if(self.head==None):
            self.head=Node(data)
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            curr=Node(data)
            temp.next=curr
    def Print(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,end="-->")
            temp=temp.next
        print()
def Add_LL(L1,L2):
    x=L1.head
    y=L2.head
    if(x==None):
        return y
    elif(y==None):
        return x
    carry=0
    g1=Node(-1)
    g=g1
    while(x!=None and y!=None):
        n=x.data+y.data+carry
        carry=0
        if(n>=10):
            carry=1
            n=n%10
        g.next=Node(n)
        g=g.next
        x=x.next
        y=y.next
    while(x!=None):
        n=x.data+carry
        carry=0
        if(n>=10):
            carry=1
            n=n%10
        g.next=Node(n)
        g=g.next
        x=x.next
    while(y!=None):
        n=y.data+carry
        carry=0
        if(n>=10):
            carry=1
            n=n%10
        g.next=Node(n)
        g=g.next
        y=y.next
    if(carry==1):
        g.next=Node(1)
        carry=0
    return g1.next



LL=LinkedList()

LL.insert(9)
LL.insert(9)
LL.insert(9)
LL.insert(9)
LL.insert(9)
LL.insert(9)
LL.insert(9)
LL.Print()
LL1=LinkedList()
LL1.insert(9)
LL1.insert(9)
LL1.insert(9)
LL1.insert(9)
LL1.Print()
k=Add_LL(LL,LL1)
while(k!=None):
    print(k.data,end=" ")
    k=k.next
print()

