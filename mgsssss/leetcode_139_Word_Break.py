'''
https://leetcode.com/problems/word-break/
2024-09-03

고난이도 문제 dp 는 항상 어렵다.
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp: dict = {}

        def dfs(i):
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            for word in wordDict:
                if s[i:len(word)+i] == word:
                    if dfs(len(word)+i):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)