'''
https://leetcode.com/problems/counting-bits/
2024-07-30

일단 풀기는 풀었는데, 더 좋은 방법을 봤다 ... ㅋㅋ
'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [i for i in range(n+1)]
        for i in range(len(res)):
            res[i] = list(bin(res[i])).count('1')
        return res