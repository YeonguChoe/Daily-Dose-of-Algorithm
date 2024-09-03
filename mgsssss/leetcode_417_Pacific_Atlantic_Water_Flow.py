'''
https://leetcode.com/problems/pacific-atlantic-water-flow/
2024-09-03

코드는 길지만 아이디만 있으면 풀 수 있는 문제!
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res: list = []
        rows, cols = len(heights), len(heights[0])
        delta = [(0,1), (1,0), (0,-1), (-1,0)]
        def bfs(row, col, visited):
            q = deque([(row, col)])
            visited.add((row, col))
            while q:
                cur_row, cur_col = q.popleft()

                for dr, dc in delta:
                    nr = cur_row + dr
                    nc = cur_col + dc
                    if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                        if (nr, nc) not in visited and heights[nr][nc] >= heights[cur_row][cur_col]:
                            visited.add((nr, nc))
                            q.append((nr, nc))

        for row in range(rows):
            bfs(row, 0, pacific)
            bfs(row, cols-1, atlantic)
        
        for col in range(cols):
            bfs(0, col, pacific)
            bfs(rows-1, col, atlantic)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res