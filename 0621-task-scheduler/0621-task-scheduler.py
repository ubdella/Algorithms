from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        ready = [-count for count in counts.values()]
        heapq.heapify(ready)
        coolingDown = deque()
        time = 0
        
        while coolingDown or ready:
            time += 1
            if ready:
                cnt = 1 + heapq.heappop(ready)
                if cnt:
                    coolingDown.append((cnt, time + n))
            # else:
            #     time = coolingDown[0][1]
            
            if coolingDown and coolingDown[0][1] == time:
                heapq.heappush(ready, coolingDown.popleft()[0])
                
        return time