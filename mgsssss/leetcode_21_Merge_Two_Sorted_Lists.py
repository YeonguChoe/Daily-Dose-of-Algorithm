'''
https://leetcode.com/problems/merge-two-sorted-lists/
2024-08-22

merge sort 를 공부하면 이문제는 너무 쉽다.
merge sort 에서 병합 부분만 알면 쉽게 풀 수 있다.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resNode = ListNode(0, None)
        dump = resNode
        while list1 and list2:
            if list1.val < list2.val:
                dump.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                dump.next = ListNode(list2.val, None)
                list2 = list2.next
            dump = dump.next
        if list1:
            dump.next = list1
        if list2:
            dump.next = list2
        return resNode.next
        