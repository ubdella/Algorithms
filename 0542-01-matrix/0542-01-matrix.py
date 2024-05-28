class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # BFS
        # Time O(R * C)     Space O(R * C)
        ROW, COL = len(mat), len(mat[0])
        q = deque()
        for r in range(ROW):
            for c in range(COL):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1
                    
        while q:
            r, c = q.popleft()
            for t_r, t_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_r = r + t_r
                new_c = c + t_c
                if new_r < 0 or new_r >= ROW or new_c < 0 or new_c >= COL or mat[new_r][new_c] != -1:
                    continue
                q.append((new_r, new_c))
                mat[new_r][new_c] = mat[r][c] + 1
        return mat