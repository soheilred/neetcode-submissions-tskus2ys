class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]
        cache = {}

        def dp(house, end):
            if house > n - end - 1:
                cache[(house, end)] = 0
                return cache[(house, end)]
            
            if (house, end) in cache:
                return cache[(house, end)]
            
            cache[(house, end)] = max(dp(house + 1, end), nums[house] + dp(house + 2, end))

            return cache[(house, end)]
        
        res = max(dp(0, 1), dp(1, 0))
        # print(cache)
        return res


        