
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = 0
        visited = set()
        def dfs(i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
                return
            else:
                visited.add((i,j))
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited or grid[i][j]=="0":
                    continue
                n+=1
                dfs(i,j)
        return n