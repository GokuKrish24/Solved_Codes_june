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
            temp.next=Node(data)
    def Print(self):
        temp=self.head
        while(temp!=None and temp.data!=-1):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def revbrute(self):
        nhead=Node(-1)
        curr=self.head
        while(curr!=None):
            temp=curr
            curr=curr.next
            temp.next=nhead
            nhead=temp
        self.head=nhead
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.Print()
LL.revbrute()
LL.Print()
