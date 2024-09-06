'''
https://leetcode.com/problems/can-place-flowers/
2024-08-29

생각나는데로 풀었다. 재밌는 문제
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
            return True if n <= 0 else False

        for i in range(0, len(flowerbed)):
            if n == 0:
                return True
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n-=1
                flowerbed[i] = 1
            elif i == len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                n-=1
                flowerbed[i] = 1                
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n-=1
                flowerbed[i] = 1
            
        return True if n == 0 else False