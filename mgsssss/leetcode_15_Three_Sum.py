'''
https://leetcode.com/problems/3sum/
2024-07-15
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        def expand(i, left, right):
            
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                # 0보다 크면 값을 줄여야 한다.
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0: # 0보다 작으면 값을 키워야 한다.
                    left += 1
                else: # 0일 경우
                    res.append([nums[i], nums[left] , nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
        nums.sort()
        right = len(nums) - 1 # 중복 연산 하지 않을려고
        for i in range(len(nums)):

            # 어짜피 값이 0 이상면 빼지를 못하니 0이 되지를 못한다.
            if nums[i] > 0:
                break

            # 0보다 클때 이전값과 현재값이 동일하다면 굳이 연산할 필요가 없다.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            expand(i, i+1, right)

        return res