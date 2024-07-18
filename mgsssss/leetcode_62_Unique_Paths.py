'''
https://leetcode.com/problems/unique-paths/
2024-07-18

작은 문제로 큰문제를 해결한다. dp 문제의 풀이 방법
하지만 dp는 풀떄마다 헷갈린다 ...
'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        def dfs(m, n):
            if m == 0 or n == 0:
                return 1

            if dp[m][n] == 0:
                dp[m][n] = dfs(m-1, n) + dfs(m, n-1)

            return dp[m][n]
        res = dfs(m-1, n-1)

        return res