class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = sorted(nums)
        return l[-k]
