class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, q = len(mat), len(mat[0]), deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = '#'
        
        while q:
            i, j  = q.popleft()
            
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                r = i + di
                c = j + dj
                if r < 0 or r >= m or c < 0 or c >= n or mat[r][c]!='#':
                    continue
                q.append((r, c))
                mat[r][c] = mat[i][j] + 1
        return mat
        