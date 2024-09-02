class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(yet, i):
            current_sum = sum(yet)
            if current_sum == target:
                res.append(yet.copy())  # Append a copy of the list to avoid mutation issues
                return
            if current_sum > target:
                return
            
            for j in range(i, len(candidates)):
                yet.append(candidates[j])
                dfs(yet, j)  # Continue with the current candidate
                yet.pop()  # Backtrack by removing the last added element
                
        res = []
        dfs([], 0)
        return res
