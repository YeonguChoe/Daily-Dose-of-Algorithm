# 풀이로직: https://ssuojae.tistory.com/258

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def find_path(self, root, target):
        stack = [(root, [root])]
        while stack:
            node, path = stack.pop()
            if node == target:
                return path
            if node.right:
                stack.append((node.right, path + [node.right]))
            if node.left:
                stack.append((node.left, path + [node.left]))
        return None

    def contains(self, root, target):
        if not root:
            return False
        if root == target:
            return True
        return self.contains(root.left, target) or self.contains(root.right, target)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path_to_p = self.find_path(root, p)
        if not path_to_p:
            return None  # p가 트리에 없으면 None 반환

        while path_to_p:
            node = path_to_p.pop()
            if self.contains(node, q):
                return node
        return None
