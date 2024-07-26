'''
https://leetcode.com/problems/design-browser-history/
2024-07-26

여러 방법이 있지만 Linked List를 사용하는게 깔끔하다.
'''


class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.now = self.head

    def visit(self, url: str) -> None:
        self.new_node = ListNode(url)
        self.now.next = self.new_node
        self.new_node.prev = self.now
        self.now =self.new_node
        return

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.now.prev is not None:
                self.now = self.now.prev
            else:
                break
        return self.now.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.now.next is not None:
                self.now = self.now.next
            else:
                break
        return self.now.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)