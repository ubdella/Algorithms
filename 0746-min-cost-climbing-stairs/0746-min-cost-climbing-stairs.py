class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @cache
        def dfs(i):
            if i == n:
                return 0
            if i > n:
                return float('inf')
            one, two = dfs(i + 1), dfs(i + 2)
            costToReturn = cost[i] if i != -1 else 0
            return costToReturn + min(one, two)
        return min(dfs(-1), dfs(0))