class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(yet, sumYet, i):
            if sumYet == target: 
                res.append(yet.copy())
                return
            if i >= len(candidates) or sumYet > target:
                return
            
            dfs(yet.copy(), sumYet, i + 1)
            
            yet.append(candidates[i])
            
            dfs(yet.copy(), sumYet + candidates[i], i)
                
                
        res = []
        dfs([], 0, 0)
        return res
