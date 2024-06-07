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
def reverse(LL):
    x=LL.head
    y=Node(-1)
    while(x!=None):
        nnode=Node(x.data)
        nnode.next=y.next
        y.next=nnode
        x=x.next
    return y.next
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(2)
LL.insert(2)
LL.insert(2)
LL.insert(1)
LL.Print()
k=reverse(LL)
x=LL.head
while(x!=None and k!=None):
    if(x.data!=k.data):
        break
    x=x.next
    k=k.next
if(x!=None):
    print("Not a pallindrome")
else:
    print("Pallindrome")
