class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        minidx, maxidx = -1, -1
        for idx, val in enumerate(nums):
            if minidx < 0 or nums[idx] < nums[minidx]:
                minidx = idx
            if maxidx < 0 or nums[idx] >= nums[maxidx]:
                maxidx = idx
        return minidx + (len(nums) - maxidx - 1) - (minidx >= maxidx)