'''
https://leetcode.com/problems/longest-palindromic-substring/
2024-08-20

Two pointer
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        res = ""
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        for i in range(len(s)):
            res = max(res, expand(i, i+1), expand(i, i+2), key=len)
        return res