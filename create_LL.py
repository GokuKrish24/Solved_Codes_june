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
LL=LinkedList()
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.Print()
