class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        l = r = res = 0
        while r < target:
            nextR = 0
            for i in range(l, r + 1):
                nextR = max(nextR, i + nums[i])
            l = r + 1
            r = nextR
            res += 1
        return res
            