class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])        
        def rob1(arr):
            prev, prevprev = 0, 0
            for num in arr:
                cur = max(num + prevprev, prev)
                prevprev = prev
                prev = cur
            return cur
        return max(rob1(nums[:-1]), rob1(nums[1:]))