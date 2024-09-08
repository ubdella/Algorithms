class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev, curr = 0, 0

        for i in range(n):
            temp = max(prev + nums[i], curr)
            prev = curr
            curr = temp
        return curr
        