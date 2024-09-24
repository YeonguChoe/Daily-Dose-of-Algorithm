'''
https://leetcode.com/problems/coin-change/
2024-09-24

이전에 한번 풀어본 문제 외웠다.
다시 한번 복습 할 수 있어서 다행이다. 난이도 상
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1 ,amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i-c] + 1, dp[i])
        
        return dp[-1] if dp[-1] != amount+1 else -1