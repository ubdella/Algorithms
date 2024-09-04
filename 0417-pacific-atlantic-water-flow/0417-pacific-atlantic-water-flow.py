class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def dfs(i, j, h):
            if i < 0 or i >= m or j < 0 or j >= n or heights[i][j] > h or (i, j) in visited:
                return [0, 0]
            visited.add((i, j))
            curHeight = heights[i][j]
            pacific, atlantic = 0, 0
            if i == 0 or j == 0:
                pacific = 1
            if i == m-1 or j == n-1:
                atlantic = 1
            
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                p, a = dfs(i + di, j + dj, curHeight)
                pacific, atlantic = pacific or p, atlantic or a
    
            return [pacific, atlantic]
        res = []

        for i in range(m):
            for j in range(n):
                visited = set()
                both = dfs(i, j, heights[i][j])
                print(both)
                if both == [1, 1]:
                    res.append([i, j])
        return res
            