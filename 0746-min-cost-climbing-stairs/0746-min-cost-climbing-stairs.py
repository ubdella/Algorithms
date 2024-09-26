class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        prev, prevprev, cur = 0, 0, 0
        for i in range(2, len(cost) + 1):
            cur = min(prevprev + cost[i - 2], prev + cost[i - 1])
            prevprev = prev
            prev = cur
        return cur