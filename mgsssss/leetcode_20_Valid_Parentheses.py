'''
https://leetcode.com/problems/valid-parentheses/description/
2024-07-16

정말 stack에 대표적인 문제
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
                continue
            if len(stack) == 0:
                return False
            if i == ")" and stack[-1] == "(":
                stack.pop()
                continue

            if i == "}" and stack[-1] == "{":
                stack.pop()
                continue

            if i == "]" and stack[-1] == "[":
                stack.pop()
                continue
            return False

        return len(stack) == 0