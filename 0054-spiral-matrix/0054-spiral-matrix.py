class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        changeDirection = {'right': 'down', 'down' : 'left', 'left': 'up', 'up': 'right'}
        directions = {'right': (0, 1), 'left' : (0, -1), 'up' : (-1, 0), 'down' : (1, 0)}
        
        
        def hitsWall(i, j):
            if i>=len(matrix) or i <0 or j<0 or j>=len(matrix[0]) or (i, j) in visited:
                return True
            return False
        
        res = []
        
        visited = set()
        
        q = deque()
        q.append((0,0))
        
        direction = 'right'
        while q:
            i, j = q.popleft()
            if hitsWall(i, j):
                break

            visited.add((i, j))
            
            res.append(matrix[i][j])
            
            di, dj = directions[direction]
            
            if hitsWall(i+di, j+dj):
                direction = changeDirection[direction]
            
            di, dj = directions[direction]
            
            q.append((i+di, j+dj))
            
            
        return res
                
            