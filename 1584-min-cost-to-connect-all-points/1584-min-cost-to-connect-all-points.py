class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 2:
            return 0
        
        # Calculate Manhattan distance between two points
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        # Initialize data structures
        mst_set = [False] * n
        min_distances = [float('inf')] * n
        min_distances[0] = 0
        total_cost = 0
        
        for _ in range(n):
            # Find the vertex with the minimum distance
            min_dist = float('inf')
            min_vertex = -1
            for v in range(n):
                if not mst_set[v] and min_distances[v] < min_dist:
                    min_dist = min_distances[v]
                    min_vertex = v
            
            # Add the minimum distance to the total cost
            total_cost += min_dist
            
            # Mark the chosen vertex as processed
            mst_set[min_vertex] = True
            
            # Update min_distances for adjacent vertices
            for v in range(n):
                if not mst_set[v]:
                    dist = distance(points[min_vertex], points[v])
                    if dist < min_distances[v]:
                        min_distances[v] = dist
        
        return total_cost