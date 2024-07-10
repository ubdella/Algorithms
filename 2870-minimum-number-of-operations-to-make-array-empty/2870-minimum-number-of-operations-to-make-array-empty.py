class Solution:
    def minOperations(self, nums):
        # Count the frequency of each number
        # Time complexity: O(n), Space complexity: O(k) where k is the number of unique elements
        counts = Counter(nums)

        operations = 0

        # Iterate through the counts
        # Time complexity: O(k)
        for count in counts.values():
            # If any number appears only once, it's impossible to make the array empty
            if count == 1:
                return -1

            # Calculate the number of operations needed for this count
            operations += count // 3  # Use as many triples as possible
            if count % 3 != 0:
                operations += 1  # If there's a remainder, we need one more operation (either a pair or a triple)

        return operations