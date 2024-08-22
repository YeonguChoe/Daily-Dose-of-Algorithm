'''
https://leetcode.com/problems/majority-element/description/
2024-08-22

생각을 많이 하게 하는 문제 좋다.
밑에는 모범 답안

모범 답안은 공간복잡도가 상당히 낮다.
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict: dict = defaultdict(int)
        nums_len = (len(nums) // 2) + 1
        for num in nums:
            nums_dict[num] += 1
            if nums_dict[num] >= nums_len:
                return num

        '''
        cnt: int = 0
        res: int = 0

        for num in nums:
            if cnt == 0:
                res = num
            if res == num:
                cnt += 1
            else:
                cnt -= 1
        return res
        '''