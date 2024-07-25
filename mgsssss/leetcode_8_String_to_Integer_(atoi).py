'''
https://leetcode.com/problems/string-to-integer-atoi/
2024-07-25

진짜 문제 그대로 푸는 문제
내 구현 능력을 올려야겠다는 생각을 함.
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        signed = 1
        s = s.lstrip()
        if len(s) == 0:
            return 0
        i = 0
        if s[i] == "+":
            signed = 1
            i += 1
        elif s[i] == "-":
            signed = -1
            i += 1
        parsed = 0
        while i < len(s):
            if s[i].isdigit():
                parsed = parsed * 10 + int(s[i])
            else:
                break
            i += 1
        MAX_INTEGER = 2 ** 31 - 1
        MIN_INTEGER = -2 ** 31
        parsed = int(parsed) * signed
        if signed > 0:
            return min(int(parsed), MAX_INTEGER)
        else:
            return max(int(parsed), MIN_INTEGER)