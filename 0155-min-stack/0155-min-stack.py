class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        self.topp = -1
        self.min = None
        
    def push(self, val: int) -> None:
        if self.topp==-1:
            self.min=val
        self.stack.append(val)
        self.topp+=1
        if(self.min>val):
            self.min = val
        self.minstack.append(self.min)
        
    def pop(self) -> None:    
        self.min = self.minstack[self.topp-1]
        self.stack = self.stack[:len(self.stack)-1]
        self.minstack = self.minstack[:len(self.minstack)-1]
        
        self.topp-=1
        
        
        
    def top(self) -> int:
        return self.stack[self.topp]

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()