'''
https://leetcode.com/problems/climbing-stairs/
2024-08-15
알면 쉽지만 모르면 어렵다 딱 dp
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(n):
            if n == 1 or n == 2:
                dp[n] = 1
                # 만약 1 또는 2가 n 으로 들어올경우 바로 그 값을 리턴해줌
                return n
            if n in dp:
                return dp[n]
            dp[n] = dfs(n-1) + dfs(n-2)
            return dp[n]
        return dfs(n) 
