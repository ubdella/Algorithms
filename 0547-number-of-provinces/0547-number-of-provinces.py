class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1]*n
        numProvin = n
        
        def find(a):
            if par[a]!=a:
                par[a]=find(par[a])
            return par[a]
        
        def union(a, b):
            p1, p2 = find(a), find(b)
            
            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
                
            return 1
                
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    numProvin-=union(i, j)
        return numProvin