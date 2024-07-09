class MinStack:

    def __init__(self):
        # use two stacks
        self.stack = [] # actual values
        self.min_stack = [] # store minimum values seen so far

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if min stack is empty or the val is smaller/equal to current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # if the element to pop is the current minimum
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            # always pop from the main stack
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            # return the top element
            return self.stack[-1] 

    def getMin(self) -> int:
        if self.min_stack:
            # the current minium value
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
