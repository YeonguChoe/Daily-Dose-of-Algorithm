'''
https://leetcode.com/problems/perfect-squares/
2024-09-09

dp 문제 그런데 생각하기 어려워서 bfs로 풀었는데 풀렸다.
'''

class Solution:
    def numSquares(self, n: int) -> int:
        n_list = [ i * i for i in range(1, floor(n**0.5)+1) ]
        q = deque([(0, 0)])
        visited = set()
        while q:
            cur_num, cur_len = q.popleft()
            if cur_num == n:
                return cur_len
            for next_num in n_list:
                total = cur_num + next_num
                if total > n:
                    break
                if total in visited:
                    continue
                q.append((total, cur_len+1))
                visited.add(total)