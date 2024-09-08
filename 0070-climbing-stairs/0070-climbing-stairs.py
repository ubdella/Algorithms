class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:
        if n in self.cache: return self.cache[n]
        if not n: return 1
        if n < 0: return 0
        self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.cache[n]
        