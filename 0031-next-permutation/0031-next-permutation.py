class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # Step 1: Find the first pair from the right where nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the smallest element in the subarray nums[i+1:] that is greater than nums[i]
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray nums[i+1:]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1