class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):
            if nums[i]>0: break
            if i>0 and nums[i] == nums[i-1]: continue
            j = i+1
            k = n-1
            
            while j<k:
                                
                treSum = nums[i] + nums[j] + nums[k]
                if treSum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j>i+1 and nums[j] == nums[j-1] and j<k: 
                        j+=1
                    while k<n-1 and nums[k] == nums[k + 1] and j<k: 
                        k-=1
                elif treSum < 0:
                    j += 1
                else:
                    k -= 1
        return res