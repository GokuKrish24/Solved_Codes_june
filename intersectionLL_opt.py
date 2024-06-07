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
def intersect_opt(head1,head2):
    x=head1
    y=head2
    while(x!=y):
        if(x==None):
            x=head2
        elif(y==None):
            y=head1
        x=x.next
        y=y.next
    return x
k=intersect_opt(head.next,head1.next)
if(k==None):
    print("No intersection")
else:
    print("intersection at",k.data)
