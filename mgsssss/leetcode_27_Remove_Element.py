'''
https://leetcode.com/problems/remove-element/description/
2024-08-28

더 좋은 방법은 있는거 같지만, python sort 를 활용하여 정렬하고 index 를 계산
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        if len(nums) == 0:
            return i
        nums.sort(key=lambda x : x==val)

        while len(nums) > i and nums[i] != val:
            i += 1
        return i