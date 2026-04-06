class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_sf, min_sf = [0] * (n+1), [0] * (n + 1)
        max_sf[0], min_sf[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            print(max_sf, min_sf)
            tmp = max_sf[i-1]
            max_sf[i] = max(nums[i], nums[i] * max_sf[i-1], nums[i] * min_sf[i-1])
            min_sf[i] = min(nums[i], nums[i] * tmp, nums[i] * min_sf[i-1])
        
        return max(max_sf[:-1])
        