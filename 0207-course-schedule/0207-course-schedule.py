class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
            
        def dfs(course):
            if course in visited:
                return False
            if not graph[course]:
                return True
            visited.add(course)
            for preq in graph[course]:
                if not dfs(preq):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
        visited = set()
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        
                