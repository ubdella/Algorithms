class Solution:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array
        n = len(nums)
        result = []

        for a in range(n - 3):
            # Skip duplicates for the first element
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                # Skip duplicates for the second element
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                # Use two pointers for the remaining two elements
                c = b + 1
                d = n - 1

                while c < d:
                    current_sum = nums[a] + nums[b] + nums[c] + nums[d]

                    if current_sum == target:
                        # Found a valid quadruplet
                        result.append([nums[a], nums[b], nums[c], nums[d]])

                        # Skip duplicates for the third element
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        # Skip duplicates for the fourth element
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1

                        c += 1
                        d -= 1

                    elif current_sum < target:
                        c += 1
                    else:
                        d -= 1

        return result