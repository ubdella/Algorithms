class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dp(i, j):
            if j >= len(prices) or j >= len(prices):
                return 0
            if prices[i] > prices[j]:
                return dp(j, j + 1)
            return max(prices[j] - prices[i] + dp(j + 2, j + 3), dp(i, j + 1))
        return dp(0, 1)