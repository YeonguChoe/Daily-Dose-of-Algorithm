class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i,n):
                # transpose the matrix
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            # reverse every row
            matrix[i].reverse()
