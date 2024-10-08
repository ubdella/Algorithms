class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dp(i, target):
            if i == len(coins) or target < 0:
                return 0
            if target == 0:
                return 1
            skip = dp(i + 1, target)
            use = dp(i, target - coins[i])
            return skip + use
        return dp(0, amount)