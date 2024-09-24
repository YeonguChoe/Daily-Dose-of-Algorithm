'''
https://leetcode.com/problems/min-cost-climbing-stairs/
2024-09-24

전형적인 dp문제 처음 dp문제 풀었을때 풀었던 문제
난이도는 eazy이지만 생각하는 방법은 dp형식으로 생각해야해서 어려웠다.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        
        def dfs(i):
            if i <= 1:
                return 0
            
            if i in dp:
                return dp[i]
            dp[i] = min(dfs(i-1)+cost[i-1], dfs(i-2)+cost[i-2])
            return dp[i]
        return dfs(len(cost))
        