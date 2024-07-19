'''
https://leetcode.com/problems/longest-repeating-character-replacement/
2024-07-19

어찌어찌 풀었다. 풀긴 풀었는데 시간복잡도 O(n)이 나오긴 했지만, 시간은 조금 걸린듯 하다.
이건 한번 공부해봐야겠다 ...
'''

from collections import deque, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def expand(left, right):
            q = deque()
            max_length = 0
            while left < right:
                q.append(s[left])
                counter_q = Counter(q)
                most_counter = counter_q.most_common(1)[0][1]
                sum = len(q) - most_counter
                if sum <= k:
                    max_length = max(len(q), max_length)
                else:
                    q.popleft()
                left += 1
            return max_length
        return expand(0, len(s))