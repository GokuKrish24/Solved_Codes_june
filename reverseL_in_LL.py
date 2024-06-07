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
def rev_k(LL,k):
    x=LL.head
    head=None
    while(x!=None):
        k1=k
        prev=None
        curr=x
        while(k1>0 and curr!=None):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            k1-=1
        if(k1!=0):
            curr=prev
            prev=None
            while(k-k1!=0 and curr!=None):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
                k1+=1
            head.next=prev
            break
        if(x==LL.head):
            LL.head=prev
            head=x
        else:
            head.next=prev
            head=x
        x.next=curr
        x=curr
LL=LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
# LL.insert(6)
# LL.insert(7)
# LL.insert(8)
# LL.insert(9)
# LL.insert(10)
# LL.insert(11)
LL.Print()
rev_k(LL,2)
LL.Print()
