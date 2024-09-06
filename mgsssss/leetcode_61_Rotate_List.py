'''
https://leetcode.com/problems/rotate-list/
2024-08-19

풀어봤는데 모범답안이랑은 많이 다름
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        q = deque()
        while node:
            q.append(node.val)
            node = node.next
        if len(q) == 0:
            return head
        if k > len(q):
            k = k % len(q)
        for i in range(k):
            val = q.pop()
            q.appendleft(val)
        new_node = ListNode(0)
        dump = new_node
        while q:
            new_node.next = ListNode(q.popleft())
            new_node = new_node.next

        return dump.next