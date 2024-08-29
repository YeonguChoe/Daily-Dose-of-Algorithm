'''
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
2024-08-29

기본적인 문제
'''

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        
        q = deque([(entrance[0], entrance[1], 0)])
        delta = [(1,0), (0,1), (-1,0), (0,-1)]
        rows, cols = len(maze), len(maze[0])
        while q:
            cur_row, cur_col, cur_length = q.popleft()
            if cur_row == 0 or cur_col == 0 or cur_row == rows - 1 or cur_col == cols -1:
                if entrance != [cur_row, cur_col]:
                    return cur_length
            for dr, dc in delta:
                nr = cur_row + dr
                nc = cur_col + dc
                if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                    if (nr, nc) not in visited and maze[nr][nc] != '+':
                        visited.add((nr, nc))
                        q.append((nr, nc, cur_length+1))
        return -1
                