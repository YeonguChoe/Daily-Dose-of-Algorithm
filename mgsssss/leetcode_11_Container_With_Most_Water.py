'''
https://leetcode.com/problems/container-with-most-water/
2024-07-24

투포인터로 풀면 쉽다.
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = [0]
        
        def expand(left, right):
            while left < right:
                max_height = min(height[left], height[right])
                max_water[0] = max(max_height * (right-left),max_water[0])
                
                if height[left] > height[right]:
                    right -= 1
                else:
                    left += 1

        right = len(height) - 1
        expand(0, right)
        return max_water[0]