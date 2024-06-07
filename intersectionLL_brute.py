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
# to find intersection
x=head.next
flag=0
while(x!=None):
    if(flag==1):
        break
    y=head1.next
    while(y!=None):
        if(x==y):
            print("intersection from",x.data)
            flag=1
            break
        y=y.next
    x=x.next

