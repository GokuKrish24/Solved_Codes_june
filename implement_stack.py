class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,element):
        self.arr.append(element)
    def pop(self):
        if(len(self.arr)==0):
            return -1
        return self.arr.pop()
stac=Stack()
stac.push(1)
stac.push(2)
print(stac.pop())
