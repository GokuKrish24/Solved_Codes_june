class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
slow=head
fast=head
k=2
for i in range(k):
    if(fast==None):
        fast=head
    fast=fast.next

if(fast==None):
    print("Same list")
else:
    while(fast.next!=None):
        slow=slow.next
        fast=fast.next
    temp=slow.next
    t1=slow.next
    slow.next=None
    while(temp.next!=None):
        temp=temp.next
    temp.next=head
    head=t1
    x=head
    while(x!=None):
        print(x.data)
        x=x.next
