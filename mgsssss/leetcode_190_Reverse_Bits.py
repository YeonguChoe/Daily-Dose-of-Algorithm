'''
https://leetcode.com/problems/reverse-bits/
2024-07-30

비트를 컨트롤 하는걸 공부해야겠다고 느낌.
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        n_list = [i for i in bin(n)]
        n_list = n_list[2:]
        n_list.reverse()
        if len(n_list) != 32:
            num = 32 - len(n_list)
            for _ in range(num):
                n_list.append('0')
        return int("".join(n_list),2)