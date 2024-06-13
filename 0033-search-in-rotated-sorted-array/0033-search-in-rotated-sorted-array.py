class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==target: return m
            
            if nums[m]>=nums[l]:
                #We're in the left sorted subset
                if target>nums[m] or target<nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                #We're in the right sorted subset
                if target<nums[m] or target>nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1