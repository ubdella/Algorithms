class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)


        nearestLeftCandle = [-1]*n
        nearestRightCandle = [-1]*(n)
        platesYet = [0]*(n+1)
        
        for i in range(n):
            platesYet[i] = platesYet[i-1] + (1 if s[i] == '*' else 0)
            if s[i] == '|': nearestLeftCandle[i] = i
            else: 
                if i-1>=0:
                    nearestLeftCandle[i] = nearestLeftCandle[i-1]
                    
        for i in range(n-1, -1, -1):
            if s[i] == '|': nearestRightCandle[i] = i
            else:
                if i+1<n:
                    nearestRightCandle[i] = nearestRightCandle[i+1]
                    
                    
        res = []
        
        
        for left, right in queries:
            left, right = nearestRightCandle[left], nearestLeftCandle[right]
            if right<=left or right == -1 or left == -1: 
                res.append(0)
                continue
            res.append(platesYet[right]-platesYet[left])
            
        return res
                    
        
                    
            
        