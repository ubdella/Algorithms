class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def dfs(curr, i):
            if i>=len(nums):
                return            
            curr.append(nums[i])
            res.append(curr.copy())
            
            for j in range(i+1, len(nums)):
                dfs(curr.copy(), j)
                
        for i in range(len(nums)):
            dfs([], i)
        
        return res