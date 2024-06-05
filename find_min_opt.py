import math

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
        while(temp!=None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def Findmid_opt(self):
        slow=self.head
        fast=self.head
        while(fast.next!=None):
            fast=fast.next
            if(fast.next!=None):
                fast=fast.next
            else:
                break
            slow=slow.next
        print(slow.data)
        

LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
# LL.insert(6)
# LL.insert(7)
LL.Print()
LL.Findmid_opt()
