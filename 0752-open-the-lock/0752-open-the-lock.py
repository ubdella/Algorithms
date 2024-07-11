class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        
        if '0000' in dead_set: return -1
        
        queue = deque([('0000', 0)])
        
        visited = set(['0000'])
        
        
        while queue:
            
            curr_state, turns = queue.popleft()
            
            if curr_state == target: return turns
            
            
            for i in range(4):
                for d in (-1, 1):
                    next_state = curr_state[:i] + str((int(curr_state[i]) + d)%10) + curr_state[i+1:]

                    if next_state not in dead_set and next_state not in visited:
                        queue.append((next_state, turns+1))
                        visited.add(next_state)
                    
                    
        return -1
                
                