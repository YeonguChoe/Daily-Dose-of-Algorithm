'''
https://leetcode.com/problems/shortest-path-in-binary-matrix/
2024-08-26

너무 쉬운 문제
'''

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        delta = [(0,1), (1,0), (0,-1), (-1,0), (-1,-1), (-1,1), (1,1), (1,-1)]
        if grid[0][0] == 1 or grid[rows-1][cols-1] == 1:
            return -1
        
        visited = set()
        q = deque([(0,0,1)])
        while q:
            cur_row, cur_col, cur_path = q.popleft()
            if cur_row == rows-1 and cur_col == cols-1:
                return cur_path
            for dr, dc in delta:
                nr = dr + cur_row
                nc = dc + cur_col
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if (nr, nc) not in visited and grid[nr][nc] == 0:
                        q.append((nr,nc,cur_path+1))
                        visited.add((nr,nc))
        return -1
        

