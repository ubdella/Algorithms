class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = maxSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(curSum, maxSum)
        return maxSum    
        