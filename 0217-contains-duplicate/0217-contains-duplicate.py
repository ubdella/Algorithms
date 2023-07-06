class Solution:
    def containsDuplicate(self, nums):

        temp = set()
        for item in nums:
            if item in temp:
                return True
            temp.add(item)
        False