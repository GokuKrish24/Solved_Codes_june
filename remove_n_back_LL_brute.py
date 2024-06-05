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
    def remove_n_back(self,n):
        j=0
        temp=self.head
        while(temp!=None):
            temp=temp.next
            j+=1
        
        if(j-n-1==0):
            self.head=self.head.next
        else:
            prev=None
            temp=self.head
            i=0
            while(i<j-n-1):
                prev=temp
                temp=temp.next
                i+=1
            prev.next=temp.next
            
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.Print()
LL.remove_n_back(4)
LL.Print()
