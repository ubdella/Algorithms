class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal curArea
            if i >= m or i < 0 or j >= n or j < 0 or (i, j) in visited or grid[i][j] == 0:
                return
            visited.add((i, j))
            curArea += 1
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(i + di, j + dj)
                
        visited = set()
        for i in range(m):
            for j in range(n):
                curArea = 0
                if grid[i][j] == 1 and (i, j) not in visited:
                    dfs(i, j)
                    maxArea = max(curArea, maxArea)
        return maxArea