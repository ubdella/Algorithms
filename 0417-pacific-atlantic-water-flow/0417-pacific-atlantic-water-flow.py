class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        
        def dfs(i, j, reachable):
            reachable[i][j] = True
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not reachable[ni][nj] and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, reachable)
        
        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        
        for j in range(n):
            dfs(0, j, pacific)
            dfs(m-1, j, atlantic)
        
        return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]