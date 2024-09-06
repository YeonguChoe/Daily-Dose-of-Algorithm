'''
https://leetcode.com/problems/find-the-town-judge/
2024-08-16

단순하지만 생각할게 많은 문제
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_dict = {}
        judge_dict = defaultdict(int)
        judge = -1
        if len(trust) == 0 and n == 1:
            return n
        for a, b in trust:
            t_dict[a] = 1
        for a, b in trust:
            judge_dict[b] += 1
        for key, val in judge_dict.items():
            if val == n-1:
                judge = key
                break
        return -1 if judge in t_dict else judge