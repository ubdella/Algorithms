class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def mark(i, j):
            for k in range(0, n):
                if matrix[i][k] != 0:
                    matrix[i][k] = 'X'
            for k in range(0, m):
                if matrix[k][j] != 0:
                    matrix[k][j] = 'X'
                
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    mark(i, j)
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0