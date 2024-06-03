class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, q = len(mat), len(mat[0]), deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '#'
        while q:
            i, j = q.popleft()
            for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                if i+di>=0 and i+di < m and j + dj >=0 and j+dj < n and mat[di + i][dj + j] == '#':
                    mat[di + i][dj + j] = mat[i][j] + 1
                    q.append((di+i, dj+j))
        return mat
        