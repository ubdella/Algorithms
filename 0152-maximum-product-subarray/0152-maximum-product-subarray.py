class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1 
        res = nums[0]
        
        for num in nums:
            curMax, curMin = max(num, curMax * num, curMin * num), min(num, curMin * num, curMax * num)
            res = max(res, curMax)
        return res
                    