class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0 
        right = len(heights) - 1
        w = 0
        while left < right:
            water = (right-left) * min(heights[right],heights[left])
            if water > w:
                w = water
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return w     