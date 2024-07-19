'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
2024-07-19

더 좋은 방법은 있을거 같은데, 현재 생각나는 방법대로 풀었다.
deque 를 사용하여 앞에 있는 문자열을 제거해주면서 카운트 해줬다.
'''

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = len(s)
        if len(s) == 1:
            return 1
        def expand(left, right):
            q = deque()
            max_lengh = 0
            while left < right:
                while s[left] in q:
                    q.popleft()

                q.append(s[left])
                max_lengh = max(len(q), max_lengh)
                left += 1
            return max_lengh
        return expand(0, right)