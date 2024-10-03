class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        max_side = 0
        @cache
        def dfs(i, j):
            if i >= rows or j >= cols or matrix[i][j] == '0':
                return 0

            right = dfs(i, j + 1)
            down = dfs(i + 1, j)
            diag = dfs(i + 1, j + 1)

            return min(right, down, diag) + 1

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    max_side = max(max_side, dfs(i, j))

        return max_side * max_side