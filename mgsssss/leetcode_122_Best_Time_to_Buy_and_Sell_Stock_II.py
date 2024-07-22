'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
2024-07-22

121번 문제와 비슷하면서 조금 다르다.
min_price가 핵심이다.
이전값이 현재값보다 작으면 무조건 빼서 list 에 append 해줬다.
prices = [1,2,3,4,5]
위에 예를 보면 1에서 사서 5에서 팔면 4이다.
하지만 (1,2) (2,3) (3,4) (4,5) 이렇게 팔아도 4이다.
그래서 매도를 하면 현재 값을 min_price에 넣어줘서 여태까지 가장 작은 값을 덮었다.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = sys.maxsize
        price_list = []
        for price in prices:
            min_price = min(min_price, price)
            if price - min_price > 0:
                price_list.append(price - min_price)
                min_price = price
            
        return sum(price_list)