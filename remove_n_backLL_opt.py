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
    def remove_back(self,n):
        b=self.head
        f=self.head
        for i in range(0,n+1):
            if(f==None):
                break
            f=f.next
        if(f==None):
            self.head=self.head.next
        else:
            while(f.next!=None):
                b=b.next
                f=f.next
            b.next=b.next.next
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.Print()
LL.remove_back(4)
LL.Print()
