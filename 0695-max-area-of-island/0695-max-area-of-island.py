class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if i >= m or i < 0 or j >= n or j < 0 or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
                
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    maxArea = max(dfs(i, j), maxArea)
        return maxArea