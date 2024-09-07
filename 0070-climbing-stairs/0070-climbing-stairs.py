class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(remaining):
            if remaining in cache:
                return cache[remaining]
            if not remaining:
                return 1
            if remaining < 0:
                return 0
            one, two = dfs(remaining - 1), dfs(remaining - 2)
            cache[remaining] = one + two
            return cache[remaining]
        dfs(n)
        return cache[n]
        