class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        
        def dfs(course):
            if course in visited:
                return False
            if course in added:
                return True
            visited.add(course)
            for p in adjList[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            res.append(course)
            added.add(course)
            return True
        
        added, visited, res = set(), set(), []
        
        for c in range(numCourses):
            if not dfs(c): return []
        
        return res
        