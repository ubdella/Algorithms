class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] = 1
        l = sorted(d.items(), key = lambda x: x[1], reverse = True)
        g = [key for key,value in l]
        return g[0:k]
        