class Solution:
    def canJump(self, nums):
        target = len(nums) - 1
        if not target:
            return True
        for i in range(target - 1, -1, -1):
            if nums[i] >= target - i:
                target = i
        return target == 0
        