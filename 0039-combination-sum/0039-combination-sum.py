class Solution:
    def combinationSum(self, candidates, target):
        res = []
        def dfs(path, i, curr):
            if i == len(candidates) or curr > target:
                return
            if curr == target:
                res.append(path[:])
                return
            dfs(path[:] + [candidates[i]], i, curr + candidates[i])
            dfs(path[:], i + 1, curr)

        dfs([], 0, 0)
        return res

