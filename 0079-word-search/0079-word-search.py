class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(pos, i, j):
            if pos == len(word):
                return True
            if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or (i, j) in visited or board[i][j] != word[pos]:
                return False
            visited.add((i, j))
            # if pos == len(word) - 1:
            #     return True
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                if dfs(pos + 1, i + di, j + dj):
                    return True
            visited.remove((i, j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if word[0] == board[i][j] and dfs(0, i, j):
                    return True
        return False