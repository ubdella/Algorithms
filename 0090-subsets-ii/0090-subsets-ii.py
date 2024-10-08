class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i + 1, path.copy())
            path.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, path)
            
        res = []
        dfs(0, [])
        return res