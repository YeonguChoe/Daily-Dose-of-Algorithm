'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
2024-09-04

생각보다 까다로웠던 문제,
ListNode의 length 를 구하고 해당 dummy를 만들어 준다. (첫번째 노드를 제거해야하는 경우 때문에)
length 를 구하면 반복문을 통하여, 뒤에서 n번째 노드를 제거 할 수 있다.
time : O(2n)
space : O(n)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length: int = 0
        node = head

        while node:
            length += 1
            node = node.next
        dummy = ListNode(None, head)
        node = dummy
        for i in range(length-n):
            node = node.next
        node.next = node.next.next
        return dummy.next