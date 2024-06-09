class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.random = None

def deepcopy(head):
    temp=head
    dic={None:None}
    nh=None
    while(temp!=None):
        k=Node(temp.data)
        if(temp==head):
            nh=k
        dic[temp]=k
        temp=temp.next
    for i in dic:
        if(i==None):
            continue
        print(i.data,dic[i].data)
    for i in dic:
        if(i==None):
            continue
        dic[i].random=dic[i.random]
        dic[i].next=dic[i.next]
    temp=nh
    while(temp!=None):
        print(temp,temp.data,temp.random)
        temp=temp.next
    return nh


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
temp=head
k=deepcopy(head)
