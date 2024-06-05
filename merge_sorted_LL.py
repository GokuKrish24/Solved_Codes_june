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

def merge(LL1,LL2):
    h1=LL1.head
    h2=LL2.head
    if(h2==None):
        return h1
    elif(h1==None):
        return h2
    n=Node(-1)
    nh=n
    if(h1.data<h2.data):
        nh.next=h1
        h1=h1.next
        nh=nh.next
    else:
        nh.next=h2
        h2=h2.next
        nh=nh.next
    while(h1!=None and h2!=None):
        if(h1.data<h2.data):
            nh.next=h1
            h1=h1.next
            nh=nh.next
        else:
            nh.next=h2
            h2=h2.next
            nh=nh.next
    while(h1!=None):
        nh.next=h1
        h1=h1.next
        nh=nh.next
    while(h2!=None):
        nh.next=h2
        h2=h2.next
        nh=nh.next
    nh.next=None
    return n.next
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.Print()
LL1=LinkedList()
# LL1.insert(2)
# LL1.insert(3)
LL1.insert(6)
LL1.insert(12)
LL1.insert(13)

k=merge(LL,LL1)
while(k!=None):
    print(k.data,end=" ")
    k=k.next
