'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
2024-07-14
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        price = sys.maxsize

        for i in prices:
            price = min(i, price)
            max_price = max(i - price, max_price)
        
        return max_price