'''
https://leetcode.com/problems/binary-tree-level-order-traversal/
2024-09-27
생각보다 쉬웠다. list 를 어떻게 이어 붙일지 고민하다가 list 와 level을 비교해서 append 시키는 방법으로 풀었다.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, level):
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
            else:
                return
            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)
        
        dfs(root, 0)
        return res