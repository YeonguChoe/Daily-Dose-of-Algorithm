'''
https://leetcode.com/problems/min-stack/
2024-07-14
'''

class MinStack:

    def __init__(self):
        self.origin_list = []
        self.min_list = []

    def push(self, val: int) -> None:
        self.origin_list.append(val)
        if len(self.min_list) == 0 or self.min_list[-1] > val or self.min_list[-1] == val:
            self.min_list.append(val)

    def pop(self) -> None:
        val = self.origin_list.pop()
        if self.min_list[-1] == val:
            self.min_list.pop()

    def top(self) -> int:
        return self.origin_list[-1]

    def getMin(self) -> int:
        if len(self.min_list) != 0:
            return self.min_list[-1]
        else:
            return min(self.origin_list)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()