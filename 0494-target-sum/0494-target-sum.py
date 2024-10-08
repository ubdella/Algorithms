class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, target):
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0
            a = dfs(i + 1, target + nums[i])
            s = dfs(i + 1, target - nums[i])
            return a + s
        return dfs(0, target)
            