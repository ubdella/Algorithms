class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par, rank = [i for i in range(n)], [1] * n
        
        def find(a):
            res = par[a]
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
            
            
        def union(a, b):
            pa, pb = find(a), find(b)
            
            if pa == pb:
                return False
            
            if rank[pa] > rank[pb]:
                par[pb] = pa
                rank[pa] += 1
                
            else:
                par[pa] = pb
                rank[pb] += 1

            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
            