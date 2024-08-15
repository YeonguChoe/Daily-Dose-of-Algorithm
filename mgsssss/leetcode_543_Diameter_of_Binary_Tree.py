'''
https://leetcode.com/problems/diameter-of-binary-tree/
2024-07-21

생각할것이 많은 문제
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        node = root
        self.res = 0
        def dfs(node):
            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res ,left + right + 2) # 현재 노드의 최대 지름 길이.
            return 1 + max(left, right) # 현재 노드에서 제일 큰 노드의 숫자

        dfs(node)
        return self.res
        
