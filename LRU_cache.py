
class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self,capacity):
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.dic={}
    def put(self,key,value):
        k=Node(key,value)
        if(self.capacity!=len(list(self.dic))):
            if(len(list(self.dic))==0):
                self.tail.prev=k
            if(key in self.dic):
                p=self.dic[key]
                p.prev.next=p.next
                p.next.prev=p.prev
            self.dic[key]=k
        else:
            if(key not in self.dic):
                print(self.tail.prev.key,self.tail.prev.value)
                del self.dic[self.tail.prev.key]
                self.dic[key]=k
                self.tail.prev.prev.next=self.tail
                self.tail.prev=self.tail.prev.prev
                print(self.tail.prev.key,self.tail.prev.value)
            else:
                p=self.dic[key]
                p.prev.next=p.next
                p.next.prev=p.prev
                self.dic[key]=k
        k.next=self.head.next
        self.head.next.prev=k
        k.prev=self.head
        self.head.next=k
    def get(self,key):
        if(key not in self.dic):
            return -1
        else:
            g=self.dic[key].value
            p=self.dic[key]
            k=Node(key,g)
            p.prev.next=p.next
            p.next.prev=p.prev
            self.dic[key]=k
            k.next=self.head.next
            self.head.next.prev=k
            k.prev=self.head
            self.head.next=k
            return g

    def Print(self):
        k=self.head
        while(k!=None):
            print(k.key,k.value,end=" ")
            k=k.next
        print()
        print(self.dic)


ans=DLL(3)
ans.put(1,10)
ans.put(2,10)
ans.put(1,20)
ans.Print()
