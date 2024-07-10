class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        
        heap = [(-count, char) for char, count in counts.items()]
        
        heapq.heapify(heap)
        
        if -heap[0][0]>(len(s)+1)//2: return ""
        
        res = []
        while len(heap)>=2:
            c1, c2 = heapq.heappop(heap), heapq.heappop(heap)
            res += [c1[1], c2[1]]
            
            if -c1[0] - 1 > 0: heapq.heappush(heap, (c1[0]+1, c1[1]))
            if -c2[0] - 1 > 0: heapq.heappush(heap, (c2[0]+1, c2[1]))
                
        if heap:
            res.append(heap[0][1])
            
        return ''.join(res)
            
            