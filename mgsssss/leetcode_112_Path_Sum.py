'''
https://leetcode.com/problems/path-sum/
2024-07-17

이런 유형의 문제는 많이 풀어봐야 쉽게 풀린다.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        q = deque()
        if root:
            q.append((root, root.val))
        while q:
            cur_node, cur_sum = q.popleft()
            if cur_node.left is None and cur_node.right is None:
                if cur_sum == targetSum:
                    return True
            if cur_node.left:
                q.append((cur_node.left, cur_sum+cur_node.left.val))

            if cur_node.right:
                q.append((cur_node.right, cur_sum+cur_node.right.val))
        return False