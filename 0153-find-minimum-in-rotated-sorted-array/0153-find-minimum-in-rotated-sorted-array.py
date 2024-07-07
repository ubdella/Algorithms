class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = (l+r)//2
        while l<r:
            m = (l+r)//2
            
            #case where we're in the larger section
            if nums[m]>nums[r]: l = m+1
            #case where we're in the smaller section
            else: 
                r = m
                
            
        return nums[r]