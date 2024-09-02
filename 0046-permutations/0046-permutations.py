
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, left):
            if len(path) == len(nums):
                res.append(path)
            for i in range(len(left)):
                copy = left.copy()
                copy.pop(i)
                dfs(path + [left[i]], copy)
        res = []
        dfs([], nums)
        return res