class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = -1
        q = deque()
        visited = set()
        good = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 0:
                    continue
                elif cell == 1:
                    good.add((i,j))
                else:
                    q.append((i,j))
                    
        if not good:
            return 0
        if not q:
            return -1
        
        while q:
            qLen = len(q)
            while qLen:
                i, j = q.popleft()
                qLen-=1
                if (i, j) in visited:
                    continue
                visited.add((i,j))
                for di, dj in (0, -1), (0, 1), (1, 0), (-1, 0):
                    newI, newJ = i+di, j+dj
                    if newI>=m or newI<0 or newJ>=n or newJ<0 or grid[newI][newJ]==0 or grid[newI][newJ]==2 or grid[newI][newJ] in visited:
                        continue
                    if grid[newI][newJ] == 1:
                        grid[newI][newJ]=2
                        q.append((newI, newJ))
                        good.remove((newI,newJ))
            minute+=1
                        
        return minute if not good else -1
        

            
                