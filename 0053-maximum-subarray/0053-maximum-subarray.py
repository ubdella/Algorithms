class Solution:
    def maxSubArray(self, nums):
        curSum, maxSum = 0, nums[0]
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(curSum, maxSum)
        return maxSum
        