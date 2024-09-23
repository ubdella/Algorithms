class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(upto):
            if upto <= 0:
                return 1
            if upto == 1:
                return 1
            return dp(upto - 1) + dp(upto - 2)
            
        return dp(n)
        