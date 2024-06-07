def detectCycle(self, head):
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                fast=head
                while(fast!=slow):
                    fast=fast.next
                    slow=slow.next
                return slow
        return None
