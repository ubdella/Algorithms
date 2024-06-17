class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        
        def dfs(curr, box):
            if not box:
                res.append(curr)
                return
            for char in box:
                box.remove(char)
                dfs(curr+[char], box.copy())
                box.add(char)
            
        
        
        dfs([], set(nums))
        return res