class Solution:
    def canJump(self, nums):
        target = len(nums) - 1
        if not target:
            return True
        dp = [False] * target
        for i in range(target - 1, -1, -1):
            for j in range(nums[i] + 1):
                if i + j > target:
                    break
                if i + j == target or dp[i + j]:
                    dp[i] = True
                    break
        return dp[0]
        