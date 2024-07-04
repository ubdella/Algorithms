class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n<0: return 0
        if n==0: return 1
        numWays = self.climbStairs(n-1) + self.climbStairs(n-2)
        return numWays