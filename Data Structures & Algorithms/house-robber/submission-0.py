class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        cache = {}

        def dp(house):
            if house > n - 1:
                cache[house] = 0
                return 0 
            
            if house in cache:
                return cache[house]
            
            cache[house] = max(nums[house] + dp(house + 2), dp(house + 1))
            return cache[house]
        
        return dp(0)
        