class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(minHeap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        
        
        totalCost = 0
        
        uf = UnionFind(len(points))
        
        while minHeap:
            cost, i, j = heapq.heappop(minHeap)
            if uf.union(i, j):
                totalCost += cost

            
        return totalCost
    
    
    
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.parent[x] != x:
            x = self.parent[x]
        else:
            return x
        return self.find(self.parent[x])
    
    def union(self, a, b):
        parA, parB = self.find(a), self.find(b)
        
        if parA == parB:
            return False
        
        if self.rank[parA] > self.rank[parB]:
            self.parent[parB] = parA
        else:
            self.parent[parA] = parB
            
        return True
        