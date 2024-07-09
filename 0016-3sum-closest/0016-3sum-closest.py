class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        n = len(nums)
        
        for i in range(n-2):
            left, right = i+1, n-1
            
            while left<right:
                currSum = nums[i] + nums[left] + nums[right]
                
                if currSum == target: return currSum
                
                if abs(currSum - target) < abs(closest_sum - target): closest_sum = currSum
                    
                if currSum<target: left+=1
                else: right-=1
                    
        return closest_sum