'''
https://leetcode.com/problems/word-search/description/
2024-08-20
문제에서 원하는 방식의 풀이는 아닌거 같은데, bfs로 풀었다. q 에 set 자료구조 하나 넣어줘서 각각의 q 마다 set 자료구조를 가지고
지속적으로 탐색해 나간다.
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(board), len(board[0])
        def bfs(row, col):
            q = deque([(row, col, 1, set( {(row, col)} ))])
            while q:
                cur_row, cur_col, cur_index, cur_set = q.popleft()
                
                if cur_index == len(word):
                    return True
                for dr, dc in delta:
                    nr = dr + cur_row
                    nc = dc + cur_col
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                        if word[cur_index] == board[nr][nc] and (nr, nc) not in cur_set:
                            temp_set = set(cur_set)
                            temp_set.add((nr, nc))
                            q.append((nr, nc, cur_index+1, temp_set))
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and bfs(row, col):
                    return True
        return False
        '''
        "ABCESEEEFS"
        [
        ["A","B","C","E"],
        ["S","F","E","S"],
        ["A","D","E","E"]
        ]
        '''