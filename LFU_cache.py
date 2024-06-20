class Node:
    def __init__(self,key,value,freq=1):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        self.freq=freq
class DLL:
    def __init__(self):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cnt=0
    def insert(self,node):
        node.next=self.head.next
        node.prev=self.head
        self.head.next.prev=node
        self.head.next=node
        self.cnt+=1
    def isEmpty(self):
        if(self.head.next==self.tail):
            return True
        return False
    def remove(self,node=None):
        if(node==None):
            k=self.tail.prev
            self.tail.prev.prev.next=self.tail
            self.tail.prev=self.tail.prev.prev
            return k
        else:
            node.prev.next=node.next
            node.next.prev=node.prev
        self.cnt-=1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.freq={}
        self.dat={}
        self.curr=0
        self.minfreq=1

    def get(self, key: int) -> int:
        if(key not in self.dat):
            return -1
        k=self.dat[key]
        fre=k.freq+1
        self.freq[k.freq].remove(k)
        if(self.freq[k.freq].isEmpty() and k.freq==self.minfreq):
                self.minfreq=fre
        g=Node(key,k.value,fre)
        if(fre not in self.freq):
            self.freq[fre]=DLL()
        self.freq[fre].insert(g)
        self.dat[key]=g
        return k.value

    def put(self, key: int, value: int) -> None:
        if(self.minfreq not in self.freq):
            self.freq[self.minfreq]=DLL()

        if(key not in self.dat):
            k=Node(key,value)
            if(self.curr==self.capacity):
                g=self.freq[self.minfreq].remove()
                del self.dat[g.key]
            else:
                self.curr+=1
            self.freq[1].insert(k)
            self.dat[key]=k
            self.minfreq=1
        else:
            k=self.dat[key]
            fre=k.freq+1
            self.freq[k.freq].remove(k)
            if(self.freq[k.freq].isEmpty() and k.freq==self.minfreq):
                self.minfreq=fre
            g=Node(key,value,fre)
            if(fre not in self.freq):
                self.freq[fre]=DLL()
            self.freq[fre].insert(g)
            self.dat[key]=g
