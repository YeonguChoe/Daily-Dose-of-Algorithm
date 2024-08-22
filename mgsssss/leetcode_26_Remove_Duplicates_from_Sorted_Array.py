'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
2024-08-22

출제자의 의도를 파악하는데 생각이 걸렸다.
새롭게 배열을 만드는게 아닌 기존 배열에서 고쳐야 한다는 생각을 했다.
배열의 index 를 삭제하면 O(n) 만큼의 시간이 걸려서 효율이 엄청 좋지 않다.
그래서 투포인터를 사용해서, 값이 다르다면 다른 값을 넣어주는 방식으로 풀었다.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[prev-1]:
                nums[prev] = nums[i]
                prev += 1
        return prev