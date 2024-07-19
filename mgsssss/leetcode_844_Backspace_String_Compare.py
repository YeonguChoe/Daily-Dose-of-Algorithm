'''
https://leetcode.com/problems/backspace-string-compare/
2024-07-19

조금만 고민하면 간단한 문제 나는 stack 을 활용했다.
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        new_t = []

        for i in range(len(s)):
            if s[i] == "#" and len(new_s) > 0:
                new_s.pop()
            elif s[i] != "#":
                new_s.append(s[i])

        for i in range(len(t)):
            if t[i] == "#" and len(new_t) > 0:
                new_t.pop()
            elif t[i] != "#":
                new_t.append(t[i])
                
        return new_s == new_t
            