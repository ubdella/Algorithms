class Solution:
	def maxProfit(self, nums):
		@cache
		def dfs(i, stockStatus):
			if i >= len(nums):
				return 0
			result = 0
			if stockStatus == 'idle':
				result = dfs(i + 1, stockStatus)
				result = max(result, dfs(i + 1, 'bought') - nums[i])
			else:
				result = dfs(i + 1, stockStatus)
				result = max(result, dfs(i + 2, 'idle') + nums[i])
			return result
		return dfs(0, 'idle')