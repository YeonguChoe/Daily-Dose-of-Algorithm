'''
https://leetcode.com/problems/decode-ways/
2024-09-25

dp 문제 !
백트래킹으로 풀어볼려다가 삽질을 많이했다.
함수 안에는 정말 문제에서 나온 그대로 표현하면 풀리기는 풀린다.
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            if i+1 < len(s) and int(s[i:i+2]) < 27:
                dp[i] = dfs(i+1) + dfs(i+2)
            else:
                dp[i] = dfs(i+1)
            return dp[i]
        return dfs(0)