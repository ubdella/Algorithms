class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev, cur = 0, 0
        for num in nums:
            nxt = max(cur, prev + num)
            prev = cur
            cur = nxt
        return cur