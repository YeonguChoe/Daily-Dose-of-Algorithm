'''
https://leetcode.com/problems/rotting-oranges/
2024-08-09

bfs로 풀어야하는 문제,
이것 저것 해보면서 풀었다.
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0] * cols for _ in range(rows)]
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        q = deque()
        cnt = 0
        def bfs(q):
            while q:
                change = False
                cur_row, cur_col, cur_cnt = q.popleft()
                visited[cur_row][cur_col] = 1
                for dr, dc in delta:
                    nr = cur_row + dr
                    nc = cur_col + dc
                    if nr < rows and nc < cols and nr >= 0 and nc >= 0:
                        if grid[nr][nc] == 1 and visited[nr][nc] == 0:
                            change = True
                            q.append((nr, nc, cur_cnt+1))
                            visited[nr][nc] = 1
                            grid[nr][nc] = 2
            return cur_cnt
        
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == 0 and grid[row][col] == 2:
                    q.append((row, col, 0))
        if len(q) != 0:
            cnt = bfs(q)
            
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1
        return cnt
        '''
        [[2,1,1]
        ,[1,1,1]
        ,[0,1,2]]
        '''

        
        
