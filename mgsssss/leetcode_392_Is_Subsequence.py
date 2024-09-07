'''
https://leetcode.com/problems/is-subsequence/
2024-09-07

생각보다 쉽게 풀림, eazy ~~~
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        q = deque()
        for i in range(len(s)):
            q.append(s[i])
        
        for i in range(len(t)):
            if len(q) == 0:
                return True
            if t[i] == q[0]:
                q.popleft()
        
        return True if len(q) == 0 else False