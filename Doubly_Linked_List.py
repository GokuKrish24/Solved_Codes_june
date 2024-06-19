
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,data):
        k=Node(data)
        if(self.head==None):
            self.head=k
            self.tail=k
        else:
            self.tail.next=k
            k.prev=self.tail
            self.tail=k
    def reverse(self):
        k=self.head
        while(True):
            k.prev,k.next=k.next,k.prev
            k=k.prev
            if(k==None):
                break
        self.head,self.tail=self.tail,self.head
    def Print(self):
        k=self.head
        while(k!=None):
            print(k.data,end=" ")
            k=k.next
        print()
D=DLL()
D.insert(1)
D.insert(2)
D.insert(3)
D.Print()
D.reverse()
D.Print()
