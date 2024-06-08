def rotateRight(head, k):
        if(head==None or head.next==None or k==0):
            return head
        else:
            n=0
            temp=head
            while(temp!=None):
                n+=1
                temp=temp.next
            k=k%n
            if(k==0):
                return head
            temp=head
            for i in range(n-k-1):
                temp=temp.next
            temp1=temp.next
            temp.next=None
            t=temp1
            while(temp1.next!=None):
                temp1=temp1.next
            temp1.next=head
            head=t
            return head
