class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        cur_max = 0
        res = 0

        for i in range(n):
            cur_max = max(height[i], cur_max)
            max_left[i] = cur_max
        
        cur_max = 0
        for i in range(n-1, -1, -1):
            cur_max = max(height[i], cur_max)
            max_right[i] = cur_max
        
        for i in range(n):
            h = min(max_left[i], max_right[i])
            if height[i] < h:
                res += h - height[i]
        return res

        