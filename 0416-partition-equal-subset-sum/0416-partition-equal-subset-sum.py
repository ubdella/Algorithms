class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)/2
        dp = set()
        
        dp.add(0)
        
        for i in range(len(nums)-1, -1, -1):
            dp_1 = dp.copy()
            for t in dp:
                if t+nums[i]==target: return True
                dp_1.add(t+nums[i])
            dp = dp_1
        return False
            