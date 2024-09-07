class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def connected(source, target):
            if source in visited:
                return False
            if source == target:
                return True
            visited.add(source)
            return any(connected(neighbour, target) for neighbour in graph[source])
            
        graph = {}
        
        for u, v in edges:
            visited = set()
            if u in graph and v in graph and connected(u, v):
                return [u, v]
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)