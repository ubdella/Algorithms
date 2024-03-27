class MyQueue:

    def __init__(self):
        self.queue = []
        self.stack = []
        self.top = -1

    def push(self, x: int) -> None:
        self.top+=1
        while self.queue:
            self.stack.append(self.queue.pop())
        self.queue.append(x)
        while self.stack:
            self.queue.append(self.stack.pop())

    def pop(self) -> int:
        self.top-=1
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()