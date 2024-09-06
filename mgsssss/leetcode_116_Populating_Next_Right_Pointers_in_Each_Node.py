'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
2024-08-19

재밌는 문제
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        node = root
        q = deque([(node, 0)])
        cnt = 0
        while q:
            cur_node, cur_cnt = q.popleft()
            if len(q) > 0 and q[0][1] == cur_cnt:
                cur_node.next = q[0][0]
            else:
                cur_node.next = None
            if cur_node.left:
                q.append((cur_node.left, cur_cnt + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_cnt + 1))
        return node