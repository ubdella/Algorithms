class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] != 'O':
                return
            board[i][j] = 'NIGGA'
            
            for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(i + di, j + dj)
                
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
            
        for i in range(len(board[0])):
            dfs(0, i)
            dfs(len(board) - 1, i)
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'NIGGA':
                    board[i][j] = 'O'
        