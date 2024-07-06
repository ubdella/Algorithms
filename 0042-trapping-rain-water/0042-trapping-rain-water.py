class Solution:
    def trap(self, height):
        if not height:  # Handle empty input
            return 0

        left, right = 0, len(height) - 1  # Initialize two pointers
        left_max, right_max = 0, 0  # Keep track of max height from left and right
        water = 0  # Total water trapped

        while left < right:
            if height[left] < height[right]:
                # If left height is smaller
                if height[left] >= left_max:
                    # Update left_max if current height is greater
                    left_max = height[left]
                else:
                    # Add trapped water
                    water += left_max - height[left]
                left += 1  # Move left pointer inward
            else:
                # If right height is smaller or equal
                if height[right] >= right_max:
                    # Update right_max if current height is greater
                    right_max = height[right]
                else:
                    # Add trapped water
                    water += right_max - height[right]
                right -= 1  # Move right pointer inward

        return water