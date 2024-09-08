'''
https://leetcode.com/problems/surrounded-regions/
2024-09-09

bfs 로 풀었다. 아이디어는 가장자리에서 O 인 경우를 타고 올라가서 그 이외에는 모두 X로 변경하면 된다.
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        visited = set()
        delta = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(row, col):
            if (row, col) in visited:
                return
            visited.add((row, col))
            q = deque([(row, col)])
            while q:
                cur_row, cur_col = q.popleft()
                for dr, dc in delta:
                    nr = dr + cur_row
                    nc = dc + cur_col
                    if nr < rows and nr >= 0 and nc < cols and nc >= 0:
                        if (nr, nc) not in visited and board[nr][nc] == 'O':
                            visited.add((nr, nc))
                            q.append((nr,nc))

        for row in range(rows):
            if board[row][0] == 'O':
                bfs(row, 0)
            if board[row][cols-1] == 'O':
                bfs(row, cols - 1)

        for col in range(cols):
            if board[0][col] == 'O':
                bfs(0, col)
            if board[rows-1][col] == 'O':
                bfs(rows - 1, col)
        for row in range(rows):
            for col in range(cols):
                board[row][col] = 'X'
        for a, b in visited:
            board[a][b] = 'O'
