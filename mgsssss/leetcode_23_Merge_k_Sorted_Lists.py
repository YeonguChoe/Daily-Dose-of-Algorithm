'''
https://leetcode.com/problems/merge-k-sorted-lists/
2024-08-22

생각보다 쉽게 풀렸다.
난이도 hard 인데 5분만에 풀렸다.
21번 문제를 풀고 바로 풀어서 오히려 쉽게 느껴졌다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []
        for list_node in lists:
            while list_node:
                heappush(hq, list_node.val)
                list_node = list_node.next
        resNode = ListNode(0, None)
        dump = resNode
        while hq:
            dump.next = ListNode(heappop(hq))
            dump = dump.next
        return resNode.next 