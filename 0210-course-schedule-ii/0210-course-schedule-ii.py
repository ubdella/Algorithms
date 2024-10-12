class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = set() # keeps track of courses in the current path
        done = set() # courses added to the result. don't gotta visit again
        result = [] # courses in topological ordering
        adj = defaultdict(list) # course : [prereqs]
        for c, p in prerequisites:
            adj[c].append(p)
            
        def dfs(c): # returns False if cycle detected
            if c in path:
                return False
            if c in done:
                return True
            path.add(c)
            for p in adj[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            result.append(c)
            done.add(c)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return result