class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m*n -1
        
        while i <= j:
            mid1D = (i + j)//2
            mid = matrix[mid1D//m][mid1D % m]
            if mid == target: return True
            elif mid < target: i = mid1D + 1
            else: j = mid1D -1             
        return False