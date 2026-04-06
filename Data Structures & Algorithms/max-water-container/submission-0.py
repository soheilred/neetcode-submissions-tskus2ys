class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur_max = 0
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            cur_max = max(height * (r - l), cur_max)

            if heights[l] == height:
                l += 1
            else:
                r -= 1

        
        return cur_max


        