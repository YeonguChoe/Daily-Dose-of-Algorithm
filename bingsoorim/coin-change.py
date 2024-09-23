class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # classic dp-bottom up problem
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
