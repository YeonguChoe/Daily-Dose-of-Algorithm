'''
https://leetcode.com/problems/binary-search/
2024-07-15

너무나 쉬운 문제 이진탐색 트리에 대한 기본
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1
            