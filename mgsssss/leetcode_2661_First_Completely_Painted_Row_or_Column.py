'''
https://leetcode.com/problems/first-completely-painted-row-or-column/
2024-07-31

생각을 많이 하게하는 문제, dfs or bfs 로 풀어보려고 했는데, 아니다.
좋은 문제 !!!
'''

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        arr_dict = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                arr_dict[mat[row][col]] = [row, col]
        row_dict = defaultdict(int)
        col_dict = defaultdict(int)
        cnt = 0
        for a in arr:
            row, col = arr_dict[a]
            row_dict[row] += 1
            col_dict[col] += 1
            if row_dict[row] == len(mat[0]):
                return cnt
            if col_dict[col] == len(mat):
                return cnt                
            cnt += 1
        


