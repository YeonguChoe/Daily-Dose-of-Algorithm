'''
https://leetcode.com/problems/shortest-bridge/
2024-08-29

코딩은 쉽지만, 한참 고민한 문제.
'''

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        def dfs(row, col):
            grid[row][col] = 2
            q.append((row, col, 0))
            for dr, dc in delta:
                nr = dr + row
                nc = dc + col
                if nr < rows and nc < cols and nr >= 0 and nc >= 0:
                    if grid[nr][nc] == 1:
                        dfs(nr, nc)

        def findOneIsland():
            for row in range(rows):
                for col in range(cols):
                    if grid[row][col]:
                        return dfs(row, col)
        findOneIsland()
        step = 0
        while q:
            cur_row, cur_col, cur_length = q.popleft()

            for dr, dc in delta:
                nr = dr + cur_row
                nc = dc + cur_col
                if nr < rows and nc < cols and nr >= 0 and nc >= 0:
                    if (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if grid[nr][nc] == 1:
                            return cur_length
                        elif grid[nr][nc] == 0:
                            q.append((nr, nc, cur_length+1))
        '''
        [0,1,0],
        [0,0,0],
        [0,0,1]

        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],

        [1,1,1,1,1]
        [1,1,0,0,0],
        [1,0,0,0,0],
        [1,0,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
        '''