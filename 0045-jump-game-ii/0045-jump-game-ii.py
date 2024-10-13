class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        maxRange = curRange = 0
        jumps = 0
        for i in range(target):
            maxRange = max(maxRange, nums[i] + i)
            if maxRange >= target:
                jumps += 1
                break            
            if i == curRange:
                jumps += 1
                curRange = maxRange

        return jumps