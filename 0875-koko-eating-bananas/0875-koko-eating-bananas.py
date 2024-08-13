class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(k):
            if k == 0: return False
            hoursLeft = h
            for pile in piles:
                needed = pile / k if pile % k == 0 else pile // k + 1
                hoursLeft -= needed
            return hoursLeft >= 0
        
        l, r = 1, max(piles)
        
        while l <= r:
            m = (l + r) // 2
            if canEat(m):
                if not canEat(m - 1): return m 
                r = m - 1
            else:
                l = m + 1
                
                