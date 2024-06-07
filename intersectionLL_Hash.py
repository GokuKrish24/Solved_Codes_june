class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(-1)
a=Node(1)
b=Node(3)
c=Node(1)
d=Node(2)
head.next=a
a.next=b
b.next=c
c.next=d
d.next=Node(4)
head1=Node(-1)
e=Node(3)
head1.next=e
e.next=d
def Hash_int(head1,head2):
    dict={}
    x=head1
    while(x!=None):
        dict[x]=1
        x=x.next
    y=head2
    while(y!=None):
        if(y in dict):
            return y
        y=y.next
    return None
k=Hash_int(head.next,head1.next)
if(k==None):
    print("No intersection found")
else:
    print("intersection found at",k.data)
