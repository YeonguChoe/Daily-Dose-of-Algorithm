'''
https://leetcode.com/problems/length-of-last-word/
2024-08-07
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s_list = s.split()
        
        return len(s_list[-1])