class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0

        for i in range(n):
            height = heights[i]
            for j in range(i, n):
                height = min(height, heights[j])
                area = max(area, height * (j - i + 1))
        
        return area

        