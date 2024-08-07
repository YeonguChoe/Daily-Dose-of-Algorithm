class Solution:
    '''
    https://leetcode.com/problems/spiral-matrix/
    2024-08-06

    나만의 방식으로 풀어봄
    성능 괜찮음
    '''
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        res = []
        next_dir = {
            'right': 'down',
            'down': 'left',
            'left': 'up',
            'up': 'right',
        }
        visited = set()
        now = 'right'
        row, col = 0, 0
        add = True
        while len(res) != rows * cols:
            if add:
                res.append(matrix[row][col])
                visited.add((row, col))
            if now == 'right':
                col += 1
            elif now == 'down':
                row += 1
            elif now == 'up':
                row -= 1
            elif now == 'left':
                col -= 1
            add = True

            if row >= rows or col >= cols or row < 0 or col < 0 or (row, col) in visited:
                add = False
                if now == 'right':
                    col -= 1
                elif now == 'down':
                    row -= 1
                elif now == 'up':
                    row += 1
                elif now == 'left':
                    col += 1
                now = next_dir[now]
        return res




