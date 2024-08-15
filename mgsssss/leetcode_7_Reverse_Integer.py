'''
https://leetcode.com/problems/reverse-integer/description/
2024-07-24

최대한 내장 함수를 사용하려고 한 풀이
'''

class Solution:
    def reverse(self, x: int) -> int:
        signed = True
        if x < 0:
            signed = False
            num = int("".join(list(reversed([ i for i in str(x)]))[:-1]))
        else:
            num = int("".join(list(reversed([ i for i in str(x)]))))
        if num >= (2**31)-1:
            return 0        
        if signed:
            return num
        return -num
