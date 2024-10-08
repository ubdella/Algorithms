class Solution:
    def maxProfit(self, nums):
        @cache
        def dfs(i, status):
            if i >= len(nums):
                return 0
            if status == 'buying':
                skip = dfs(i + 1, 'buying')
                buy = dfs(i + 1, 'selling') - nums[i]
                return max(skip, buy)
            else:
                skip = dfs(i + 1, 'selling')
                sell = dfs(i + 2, 'buying') + nums[i]
                return max(skip, sell)
        return dfs(0, 'buying')
            