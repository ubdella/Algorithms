class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        n = len(nums)
        prefix_product = suffix_product = 1
        result = float('-inf')

        for i in range(n):
            prefix_product *= nums[i]
            suffix_product *= nums[n-1-i]
            result = max(result, prefix_product, suffix_product)

            if prefix_product == 0:
                prefix_product = 1
            if suffix_product == 0:
                suffix_product = 1

        return result
                    