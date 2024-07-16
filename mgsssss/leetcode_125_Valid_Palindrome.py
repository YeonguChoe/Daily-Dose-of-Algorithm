'''
https://leetcode.com/problems/valid-palindrome/
2024-07-16

넘나 쉬운 문제 3분컷
'''

from collections import deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque([i.lower() for i in s if i.isalnum()])
        while q:
            if len(q) == 1:
                return True

            if q.popleft() != q.pop():
                return False
                
        return True