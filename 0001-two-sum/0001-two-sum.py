class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for idx, item in enumerate(nums):
            if target - item in hmap:
                return [idx, hmap[target - item]]
            else:
                hmap[item] = idx
        
        