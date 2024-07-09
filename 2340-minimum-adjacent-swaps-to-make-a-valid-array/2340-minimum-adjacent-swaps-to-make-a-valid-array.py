class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1: return 0
        
        minPos = nums.index(min(nums))
        maxPos = n-1-nums[::-1].index(max(nums))
        
        #for min element
        minSwaps = minPos
        
        #for max element
        maxSwaps = n-1-maxPos
        
        if minPos>maxPos:
            return minSwaps + maxSwaps -1
        else:
            return minSwaps +maxSwaps
