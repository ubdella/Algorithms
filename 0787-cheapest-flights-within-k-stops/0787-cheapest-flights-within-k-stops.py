class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]  # [[[cost, destination]]]
        for source, destination, price in flights:
            adj[source].append([price, destination])
        
        minHeap = [(0, src, k + 1)]  # [(cost, node, remaining stops)]
        
        # Use a dictionary to keep track of the minimum cost and remaining stops for each node
        best = {src: [0, k + 1]}  # {node: [min_cost, max_remaining_stops]}
        
        while minHeap:
            cost, node, stops = heapq.heappop(minHeap)
            
            if node == dst:
                return cost
            
            if stops > 0:
                for nei_cost, nei_node in adj[node]:
                    new_cost = cost + nei_cost
                    new_stops = stops - 1
                    
                    if nei_node not in best or new_cost < best[nei_node][0] or new_stops > best[nei_node][1]:
                        heapq.heappush(minHeap, (new_cost, nei_node, new_stops))
                        best[nei_node] = [new_cost, new_stops]
        
        return -1