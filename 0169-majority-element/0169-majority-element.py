class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums)//2
        counter = {}
        for item in nums:
            if item in counter:
                counter[item] +=1
            else:
                counter[item] = 1
            if counter[item] > threshold:
                return item