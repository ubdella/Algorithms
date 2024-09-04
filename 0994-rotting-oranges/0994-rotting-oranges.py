class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        numFresh = 0
        minute = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    numFresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        while q and numFresh:
            qLen = len(q)
            minute += 1
            while qLen:
                i, j = q.popleft()
                qLen -= 1
                for di, dj in (1, 0), (-1, 0), (0, 1), (0, -1):
                    newI, newJ = i + di, j + dj
                    if newI < 0 or newI >= m or newJ < 0 or newJ >= n or grid[newI][newJ] != 1:
                        continue
                    numFresh -= 1
                    grid[newI][newJ] = 2
                    q.append((newI, newJ))
        return minute if numFresh == 0 else -1
        