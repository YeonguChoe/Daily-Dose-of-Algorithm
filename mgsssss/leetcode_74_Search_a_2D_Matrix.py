'''
https://leetcode.com/problems/search-a-2d-matrix/
2024-09-25

생각보다 쉽게 풀린 문제,
바이너리 서치를 사용하면 된다.
처음 봤을때는 잘 떠오르지 않았는데, 배열을 길게 옆으로 세운다고 생각하면 된다.
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0:
            left, right = 0, cols-1
        else:
            left, right = 0, (rows * cols) - 1
        while left <= right:
            m = (left + right) // 2
            r, c = divmod(m, cols)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = m - 1
            else:
                left = m + 1
        return False