class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        left = 0
        right = n - 1
        row = 0
        while left < right:
            for col in range(left, right):
                temp = matrix[row][col]
                matrix[row][col] = matrix[n - 1 - col][row]
                matrix[n - 1 - col][row] = matrix[n - 1 - row][n - 1 - col]
                matrix[n - 1 - row][n - 1 - col] = matrix[col][ n - 1 - row]
                matrix[col][ n - 1 - row] = temp
            left += 1
            right -= 1
            row += 1