class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,element):
        def insert(arr,element):
            if(len(self.arr)==0):
                arr.append(element)
                return
            t=arr.pop(0)
            insert(arr,element)
            arr.append(t)
        def insert1(arr):
            if(len(self.arr)==0):
                return
            t=arr.pop(0)
            insert1(arr)
            arr.append(t)
        insert1(self.arr)
        insert(self.arr,element)
        print(self.arr)
    def pop(self):
        if(len(self.arr)==0):
            return -1
        return self.arr.pop(0)
stak=Stack()
stak.push(1)
stak.push(2)
stak.push(3)
stak.push(4)
print(stak.pop())
print(stak.pop())
print(stak.arr)
