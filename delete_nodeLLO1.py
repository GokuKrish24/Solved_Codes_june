def deleteNode(self, node):
        temp=node.next
        node.val=temp.val
        node.next=temp.next
        temp.next=None
