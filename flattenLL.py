class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.child=None


def Print(head):
    x=head
    while(x!=None):
        print(x.data,end="-->")
        x=x.child
    
def merge(head1,head2):
    n=Node(-1)
    nh=n
    x=head1
    y=head2
    while(x!=None and y!=None):
        if(x.data<y.data):
            nh.child=x
            nh=nh.child
            x=x.child
        else:
            nh.child=y
            nh=nh.child
            y=y.child
    while(x!=None):
        nh.child=x
        x=x.child
        nh=nh.child
    while(y!=None):
        nh.child=y
        y=y.child
        nh=nh.child
    nh.child=None
    return n.child

def Flatten(head):
    x=head
    y=head.next
    while(y!=None):
        k=y.next
        x=merge(x,y)
        y=k
    return x


# head1=Node(3)
# head1.next=Node(4)
# head1.next.next=Node(5)
# head2=Node(1)
# head2.next=Node(2)
# k=merge(head1,head2)
head=Node(3)
head.next=Node(2)
head.next.child=Node(10)
head.next.next=Node(1)
head.next.next.child=Node(7)
head.next.next.child.child=Node(11)
head.next.next.child.child.child=Node(12)
head.next.next.next=Node(4)
head.next.next.next.child=Node(9)
head.next.next.next.next=Node(5)
head.next.next.next.next.child=Node(6)
head.next.next.next.next.child.child=Node(8)
#Print(head)
k=Flatten(head)
Print(k)
