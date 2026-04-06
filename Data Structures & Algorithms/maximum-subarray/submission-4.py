class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 0
        n = len(nums)
        max_sum = -float('inf')
        s = 0

        while r < n:
            cur_sum = 0
            while r < n and cur_sum >= 0:
                # print(l, r, cur_sum, max_sum)
                cur_sum += nums[r]
                r += 1

                if cur_sum > max_sum:
                    max_sum = cur_sum
                    s = l

            l = r
        return max_sum


        