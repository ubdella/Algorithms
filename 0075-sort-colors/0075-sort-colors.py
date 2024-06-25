class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums) - 1
        k = 0
        
        def swap(a, b):
            t = nums[a]
            nums[a] = nums[b]
            nums[b] = t
            
        while k<=j:
            if nums[k]==0:
                swap(k, i)
                i+=1
                
            elif nums[k]==2:
                swap(k, j)
                j-=1
                k-=1
                
            k+=1               
                
            