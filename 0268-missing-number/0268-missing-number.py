class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = sum([i for i in range(len(nums) + 1)])
        for i in range(len(nums)):
            res -= nums[i]
        return res
