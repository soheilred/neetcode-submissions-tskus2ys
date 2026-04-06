import bisect
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r = 0
        min_len = float('inf')
        n = len(nums)
        total = 0

        for l in range(n):
            if l > 0: total -= nums[l-1]
            # print(l, r, total, min_len)

            while r < n and total < target:
                total += nums[r]
                r += 1
            
            if target <= total:
                min_len = min(min_len, r - l)
            


        return min_len if min_len != float('inf') else 0
