class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        cnt=0
        while(len(self.stack)!=0 and self.stack[-1][0]<=price):
            cnt+=1+self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price,cnt))
        cnt+=1
        return cnt
