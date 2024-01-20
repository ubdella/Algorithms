class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for item in nums:
            if item in hset:
                return True
            else:
                hset.add(item)
        return False