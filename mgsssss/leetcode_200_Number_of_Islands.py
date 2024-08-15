'''
https://leetcode.com/problems/number-of-islands/
2024-08-09

처음 bfs dfs 풀었을때 풀었던 문제,
기본 문제
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        cnt = 0
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        def bfs(row, col):
            visited.add((row, col))
            q = deque([(row, col)])
            while q:
                cur_row, cur_col = q.popleft()
                for dr, dc in delta:
                    nr = cur_row + dr
                    nc = cur_col + dc
                    if nr < rows and nc < cols and nr >= 0 and nc >= 0:
                        if (nr, nc) not in visited and grid[nr][nc] == "1":
                            q.append((nr, nc))
                            visited.add((nr, nc))
            return
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    cnt += 1
        return cnt
