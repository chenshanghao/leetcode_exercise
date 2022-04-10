class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        stack_length = len(self.stack)
        if stack_length > 0:
            self.stack = self.stack[0: stack_length - 1]
            


    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()