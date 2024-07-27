'''
https://leetcode.com/problems/pascals-triangle/
2024-07-27

이렇게 해서 풀릴까 생각했는데 진짜 풀림
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * i for i in range(numRows+1) ]
        res = res[1:]
        for i in range(1, numRows):
            for j in range(1, len(res[i])-1):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        