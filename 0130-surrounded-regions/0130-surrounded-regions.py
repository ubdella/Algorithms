class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i, j):
            if i == m or j == n or i < 0 or j < 0 or (i, j) in visited or board[i][j] == "X": 
                return True
            if i == m - 1 or i == 0 or j == 0 or j == n - 1: 
                return False
            visited.add((i, j))
            surrounded = True
            for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                if not dfs(i + di, j + dj):
                    surrounded = False
            return surrounded
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited = set()
                if board[i][j] == "O" and dfs(i, j):
                    for r, c in visited:
                        board[r][c] = "X"
        
        