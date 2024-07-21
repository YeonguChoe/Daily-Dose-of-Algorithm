"""
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A subarray arr is good if it there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:
1 <= nums.length <= 10**5
1 <= nums[i], k <= 10**9
"""
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        pair_count = 0
        res = 0
        freq = defaultdict(int)
        for right in range(n):
            freq[nums[right]] += 1 # == Counter(nums[:right+1])
            pair_count += freq[nums[right]] - 1
            # print(freq, pair_count)
            while pair_count >= k:
                print(n, right, res, freq, pair_count, '*')
                res += n - right
                pair_count -= freq[nums[left]] - 1
                freq[nums[left]] -= 1
                left += 1
            print(n, right, res, freq, pair_count)    

        return res
