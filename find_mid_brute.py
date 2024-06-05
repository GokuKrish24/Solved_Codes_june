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
    def Findmid_brut(self):
        cnt=0
        temp=self.head
        while(temp!=None):
            cnt+=1
            temp=temp.next
        n=math.ceil(cnt/2)
        temp=self.head
        while(n>1):
            temp=temp.next
            n-=1
        print(temp.data)

LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.Print()
LL.Findmid_brut()
