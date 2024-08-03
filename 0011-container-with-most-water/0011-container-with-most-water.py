class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(i, j):
            return min(height[i], height[j])*(j-i)
        
        i, j = 0, len(height)-1
        
        maximum = 0
        
        while i<j:
            maximum = max(maximum, area(i, j))
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
                
        return maximum
        