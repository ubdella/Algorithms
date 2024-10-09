class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for i in range(n + 1)]
        for source, destination, time in times:
            adjList[source].append([time, destination])
            
        heap = [[0, k]]
        time = 0
        
        visited = set()
        
        while heap and len(visited) < n:
            timeTaken, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            time = timeTaken
            for neighbor in adjList[node]:
                if neighbor[1] not in visited:
                    heapq.heappush(heap, [timeTaken + neighbor[0], neighbor[1]])
                    
        return time if len(visited) == n else -1
        