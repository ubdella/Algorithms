class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(path, pathSum, i):
            if pathSum == target:
                res.append(path[:])
                return
            if i >= len(candidates) or pathSum > target:
                return
            path.append(candidates[i])
            dfs(path, pathSum + candidates[i], i + 1)
            path.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(path, pathSum, i + 1)
        candidates.sort()
        res = []
        dfs([], 0, 0)
        return res