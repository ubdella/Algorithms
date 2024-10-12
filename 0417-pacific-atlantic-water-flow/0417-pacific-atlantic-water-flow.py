class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i, j, elevation, visited):
            if i < 0 or j < 0 or i == len(heights) or j == len(heights[0]) or elevation > heights[i][j] or (i, j) in visited:
                return
            

            visited.add((i, j))

            dfs(i + 1, j, heights[i][j], visited)
            dfs(i - 1, j, heights[i][j], visited)
            dfs(i, j + 1, heights[i][j], visited)
            dfs(i, j - 1, heights[i][j], visited)

        pacific, atlantic = set(), set()

        for i in range(len(heights)):
            dfs(i, 0, float('-inf'), pacific)
            dfs(i, len(heights[0]) - 1, float('-inf'), atlantic)
            
        for i in range(len(heights[0])):
            dfs(0, i, float('-inf'), pacific)
            dfs(len(heights) - 1, i, float('-inf'), atlantic)
            
        return list(pacific & atlantic)