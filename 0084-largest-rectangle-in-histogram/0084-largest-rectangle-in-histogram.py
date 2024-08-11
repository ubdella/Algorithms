class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        heights.append(0)  # Add a 0 at the end to pop all remaining heights

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        return max_area
        