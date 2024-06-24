class MinStack:

    def __init__(self):
        self.arr=[]
        self.minstack=[]


    def push(self, val: int) -> None:
        if(len(self.minstack)==0 or val<=self.minstack[-1]):
            self.minstack.append(val)
        self.arr.append(val)


    def pop(self) -> None:
        if(len(self.arr)==0):
            return
        if(self.arr[-1]==self.minstack[-1]):
            self.minstack.pop()
        self.arr.pop()
        

    def top(self) -> int:
        if(len(self.arr)==0):
            return
        return self.arr[-1]

    def getMin(self) -> int:
        if(len(self.minstack)==0):
            return
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
