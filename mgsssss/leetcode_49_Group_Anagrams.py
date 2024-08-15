'''
https://leetcode.com/problems/group-anagrams/
2024-07-16

간단한 아이디어와 python의 파워풀함
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)
        for i in strs:
            s = "".join(sorted(i))
            str_dict[s].append(i)
        return list(str_dict.values())