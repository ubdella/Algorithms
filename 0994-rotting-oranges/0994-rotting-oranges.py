class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = deque()
        good = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]
                if cell == 0:
                    continue
                elif cell == 1:
                    good+=1
                else:
                    q.append((i,j))
                    
        
        while q and good:
            qLen = len(q)
            while qLen:
                i, j = q.popleft()
                qLen-=1
                for di, dj in (0, -1), (0, 1), (1, 0), (-1, 0):
                    newI, newJ = i+di, j+dj
                    if newI>=m or newI<0 or newJ>=n or newJ<0 or grid[newI][newJ]==0 or grid[newI][newJ]==2:
                        continue

                    grid[newI][newJ]=2
                    q.append((newI, newJ))
                    good-=1
            minute+=1
                        
        return minute if not good else -1
        

            
                