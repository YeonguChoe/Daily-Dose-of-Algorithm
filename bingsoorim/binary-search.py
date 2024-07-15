class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                # return index
                return mid
            elif target < nums[mid]:
                # binary search the first half
                right = mid-1
            else:
                # target > nums[mid] then binary search the second half
                left = mid+1
        return -1
