class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, box):
            if not box:
                res.append(curr)
                return
            for i in range(len(box)):
                sendbox = box.copy()
                sendbox.pop(i)
                dfs(curr+[box[i]],sendbox)
        
        dfs([], nums)
        return res