class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur_sum = res_min = float('inf')

        for r in range(n):
            cur_sum = min(0, cur_sum) + nums[r]
            res_min = min(res_min, cur_sum)
        
        # Standard Kadane's for maximum subarray sum
        cur_max = res_max = float('-inf')
        for x in nums:
            cur_max = max(x, cur_max + x)
            res_max = max(res_max, cur_max)

        
        # If all numbers are negative, total - res_min would be 0 (empty subarray), 
        # but we must return a non-empty subarray (res_max).
        if total == res_min:
            return res_max
            
        return max(res_max, total - res_min)