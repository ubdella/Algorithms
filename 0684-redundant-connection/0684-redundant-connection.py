class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        
        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                for nei in graph[source]:
                    if dfs(nei, target):
                        return True
            return False
        
        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        return []