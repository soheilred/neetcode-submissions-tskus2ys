class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        N = len(nums)

        for left in range(N):
            total = nums[left]
            for right in range(left + 1, N):
                total += nums[right]
                if total < 0:
                    total = 0
                    break
                res = max(res, total)
        
        return res

        