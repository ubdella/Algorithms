class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        visited = set()
        
        adjList = {i:[] for i in range(numCourses)}
        for pair in prerequisites:
            adjList[pair[0]].append(pair[1])

        def dfs(c):
            if c in visited:
                return False
            if not adjList[c]:
                return True
            visited.add(c)
            for prereq in adjList[c]:
                if not dfs(prereq): return False
            visited.remove(c)
            adjList[c] = []
            return True
        for c in range(numCourses):
            if not dfs(c): return False
        return True

                
                
                