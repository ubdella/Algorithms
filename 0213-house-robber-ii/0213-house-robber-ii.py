class Solution:
    def rob(self, nums: List[int]) -> int:      
        def rob1(arr):
            prev, prevprev = 0, 0
            for num in arr:
                cur = max(num + prevprev, prev)
                prevprev = prev
                prev = cur
            return prev
        return max(nums[0], rob1(nums[:-1]), rob1(nums[1:]))