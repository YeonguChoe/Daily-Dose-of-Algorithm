'''
https://leetcode.com/problems/linked-list-cycle/
2024-07-22

set 을 사용해서 set 자료구조에 node 가 들어와 있으면 순환구조라고 볼 수 있다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()

        while node:
            if node in visited:
                return True
            visited.add(node)
            node = node.next
        return False
