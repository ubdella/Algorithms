class Solution:
    def maxProduct(self, nums):
        minProduct = 1
        maxProduct = 1
        result = float('-inf')
        for num in nums:
            if num == 0:
                minProduct, maxProduct = 1, 1
                result = max(result, 0)
                continue
            maxMult, minMult = maxProduct * num, minProduct * num
            minProduct = min(maxMult, minMult, num)
            maxProduct = max(maxMult, minMult, num)
            result = max(result, maxProduct)
        return result