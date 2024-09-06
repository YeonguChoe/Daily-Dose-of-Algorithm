'''
https://leetcode.com/problems/roman-to-integer/
2024-08-22

문제 그대로 코드로 옮기면 되는 문제
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        nums_dict = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    'IV': 4,
                    'IX': 9,
                    'XL': 40,
                    'XC': 90,
                    'CD': 400,
                    'CM': 900
        }
        index = 0
        len_s = len(s)
        res = 0
        while len_s > 0:
            if len_s > 1 and s[index:index+2] in nums_dict:
                res += nums_dict[s[index:index+2]]
                index += 2
                len_s -= 2
                continue
            
            res += nums_dict[s[index]]
            index += 1
            len_s -= 1
        return res

        