class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target: return m
            #We're in the left sorted part:
            if nums[m]>nums[r]:
                if target<nums[l] or target>nums[m]: l = m+1
                else: r = m-1
                    
            #We're in the right sorted part
            else:
                if target>nums[r] or target<nums[m]: r = m-1
                else: l = m+1
        return -1