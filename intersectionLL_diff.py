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
def diff_length(head1,head2):
    n=0
    x=head1
    while(x!=None):
        n+=1
        x=x.next
    m=0
    y=head2
    while(y!=None):
        m+=1
        y=y.next
    x=head1
    y=head2
    if(m>n):
        n,m=m,n
        x,y=y,x
    for i in range(abs(n-m)):
        x=x.next
    while(x!=None and y!=None):
        print(x.data)
        print(y.data)
        if(x==y):
            return x
        x=x.next
        y=y.next
    return None
k=diff_length(head.next,head1.next)
if(k==None):
    print("Intersection Not found")
else:
    print("Intersection found at",k.data)

