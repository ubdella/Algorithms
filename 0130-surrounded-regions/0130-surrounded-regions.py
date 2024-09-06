class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if i == m or j == n or i < 0 or j < 0 or board[i][j] != "O": 
                return 
            board[i][j] = "T"
            for di, dj in (1, 0), (-1, 0), (0, -1), (0, 1):
                dfs(i + di, j + dj)
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for i in range(n):
            dfs(0, i)
            dfs(m -1, i)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
                
                
            
            
        
        