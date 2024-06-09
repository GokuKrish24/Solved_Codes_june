class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None


def deepcopy(head):
    temp=head
    while(temp!=None):
        k=Node(temp.data)
        k.next=temp.next
        temp.next=k
        temp=temp.next.next
    temp=head
    while(temp!=None):
        temp.next.random= None if temp.random==None else temp.random.next
        temp=temp.next.next
    n=Node(-1)
    nh=n
    temp=head

    while(temp!=None):
        nh.next=temp.next
        temp.next=temp.next.next
        temp=temp.next
        nh=nh.next
    return n.next



    # while(temp!=None):
    #     print(temp.data,end=" ")
    #     temp=temp.next
a=head=Node(7)
b=head.next=Node(13)
c=head.next.next=Node(11)
d=head.next.next.next=Node(10)
e=head.next.next.next.next=Node(1)
head.random=None
b.random=a
c.random=e
d.random=c
e.random=a
k=deepcopy(head)
while(k!=None):
    print(k,k.data,k.random)
    k=k.next
