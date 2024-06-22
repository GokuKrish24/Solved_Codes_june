class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if(len(heights)==0):
            return
        stack=[0]
        lefts=[0]
        for i in range(1,len(heights)):
            while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                stack.append(i)
                lefts.append(0)
            else:
                lefts.append(stack[-1]+1)
                stack.append(i)
        stack=[len(heights)-1]
        rights=[len(heights)-1]
        for i in range(len(heights)-2,-1,-1):
            while(len(stack)!=0 and heights[stack[-1]]>=heights[i]):
                stack.pop()
            if(len(stack)==0):
                stack.append(i)
                rights.insert(0,len(heights)-1)
            else:
                rights.insert(0,stack[-1]-1)
                stack.append(i)
        m=-100000000
        print(lefts)
        print(rights)
        for i in range(len(lefts)):
            m=max(m,(rights[i]-lefts[i]+1)*heights[i])
        return m            
