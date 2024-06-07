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
def Pallindrome(LL):
    slow=LL.head
    prev=None
    fast=LL.head
    while(fast!=None and fast.next!=None):
        prev=slow
        slow=slow.next
        fast=fast.next
        if(fast.next!=None):
            fast=fast.next
    if(prev==None):
      return True
    prevl=None 
    curr=slow
    while(curr!=None):
        temp=curr.next
        curr.next=prevl
        prevl=curr
        curr=temp
    prev.next=prevl
    x=LL.head
    y=prevl
    while(x!=prevl and x!=None and y!=None):
        if(x.data!=y.data):
            break
        x=x.next
        y=y.next
    if(x!=prevl):
        print("Not Pallindrome")
    else:
        print("Pallindrome")


LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(2)
LL.insert(2)
LL.insert(2)
LL.Print()
Pallindrome(LL)
