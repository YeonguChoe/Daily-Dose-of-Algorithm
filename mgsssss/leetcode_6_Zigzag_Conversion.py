'''
https://leetcode.com/problems/zigzag-conversion/
2024-07-22

너무 생각을 많이 하면 어려운 문제, 일단 손으로 그려보면 쉽게 풀린다.
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        down = False
        rows = 0
        numList = [[] for _ in range(numRows)]
        for i in range(len(s)):
            numList[rows].append(s[i])
            if rows == 0:
                down = False
            elif rows == numRows-1:
                down = True

            if down:
                rows -= 1
            else:
                rows += 1
        return "".join(["".join(i) for i in numList])